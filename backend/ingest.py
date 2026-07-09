"""
ingest.py — Build the Ableton knowledge base in ChromaDB.

What this script does:
  1. Downloads the Ableton Live 12 manual PDF (if not cached locally)
  2. Parses every page and splits it into overlapping text chunks
  3. Scrapes a curated list of Ableton 12 tips articles from the web
  4. Embeds every chunk with nomic-embed-text via Ollama
  5. Upserts everything into ChromaDB (safe to re-run — no duplicates)

Run it once before starting the server:
    ./venv/bin/python ingest.py

Or force a full re-index (wipes the collection first):
    ./venv/bin/python ingest.py --reset

What is "chunking"?
    LLMs and embedding models have a token limit — you can't embed a
    500-page PDF as one string.  Chunking splits the text into smaller
    overlapping windows so each chunk is self-contained but context
    from the edges is not lost (the overlap carries it into the
    next chunk).
"""

import argparse
import hashlib
import io
import re
import sys
import time
from pathlib import Path
from typing import Generator

import chromadb
import requests
from bs4 import BeautifulSoup
from chromadb import Settings
from chromadb.utils.embedding_functions import OllamaEmbeddingFunction
from pypdf import PdfReader
from tqdm import tqdm

# ── Config ────────────────────────────────────────────────────────────────────

MANUAL_URL = (
    "https://cdn-resources.ableton.com/resources/pdfs/live-manual/12/"
    "2026-06-12/live12-manual-en.pdf"
)
MANUAL_CACHE_PATH = Path("./ableton12_manual.pdf")

CHROMA_PATH = "./chroma_db"
COLLECTION_NAME = "ableton_tips"
EMBED_MODEL = "nomic-embed-text"

# Chunk sizing.
# CHUNK_SIZE:    target character count per chunk (~300–400 tokens for nomic).
# CHUNK_OVERLAP: characters shared between adjacent chunks so sentences
#                at boundaries are not orphaned.
CHUNK_SIZE = 1200
CHUNK_OVERLAP = 200

# Articles to scrape.  Add/remove URLs here freely.
WEB_SOURCES = [
    {
        "url": "https://www.musicradar.com/news/ableton-live-12-guide",
        "label": "MusicRadar: producer's guide to Live 12",
    },
    {
        "url": "https://www.musicradar.com/how-to/live-12-5-things-you-need-to-know",
        "label": "MusicRadar: 5 things you need to know about Live 12",
    },
    {
        "url": "https://www.musicradar.com/news/ableton-live-12-whats-new-devices-midi-workflow",
        "label": "MusicRadar: new devices, MIDI additions, and workflow changes",
    },
    {
        "url": "https://www.musicradar.com/news/ultimate-guide-to-ableton-live-12-roar",
        "label": "MusicRadar: ultimate guide to Roar saturation",
    },
    {
        "url": "https://www.musicradar.com/news/ableton-live-12-ultimate-guide-to-meld",
        "label": "MusicRadar: ultimate guide to Meld synth",
    },
    {
        "url": (
            "https://www.musicradar.com/tutorials/music-production-tutorials/"
            "stuck-for-ideas-heres-how-to-create-fresh-basslines-and-melodies-"
            "with-ableton-live-12s-midi-tools"
        ),
        "label": "MusicRadar: basslines and melodies with Live 12 MIDI tools",
    },
    {
        "url": "https://www.ableton.com/en/blog/three-things-to-try-in-ableton-live-12-2/",
        "label": "Ableton blog: three things to try in Live 12.2",
    },
    {
        "url": "https://cdm.link/twelve-things-to-try-in-live-12/",
        "label": "CDM: twelve things to try in Live 12",
    },
    # ── Tips & workflow ───────────────────────────────────────────────────────
    {
        "url": "https://www.mind-flux.com/news-1/2024/7/29/40-essential-ableton-tips-to-boost-your-music-production",
        "label": "Mind Flux: 40 essential Ableton tips",
    },
    {
        "url": "https://adieusounds.com/blogs/news/ableton-live-12-best-new-features-tips-and-tricks",
        "label": "Adieu Sounds: Live 12 best new features, tips and tricks",
    },
    {
        "url": "https://digitalgrooveonline.com/blog/mastering-ableton-live-12--shortcuts-and-workflow-tips",
        "label": "Digital Groove Online: shortcuts and workflow tips",
    },
    {
        "url": "https://www.bax-shop.co.uk/blog/studio-recording/discover-10-time-saving-techniques-in-ableton-live-with-workflow-hacks/",
        "label": "Bax Shop: 10 time-saving workflow hacks",
    },
    {
        "url": "https://distinctmastering.com/post/maximizing-workflow-in-ableton-live-12-advanced-browser-tips-for-music-producers",
        "label": "Distinct Mastering: advanced browser tips",
    },
    {
        "url": "https://distinctmastering.com/post/ableton-12-1-update-new-features-instruments-and-hidden-gems",
        "label": "Distinct Mastering: Live 12.1 hidden gems",
    },
    {
        "url": "https://sonicbloom.net/25-essential-workflow-tips/",
        "label": "Sonic Bloom: 25 essential workflow tips",
    },
    {
        "url": "https://www.productionmusiclive.com/blogs/news/10-essential-workflow-tips-for-ableton-live",
        "label": "Production Music Live: 10 essential workflow tips",
    },
    {
        "url": "https://cymatics.fm/blogs/production/20-tips-ableton-tutorial",
        "label": "Cymatics: 20 Ableton tips and tutorial",
    },
    {
        "url": "https://brevemusicstudios.com/tips-for-managing-large-projects-in-ableton-live/",
        "label": "Breve Music Studios: managing large Ableton projects",
    },
    {
        "url": "https://www.edmprod.com/ableton-live-tips/",
        "label": "EDMProd: Ableton Live tips",
    },
    {
        "url": "https://www.edmprod.com/ableton-workflow-bible/",
        "label": "EDMProd: Ableton workflow bible",
    },
    {
        "url": "https://www.edmprod.com/how-to-use-ableton-live/",
        "label": "EDMProd: how to use Ableton Live",
    },
    {
        "url": "https://www.edmprod.com/ableton-drum-rack-tips/",
        "label": "EDMProd: Ableton Drum Rack tips",
    },
    {
        "url": "https://www.edmprod.com/resampling-audio/",
        "label": "EDMProd: resampling audio in Ableton",
    },
    # ── Shortcuts ─────────────────────────────────────────────────────────────
    {
        "url": "https://www.ableton.com/en/manual/live-keyboard-shortcuts/",
        "label": "Ableton manual: complete keyboard shortcuts reference",
    },
    {
        "url": "https://help.ableton.com/hc/en-us/articles/12840878679452-New-Keyboard-Shortcuts-in-Live-12",
        "label": "Ableton help: new keyboard shortcuts in Live 12",
    },
    {
        "url": "https://www.mind-flux.com/news-1/2024/7/29/essential-keyboard-shortcuts-for-ableton-live-12",
        "label": "Mind Flux: essential keyboard shortcuts for Live 12",
    },
    {
        "url": "https://sonicbloom.net/all-new-shortcuts-ableton-live-12-1/",
        "label": "Sonic Bloom: all new shortcuts in Live 12.1",
    },
    {
        "url": "https://www.edmprod.com/ableton-shortcuts/",
        "label": "EDMProd: complete Ableton shortcuts guide",
    },
    {
        "url": "https://blog.artistmgmt.org/ableton-12-shortcuts",
        "label": "Artist Mgmt Blog: Ableton 12 shortcuts",
    },
    # ── Mixing ────────────────────────────────────────────────────────────────
    {
        "url": "https://www.productionmusiclive.com/blogs/news/11-mixing-tips-in-ableton-live-mixing-problems-every-producer-will-face",
        "label": "Production Music Live: 11 mixing tips",
    },
    {
        "url": "https://www.musicguymixing.com/how-to-mix-in-ableton/",
        "label": "Music Guy Mixing: how to mix in Ableton",
    },
    {
        "url": "https://www.levelsmusicproduction.com/blog/ableton-live-12-mixing-with-the-magic-headroom-trick",
        "label": "Levels Music: mixing with the magic headroom trick",
    },
    {
        "url": "https://www.producerspot.com/referencing-mixes-in-ableton-live-a-complete-guide/",
        "label": "ProducerSpot: referencing mixes in Ableton",
    },
    # ── MIDI & generative tools ───────────────────────────────────────────────
    {
        "url": "https://help.ableton.com/hc/en-us/articles/11535349458588-MIDI-Tools-and-Device-Updates-in-Live-12-FAQ",
        "label": "Ableton help: MIDI tools and device updates FAQ",
    },
    {
        "url": "https://soundand.design/ableton-live-12-suites-midi-effects-585f08f8cfba",
        "label": "Sound and Design: Live 12 MIDI effects deep-dive",
    },
    {
        "url": "https://www.attackmagazine.com/technique/tutorials/getting-started-with-ableton-lives-generative-midi-tools/",
        "label": "Attack Magazine: generative MIDI tools tutorial",
    },
    # ── New features & release notes ─────────────────────────────────────────
    {
        "url": "https://www.ableton.com/en/live/all-new-features/",
        "label": "Ableton: all new features in Live 12",
    },
    {
        "url": "https://www.ableton.com/en/release-notes/live-12/",
        "label": "Ableton: Live 12 official release notes",
    },
    {
        "url": "https://www.ableton.com/en/blog/live-12-2-is-out-now/",
        "label": "Ableton blog: Live 12.2 release",
    },
    {
        "url": "https://www.ableton.com/en/blog/live-12-3-is-here/",
        "label": "Ableton blog: Live 12.3 release",
    },
    {
        "url": "https://www.productionmusiclive.com/blogs/news/top-10-features-in-live-12-update",
        "label": "Production Music Live: top 10 features in Live 12",
    },
    {
        "url": "https://www.attackmagazine.com/news/ableton-live-12-whats-new/",
        "label": "Attack Magazine: what's new in Live 12",
    },
    {
        "url": "https://www.attackmagazine.com/technique/video-tutorials/live-12-2-exploring-the-new-features/",
        "label": "Attack Magazine: exploring Live 12.2 new features",
    },
    {
        "url": "https://synthanatomy.com/2026/04/ableton-live-12-stay-creative-and-in-focus-an-overview-of-the-new-features.html",
        "label": "Synth Anatomy: Live 12 new features overview",
    },
    {
        "url": "https://edmtips.com/ableton-live-12-features-and-review/",
        "label": "EDM Tips: Live 12 features and review",
    },
    {
        "url": "https://www.synthtopia.com/content/2024/03/05/ableton-live-12-now-available-heres-whats-new/",
        "label": "Synthtopia: Live 12 launch — what's new",
    },
    {
        "url": "https://www.synthtopia.com/content/2024/10/08/ableton-live-12-1-now-available-heres-whats-new/",
        "label": "Synthtopia: Live 12.1 — what's new",
    },
    {
        "url": "https://www.synthtopia.com/content/2025/06/13/live-12-2-now-available-heres-whats-new/",
        "label": "Synthtopia: Live 12.2 — what's new",
    },
    {
        "url": "https://www.synthtopia.com/content/2026/05/06/ableton-live-12-4-available-now/",
        "label": "Synthtopia: Live 12.4 — what's new",
    },
    {
        "url": "https://news.dlkmusicpro.com/ableton-live-2025-cutting-edge-features-for-music-makers/",
        "label": "DLK Music Pro: cutting-edge Live 12 features 2025",
    },
    # ── Instruments & sound design ────────────────────────────────────────────
    {
        "url": "https://www.producerspot.com/ableton-live-tutorial-how-to-synthesize-percussion-in-operator-recipes/",
        "label": "ProducerSpot: synthesize percussion in Operator",
    },
    {
        "url": "https://www.producerspot.com/how-to-sample-sampling-bass-in-ableton-tutorials-tips-tricks-ashley-young/",
        "label": "ProducerSpot: sampling bass in Ableton",
    },
    {
        "url": "https://www.producerspot.com/tips-tutorials-on-how-to-manipulate-time-signature-and-tempo-in-ableton-live/",
        "label": "ProducerSpot: time signature and tempo manipulation",
    },
    {
        "url": "https://www.ableton.com/en/blog/simpler-and-sampler-pro-tips-and-techniques-slynk/",
        "label": "Ableton blog: Simpler and Sampler pro tips",
    },
    {
        "url": "https://www.ableton.com/en/blog/keep-it-simpler-tips-synthesis-and-sound-design/",
        "label": "Ableton blog: synthesis and sound design tips",
    },
    {
        "url": "https://www.ableton.com/en/blog/step-by-step-guide-for-sub-bass-chords-and-fx/",
        "label": "Ableton blog: sub-bass, chords and FX guide",
    },
    # ── Automation & warping ──────────────────────────────────────────────────
    {
        "url": "https://www.pointblankmusicschool.com/blog/understanding-automation-in-ableton-live-12/",
        "label": "Point Blank: understanding automation in Live 12",
    },
    {
        "url": "https://edmtips.com/ableton-automation-tricks/",
        "label": "EDM Tips: automation tricks in Ableton",
    },
    {
        "url": "https://www.musicguymixing.com/how-to-automate-in-ableton/",
        "label": "Music Guy Mixing: how to automate in Ableton",
    },
    {
        "url": "https://www.audeobox.com/learn/ableton/how-to-warp-audio-in-ableton/",
        "label": "Audeobox: how to warp audio in Ableton",
    },
    {
        "url": "https://mixelite.com/blog/warp-tracks-ableton-live/",
        "label": "Mixelite: warping tracks in Ableton Live",
    },
    # ── Session/Arrangement & performance ─────────────────────────────────────
    {
        "url": "https://www.audeobox.com/learn/ableton/session-view-for-live-performance/",
        "label": "Audeobox: Session View for live performance",
    },
    {
        "url": "https://www.pushpatterns.com/blog/ableton-live-12-tutorial-for-beginners",
        "label": "Push Patterns: Live 12 tutorial for beginners",
    },
    {
        "url": "https://www.soundonsound.com/techniques/preparing-performance-ableton-live",
        "label": "Sound On Sound: preparing a performance in Ableton",
    },
    # ── Drums & sampling ──────────────────────────────────────────────────────
    {
        "url": "https://www.ableton.com/en/blog/get-swing-drum-programming-tips/",
        "label": "Ableton blog: swing and drum programming tips",
    },
    {
        "url": "https://www.ableton.com/en/blog/beginners-guide-to-chords-bass-melodies/",
        "label": "Ableton blog: beginner's guide to chords, bass and melodies",
    },
    {
        "url": "https://plugg-supply.net/articles/ableton-live-12-tutorial-2026",
        "label": "Plugg Supply: Ableton Live 12 tutorial 2026",
    },
    # ── Ableton Live 12 manual chapters (ableton.com/en/live-manual/12/) ────────
    {
        "url": "https://www.ableton.com/en/live-manual/12/live-concepts/",
        "label": "Ableton 12 manual: Live concepts overview",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/first-steps/",
        "label": "Ableton 12 manual: first steps",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/session-view/",
        "label": "Ableton 12 manual: Session View",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/arrangement-view/",
        "label": "Ableton 12 manual: Arrangement View",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/clip-view/",
        "label": "Ableton 12 manual: Clip View",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/audio-clips-tempo-and-warping/",
        "label": "Ableton 12 manual: audio clips, tempo and warping",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/editing-midi/",
        "label": "Ableton 12 manual: editing MIDI notes and velocities",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/midi-tools/",
        "label": "Ableton 12 manual: MIDI tools (new in Live 12)",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/clip-envelopes/",
        "label": "Ableton 12 manual: clip envelopes",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/automation-and-editing-envelopes/",
        "label": "Ableton 12 manual: automation and editing envelopes",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/launching-clips/",
        "label": "Ableton 12 manual: launching clips",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/recording-new-clips/",
        "label": "Ableton 12 manual: recording new clips",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/bounce-to-audio/",
        "label": "Ableton 12 manual: bounce to audio",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/comping/",
        "label": "Ableton 12 manual: comping",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/mixing/",
        "label": "Ableton 12 manual: mixing",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/routing-and-i-o/",
        "label": "Ableton 12 manual: routing and I/O",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/working-with-instruments-and-effects/",
        "label": "Ableton 12 manual: working with instruments and effects",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/instrument-drum-and-effect-racks/",
        "label": "Ableton 12 manual: instrument, Drum Rack and effect racks",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/live-instrument-reference/",
        "label": "Ableton 12 manual: instrument reference (Operator, Wavetable, Simpler, Sampler, Drift, Analog, Impulse)",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/",
        "label": "Ableton 12 manual: audio effects reference (EQ Eight, Compressor, Reverb, Delay, Saturator, Glue, Roar)",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/live-midi-effect-reference/",
        "label": "Ableton 12 manual: MIDI effects reference",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/working-with-the-browser/",
        "label": "Ableton 12 manual: working with the browser",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/managing-files-and-sets/",
        "label": "Ableton 12 manual: managing files and sets",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/using-grooves/",
        "label": "Ableton 12 manual: using grooves and swing",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/converting-audio-to-midi/",
        "label": "Ableton 12 manual: converting audio to MIDI",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/stem-separation/",
        "label": "Ableton 12 manual: stem separation",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/midi-and-key-remote-control/",
        "label": "Ableton 12 manual: MIDI and key remote control",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/synchronizing-with-link-tempo-follower-and-midi/",
        "label": "Ableton 12 manual: sync with Link, Tempo Follower and MIDI",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/max-for-live/",
        "label": "Ableton 12 manual: Max for Live",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/live-keyboard-shortcuts/",
        "label": "Ableton 12 manual: all keyboard shortcuts",
    },
    {
        "url": "https://www.ableton.com/en/live-manual/12/using-push-2/",
        "label": "Ableton 12 manual: using Push 2",
    },
]

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}


# ── ChromaDB setup ────────────────────────────────────────────────────────────

def build_collection(reset: bool = False):
    """
    Return the ChromaDB collection, optionally wiping it first.

    'upsert' (used later) means: insert if the ID is new, update if it
    already exists.  This makes the script safe to re-run without
    duplicating chunks.
    """
    embedding_fn = OllamaEmbeddingFunction(
        url="http://localhost:11434",
        model_name=EMBED_MODEL,
    )
    client = chromadb.PersistentClient(
        path=CHROMA_PATH,
        settings=Settings(anonymized_telemetry=False),
    )

    if reset:
        try:
            client.delete_collection(COLLECTION_NAME)
            print(f"[reset] Deleted existing collection '{COLLECTION_NAME}'.")
        except Exception:
            pass

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_fn,
        metadata={"hnsw:space": "cosine"},
    )
    return collection


# ── Chunking ──────────────────────────────────────────────────────────────────

def _clean(text: str) -> str:
    """
    Normalise whitespace that PDF extraction leaves behind.
    Collapsed newlines and repeated spaces make chunks more coherent.
    """
    text = re.sub(r"\n{3,}", "\n\n", text)       # 3+ newlines → paragraph break
    text = re.sub(r"[ \t]{2,}", " ", text)        # multiple spaces → one
    text = re.sub(r"\n[ \t]+", "\n", text)        # leading spaces on lines
    return text.strip()


def chunk_text(
    text: str,
    chunk_size: int = CHUNK_SIZE,
    overlap: int = CHUNK_OVERLAP,
) -> Generator[str, None, None]:
    """
    Sliding-window character chunker.

    Why overlap?
        If a sentence starts at character 1190 and ends at 1230, a hard
        cut at 1200 would put the first half in chunk N and the second
        half in chunk N+1 with no context link.  With 200-char overlap,
        chunk N+1 starts at char 1000, so the full sentence appears in
        both chunks — whichever one is retrieved will have complete info.
    """
    text = _clean(text)
    start = 0
    while start < len(text):
        end = start + chunk_size
        yield text[start:end]
        if end >= len(text):
            break
        start = end - overlap   # slide back by overlap amount


def make_id(source: str, index: int) -> str:
    """
    Deterministic ID so the same chunk always gets the same ID.
    This is what makes upsert idempotent (no duplicates on re-runs).
    """
    raw = f"{source}::chunk_{index}"
    return hashlib.md5(raw.encode()).hexdigest()


# ── PDF ingestion ─────────────────────────────────────────────────────────────

def download_manual() -> Path:
    """
    Download the Ableton 12 manual PDF and cache it locally.
    If the cache file already exists, skip the download.
    """
    if MANUAL_CACHE_PATH.exists():
        size_mb = MANUAL_CACHE_PATH.stat().st_size / 1_000_000
        print(f"[PDF] Using cached manual ({size_mb:.1f} MB): {MANUAL_CACHE_PATH}")
        return MANUAL_CACHE_PATH

    print(f"[PDF] Downloading Ableton 12 manual from:\n      {MANUAL_URL}")
    resp = requests.get(MANUAL_URL, headers=HEADERS, stream=True, timeout=60)
    resp.raise_for_status()

    total = int(resp.headers.get("content-length", 0))
    with open(MANUAL_CACHE_PATH, "wb") as f, tqdm(
        total=total, unit="B", unit_scale=True, desc="Downloading"
    ) as bar:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)
            bar.update(len(chunk))

    print(f"[PDF] Saved to {MANUAL_CACHE_PATH}")
    return MANUAL_CACHE_PATH


def ingest_pdf(collection, pdf_path: Path):
    """
    Parse every page of the PDF, chunk each page's text, and upsert
    into ChromaDB.

    Why page-by-page?
        Ableton's manual has distinct chapters.  Keeping the page number
        as metadata means we can surface "see manual page 47" in the
        response later if we want.

    pypdf extracts text by reading the PDF's internal content streams.
    Some pages may be mostly images (e.g. diagrams) and return little
    text — we skip those.
    """
    reader = PdfReader(str(pdf_path))
    n_pages = len(reader.pages)
    print(f"[PDF] {n_pages} pages found in {pdf_path.name}")

    ids, docs, metas = [], [], []
    chunk_index = 0

    for page_num, page in enumerate(
        tqdm(reader.pages, desc="Parsing PDF pages", unit="pg"), start=1
    ):
        raw = page.extract_text() or ""
        if len(raw.strip()) < 80:
            # Skip near-empty pages (chapter dividers, diagrams, etc.)
            continue

        for chunk in chunk_text(raw):
            if len(chunk.strip()) < 60:
                continue   # skip tiny fragments
            ids.append(make_id(f"manual_p{page_num}", chunk_index))
            docs.append(chunk)
            metas.append({
                "source": "manual",
                "page": page_num,
                "topic": "manual",
            })
            chunk_index += 1

        # Upsert in batches of 100 to avoid sending one giant request.
        if len(ids) >= 100:
            collection.upsert(documents=docs, ids=ids, metadatas=metas)
            ids, docs, metas = [], [], []

    # Final partial batch.
    if ids:
        collection.upsert(documents=docs, ids=ids, metadatas=metas)

    print(f"[PDF] Ingested {chunk_index} chunks from the manual.")
    return chunk_index


# ── Web scraping ──────────────────────────────────────────────────────────────

def fetch_article_text(url: str) -> str:
    """
    Fetch a web page and extract its main article text.

    BeautifulSoup parses the HTML DOM.  We remove boilerplate elements
    (nav, header, footer, ads) and then pull paragraph text.
    This is a simple heuristic — not perfect but good enough for
    editorial articles like these.
    """
    try:
        resp = requests.get(url, headers=HEADERS, timeout=20)
        resp.raise_for_status()
    except Exception as e:
        print(f"  [SKIP] {url}\n         {e}")
        return ""

    soup = BeautifulSoup(resp.text, "lxml")

    # Remove noise elements.
    for tag in soup(["script", "style", "nav", "header", "footer",
                     "aside", "form", "noscript", "figure", "figcaption"]):
        tag.decompose()

    # Try to find the article body first.
    article = (
        soup.find("article")
        or soup.find("main")
        or soup.find(class_=re.compile(r"article|post|content|body", re.I))
        or soup
    )

    paragraphs = article.find_all(["p", "h2", "h3", "li"])
    text = "\n".join(p.get_text(separator=" ", strip=True) for p in paragraphs)
    return text


def ingest_web(collection):
    """
    Scrape each article, chunk its text, and upsert into ChromaDB.

    We tag each chunk with source='web' and the article URL so we know
    where it came from.
    """
    total_chunks = 0

    for source in WEB_SOURCES:
        url = source["url"]
        label = source["label"]
        print(f"\n[WEB] {label}")
        print(f"      {url}")

        text = fetch_article_text(url)
        if not text or len(text) < 200:
            print("      [SKIP] Too little text extracted.")
            continue

        ids, docs, metas = [], [], []
        for i, chunk in enumerate(chunk_text(text)):
            if len(chunk.strip()) < 60:
                continue
            ids.append(make_id(url, i))
            docs.append(chunk)
            metas.append({
                "source": "web",
                "url": url,
                "topic": label,
            })

        if ids:
            collection.upsert(documents=docs, ids=ids, metadatas=metas)
            print(f"      → {len(ids)} chunks stored.")
            total_chunks += len(ids)
        else:
            print("      [SKIP] No usable chunks after filtering.")

        time.sleep(1)   # be polite to servers

    return total_chunks


# ── Curated seed tips ─────────────────────────────────────────────────────────

def ingest_seed(collection):
    """
    Also (re-)upsert the hand-written tips from seed_data.py so
    everything lives in one collection.
    """
    from seed_data import ABLETON_TIPS

    collection.upsert(
        documents=[t["text"] for t in ABLETON_TIPS],
        ids=[t["id"] for t in ABLETON_TIPS],
        metadatas=[{"source": "curated", "topic": t["topic"]} for t in ABLETON_TIPS],
    )
    print(f"\n[SEED] Upserted {len(ABLETON_TIPS)} curated tips.")
    return len(ABLETON_TIPS)


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Ingest Ableton 12 knowledge into ChromaDB.")
    parser.add_argument(
        "--reset", action="store_true",
        help="Wipe the ChromaDB collection before ingesting (full re-index)."
    )
    parser.add_argument(
        "--skip-pdf", action="store_true",
        help="Skip the manual PDF (faster for web-only updates)."
    )
    parser.add_argument(
        "--skip-web", action="store_true",
        help="Skip web scraping (faster for PDF-only updates)."
    )
    parser.add_argument(
        "--pdf-path", type=str, default=None,
        help="Path to an already-downloaded PDF (skips the download)."
    )
    args = parser.parse_args()

    print("=" * 60)
    print("  Ableton 12 Knowledge Base Ingestor")
    print("=" * 60)

    collection = build_collection(reset=args.reset)
    before = collection.count()
    print(f"\n[DB] Collection '{COLLECTION_NAME}' currently has {before} entries.\n")

    total = 0

    # 1. Curated hand-written tips
    total += ingest_seed(collection)

    # 2. Manual PDF
    if not args.skip_pdf:
        pdf_path = Path(args.pdf_path) if args.pdf_path else download_manual()
        total += ingest_pdf(collection, pdf_path)
    else:
        print("\n[PDF] Skipped (--skip-pdf).")

    # 3. Web articles
    if not args.skip_web:
        total += ingest_web(collection)
    else:
        print("\n[WEB] Skipped (--skip-web).")

    after = collection.count()
    print("\n" + "=" * 60)
    print(f"  Done.  DB grew from {before} → {after} entries.")
    print(f"  (processed {total} chunks this run)")
    print("=" * 60)


if __name__ == "__main__":
    main()
