import asyncio
import base64
import json
import os
import re
import tempfile
from concurrent.futures import ThreadPoolExecutor
from contextlib import asynccontextmanager

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from rag import query_tips, seed_tips
from vision import describe_screenshot, llama_answer, stream_describe, warm_up


# ── Lifespan ─────────────────────────────────────────────────────────────────

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("[Server] Seeding ChromaDB curated tips…")
    seed_tips()
    print("[Server] Warming up LLaVA (~15s, model loads into GPU)…")
    try:
        # await in thread so the event loop isn't blocked, but we still wait
        # for warmup to finish before the server reports Ready.
        # This guarantees the first real request is fast (~5s), not 18s+.
        await asyncio.to_thread(warm_up)
        print("[Server] Ready — LLaVA warm, first request ~5s.")
    except Exception as e:
        print(f"[Server] Warmup failed, first request will be slow: {e}")
        print("[Server] Ready (cold).")
    yield
    print("[Server] Shutting down.")


# ── App ───────────────────────────────────────────────────────────────────────

app = FastAPI(
    title="Sidekick API",
    version="0.2.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Models ────────────────────────────────────────────────────────────────────

class DescribeRequest(BaseModel):
    image: str
    question: str | None = None
    app: str = "ableton"

class DescribeResponse(BaseModel):
    description: str

class TipsRequest(BaseModel):
    description: str
    question: str | None = None
    app: str = "ableton"

class SingleTip(BaseModel):
    text: str
    topic: str

class AnswerRequest(BaseModel):
    image: str
    question: str
    description: str | None = None   # pre-computed from /describe; enables fast Llama 3.2 path
    app: str = "ableton"

class AnswerResponse(BaseModel):
    answer: str
    tip: SingleTip | None = None
    image_url: str | None = None

class AnalyzeRequest(BaseModel):
    image: str
    question: str | None = None
    app: str = "ableton"

class Tip(BaseModel):
    text: str
    topic: str
    distance: float

class AnalyzeResponse(BaseModel):
    screen_description: str
    tips: list[Tip]


# ── Routes ────────────────────────────────────────────────────────────────────

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/tip/random", response_model=SingleTip)
def random_tip(app_name: str = "ableton"):
    import random
    from seed_data import ABLETON_TIPS
    from blender_seed_data import BLENDER_TIPS
    from figma_seed_data import FIGMA_TIPS
    pool = {"ableton": ABLETON_TIPS, "blender": BLENDER_TIPS, "figma": FIGMA_TIPS}
    tip = random.choice(pool.get(app_name, ABLETON_TIPS))
    return SingleTip(text=tip["text"], topic=tip["topic"])


@app.post("/describe/stream")
async def describe_stream(req: DescribeRequest):
    """
    SSE endpoint — emits tokens as LLaVA generates them.
    First token arrives in ~0.5s on M3 with model warm.

    Format: data: {"text": "<token>"}\n\n
            data: [DONE]\n\n
    """
    async def event_gen():
        try:
            async for token in stream_describe(req.image, req.app):
                yield f"data: {json.dumps({'text': token})}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"
        finally:
            yield "data: [DONE]\n\n"

    return StreamingResponse(
        event_gen(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
            "Connection": "keep-alive",
        },
    )


@app.post("/describe", response_model=DescribeResponse)
def describe_image(req: DescribeRequest):
    try:
        desc = describe_screenshot(req.image, req.app)
        return DescribeResponse(description=desc)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ── Image search ─────────────────────────────────────────────────────────────

# Ableton concepts where a visual reference actually helps
_VISUAL_CONCEPTS = {
    "session view", "arrangement view", "clip view", "detail view",
    "drum rack", "instrument rack", "audio effect rack", "midi effect rack",
    "simpler", "sampler", "operator", "wavetable", "analog", "drift",
    "browser", "mixer", "sends", "return track",
    "clip", "scene", "slot", "warp", "warp mode",
    "piano roll", "midi editor", "note editor",
    "automation", "envelope", "modulation",
    "eq eight", "compressor", "reverb", "delay", "saturator", "glue",
    "macro", "chain", "rack",
    "push", "controller", "launchpad",
    "crossfader", "cue", "groove pool",
}

def _needs_image(question: str, answer: str) -> bool:
    q = question.lower()
    # Only show images for explicit how-to / show-me requests, never definitions
    explicit = any(kw in q for kw in (
        "show me", "how to", "how do i", "how can i", "tutorial", "demo",
    ))
    if not explicit:
        return False
    text = f"{q} {answer.lower()}"
    return any(c in text for c in _VISUAL_CONCEPTS)

def _youtube_thumbnail(query: str) -> str | None:
    """Search YouTube for Ableton content and return the first video thumbnail."""
    try:
        import requests
        r = requests.get(
            "https://www.youtube.com/results",
            params={"search_query": f"Ableton Live {query}"},
            headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"},
            timeout=5,
        )
        match = re.search(r'"videoId":"([a-zA-Z0-9_-]{11})"', r.text)
        if match:
            vid_id = match.group(1)
            return f"https://img.youtube.com/vi/{vid_id}/hqdefault.jpg"
    except Exception as e:
        print(f"[image] search failed: {e}")
    return None


def _best_tip(query: str, app: str = "ableton") -> SingleTip | None:
    """Find the most relevant curated tip for the given app, or None if nothing fits."""
    push_q = any(w in query.lower() for w in ("push", "controller", "hardware", "pad"))

    def is_clean(tip: dict) -> bool:
        text = tip["text"].lstrip()
        if not text or not text[0].isupper():        return False
        if len(text) < 80:                            return False
        if tip["distance"] > 0.42:                    return False
        if not push_q and "push 2" in text.lower():  return False
        return True

    try:
        curated = query_tips(query, n_results=5, where={"source": "curated"}, app=app)
        good = [t for t in curated if is_clean(t)]
        if good:
            print(f"[tip/{app}] curated dist={good[0]['distance']:.3f} topic={good[0]['topic']}")
            return SingleTip(text=good[0]["text"], topic=good[0]["topic"])
    except Exception as e:
        print(f"[tip/{app}] curated query failed: {e}")

    try:
        candidates = query_tips(query, n_results=10, app=app)
        concise = [t for t in candidates if is_clean(t) and len(t["text"]) <= 480]
        if concise:
            print(f"[tip/{app}] fallback dist={concise[0]['distance']:.3f} topic={concise[0]['topic']}")
            return SingleTip(text=concise[0]["text"], topic=concise[0]["topic"])
    except Exception as e:
        print(f"[tip/{app}] fallback query failed: {e}")

    print(f"[tip/{app}] no confident match — returning None")
    return None


@app.post("/answer", response_model=AnswerResponse)
def answer_question(req: AnswerRequest):
    """
    Hybrid pipeline:
      - If frontend passes a pre-computed description (the common case after
        the background /describe completes), we skip LLaVA entirely and call
        Llama 3.2 directly — answers in ~1-2s instead of ~6-8s.
      - If no description is available, LLaVA describes the image first, then
        Llama 3.2 answers. Still better than LLaVA answering alone.
    Image search runs in a background thread so it adds zero extra latency.
    """
    # Start image search in background (runs while models process)
    img_future = None
    if _needs_image(req.question, req.description or ""):
        _executor = ThreadPoolExecutor(max_workers=1)
        img_future = _executor.submit(_youtube_thumbnail, req.question)

    # Get screen description (fast path: already done by frontend)
    if req.description:
        screen_desc = req.description
        print(f"[/answer] using pre-computed description (fast path)")
    else:
        try:
            screen_desc = describe_screenshot(req.image, req.app)
            print(f"[/answer] LLaVA describe: {screen_desc[:60]!r}")
        except Exception as e:
            if img_future:
                img_future.cancel()
            raise HTTPException(status_code=500, detail=f"Vision error: {e}")

    # Get RAG tip — pass to Llama so it can weave it into the answer
    tip = _best_tip(f"{req.question} {screen_desc}", app=req.app)
    tip_text = tip.text if tip else None

    # Llama 3.2 answers with screen context + optional tip
    try:
        answer = llama_answer(req.question, screen_desc, tip_text, app=req.app)
        print(f"[/answer] llama: {answer[:80]!r}")
    except Exception as e:
        if img_future:
            img_future.cancel()
        raise HTTPException(status_code=500, detail=f"Answer error: {e}")

    image_url: str | None = None
    if img_future:
        try:
            image_url = img_future.result(timeout=2)
        except Exception:
            pass

    return AnswerResponse(answer=answer, tip=tip, image_url=image_url)


class SuggestRequest(BaseModel):
    question: str
    answer: str
    app: str = "ableton"

class SuggestResponse(BaseModel):
    suggestions: list[str]

@app.post("/suggest", response_model=SuggestResponse)
def suggest_followups(req: SuggestRequest):
    import ollama as _ol
    prompt = (
        f"A user learning {req.app} asked: \"{req.question}\"\n"
        f"Answer they received: \"{req.answer[:500]}\"\n\n"
        "Suggest exactly 3 short follow-up questions they might ask next. "
        "Each must be under 9 words. Return only the 3 questions, one per line, no numbers, no bullets."
    )
    try:
        resp = _ol.generate(model="llama3.2", prompt=prompt)
        lines = [
            l.strip().lstrip("0123456789.-) ").strip()
            for l in resp["response"].strip().split("\n")
            if l.strip()
        ][:3]
        return SuggestResponse(suggestions=lines)
    except Exception as e:
        print(f"[/suggest] failed: {e}")
        return SuggestResponse(suggestions=[])


@app.post("/tips", response_model=SingleTip)
def get_tip(req: TipsRequest):
    q = req.question.strip() if req.question else ""
    query = q if len(q) > 3 else req.description
    tip = _best_tip(query, app=req.app)
    if tip:
        return tip
    raise HTTPException(status_code=404, detail="No confident tip found")


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(req: AnalyzeRequest):
    try:
        description = describe_screenshot(req.image, req.app)
        rag_query = f"{req.question} {description}" if req.question else description
        raw_tips = query_tips(rag_query, app=req.app)
        return AnalyzeResponse(
            screen_description=description,
            tips=[Tip(**t) for t in raw_tips],
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/analyze/upload", response_model=AnalyzeResponse)
async def analyze_upload(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image.")
    suffix = os.path.splitext(file.filename or ".png")[1] or ".png"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name
    try:
        description = describe_screenshot(tmp_path)
        raw_tips = query_tips(description)
        return AnalyzeResponse(
            screen_description=description,
            tips=[Tip(**t) for t in raw_tips],
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        os.unlink(tmp_path)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
