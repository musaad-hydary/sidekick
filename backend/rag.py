"""
RAG (Retrieval-Augmented Generation) layer using ChromaDB.

Single collection 'tutor_tips' holds tips for all apps (Ableton, Blender, Figma).
Each tip has an 'app' metadata field used for filtering at query time.
"""

import ollama as _ollama
import chromadb
from chromadb import Settings
from chromadb import EmbeddingFunction, Documents, Embeddings

from seed_data import ABLETON_TIPS
from blender_seed_data import BLENDER_TIPS
from figma_seed_data import FIGMA_TIPS

# ── Configuration ────────────────────────────────────────────────────────────

CHROMA_PATH      = "./chroma_db"
EMBED_MODEL      = "nomic-embed-text"
COLLECTION_NAME  = "tutor_tips"
N_RESULTS        = 4
BATCH_SIZE       = 50   # tips per upsert call
EMBED_TIMEOUT    = 300  # seconds — Ollama can be slow on first load


# ── Custom embedding function with configurable timeout ──────────────────────

class _OllamaEmbedFn(EmbeddingFunction):
    def __init__(self, model: str, timeout: float = EMBED_TIMEOUT):
        self._model  = model
        self._client = _ollama.Client(timeout=timeout)

    def __call__(self, input: Documents) -> Embeddings:
        resp = self._client.embed(model=self._model, input=list(input))
        return [list(e) for e in resp.embeddings]


# ── Client & Collection ──────────────────────────────────────────────────────

def _build_client_and_collection():
    client = chromadb.PersistentClient(
        path=CHROMA_PATH,
        settings=Settings(anonymized_telemetry=False),
    )
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=_OllamaEmbedFn(EMBED_MODEL),
        metadata={"hnsw:space": "cosine"},
    )
    return collection


_collection = None


def get_collection():
    global _collection
    if _collection is None:
        _collection = _build_client_and_collection()
    return _collection


# ── Seeding ──────────────────────────────────────────────────────────────────

def _seed_app_tips(collection, tips: list[dict], app: str):
    """Upsert only tips whose IDs are not already in the collection."""
    all_ids = [t["id"] for t in tips]

    # Fast ID-only lookup — no embedding needed
    existing_ids = set(collection.get(ids=all_ids, include=[])["ids"])
    new_tips = [t for t in tips if t["id"] not in existing_ids]

    if not new_tips:
        print(f"[RAG] {app}: all {len(tips)} tips already seeded, skipping.")
        return

    print(f"[RAG] {app}: seeding {len(new_tips)} new tips in batches of {BATCH_SIZE}…")
    for i in range(0, len(new_tips), BATCH_SIZE):
        batch = new_tips[i : i + BATCH_SIZE]
        collection.upsert(
            documents=[t["text"] for t in batch],
            ids=[t["id"] for t in batch],
            metadatas=[
                {"source": "curated", "topic": t["topic"], "app": app}
                for t in batch
            ],
        )
        done = min(i + BATCH_SIZE, len(new_tips))
        print(f"[RAG]   {app}: {done}/{len(new_tips)}")

    print(f"[RAG] {app}: done.")


def seed_tips():
    """Seed all apps' tips. Only embeds tips not already present."""
    collection = get_collection()
    _seed_app_tips(collection, ABLETON_TIPS, "ableton")
    _seed_app_tips(collection, BLENDER_TIPS, "blender")
    _seed_app_tips(collection, FIGMA_TIPS,   "figma")
    print(f"[RAG] Total docs in collection: {collection.count()}")


def seed_if_empty():
    seed_tips()


# ── Querying ─────────────────────────────────────────────────────────────────

def query_tips(
    query_text: str,
    n_results: int = N_RESULTS,
    where: dict | None = None,
    app: str = "ableton",
) -> list[dict]:
    """
    Find the most semantically similar tips to query_text, filtered by app.
    Pass where={"source": "curated"} to restrict to hand-written tips only.
    The app filter is always merged in so results never cross app boundaries.
    """
    collection = get_collection()

    app_filter: dict = {"app": app}
    if where:
        combined = {"$and": [{k: v} for k, v in {**app_filter, **where}.items()]}
    else:
        combined = app_filter

    total = collection.count()
    if total == 0:
        return []

    kwargs: dict = {
        "query_texts": [query_text],
        "n_results": min(n_results, total),
        "include": ["documents", "metadatas", "distances"],
        "where": combined,
    }

    results = collection.query(**kwargs)

    tips = []
    for doc, meta, dist in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    ):
        tips.append({
            "text":     doc,
            "topic":    meta.get("topic", "general"),
            "source":   meta.get("source", "unknown"),
            "distance": round(dist, 4),
        })

    return tips
