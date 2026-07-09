# Sidekick

A local AI tutor that lives in a corner of your screen while you work in Ableton Live, Blender, or Figma. Take a screenshot of anything on screen and ask a question, or chat without a screenshot for general help. All inference runs locally using Ollama.

## How it works

1. The app detects which creative tool is in focus and shows itself automatically.
2. Press the capture shortcut (default `Alt+A`) to drag-select a region of your screen.
3. LLaVA (a vision model) describes what it sees. Llama 3.2 answers your question using that description plus relevant tips retrieved from a ChromaDB vector store.
4. You can keep asking follow-up questions in the same session.
5. Sessions are saved to history automatically and can be favourited.

## Stack

| Layer | Technology |
|---|---|
| Desktop shell | Tauri v2 (Rust) |
| Frontend | React + TypeScript (Vite) |
| Backend | FastAPI (Python) |
| Vision model | LLaVA via Ollama |
| Language model | Llama 3.2 via Ollama |
| Embeddings | nomic-embed-text via Ollama |
| Vector store | ChromaDB |

## Requirements

- [Rust](https://rustup.rs)
- [Node.js](https://nodejs.org) 18+
- [Python](https://python.org) 3.11+
- [Ollama](https://ollama.com) with the following models pulled:

```
ollama pull llava
ollama pull llama3.2
ollama pull nomic-embed-text
```

## Setup

```bash
# 1. Install frontend dependencies
npm install

# 2. Install backend dependencies
cd backend && pip install -r requirements.txt && cd ..

# 3. Start the backend
cd backend && uvicorn main:app --port 8000

# 4. Build and run the desktop app (separate terminal)
npm run tauri build
```

The built app will be at `src-tauri/target/release/bundle/macos/Sidekick.app`. Open it directly or drag it to your Applications folder.

On first run, the backend seeds ~770 curated tips into ChromaDB. This takes a minute and only happens once.

## Features

- Screen capture with drag-to-select overlay
- Text-only chat mode (no screenshot required)
- Markdown-rendered answers
- RAG-powered tips from a curated knowledge base (Ableton, Blender, Figma)
- Suggested follow-up questions after each answer
- Quick-start chips when a description loads
- XP and streak tracking with unlockable colour themes
- Favourited and recent chat history
- Dark and light mode
- Configurable capture shortcut
- Auto-shows/hides based on which app is in focus

## Architecture notes

The frontend and backend are separate processes. Tauri spawns the desktop window; the FastAPI backend runs as a sidecar on port 8000. The two communicate over HTTP from the renderer process.

When a screenshot is taken, the frontend streams a description from LLaVA in real time so you see text appear while the model is still generating. When you ask a question, the pre-computed description is passed straight to Llama 3.2, skipping a second LLaVA call and cutting answer latency from ~8s to ~2s.

The RAG layer uses cosine similarity search over ChromaDB with nomic-embed-text embeddings. Tips are filtered by app at query time so Blender tips never appear in an Ableton session.
