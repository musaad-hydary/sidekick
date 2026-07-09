import asyncio
import base64
import io
from collections.abc import AsyncGenerator
from pathlib import Path

import ollama
from PIL import Image

VISION_MODEL = "llava:latest"
LLAMA_MODEL  = "llama3.2:latest"

# ── Per-app prompt config ─────────────────────────────────────────────────────

_APP_CONFIG: dict[str, dict[str, str]] = {
    "ableton": {
        "vision_system": (
            "You are a visual analyzer for Ableton Live. "
            "Identify the exact panel or feature shown and what the user is doing. "
            "Do NOT say 'The image shows' or 'I can see'. "
            "Start directly with the panel name."
        ),
        "llama_system": (
            "You are a concise Ableton Live 12 expert tutor. "
            "Answer the user's question in 1-2 sentences. "
            "Be specific, practical, and reference what's visible on their screen when relevant. "
            "No preamble. No 'As an AI'. Just the answer."
        ),
        "describe_prompt": (
            "Name the Ableton panel shown and what the user is doing. "
            "One sentence only, starting with the panel name."
        ),
    },
    "blender": {
        "vision_system": (
            "You are a visual analyzer for Blender 3D. "
            "Identify the exact workspace, editor type, or mode shown and what the user is doing. "
            "Do NOT say 'The image shows' or 'I can see'. "
            "Start directly with the editor name (e.g. '3D Viewport in Edit Mode', 'Shader Editor', 'UV Editor')."
        ),
        "llama_system": (
            "You are a concise Blender 3D expert tutor. "
            "Answer the user's question in 1-2 sentences. "
            "Be specific and practical — mention keyboard shortcuts when relevant. "
            "No preamble. No 'As an AI'. Just the answer."
        ),
        "describe_prompt": (
            "Name the Blender editor or workspace shown and what the user is doing. "
            "One sentence only, starting with the editor name."
        ),
    },
    "figma": {
        "vision_system": (
            "You are a visual analyzer for Figma. "
            "Identify the exact panel, canvas content, or mode shown and what the user is doing. "
            "Do NOT say 'The image shows' or 'I can see'. "
            "Start directly with what is visible (e.g. 'Auto layout frame', 'Component panel', 'Prototype connections')."
        ),
        "llama_system": (
            "You are a concise Figma design tool expert tutor. "
            "Answer the user's question in 1-2 sentences. "
            "Be specific and practical — reference Figma features, shortcuts, or panel names when relevant. "
            "No preamble. No 'As an AI'. Just the answer."
        ),
        "describe_prompt": (
            "Name the Figma panel or canvas element shown and what the user is doing. "
            "One sentence only, starting with what's visible."
        ),
    },
}

_DEFAULT_APP = "ableton"


def _cfg(app: str) -> dict[str, str]:
    return _APP_CONFIG.get(app, _APP_CONFIG[_DEFAULT_APP])


# ── Shared options ────────────────────────────────────────────────────────────

DESCRIBE_OPTIONS = {
    "num_gpu": 99, "num_predict": 50, "num_ctx": 2048, "temperature": 0.0, "top_k": 1,
}
LLAMA_OPTIONS = {
    "num_gpu": 99, "num_predict": 120, "num_ctx": 2048, "temperature": 0.0, "top_k": 1,
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def _vision_messages(prompt: str, b64: str, app: str = _DEFAULT_APP) -> list[dict]:
    return [
        {"role": "system", "content": _cfg(app)["vision_system"]},
        {"role": "user",   "content": prompt, "images": [b64]},
    ]


def _prepare_image(source: str) -> str:
    if not Path(source).exists():
        if "," in source:
            source = source.split(",", 1)[1]
        raw = base64.b64decode(source)
        img = Image.open(io.BytesIO(raw))
    else:
        img = Image.open(source)

    img = img.convert("RGB")
    w, h = img.size
    if max(w, h) > 512:
        scale = 512 / max(w, h)
        img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)

    buf = io.BytesIO()
    img.save(buf, format="PNG", optimize=True)
    return base64.b64encode(buf.getvalue()).decode("utf-8")


# ── Warm-up ───────────────────────────────────────────────────────────────────

def warm_up():
    """Load LLaVA and Llama 3.2 into GPU memory at startup."""
    img = Image.new("RGB", (8, 8), (255, 255, 255))
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    ollama.chat(
        model=VISION_MODEL,
        messages=_vision_messages("1", b64),
        keep_alive=-1,
        options={"num_gpu": 99, "num_ctx": 2048, "num_predict": 1},
    )
    ollama.chat(
        model=LLAMA_MODEL,
        messages=[{"role": "user", "content": "hi"}],
        keep_alive=-1,
        options={"num_gpu": 99, "num_ctx": 512, "num_predict": 1},
    )


# ── Public API ────────────────────────────────────────────────────────────────

def describe_screenshot(image_source: str, app: str = _DEFAULT_APP) -> str:
    """LLaVA: describe what panel/workspace is visible, using the app-specific prompt."""
    b64 = _prepare_image(image_source)
    cfg = _cfg(app)
    response = ollama.chat(
        model=VISION_MODEL,
        messages=_vision_messages(cfg["describe_prompt"], b64, app),
        keep_alive=-1,
        options=DESCRIBE_OPTIONS,
    )
    return response.message.content.strip()


def llama_answer(
    question: str,
    screen_desc: str,
    tip_text: str | None = None,
    app: str = _DEFAULT_APP,
) -> str:
    """Llama 3.2: answer a question using screen context + optional RAG tip."""
    context = f"Screen shows: {screen_desc}"
    if tip_text:
        context += f"\nRelevant tip: {tip_text}"

    prompt = f"{context}\n\nUser question: {question}"
    response = ollama.chat(
        model=LLAMA_MODEL,
        messages=[
            {"role": "system", "content": _cfg(app)["llama_system"]},
            {"role": "user",   "content": prompt},
        ],
        keep_alive=-1,
        options=LLAMA_OPTIONS,
    )
    return response.message.content.strip()


async def stream_describe(
    image_source: str,
    app: str = _DEFAULT_APP,
) -> AsyncGenerator[str, None]:
    b64   = _prepare_image(image_source)
    cfg   = _cfg(app)
    queue: asyncio.Queue[str | None] = asyncio.Queue()
    loop  = asyncio.get_running_loop()

    def _run():
        try:
            for chunk in ollama.chat(
                model=VISION_MODEL,
                messages=_vision_messages(cfg["describe_prompt"], b64, app),
                stream=True,
                keep_alive=-1,
                options=DESCRIBE_OPTIONS,
            ):
                if chunk.message.content:
                    loop.call_soon_threadsafe(queue.put_nowait, chunk.message.content)
        finally:
            loop.call_soon_threadsafe(queue.put_nowait, None)

    loop.run_in_executor(None, _run)
    while True:
        token = await queue.get()
        if token is None:
            break
        yield token
