import { useCallback, useEffect, useState } from "react";
import { invoke } from "@tauri-apps/api/core";
import { emitTo } from "@tauri-apps/api/event";
import "./overlay.css";

interface Pt { x: number; y: number }

export default function Overlay() {
  const [start,   setStart]   = useState<Pt | null>(null);
  const [current, setCurrent] = useState<Pt | null>(null);

  // Reset on (re-)focus so stale selection doesn't linger between activations.
  const reset = useCallback(() => {
    setStart(null);
    setCurrent(null);
  }, []);

  useEffect(() => {
    window.addEventListener("focus", reset);
    return () => window.removeEventListener("focus", reset);
  }, [reset]);

  useEffect(() => {
    const onKey = async (e: KeyboardEvent) => {
      if (e.key === "Escape") { reset(); await invoke("hide_overlay"); }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [reset]);

  const onMouseDown = (e: React.MouseEvent) => {
    setStart({ x: e.clientX, y: e.clientY });
    setCurrent({ x: e.clientX, y: e.clientY });
  };

  const onMouseMove = (e: React.MouseEvent) => {
    if (!start) return;
    setCurrent({ x: e.clientX, y: e.clientY });
  };

  const onMouseUp = async (e: React.MouseEvent) => {
    if (!start) return;

    const x    = Math.min(start.x, e.clientX);
    const y    = Math.min(start.y, e.clientY);
    const w    = Math.abs(e.clientX - start.x);
    const h    = Math.abs(e.clientY - start.y);
    const endX = e.clientX;
    const endY = e.clientY;

    if (w < 16 || h < 16) { reset(); return; }

    // Hide overlay BEFORE capture so screencapture sees the real screen.
    // We do NOT re-show the overlay after this — the prompt lives in the
    // main window instead, avoiding the focus→reset() race.
    await invoke("hide_overlay");
    await new Promise<void>(r => setTimeout(r, 200));

    try {
      const b64 = await invoke<string>("capture_region", { x, y, w, h });
      await emitTo("main", "capture_ready", {
        image: b64,
        selectionRight:  endX,
        selectionBottom: endY,
      });
    } catch (err) {
      await emitTo("main", "capture_error", { message: String(err) });
    } finally {
      reset();
    }
  };

  const rect = start && current ? {
    left:   Math.min(start.x, current.x),
    top:    Math.min(start.y, current.y),
    width:  Math.abs(current.x - start.x),
    height: Math.abs(current.y - start.y),
  } : null;

  return (
    <div
      className="overlay-root"
      onMouseDown={onMouseDown}
      onMouseMove={onMouseMove}
      onMouseUp={onMouseUp}
    >
      <div className="overlay-dim" />

      {rect && (
        <div className="selection-rect" style={{
          left: rect.left, top: rect.top,
          width: rect.width, height: rect.height,
        }} />
      )}

      {rect && (
        <div className="size-hint" style={{ left: rect.left + 4, top: rect.top + 4 }}>
          {Math.round(rect.width)} × {Math.round(rect.height)}
        </div>
      )}

      <div className="instruction">Drag to select area &nbsp;·&nbsp; Esc to cancel</div>
    </div>
  );
}
