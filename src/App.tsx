import { useEffect, useRef, useState } from "react";
import { invoke } from "@tauri-apps/api/core";
import { listen } from "@tauri-apps/api/event";
import {
  getCurrentWindow,
  LogicalSize,
  LogicalPosition,
} from "@tauri-apps/api/window";
import ReactMarkdown from "react-markdown";
import "./App.css";

const API = "http://localhost:8000";

// ── Types ─────────────────────────────────────────────────────────────────────

interface SingleTip {
  text: string;
  topic: string;
}
interface ChatEntry {
  question: string;
  answer: string;
  tip: SingleTip | null;
  imageUrl: string | null;
}
interface HistoryEntry {
  id: string;
  timestamp: number;
  screenshot: string | null;
  description: string | null;
  chat: ChatEntry[];
  type: "manual" | "auto";
}
type AppMode = "ableton" | "blender" | "figma";

interface Stats {
  totalCaptures: number;
  xp: number;
  topics: Record<string, number>;
  streak: { lastDate: string; count: number };
  activeTheme: string;
  colorMode: "dark" | "light";
  idleTips: boolean;
  showSuggestions: boolean;
  activeApp: AppMode;
}
type Phase =
  | "menu"
  | "idle"
  | "capture_prompt"
  | "result"
  | "error"
  | "permission"
  | "history"
  | "progress"
  | "settings";

// ── Themes ────────────────────────────────────────────────────────────────────

const THEMES = [
  { id: "default", name: "Default", xpRequired: 0, emoji: "⚫" },
  { id: "aurora", name: "Aurora", xpRequired: 50, emoji: "🩵" },
  { id: "ember", name: "Ember", xpRequired: 100, emoji: "🔶" },
  { id: "grove", name: "Grove", xpRequired: 150, emoji: "🍃" },
  { id: "dusk", name: "Dusk", xpRequired: 200, emoji: "🟣" },
  { id: "neon", name: "Neon", xpRequired: 250, emoji: "💜" },
  { id: "midnight", name: "Midnight", xpRequired: 300, emoji: "🌊" },
  { id: "sakura", name: "Sakura", xpRequired: 350, emoji: "🌸" },
  { id: "void", name: "Void", xpRequired: 400, emoji: "⬛" },
];

const QUICK_CHIPS: Record<AppMode, [string, string, string]> = {
  ableton: [
    "Explain this screen",
    "What can I do next?",
    "Any shortcuts here?",
  ],
  blender: [
    "Explain what I'm seeing",
    "What's the next step?",
    "Any useful shortcuts?",
  ],
  figma: [
    "Break down this design",
    "How can I improve this?",
    "Any shortcuts here?",
  ],
};

function getMilestoneProgress(xp: number) {
  const prev = Math.floor(xp / 50) * 50;
  const pct = Math.round(((xp - prev) / 50) * 100);
  const nextTheme = THEMES.find((t) => t.xpRequired > xp);
  return { pct, nextTheme };
}

// ── Persistence ───────────────────────────────────────────────────────────────

function loadHistory(): HistoryEntry[] {
  try {
    return JSON.parse(localStorage.getItem("ableton-history") || "[]");
  } catch {
    return [];
  }
}
function saveHistory(h: HistoryEntry[]) {
  localStorage.setItem("ableton-history", JSON.stringify(h));
}

function defaultStats(): Stats {
  return {
    totalCaptures: 0,
    xp: 0,
    topics: {},
    streak: { lastDate: "", count: 0 },
    activeTheme: "default",
    colorMode: "dark",
    idleTips: true,
    showSuggestions: true,
    activeApp: "ableton",
  };
}
function loadStats(): Stats {
  try {
    return {
      ...defaultStats(),
      ...JSON.parse(localStorage.getItem("ableton-stats") || "{}"),
    };
  } catch {
    return defaultStats();
  }
}
function saveStats(s: Stats) {
  localStorage.setItem("ableton-stats", JSON.stringify(s));
}

// ── Helpers ───────────────────────────────────────────────────────────────────

async function makeThumbnail(source: string, size = 220): Promise<string> {
  return new Promise((resolve) => {
    const img = new Image();
    img.onload = () => {
      const scale = Math.min(1, size / Math.max(img.width, img.height));
      const c = document.createElement("canvas");
      c.width = Math.round(img.width * scale);
      c.height = Math.round(img.height * scale);
      c.getContext("2d")!.drawImage(img, 0, 0, c.width, c.height);
      resolve(c.toDataURL("image/jpeg", 0.72));
    };
    img.src = source.startsWith("data:")
      ? source
      : `data:image/png;base64,${source}`;
  });
}

function timeAgo(ts: number): string {
  const s = Math.floor((Date.now() - ts) / 1000);
  if (s < 60) return "just now";
  if (s < 3600) return `${Math.floor(s / 60)}m ago`;
  if (s < 86400) return `${Math.floor(s / 3600)}h ago`;
  return `${Math.floor(s / 86400)}d ago`;
}

// ── Component ─────────────────────────────────────────────────────────────────

export default function App() {
  const [phase, setPhase] = useState<Phase>("idle");
  const [errorMsg, setErrorMsg] = useState("");
  const [capturedImage, setCapturedImage] = useState<string | null>(null);
  const [description, setDescription] = useState<string | null>(null);
  const [descLoading, setDescLoading] = useState(false);
  const [question, setQuestion] = useState("");
  const [followUp, setFollowUp] = useState("");
  const [chat, setChat] = useState<ChatEntry[]>([]);
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState<HistoryEntry[]>(() => loadHistory());
  const [stats, setStats] = useState<Stats>(() => loadStats());
  const [idleTip, setIdleTip] = useState<SingleTip | null>(null);
  const [shortcutDisplay, setShortcutDisplay] = useState(
    () => localStorage.getItem("ableton-shortcut-display") || "⌥A",
  );
  const [pendingShortcut, setPendingShortcut] = useState<{
    raw: string;
    display: string;
  } | null>(null);
  const [recordingShortcut, setRecordingShortcut] = useState(false);
  const [sessionSaved, setSessionSaved] = useState(false);
  const [deleteTarget, setDeleteTarget] = useState<{
    id: string;
    label: string;
  } | null>(null);
  const [copiedIdx, setCopiedIdx] = useState<number | null>(null);
  const [collapsed, setCollapsed] = useState(false);
  const [isLeaving, setIsLeaving] = useState(false);
  const [suggestions, setSuggestions] = useState<string[]>([]);
  const [xpToast, setXpToast] = useState<{
    name: string;
    emoji: string;
  } | null>(null);
  const [historySearch, setHistorySearch] = useState("");
  const miniDownTimeRef = useRef(0);

  const chatRef = useRef<ChatEntry[]>([]);
  const imgRef = useRef<string | null>(null);
  const descRef2 = useRef<string | null>(null);
  const abortRef = useRef<AbortController | null>(null);
  const skipDescRef = useRef(false);
  const sessionSavedRef = useRef(false);
  const savedEntryIdRef = useRef<string | null>(null);
  const restoredEntryRef = useRef<{
    id: string;
    origType: "manual" | "auto";
  } | null>(null);
  const questionRef = useRef<HTMLInputElement>(null);
  const followUpRef = useRef<HTMLInputElement>(null);
  const bottomRef = useRef<HTMLDivElement>(null);
  const contentRef = useRef<HTMLDivElement>(null);
  const recorderRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    chatRef.current = chat;
  }, [chat]);
  useEffect(() => {
    imgRef.current = capturedImage;
  }, [capturedImage]);
  useEffect(() => {
    descRef2.current = description;
  }, [description]);
  useEffect(() => {
    sessionSavedRef.current = sessionSaved;
  }, [sessionSaved]);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "instant" });
  }, [chat, loading]);

  useEffect(() => {
    const saved = localStorage.getItem("ableton-shortcut-raw");
    if (saved && saved !== "Alt+A")
      invoke("update_shortcut", { shortcutStr: saved }).catch(console.error);
  }, []);

  // Auto-detect which target app is frontmost and switch RAG context
  useEffect(() => {
    // Set initial state from whatever is currently frontmost
    invoke<string>("get_active_app")
      .then((app) => {
        if (app) setActiveApp(app as AppMode);
      })
      .catch(() => {});

    // Update whenever user switches to a different target app
    const unlistenPromise = listen<string>("active_app_changed", (event) => {
      setActiveApp(event.payload as AppMode);
    });

    return () => {
      unlistenPromise.then((fn) => fn());
    };
  }, []);

  useEffect(() => {
    if (phase !== "idle") return;
    let alive = true;
    const fetchTip = async () => {
      try {
        const r = await fetch(
          `${API}/tip/random?app_name=${loadStats().activeApp}`,
        );
        if (r.ok && alive) setIdleTip(await r.json());
      } catch {}
    };
    fetchTip();
    const id = setInterval(fetchTip, 15000);
    return () => {
      alive = false;
      clearInterval(id);
    };
  }, [phase]);

  useEffect(() => {
    const u = listen("permission_needed", () => setPhase("permission"));
    return () => {
      u.then((f) => f());
    };
  }, []);

  useEffect(() => {
    const u = listen<{ message: string }>("capture_error", (ev) => {
      setErrorMsg(ev.payload.message);
      setPhase("error");
    });
    return () => {
      u.then((f) => f());
    };
  }, []);

  useEffect(() => {
    const u = listen<{ image: string }>("capture_ready", async (ev) => {
      const prevChat = chatRef.current;
      const prevImg = imgRef.current;
      const prevDesc = descRef2.current;
      const wasSaved = sessionSavedRef.current;
      // Auto-save only genuinely new sessions (not restored history entries)
      if (prevChat.length > 0 && !wasSaved && !restoredEntryRef.current) {
        const thumb = prevImg ? await makeThumbnail(prevImg) : null;
        const entry: HistoryEntry = {
          id: Date.now().toString(),
          timestamp: Date.now(),
          screenshot: thumb,
          description: prevDesc,
          chat: [...prevChat],
          type: "auto",
        };
        const existing = loadHistory();
        const manuals = existing.filter((e) => e.type === "manual");
        const autos = existing.filter((e) => e.type !== "manual").slice(0, 9);
        const h = [entry, ...autos, ...manuals];
        saveHistory(h);
        setHistory(h);
      }

      const s = loadStats();
      s.totalCaptures = (s.totalCaptures || 0) + 1;
      const prevXp = s.xp;
      s.xp += 5;
      const newlyUnlocked = THEMES.find(
        (t) => t.xpRequired > prevXp && t.xpRequired <= s.xp,
      );
      if (newlyUnlocked) {
        setTimeout(() => {
          setXpToast({ name: newlyUnlocked.name, emoji: newlyUnlocked.emoji });
          setTimeout(() => setXpToast(null), 3500);
        }, 800);
      }
      const today = new Date().toISOString().split("T")[0];
      const yesterday = new Date(Date.now() - 86400000)
        .toISOString()
        .split("T")[0];
      if (s.streak.lastDate === today) {
        /* already counted */
      } else if (s.streak.lastDate === yesterday) {
        s.streak.count += 1;
        s.streak.lastDate = today;
      } else {
        s.streak.count = 1;
        s.streak.lastDate = today;
      }
      saveStats(s);
      setStats({ ...s });

      abortRef.current?.abort();
      restoredEntryRef.current = null;
      setCapturedImage(ev.payload.image);
      setDescription(null);
      setDescLoading(true);
      setChat([]);
      setQuestion("");
      setFollowUp("");
      setLoading(false);
      setSessionSaved(false);
      setSuggestions([]);
      setPhase("capture_prompt");
      contentRef.current?.scrollTo({ top: 0 });
      const win = getCurrentWindow();
      await win.show();
      await win.setFocus();
      setTimeout(() => questionRef.current?.focus(), 20);
    });
    return () => {
      u.then((f) => f());
    };
  }, []);

  useEffect(() => {
    if (!capturedImage) return;
    if (skipDescRef.current) {
      skipDescRef.current = false;
      return;
    }
    const ctrl = new AbortController();
    abortRef.current = ctrl;
    fetch(`${API}/describe`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        image: capturedImage,
        app: loadStats().activeApp,
      }),
      signal: ctrl.signal,
    })
      .then((r) =>
        r.ok
          ? (r.json() as Promise<{ description: string }>)
          : Promise.reject(r.status),
      )
      .then((d) => {
        setDescription(d.description);
        setDescLoading(false);
      })
      .catch((err) => {
        if ((err as Error)?.name !== "AbortError")
          console.warn("[describe]", err);
        setDescLoading(false);
      });
    return () => ctrl.abort();
  }, [capturedImage]);

  // ── Helpers ────────────────────────────────────────────────────────────────

  const trackTopic = (topic: string | null) => {
    if (!topic) return;
    const s = loadStats();
    s.topics[topic] = (s.topics[topic] || 0) + 1;
    saveStats(s);
    setStats({ ...s });
  };

  const callAnswer = async (
    q: string,
    image: string | null,
  ): Promise<ChatEntry> => {
    const app = loadStats().activeApp;
    const res = await fetch(`${API}/answer`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        image: image ?? "",
        question: q,
        description: image
          ? description || undefined
          : `No screenshot. User is asking a general question about ${app}.`,
        app,
      }),
    });
    if (!res.ok) throw new Error(await res.text());
    const data: {
      answer: string;
      tip: SingleTip | null;
      image_url: string | null;
    } = await res.json();
    const shownTips = new Set(chat.map((e) => e.tip?.text).filter(Boolean));
    const tip = data.tip && !shownTips.has(data.tip.text) ? data.tip : null;
    trackTopic(data.tip?.topic ?? null);
    return {
      question: q,
      answer: data.answer,
      tip,
      imageUrl: data.image_url ?? null,
    };
  };

  const saveSession = async () => {
    if (!capturedImage || chat.length === 0) return;
    const restored = restoredEntryRef.current;

    if (sessionSaved) {
      // Unfavourite → always move to Recent (never delete)
      const targetId = savedEntryIdRef.current ?? restored?.id;
      if (targetId) {
        const h = loadHistory().map((e) =>
          e.id === targetId ? { ...e, type: "auto" as const } : e,
        );
        saveHistory(h);
        setHistory(h);
      }
      savedEntryIdRef.current = null;
      setSessionSaved(false);
      return;
    }

    // Favourite
    if (restored) {
      // Update existing entry in-place — moves it from Recent to Favourited
      const h = loadHistory().map((e) =>
        e.id === restored.id
          ? { ...e, type: "manual" as const, chat: [...chat] }
          : e,
      );
      saveHistory(h);
      setHistory(h);
      savedEntryIdRef.current = restored.id;
    } else {
      // New session — create a fresh manual entry
      const id = Date.now().toString();
      const thumb = await makeThumbnail(capturedImage);
      const entry: HistoryEntry = {
        id,
        timestamp: Date.now(),
        screenshot: thumb,
        description,
        chat: [...chat],
        type: "manual",
      };
      const existing = loadHistory();
      const manuals = existing.filter((e) => e.type === "manual");
      const autos = existing.filter((e) => e.type !== "manual").slice(0, 4);
      const h = [entry, ...manuals, ...autos];
      saveHistory(h);
      setHistory(h);
      savedEntryIdRef.current = id;
    }
    setSessionSaved(true);
  };

  const updateSavedEntry = (newChat: ChatEntry[]) => {
    const id = savedEntryIdRef.current;
    if (!id) return;
    const h = loadHistory().map((e) =>
      e.id === id ? { ...e, chat: newChat } : e,
    );
    saveHistory(h);
    setHistory(h);
  };

  const deleteHistory = (id: string) => {
    const h = loadHistory().filter((e) => e.id !== id);
    saveHistory(h);
    setHistory(h);
  };

  // ── Handlers ───────────────────────────────────────────────────────────────

  const handleAsk = async (e: React.FormEvent) => {
    e.preventDefault();
    const q = question.trim();
    if (!q || loading) return;
    setSuggestions([]);
    setLoading(true);
    try {
      const entry = await callAnswer(q, capturedImage);
      setChat([entry]);
      setQuestion("");
      setPhase("result");
      fetchSuggestions(q, entry.answer);
      setTimeout(() => followUpRef.current?.focus(), 20);
    } catch (err) {
      setErrorMsg(String(err));
      setPhase("error");
    } finally {
      setLoading(false);
    }
  };

  const handleFollowUp = async (e: React.FormEvent) => {
    e.preventDefault();
    const q = followUp.trim();
    if (!q || loading) return;
    setSuggestions([]);
    setLoading(true);
    try {
      const entry = await callAnswer(q, capturedImage);
      const newChat = [...chatRef.current, entry];
      setChat(newChat);
      setFollowUp("");
      if (sessionSavedRef.current) updateSavedEntry(newChat);
      fetchSuggestions(q, entry.answer);
    } catch (err) {
      setErrorMsg(String(err));
      setPhase("error");
    } finally {
      setLoading(false);
    }
  };

  const handleNewCapture = async () => {
    // Auto-save unsaved new sessions (screenshot or text-only)
    if (!sessionSaved && chat.length > 0 && !restoredEntryRef.current) {
      const thumb = capturedImage ? await makeThumbnail(capturedImage) : null;
      const entry: HistoryEntry = {
        id: Date.now().toString(),
        timestamp: Date.now(),
        screenshot: thumb,
        description,
        chat: [...chat],
        type: "auto",
      };
      const existing = loadHistory();
      const manuals = existing.filter((e) => e.type === "manual");
      const autos = existing.filter((e) => e.type !== "manual").slice(0, 9);
      const h = [entry, ...autos, ...manuals];
      saveHistory(h);
      setHistory(h);
    }
    abortRef.current?.abort();
    setCapturedImage(null);
    setDescription(null);
    setDescLoading(false);
    setChat([]);
    setQuestion("");
    setFollowUp("");
    setLoading(false);
    setSessionSaved(false);
    setSuggestions([]);
    restoredEntryRef.current = null;
    setPhase("idle");
  };

  const handleBack = () => {
    if (["settings", "history", "progress", "idle"].includes(phase)) {
      setPhase("menu");
      return;
    }
    handleNewCapture().then(() => setPhase("menu"));
  };

  const restoreHistory = (entry: HistoryEntry) => {
    skipDescRef.current = true;
    abortRef.current?.abort();
    setCapturedImage(entry.screenshot);
    setDescription(entry.description);
    setDescLoading(false);
    setChat(entry.chat);
    setQuestion("");
    setFollowUp("");
    setLoading(false);
    const isManual = entry.type === "manual";
    setSessionSaved(isManual);
    savedEntryIdRef.current = isManual ? entry.id : null;
    restoredEntryRef.current = { id: entry.id, origType: entry.type };
    setPhase("result");
  };

  const setTheme = (id: string) => {
    const s = loadStats();
    s.activeTheme = id;
    saveStats(s);
    setStats({ ...s });
  };

  const setColorMode = (mode: "dark" | "light") => {
    const s = loadStats();
    s.colorMode = mode;
    saveStats(s);
    setStats({ ...s });
  };

  const toggleIdleTips = () => {
    const s = loadStats();
    s.idleTips = !s.idleTips;
    saveStats(s);
    setStats({ ...s });
  };

  const toggleSuggestions = () => {
    const s = loadStats();
    s.showSuggestions = !s.showSuggestions;
    saveStats(s);
    setStats({ ...s });
  };

  const setActiveApp = (app: AppMode) => {
    const s = loadStats();
    s.activeApp = app;
    saveStats(s);
    setStats({ ...s });
  };

  const handleShortcutKeyDown = (e: React.KeyboardEvent) => {
    e.preventDefault();
    e.stopPropagation();
    if (["Alt", "Control", "Shift", "Meta"].includes(e.key)) return;
    const mods: string[] = [];
    if (e.altKey) mods.push("Alt");
    if (e.ctrlKey) mods.push("Ctrl");
    if (e.shiftKey) mods.push("Shift");
    if (e.metaKey) mods.push("Super");
    const key = e.code.startsWith("Key")
      ? e.code.slice(3)
      : e.code.startsWith("Digit")
        ? e.code.slice(5)
        : e.key.length === 1
          ? e.key.toUpperCase()
          : e.key;
    const raw = [...mods, key].join("+");
    const syms: Record<string, string> = {
      Alt: "⌥",
      Ctrl: "⌃",
      Shift: "⇧",
      Super: "⌘",
    };
    setPendingShortcut({
      raw,
      display: mods.map((m) => syms[m] || m).join("") + key,
    });
  };

  const applyShortcut = async () => {
    if (!pendingShortcut) return;
    try {
      await invoke("update_shortcut", { shortcutStr: pendingShortcut.raw });
      localStorage.setItem("ableton-shortcut-display", pendingShortcut.display);
      localStorage.setItem("ableton-shortcut-raw", pendingShortcut.raw);
      setShortcutDisplay(pendingShortcut.display);
      setRecordingShortcut(false);
      setPendingShortcut(null);
    } catch (err) {
      console.error("Shortcut update failed:", err);
    }
  };

  const copyAnswer = (text: string, idx: number) => {
    navigator.clipboard.writeText(text);
    setCopiedIdx(idx);
    setTimeout(() => setCopiedIdx(null), 2000);
  };

  const fetchSuggestions = async (question: string, answer: string) => {
    try {
      const r = await fetch(`${API}/suggest`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question, answer, app: loadStats().activeApp }),
      });
      if (r.ok) {
        const data = await r.json();
        setSuggestions(data.suggestions || []);
      }
    } catch {}
  };

  const handleSuggestionClick = async (text: string) => {
    if (loading) return;
    setSuggestions([]);
    setFollowUp(text);
    setLoading(true);
    try {
      const entry = await callAnswer(text, capturedImage);
      const newChat = [...chatRef.current, entry];
      setChat(newChat);
      setFollowUp("");
      if (sessionSavedRef.current) updateSavedEntry(newChat);
      fetchSuggestions(text, entry.answer);
    } catch (err) {
      setErrorMsg(String(err));
      setPhase("error");
    } finally {
      setLoading(false);
    }
  };

  const handleChipSubmit = async (text: string) => {
    if (loading) return;
    setSuggestions([]);
    setQuestion(text);
    setLoading(true);
    try {
      const entry = await callAnswer(text, capturedImage);
      setChat([entry]);
      setQuestion("");
      setPhase("result");
      fetchSuggestions(text, entry.answer);
      setTimeout(() => followUpRef.current?.focus(), 20);
    } catch (err) {
      setErrorMsg(String(err));
      setPhase("error");
    } finally {
      setLoading(false);
    }
  };

  const startTextChat = () => {
    abortRef.current?.abort();
    restoredEntryRef.current = null;
    setCapturedImage(null);
    setDescription(null);
    setDescLoading(false);
    setChat([]);
    setQuestion("");
    setFollowUp("");
    setLoading(false);
    setSessionSaved(false);
    setSuggestions([]);
    setPhase("capture_prompt");
    setTimeout(() => questionRef.current?.focus(), 20);
  };

  const handleCollapse = async () => {
    if (isLeaving) return;
    setIsLeaving(true);
    await new Promise((r) => setTimeout(r, 150));
    const win = getCurrentWindow();
    const size = 56;
    const margin = 20;
    const ax =
      (window.screen as unknown as Record<string, number>)["availLeft"] ?? 0;
    const ay =
      (window.screen as unknown as Record<string, number>)["availTop"] ?? 0;
    const aw = window.screen.availWidth;
    const ah = window.screen.availHeight;
    const cx = ax + aw - size - margin;
    const cy = ay + ah - size - margin;
    await win.setMinSize(new LogicalSize(size, size));
    await win.setSize(new LogicalSize(size, size));
    await win.setPosition(new LogicalPosition(cx, cy));
    setIsLeaving(false);
    setCollapsed(true);
  };

  const handleExpand = async () => {
    if (isLeaving) return;
    setIsLeaving(true);
    await new Promise((r) => setTimeout(r, 150));
    const win = getCurrentWindow();
    const pos = await win.outerPosition();
    const sf = await win.scaleFactor();
    const lx = pos.x / sf;
    const ly = pos.y / sf;
    const sw = window.screen.width;
    const sh = window.screen.height;
    const newW = 300,
      newH = 480;
    const cx = Math.max(0, Math.min(lx, sw - newW));
    const cy = Math.max(0, Math.min(ly, sh - newH));
    await win.setSize(new LogicalSize(newW, newH));
    await win.setMinSize(new LogicalSize(260, 380));
    await win.setPosition(new LogicalPosition(cx, cy));
    setIsLeaving(false);
    setCollapsed(false);
  };

  const handleTitlebarDrag = (e: React.MouseEvent) => {
    if (e.button !== 0) return;
    if ((e.target as HTMLElement).closest("button")) return;
    getCurrentWindow()
      .startDragging()
      .catch(() => {});
  };

  // ── Derived ────────────────────────────────────────────────────────────────

  const showBack = phase !== "menu";
  const showFooter = phase === "capture_prompt" || phase === "result";
  const APP_NAMES: Record<AppMode, string> = {
    ableton: "Ableton",
    blender: "Blender",
    figma: "Figma",
  };
  const titleMap: Partial<Record<Phase, string>> = {
    menu: "Sidekick",
    history: "Recent",
    progress: "Progress",
    settings: "Settings",
  };
  const titlebarName = titleMap[phase] ?? APP_NAMES[stats.activeApp];
  const milestone = getMilestoneProgress(stats.xp);
  const imgSrc = (s: string) =>
    s.startsWith("data:") ? s : `data:image/png;base64,${s}`;

  const footerValue = phase === "result" ? followUp : question;
  const footerPlaceholder = loading
    ? "Thinking…"
    : phase === "result"
      ? "Ask a follow-up…"
      : capturedImage
        ? "Ask about this screen…"
        : `Ask about ${APP_NAMES[stats.activeApp]}…`;
  const footerRef = phase === "result" ? followUpRef : questionRef;

  const handleFooterChange = (v: string) => {
    if (loading) return;
    (phase === "result" ? setFollowUp : setQuestion)(v);
  };
  const handleFooterSubmit = (e: React.FormEvent) => {
    (phase === "result" ? handleFollowUp : handleAsk)(e);
  };

  // ── Render ─────────────────────────────────────────────────────────────────

  const appEmoji = { ableton: "🎛", blender: "🧊", figma: "🎨" }[
    stats.activeApp
  ];

  if (collapsed) {
    return (
      <div
        className={`app-shell app-shell--collapsed${isLeaving ? " leaving" : ""}`}
        data-tauri-drag-region
        data-theme={stats.activeTheme}
        data-mode={stats.colorMode}
        onMouseDown={() => {
          miniDownTimeRef.current = Date.now();
        }}
        onClick={() => {
          if (Date.now() - miniDownTimeRef.current < 200) handleExpand();
        }}
        title="Click to expand · Drag to move"
      >
        <span className="mini-icon">{appEmoji}</span>
      </div>
    );
  }

  return (
    <div
      className={`app-shell${isLeaving ? " leaving" : ""}`}
      data-theme={stats.activeTheme}
      data-mode={stats.colorMode}
    >
      {/* Titlebar */}
      <div
        className="titlebar"
        data-tauri-drag-region
        onMouseDown={handleTitlebarDrag}
      >
        <div className="traffic-lights">
          <button
            className="traffic-dot dot-red"
            onClick={() => getCurrentWindow().hide()}
            title="Hide"
          />
          <button
            className="traffic-dot dot-yellow"
            onClick={() => getCurrentWindow().minimize()}
            title="Minimize"
          />
          <button
            className="traffic-dot dot-purple"
            onClick={handleCollapse}
            title="Collapse"
          />
        </div>
        {showBack && (
          <button className="back-arrow" onClick={handleBack}>
            ‹
          </button>
        )}
        <span className="titlebar-name">{titlebarName}</span>
        <div className="titlebar-right">
          {(phase === "menu" || phase === "idle") && (
            <button
              className="gear-btn"
              onClick={() => setPhase("settings")}
              title="Settings"
            >
              ⚙︎
            </button>
          )}
        </div>
      </div>

      {/* Scrollable content area */}
      <div className="content" ref={contentRef}>
        {phase === "menu" && (
          <div className="menu-view">
            <button className="tutor-card" onClick={() => setPhase("idle")}>
              <span className="tutor-icon">
                {{ ableton: "🎛", blender: "🧊", figma: "🎨" }[stats.activeApp]}
              </span>
              <div className="tutor-info">
                <span className="tutor-name">Start Learning</span>
                <span className="tutor-desc">
                  {
                    {
                      ableton: "Ableton Live",
                      blender: "Blender 3D",
                      figma: "Figma",
                    }[stats.activeApp]
                  }
                </span>
              </div>
              <span className="tutor-chevron">›</span>
            </button>
            <div className="menu-actions">
              <button
                className="menu-action-btn"
                onClick={() => setPhase("history")}
              >
                <span className="menu-action-icon">🕐</span>
                <span className="menu-action-label">Chats & Captures</span>
                <span className="menu-action-badge">{history.length}</span>
              </button>
              <button
                className="menu-action-btn"
                onClick={() => setPhase("progress")}
              >
                <span className="menu-action-icon">⚡</span>
                <span className="menu-action-label">Progress</span>
                <span className="menu-action-badge xp-badge">
                  {stats.xp} XP
                </span>
              </button>
            </div>
          </div>
        )}

        {phase === "idle" && (
          <div className="idle">
            <div className="idle-key">{shortcutDisplay}</div>
            <div className="idle-hint">
              Press {shortcutDisplay} anywhere
              <br />
              then drag to capture screen
            </div>
            <button className="text-chat-btn" onClick={startTextChat}>
              Chat without screenshot →
            </button>
            {idleTip && stats.idleTips && (
              <div className="idle-tip">
                <div className="idle-tip-header">
                  <span className="idle-tip-topic">{idleTip.topic}</span>
                  <span className="idle-tip-tag">TIP</span>
                </div>
                <p className="idle-tip-text">{idleTip.text}</p>
              </div>
            )}
          </div>
        )}

        {phase === "history" &&
          (() => {
            const searchLower = historySearch.toLowerCase().trim();
            const filtered = searchLower
              ? history.filter(
                  (e) =>
                    e.chat.some((c) =>
                      c.question.toLowerCase().includes(searchLower),
                    ) || e.description?.toLowerCase().includes(searchLower),
                )
              : history;
            const saved = filtered.filter((e) => e.type === "manual");
            const recent = filtered.filter((e) => e.type !== "manual");
            const card = (entry: HistoryEntry) => {
              const onDelete = () => {
                if (entry.type === "manual") {
                  setDeleteTarget({
                    id: entry.id,
                    label: entry.chat[0]?.question ?? "this capture",
                  });
                } else {
                  deleteHistory(entry.id);
                }
              };
              return (
                <div key={entry.id} className="history-card">
                  <button
                    className="history-card-body"
                    onClick={() => restoreHistory(entry)}
                  >
                    {entry.screenshot ? (
                      <img
                        className="history-thumb"
                        src={entry.screenshot}
                        alt="capture"
                      />
                    ) : (
                      <div className="history-thumb history-thumb--chat">
                        💬
                      </div>
                    )}
                    <div className="history-info">
                      <div className="history-time">
                        {timeAgo(entry.timestamp)}
                      </div>
                      <div className="history-q">
                        {entry.chat[0]?.question ?? "No questions asked"}
                      </div>
                      <div className="history-meta">
                        {entry.chat.length} Q&amp;A
                      </div>
                    </div>
                    <span className="history-chevron">›</span>
                  </button>
                  <button
                    className="history-delete"
                    onClick={onDelete}
                    title="Delete"
                  >
                    ×
                  </button>
                </div>
              );
            };
            return (
              <div className="history-view">
                <input
                  className="history-search"
                  placeholder="Search captures…"
                  value={historySearch}
                  onChange={(e) => setHistorySearch(e.target.value)}
                />
                {filtered.length === 0 ? (
                  <div className="history-empty">
                    <div className="history-empty-icon">🔍</div>
                    {history.length === 0
                      ? "No captures yet."
                      : "No results for that search."}
                    {history.length === 0 && (
                      <>
                        <br />
                        Captures auto-save when you start a new one,
                        <br />
                        or hit Save manually.
                      </>
                    )}
                  </div>
                ) : (
                  <>
                    {saved.length > 0 && (
                      <div className="history-section history-section--fav">
                        <div className="history-section-label">
                          ★ Favourited
                        </div>
                        {saved.map(card)}
                      </div>
                    )}
                    {recent.length > 0 && (
                      <div className="history-section">
                        <div className="history-section-label">Recent</div>
                        {recent.map(card)}
                      </div>
                    )}
                  </>
                )}
              </div>
            );
          })()}

        {phase === "progress" && (
          <div className="progress-view">
            <div className="level-card">
              <div className="level-row">
                <span className="level-xp">{stats.xp} XP</span>
                {milestone.nextTheme ? (
                  <span className="level-next">
                    Next: {milestone.nextTheme.emoji} {milestone.nextTheme.name}{" "}
                    at {milestone.nextTheme.xpRequired}
                  </span>
                ) : (
                  <span className="level-next">All themes unlocked 🎉</span>
                )}
              </div>
              <div className="xp-bar-track">
                <div
                  className="xp-bar-fill"
                  style={{ width: `${milestone.pct}%` }}
                />
              </div>
              <div className="xp-sub">
                {stats.totalCaptures} captures · {stats.streak.count} day streak
              </div>
            </div>

            <div className="progress-section">
              <div className="progress-section-label">Themes</div>
              <div className="themes-grid">
                {THEMES.map((theme) => {
                  const unlocked = stats.xp >= theme.xpRequired;
                  const active = stats.activeTheme === theme.id;
                  return (
                    <button
                      key={theme.id}
                      className={`theme-chip${active ? " theme-active" : ""}${!unlocked ? " theme-locked" : ""}`}
                      onClick={() => unlocked && setTheme(theme.id)}
                      disabled={!unlocked}
                    >
                      <span className="theme-emoji">{theme.emoji}</span>
                      <span className="theme-name">{theme.name}</span>
                      {!unlocked && (
                        <span className="theme-lock">
                          {theme.xpRequired} XP
                        </span>
                      )}
                      {active && <span className="theme-check">✓</span>}
                    </button>
                  );
                })}
              </div>
              {THEMES.some((t) => stats.xp < t.xpRequired) && (
                <p className="themes-unlock-hint">
                  Capture screens when learning to earn XP and unlock new
                  themes!
                </p>
              )}
            </div>
          </div>
        )}

        {phase === "settings" && (
          <div className="settings-view">
            <div className="settings-card">
              <div className="settings-card-left">
                <div className="settings-card-label">Appearance</div>
                <div className="settings-card-sub">Color mode</div>
              </div>
              <div className="mode-toggle">
                <button
                  className={`mode-btn${stats.colorMode === "dark" ? " mode-active" : ""}`}
                  onClick={() => setColorMode("dark")}
                >
                  🌑 Dark
                </button>
                <button
                  className={`mode-btn${stats.colorMode === "light" ? " mode-active" : ""}`}
                  onClick={() => setColorMode("light")}
                >
                  ☀️ Light
                </button>
              </div>
            </div>
            <div className="settings-card">
              <div className="settings-card-left">
                <div className="settings-card-label">Idle tips</div>
                <div className="settings-card-sub">Show tips while waiting</div>
              </div>
              <button
                className={`toggle-pill${stats.idleTips ? " toggle-on" : ""}`}
                onClick={toggleIdleTips}
                aria-label="Toggle idle tips"
              >
                <span className="toggle-knob" />
              </button>
            </div>
            <div className="settings-card">
              <div className="settings-card-left">
                <div className="settings-card-label">Follow-up suggestions</div>
                <div className="settings-card-sub">Show after each answer</div>
              </div>
              <button
                className={`toggle-pill${stats.showSuggestions ? " toggle-on" : ""}`}
                onClick={toggleSuggestions}
                aria-label="Toggle follow-up suggestions"
              >
                <span className="toggle-knob" />
              </button>
            </div>
            <div className="settings-card">
              <div className="settings-card-left">
                <div className="settings-card-label">Capture shortcut</div>
                <div className="settings-card-sub">Click Change to remap</div>
              </div>
              <div className="settings-shortcut-right">
                {recordingShortcut ? (
                  <div
                    ref={recorderRef}
                    className="shortcut-recorder"
                    tabIndex={0}
                    onKeyDown={handleShortcutKeyDown}
                  >
                    {pendingShortcut ? (
                      <span className="shortcut-preview">
                        {pendingShortcut.display}
                      </span>
                    ) : (
                      <span className="shortcut-hint-text">Type combo…</span>
                    )}
                  </div>
                ) : (
                  <div className="shortcut-current">{shortcutDisplay}</div>
                )}
                {recordingShortcut ? (
                  <div className="shortcut-btns">
                    <button
                      className="shortcut-apply"
                      onClick={applyShortcut}
                      disabled={!pendingShortcut}
                    >
                      Apply
                    </button>
                    <button
                      className="shortcut-cancel"
                      onClick={() => {
                        setRecordingShortcut(false);
                        setPendingShortcut(null);
                      }}
                    >
                      Cancel
                    </button>
                  </div>
                ) : (
                  <button
                    className="shortcut-change"
                    onClick={() => {
                      setRecordingShortcut(true);
                      setTimeout(() => recorderRef.current?.focus(), 20);
                    }}
                  >
                    Change
                  </button>
                )}
              </div>
            </div>
          </div>
        )}

        {phase === "permission" && (
          <div className="idle">
            <div
              className="idle-key"
              style={{
                background: "linear-gradient(145deg,#ff9f0a,#ff6b00)",
                fontSize: 20,
              }}
            >
              🔒
            </div>
            <div className="idle-hint">
              Screen Recording permission needed.
              <br />
              System Settings → Privacy → Screen Recording,
              <br />
              then press <strong>{shortcutDisplay}</strong> again.
            </div>
            <button className="back-btn" onClick={() => setPhase("idle")}>
              OK
            </button>
          </div>
        )}

        {phase === "capture_prompt" &&
          (capturedImage ? (
            <div className="capture-view">
              <div className="chat-you-row">
                <div className="chat-img-bubble">
                  <img src={imgSrc(capturedImage)} alt="captured" />
                </div>
              </div>

              {descLoading && !description && (
                <div className="chat-answer-row">
                  <div className="typing-bubble">
                    <span className="typing-dot" />
                    <span className="typing-dot" />
                    <span className="typing-dot" />
                  </div>
                </div>
              )}
              {description && (
                <div className="chat-answer-row">
                  <div className="chat-answer-bubble">
                    {"This screenshot shows " +
                      description.charAt(0).toLowerCase() +
                      description.slice(1)}
                    <div className="desc-prompt">
                      What would you like to explore?
                    </div>
                  </div>
                </div>
              )}

              {description && !loading && (
                <div className="quick-chips">
                  {QUICK_CHIPS[stats.activeApp].map((chip, j) => (
                    <button
                      key={j}
                      className="quick-chip"
                      onClick={() => handleChipSubmit(chip)}
                    >
                      {chip}
                    </button>
                  ))}
                </div>
              )}

              {loading && (
                <>
                  <div className="chat-you-row">
                    <div className="chat-you-bubble">{question}</div>
                  </div>
                  <div className="chat-answer-row">
                    <div className="typing-bubble">
                      <span className="typing-dot" />
                      <span className="typing-dot" />
                      <span className="typing-dot" />
                    </div>
                  </div>
                </>
              )}
              <div ref={bottomRef} />
            </div>
          ) : (
            <div className="text-only-view">
              {!loading && (
                <div className="text-only-empty">
                  <div className="text-only-icon">{appEmoji}</div>
                  <div className="text-only-hint">
                    Ask me anything about {APP_NAMES[stats.activeApp]}
                  </div>
                </div>
              )}
              {loading && (
                <div className="capture-view">
                  <div className="chat-you-row">
                    <div className="chat-you-bubble">{question}</div>
                  </div>
                  <div className="chat-answer-row">
                    <div className="typing-bubble">
                      <span className="typing-dot" />
                      <span className="typing-dot" />
                      <span className="typing-dot" />
                    </div>
                  </div>
                </div>
              )}
              <div ref={bottomRef} />
            </div>
          ))}

        {phase === "error" && (
          <div className="error-state">
            <div className="error-icon">⚠</div>
            <div className="error-msg">{errorMsg}</div>
            <button className="back-btn" onClick={handleNewCapture}>
              Try again
            </button>
          </div>
        )}

        {phase === "result" && (
          <div className="chat-view">
            <div className="chat-entry">
              {capturedImage && (
                <div className="chat-you-row">
                  <div className="chat-img-bubble">
                    <img src={imgSrc(capturedImage)} alt="captured" />
                  </div>
                </div>
              )}
              {description && (
                <div className="chat-answer-row">
                  <div className="chat-answer-bubble">
                    {"This screenshot shows " +
                      description.charAt(0).toLowerCase() +
                      description.slice(1)}
                  </div>
                </div>
              )}
            </div>

            {chat.map((entry, i) => (
              <div key={i} className="chat-entry">
                <div className="chat-you-row">
                  <div className="chat-you-bubble">{entry.question}</div>
                </div>
                <div className="chat-answer-row">
                  <div className="chat-answer-bubble">
                    <div className="md-content">
                      <ReactMarkdown>{entry.answer}</ReactMarkdown>
                    </div>
                    {entry.imageUrl && (
                      <img
                        className="answer-image"
                        src={entry.imageUrl}
                        alt="reference"
                        onError={(e) => {
                          (e.target as HTMLImageElement).style.display = "none";
                        }}
                      />
                    )}
                    {entry.tip && (
                      <div className="tip-footer">
                        <span className="tip-topic">{entry.tip.topic}</span>
                        <p className="tip-text">{entry.tip.text}</p>
                      </div>
                    )}
                    <button
                      className={`copy-btn${copiedIdx === i ? " copy-btn--copied" : ""}`}
                      onClick={() => copyAnswer(entry.answer, i)}
                    >
                      {copiedIdx === i ? "✓ Copied" : "Copy"}
                    </button>
                  </div>
                </div>
                {i === chat.length - 1 &&
                  suggestions.length > 0 &&
                  !loading &&
                  stats.showSuggestions && (
                    <div className="suggestions">
                      {suggestions.map((s, j) => (
                        <button
                          key={j}
                          className="suggestion-chip"
                          onClick={() => handleSuggestionClick(s)}
                        >
                          {s}
                        </button>
                      ))}
                    </div>
                  )}
              </div>
            ))}

            {loading && (
              <div className="chat-entry">
                <div className="chat-you-row">
                  <div className="chat-you-bubble">{followUp}</div>
                </div>
                <div className="chat-answer-row">
                  <div className="typing-bubble">
                    <span className="typing-dot" />
                    <span className="typing-dot" />
                    <span className="typing-dot" />
                  </div>
                </div>
              </div>
            )}

            <div ref={bottomRef} />
          </div>
        )}
      </div>

      {/* XP milestone toast */}
      {xpToast && (
        <div className="xp-toast">
          <span className="xp-toast-emoji">{xpToast.emoji}</span>
          <div className="xp-toast-body">
            <div className="xp-toast-title">{xpToast.name} unlocked!</div>
            <div className="xp-toast-sub">New theme in Progress</div>
          </div>
        </div>
      )}

      {/* Delete confirmation modal */}
      {deleteTarget && (
        <div className="modal-overlay">
          <div className="modal">
            <div className="modal-title">Delete saved capture?</div>
            <div className="modal-msg">"{deleteTarget.label}"</div>
            <div className="modal-actions">
              <button
                className="modal-cancel"
                onClick={() => setDeleteTarget(null)}
              >
                Cancel
              </button>
              <button
                className="modal-delete"
                onClick={() => {
                  deleteHistory(deleteTarget.id);
                  setDeleteTarget(null);
                }}
              >
                Delete
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Sticky input footer — rendered outside .content so it never scrolls away */}
      {showFooter && (
        <div className="input-footer">
          <form onSubmit={handleFooterSubmit}>
            <div
              className={`input-bar${loading ? " input-bar--disabled" : ""}`}
            >
              <input
                ref={footerRef}
                className="capture-input"
                value={loading ? "" : footerValue}
                onChange={(e) => handleFooterChange(e.target.value)}
                placeholder={footerPlaceholder}
                disabled={loading}
              />
              <button
                type="submit"
                className="send-btn"
                disabled={loading || !footerValue.trim()}
              >
                ↑
              </button>
            </div>
            <div className="capture-actions">
              <button
                type="button"
                className="back-btn"
                onClick={handleNewCapture}
              >
                {phase === "result" ? "← New capture" : "Cancel"}
              </button>
              {phase === "result" && chat.length > 0 && (
                <button
                  type="button"
                  className={`save-btn${sessionSaved ? " save-btn--saved" : ""}`}
                  onClick={saveSession}
                  disabled={loading}
                  title={
                    sessionSaved
                      ? "Click to unfavourite"
                      : "Favourite this session"
                  }
                >
                  {sessionSaved ? "★ Favourited" : "★ Favourite"}
                </button>
              )}
            </div>
          </form>
        </div>
      )}
    </div>
  );
}
