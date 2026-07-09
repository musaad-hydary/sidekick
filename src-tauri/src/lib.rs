use base64::{engine::general_purpose::STANDARD, Engine as _};
use tauri::{Emitter, Manager};
use tauri_plugin_global_shortcut::{Code, GlobalShortcutExt, Modifiers, Shortcut, ShortcutState};

#[cfg(target_os = "macos")]
#[link(name = "CoreGraphics", kind = "framework")]
extern "C" {
    fn CGPreflightScreenCaptureAccess() -> bool;
    fn CGRequestScreenCaptureAccess() -> bool;
}

// ── Commands ──────────────────────────────────────────────────────────────────

#[tauri::command]
async fn capture_region(
    app: tauri::AppHandle,
    x: f64, y: f64, w: f64, h: f64,
) -> Result<String, String> {
    #[cfg(target_os = "macos")]
    {
        let has_perm = unsafe { CGPreflightScreenCaptureAccess() };
        if !has_perm {
            unsafe { CGRequestScreenCaptureAccess() };
            return Err(
                "Screen Recording permission required.\n\
                 Enable Sidekick in System Settings → Privacy & Security → Screen Recording,\n\
                 then press your capture shortcut again.".to_string()
            );
        }
    }

    let path = "/tmp/sidekick_capture.png";
    let _ = std::fs::remove_file(path);

    let overlay = app.get_webview_window("overlay").ok_or("overlay window not found")?;
    let pos   = overlay.outer_position().map_err(|e| e.to_string())?;
    let scale = overlay.scale_factor().map_err(|e| e.to_string())?;

    let sx = (pos.x as f64 / scale) + x;
    let sy = (pos.y as f64 / scale) + y;

    let output = std::process::Command::new("screencapture")
        .args(["-x", "-t", "png",
               "-R", &format!("{},{},{},{}", sx as i32, sy as i32, w as i32, h as i32),
               path])
        .output()
        .map_err(|e| format!("screencapture launch failed: {e}"))?;

    if !output.status.success() {
        let stderr = String::from_utf8_lossy(&output.stderr);
        let msg = stderr.trim();
        return Err(format!(
            "screencapture failed: {}",
            if msg.is_empty() {
                format!("exit {:?} — grant Screen Recording in System Settings", output.status.code())
            } else {
                msg.to_string()
            }
        ));
    }

    let bytes = std::fs::read(path).map_err(|e| format!("could not read capture: {e}"))?;
    let _ = std::fs::remove_file(path);
    Ok(STANDARD.encode(&bytes))
}

#[tauri::command]
async fn show_overlay(app: tauri::AppHandle) -> Result<(), String> {
    if let Some(w) = app.get_webview_window("overlay") {
        w.show().map_err(|e| e.to_string())?;
        w.set_focus().map_err(|e| e.to_string())?;
    }
    Ok(())
}

#[tauri::command]
async fn hide_overlay(app: tauri::AppHandle) -> Result<(), String> {
    if let Some(w) = app.get_webview_window("overlay") {
        w.hide().map_err(|e| e.to_string())?;
    }
    Ok(())
}

#[tauri::command]
async fn move_main_window(app: tauri::AppHandle, x: f64, y: f64) -> Result<(), String> {
    if let Some(w) = app.get_webview_window("main") {
        w.set_position(tauri::LogicalPosition::new(x, y)).map_err(|e| e.to_string())?;
    }
    Ok(())
}

// ── Custom shortcut ───────────────────────────────────────────────────────────

fn do_capture(app: &tauri::AppHandle) {
    #[cfg(target_os = "macos")]
    {
        let has_perm = unsafe { CGPreflightScreenCaptureAccess() };
        if !has_perm {
            unsafe { CGRequestScreenCaptureAccess() };
            if let Some(main) = app.get_webview_window("main") {
                let _ = main.emit("permission_needed", ());
            }
            return;
        }
    }
    if let Some(overlay) = app.get_webview_window("overlay") {
        let _ = overlay.show();
        let _ = overlay.set_focus();
    }
}

fn key_code(s: &str) -> Result<Code, String> {
    match s.to_uppercase().as_str() {
        "A" => Ok(Code::KeyA), "B" => Ok(Code::KeyB), "C" => Ok(Code::KeyC),
        "D" => Ok(Code::KeyD), "E" => Ok(Code::KeyE), "F" => Ok(Code::KeyF),
        "G" => Ok(Code::KeyG), "H" => Ok(Code::KeyH), "I" => Ok(Code::KeyI),
        "J" => Ok(Code::KeyJ), "K" => Ok(Code::KeyK), "L" => Ok(Code::KeyL),
        "M" => Ok(Code::KeyM), "N" => Ok(Code::KeyN), "O" => Ok(Code::KeyO),
        "P" => Ok(Code::KeyP), "Q" => Ok(Code::KeyQ), "R" => Ok(Code::KeyR),
        "S" => Ok(Code::KeyS), "T" => Ok(Code::KeyT), "U" => Ok(Code::KeyU),
        "V" => Ok(Code::KeyV), "W" => Ok(Code::KeyW), "X" => Ok(Code::KeyX),
        "Y" => Ok(Code::KeyY), "Z" => Ok(Code::KeyZ),
        "0" => Ok(Code::Digit0), "1" => Ok(Code::Digit1), "2" => Ok(Code::Digit2),
        "3" => Ok(Code::Digit3), "4" => Ok(Code::Digit4), "5" => Ok(Code::Digit5),
        "6" => Ok(Code::Digit6), "7" => Ok(Code::Digit7), "8" => Ok(Code::Digit8),
        "9" => Ok(Code::Digit9),
        "F1"  => Ok(Code::F1),  "F2"  => Ok(Code::F2),  "F3"  => Ok(Code::F3),
        "F4"  => Ok(Code::F4),  "F5"  => Ok(Code::F5),  "F6"  => Ok(Code::F6),
        "F7"  => Ok(Code::F7),  "F8"  => Ok(Code::F8),  "F9"  => Ok(Code::F9),
        "F10" => Ok(Code::F10), "F11" => Ok(Code::F11), "F12" => Ok(Code::F12),
        _ => Err(format!("unsupported key: {s}")),
    }
}

fn parse_shortcut(s: &str) -> Result<Shortcut, String> {
    let parts: Vec<&str> = s.split('+').collect();
    if parts.is_empty() { return Err("empty shortcut".into()); }

    let key_str  = parts.last().unwrap();
    let mod_strs = &parts[..parts.len() - 1];

    let mut mods = Modifiers::empty();
    for m in mod_strs {
        match m.to_lowercase().as_str() {
            "alt" | "option"             => mods |= Modifiers::ALT,
            "ctrl" | "control"           => mods |= Modifiers::CONTROL,
            "shift"                      => mods |= Modifiers::SHIFT,
            "super" | "cmd" | "command" | "meta" => mods |= Modifiers::SUPER,
            _ => return Err(format!("unknown modifier: {m}")),
        }
    }

    let code = key_code(key_str)?;
    Ok(Shortcut::new(if mods.is_empty() { None } else { Some(mods) }, code))
}

#[tauri::command]
async fn update_shortcut(app: tauri::AppHandle, shortcut_str: String) -> Result<(), String> {
    app.global_shortcut().unregister_all().map_err(|e| e.to_string())?;
    let shortcut = parse_shortcut(&shortcut_str)?;
    app.global_shortcut()
        .on_shortcut(shortcut, |app, _, event| {
            if event.state() != ShortcutState::Pressed { return; }
            do_capture(app);
        })
        .map_err(|e| e.to_string())?;
    Ok(())
}

// ── Ableton visibility ────────────────────────────────────────────────────────

fn frontmost_app() -> String {
    std::process::Command::new("osascript")
        .args(["-e",
            "tell application \"System Events\" \
             to get name of first application process whose frontmost is true"])
        .output()
        .map(|o| String::from_utf8_lossy(&o.stdout).trim().to_string())
        .unwrap_or_default()
}

const TARGET_APPS: &[&str] = &["Live", "Blender", "Figma"];
const TUTOR_APPS:  &[&str] = &["sidekick", "Sidekick"];

fn detect_active_app(front: &str) -> &'static str {
    match front {
        "Live"    => "ableton",
        "Blender" => "blender",
        "Figma"   => "figma",
        _         => "",
    }
}

fn any_target_running() -> bool {
    TARGET_APPS.iter().any(|name| {
        std::process::Command::new("pgrep")
            .args(["-x", name])
            .output()
            .map(|o| o.status.success())
            .unwrap_or(false)
    })
}

fn should_show_for_front(front: &str) -> bool {
    if TARGET_APPS.iter().any(|a| front == *a) { return true; }
    if TUTOR_APPS.iter().any(|a| front == *a)  { return any_target_running(); }
    false
}

fn should_show() -> bool {
    should_show_for_front(&frontmost_app())
}

#[tauri::command]
fn get_active_app() -> String {
    detect_active_app(&frontmost_app()).to_string()
}

// ── App entry point ───────────────────────────────────────────────────────────

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_opener::init())
        .plugin(tauri_plugin_global_shortcut::Builder::default().build())
        .setup(|app| {
            // Position main window bottom-right at startup
            if let Some(main) = app.get_webview_window("main") {
                if let Ok(Some(monitor)) = main.primary_monitor() {
                    let scale  = monitor.scale_factor();
                    let sw     = monitor.size().width  as f64 / scale;
                    let sh     = monitor.size().height as f64 / scale;
                    let win_w  = 340.0_f64;
                    let win_h  = 480.0_f64;
                    let margin = 20.0_f64;
                    let _ = main.set_position(tauri::LogicalPosition::new(
                        sw - win_w - margin,
                        sh - win_h - margin,
                    ));
                }
            }

            let initially_visible = should_show();
            if let Some(main) = app.get_webview_window("main") {
                if !initially_visible { let _ = main.hide(); }
            }

            // Background thread: show/hide based on active app
            let app_handle = app.handle().clone();
            std::thread::spawn(move || {
                let mut was_visible = initially_visible;
                let mut last_app    = String::new();
                loop {
                    std::thread::sleep(std::time::Duration::from_millis(1500));
                    let front   = frontmost_app();
                    let visible = should_show_for_front(&front);

                    // Emit active_app_changed whenever a new target app comes to front
                    let detected = detect_active_app(&front);
                    if !detected.is_empty() && detected != last_app {
                        last_app = detected.to_string();
                        if let Some(main) = app_handle.get_webview_window("main") {
                            let _ = main.emit("active_app_changed", detected);
                        }
                    }

                    if visible != was_visible {
                        if let Some(main) = app_handle.get_webview_window("main") {
                            if visible { let _ = main.show(); }
                            else       { let _ = main.hide(); }
                        }
                        was_visible = visible;
                    }
                }
            });

            // Register default shortcut (Alt+A). The frontend will call
            // update_shortcut on mount if the user saved a different one.
            let shortcut = Shortcut::new(Some(Modifiers::ALT), Code::KeyA);
            app.global_shortcut().on_shortcut(shortcut, |app, _, event| {
                if event.state() != ShortcutState::Pressed { return; }
                do_capture(app);
            })?;

            Ok(())
        })
        .invoke_handler(tauri::generate_handler![
            capture_region,
            show_overlay,
            hide_overlay,
            move_main_window,
            update_shortcut,
            get_active_app,
        ])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
