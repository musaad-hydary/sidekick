import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import Overlay from "./Overlay";

// Both windows load the same index.html / JS bundle.
// We tell them apart by the URL hash that tauri.conf.json sets:
//   main window    → http://localhost:1420/         (no hash)
//   overlay window → http://localhost:1420/#overlay
const isOverlay = window.location.hash === "#overlay";

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    {isOverlay ? <Overlay /> : <App />}
  </React.StrictMode>
);
