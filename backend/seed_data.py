"""
Ableton Live teaching tips — the raw knowledge base we load into ChromaDB.

Each entry is a dict with:
  - 'id':      a unique string key (ChromaDB requires this)
  - 'text':    the tip itself — this is what gets embedded and searched
  - 'topic':   metadata tag so we can filter later if we want
"""

ABLETON_TIPS = [
    # ── Arrangement View ────────────────────────────────────────────────────
    {
        "id": "arr_01",
        "topic": "arrangement",
        "text": (
            "The Arrangement View is Ableton's timeline editor — it runs left to right "
            "like a traditional DAW. Each horizontal row is a track. Press Tab to toggle "
            "between Arrangement View and Session View. Use Ctrl+D (Cmd+D on Mac) to "
            "duplicate a selected clip region."
        ),
    },
    {
        "id": "arr_02",
        "topic": "arrangement",
        "text": (
            "To zoom in on the Arrangement View, scroll the mouse wheel while hovering "
            "over the timeline ruler at the top. Hold Ctrl/Cmd while scrolling to zoom "
            "vertically (track height). Press Z to auto-zoom to the selection."
        ),
    },
    {
        "id": "arr_03",
        "topic": "arrangement",
        "text": (
            "Loop a section in the Arrangement View by clicking and dragging on the "
            "scrub area (the bar at the very top). Press Ctrl+L (Cmd+L) to toggle loop. "
            "The yellow loop brace defines what plays when Loop is on."
        ),
    },

    # ── Session View ────────────────────────────────────────────────────────
    {
        "id": "ses_01",
        "topic": "session",
        "text": (
            "Session View is a non-linear performance grid. Each cell contains a clip. "
            "Click a clip's triangle to launch it. The clip keeps looping until you "
            "stop it or launch another. This is Ableton's signature live-performance "
            "workflow."
        ),
    },
    {
        "id": "ses_02",
        "topic": "session",
        "text": (
            "A Scene is an entire horizontal row of clips in Session View. Click the "
            "launch arrow on the right side of a scene to fire all clips in that row "
            "simultaneously. Use scenes to represent song sections (Intro, Verse, Chorus)."
        ),
    },
    {
        "id": "ses_03",
        "topic": "session",
        "text": (
            "Record a live Session View performance into the Arrangement View by pressing "
            "the Arrangement Record button (circle icon in the transport bar). Everything "
            "you trigger in Session View is captured to the timeline."
        ),
    },

    # ── Mixer ───────────────────────────────────────────────────────────────
    {
        "id": "mix_01",
        "topic": "mixer",
        "text": (
            "The Mixer section sits at the bottom of each track (Session View) or on the "
            "right panel. Each track has a volume fader, a pan knob, Solo (S), Mute (the "
            "activator button), and an Arm button (record enable). "
            "Right-click any knob to 'Set to Default' or enter an exact value."
        ),
    },
    {
        "id": "mix_02",
        "topic": "mixer",
        "text": (
            "Send tracks (A, B, C…) let you route audio from multiple tracks into a "
            "shared effects chain — ideal for reverb or delay. Turn up the Send knob on "
            "any track to blend its signal into that Return track. This avoids duplicating "
            "effects on every channel."
        ),
    },
    {
        "id": "mix_03",
        "topic": "mixer",
        "text": (
            "Group tracks by selecting multiple tracks and pressing Ctrl+G (Cmd+G). The "
            "group becomes one collapsible track with a shared volume fader — great for "
            "grouping all drums or all synths and applying bus compression."
        ),
    },
    {
        "id": "mix_04",
        "topic": "mixer",
        "text": (
            "The Master track controls the final output level. Watch the Master meter — "
            "if it clips (goes red), lower the Master fader or use a limiter on the Master "
            "track to prevent distortion. A common starting point is -0.3 dB true peak."
        ),
    },

    # ── Clips ───────────────────────────────────────────────────────────────
    {
        "id": "clip_01",
        "topic": "clips",
        "text": (
            "Double-click any clip to open the Clip View panel at the bottom of the screen. "
            "Here you set loop points, clip gain, transpose, warp mode, and MIDI notes "
            "depending on whether it is an audio or MIDI clip."
        ),
    },
    {
        "id": "clip_02",
        "topic": "clips",
        "text": (
            "Warp mode stretches or squeezes audio to match the project tempo without "
            "changing pitch. Choose the warp algorithm based on the content: "
            "Complex Pro for full mixes, Beats for drums, Tones for monophonic instruments, "
            "Texture for ambient pads."
        ),
    },
    {
        "id": "clip_03",
        "topic": "clips",
        "text": (
            "MIDI clips contain notes you can edit in the Piano Roll (open by "
            "double-clicking a MIDI clip). Draw notes with the pencil tool (B), "
            "select with the pointer (Esc), and delete with Backspace. "
            "Ctrl+A selects all notes."
        ),
    },
    {
        "id": "clip_04",
        "topic": "clips",
        "text": (
            "Clip envelopes let you automate parameters per clip, even in Session View. "
            "In the Clip View, click the 'E' (envelope) button, choose a device/parameter, "
            "and draw automation directly inside the clip — it loops with the clip."
        ),
    },

    # ── Instruments & Devices ───────────────────────────────────────────────
    {
        "id": "dev_01",
        "topic": "devices",
        "text": (
            "Devices (instruments and effects) live in the Device Chain at the bottom of "
            "the screen when a track is selected. Drag any device from the Browser onto a "
            "track to add it. Signal flows left to right through the chain."
        ),
    },
    {
        "id": "dev_02",
        "topic": "devices",
        "text": (
            "Instrument Rack lets you stack multiple instruments on one MIDI track. Each "
            "instrument in the rack can be triggered by a different key range or velocity "
            "range — perfect for split keyboards or layered sounds."
        ),
    },
    {
        "id": "dev_03",
        "topic": "devices",
        "text": (
            "Audio Effect Rack chains effects inside a single device slot with parallel "
            "signal paths (chains). Use the Chain Selector macro to switch between effect "
            "chains on the fly — great for live performance or morphing sounds."
        ),
    },
    {
        "id": "dev_04",
        "topic": "devices",
        "text": (
            "Macro knobs on Racks let you control multiple parameters simultaneously with "
            "one knob. Right-click any parameter inside a rack and choose 'Map to Macro X'. "
            "Then name and assign MIDI to that macro for expressive control."
        ),
    },

    # ── EQ & Compression ────────────────────────────────────────────────────
    {
        "id": "eq_01",
        "topic": "eq",
        "text": (
            "EQ Eight is Ableton's main equalizer. It has 8 bands. Click a band's dot "
            "and drag up/down to boost/cut, left/right to change frequency. "
            "Double-click a dot to enter exact values. Use a High-Pass filter on bass "
            "tracks, Low-Pass on high-frequency heavy elements."
        ),
    },
    {
        "id": "eq_02",
        "topic": "eq",
        "text": (
            "Spectrum is an analyzer device you drop after EQ Eight to visually see "
            "the frequency content in real time. This helps you find problem frequencies "
            "to cut or areas that are too thin to boost. Use it for learning what your "
            "audio actually looks like."
        ),
    },
    {
        "id": "comp_01",
        "topic": "compression",
        "text": (
            "Compressor reduces dynamic range — it turns down loud parts. Key controls: "
            "Threshold (where compression starts), Ratio (how much it compresses), "
            "Attack (how fast it reacts), Release (how fast it lets go). "
            "High ratio + low threshold = heavy compression."
        ),
    },
    {
        "id": "comp_02",
        "topic": "compression",
        "text": (
            "Glue Compressor emulates classic bus compression. Use it on your drum group "
            "or master bus to glue elements together. Start with a 2:1 ratio, medium "
            "attack, auto release. The 'soft knee' setting makes it more transparent."
        ),
    },

    # ── MIDI & Automation ────────────────────────────────────────────────────
    {
        "id": "midi_01",
        "topic": "midi",
        "text": (
            "To record MIDI, arm the track (press the circle Arm button), then press "
            "the session record button or just click a clip slot. Play your MIDI controller "
            "and notes are recorded. Press Shift+Tab to enter overdub mode to layer notes "
            "onto an existing clip."
        ),
    },
    {
        "id": "midi_02",
        "topic": "midi",
        "text": (
            "MIDI mapping: press Ctrl+M (Cmd+M) to enter MIDI Map mode. Click any "
            "on-screen control, then move a physical knob or button. Ableton maps them "
            "permanently. Press Ctrl+M again to exit. Delete maps by selecting the "
            "mapping and pressing Delete."
        ),
    },
    {
        "id": "auto_01",
        "topic": "automation",
        "text": (
            "Automate any parameter in Arrangement View by pressing A to show the "
            "automation lane. Click the parameter name dropdown on the lane to pick what "
            "to automate. Draw breakpoints with the pencil, or record live automation "
            "by enabling the automation arm button."
        ),
    },
    {
        "id": "auto_02",
        "topic": "automation",
        "text": (
            "In Session View, automation is written per-clip using Clip Envelopes. "
            "To automate a device parameter in Session View you must either use a "
            "Clip Envelope or record the automation into the Arrangement View by "
            "recording the entire session."
        ),
    },

    # ── Browser ─────────────────────────────────────────────────────────────
    {
        "id": "brow_01",
        "topic": "browser",
        "text": (
            "The Browser (left panel) is where you find all instruments, effects, "
            "samples, and presets. Press Ctrl+Alt+B (Cmd+Alt+B) to show/hide it. "
            "Drag items directly onto tracks or clip slots. Use the search bar at the "
            "top to find anything by name."
        ),
    },
    {
        "id": "brow_02",
        "topic": "browser",
        "text": (
            "Collections (star tags) let you mark favorite presets and sounds in the "
            "Browser for quick access. Right-click any preset and add it to a collection. "
            "This is a fast way to build a personal library of go-to sounds."
        ),
    },

    # ── Transport & Global ───────────────────────────────────────────────────
    {
        "id": "trans_01",
        "topic": "transport",
        "text": (
            "The Transport Bar at the top controls playback. Spacebar = play/stop. "
            "Shift+Spacebar = play from the last stopped position (instead of returning "
            "to start). F9 arms session recording. The BPM field shows project tempo — "
            "click and drag it to change, or tap the 'TAP' button to set by feel."
        ),
    },
    {
        "id": "trans_02",
        "topic": "transport",
        "text": (
            "The Metronome (click track) is toggled by the metronome icon in the transport. "
            "You can adjust its volume in Preferences → Record/Warp/Launch. "
            "Enable 'Count-in' to get a bar of click before recording starts."
        ),
    },

    # ── Warping & Audio ──────────────────────────────────────────────────────
    {
        "id": "warp_01",
        "topic": "warping",
        "text": (
            "When you drag an audio file into Ableton, it auto-detects tempo and adds "
            "warp markers. Double-click the waveform to open the Clip View. "
            "Warp is on by default. If the file drifts out of time, manually place "
            "warp markers at beat transients to anchor them to the grid."
        ),
    },
    {
        "id": "warp_02",
        "topic": "warping",
        "text": (
            "To pitch-shift audio without changing tempo, use the Transpose knob in "
            "Clip View (semitones) and Detune (cents). For formant-preserving pitch "
            "shifting (vocals, guitars), use Complex Pro warp mode and enable "
            "Formants mode."
        ),
    },

    # ── Max for Live ─────────────────────────────────────────────────────────
    {
        "id": "m4l_01",
        "topic": "max_for_live",
        "text": (
            "Max for Live (M4L) is a visual programming environment built into Ableton "
            "Suite. You can build custom instruments, effects, and MIDI tools as 'patches'. "
            "Browse existing M4L devices in the Browser under 'Max for Live'. "
            "Open and edit patches with the Edit button on any M4L device."
        ),
    },

    # ── Performance tips ────────────────────────────────────────────────────
    {
        "id": "perf_01",
        "topic": "performance",
        "text": (
            "Increase CPU buffer size (Preferences → Audio → Buffer Size) to reduce "
            "audio dropouts during playback/export. Use a smaller buffer (64–128 samples) "
            "when recording (low latency), and a larger buffer (512–1024) during mixing."
        ),
    },
    {
        "id": "perf_02",
        "topic": "performance",
        "text": (
            "Freeze a CPU-heavy track by right-clicking it and choosing 'Freeze Track'. "
            "This renders it to audio temporarily, freeing CPU. To edit it again, "
            "right-click → 'Unfreeze'. Freeze before exporting to reduce load."
        ),
    },

    # ── Tracks — add, delete, rename, organize ───────────────────────────────
    {
        "id": "track_01",
        "topic": "tracks",
        "text": (
            "To add a new track: right-click anywhere in the track list (Session or Arrangement View) "
            "and choose 'Insert MIDI Track', 'Insert Audio Track', or 'Insert Return Track'. "
            "Mac shortcuts: Cmd+Shift+T (MIDI), Cmd+Shift+A (Audio). "
            "Or drag any instrument/sample from the Browser directly onto an empty slot — "
            "Ableton creates the track and loads the instrument automatically."
        ),
    },
    {
        "id": "track_02",
        "topic": "tracks",
        "text": (
            "Rename a track: double-click the track's name label and type a new name, then press Enter. "
            "Change track color: right-click the track name → pick a color from the palette. "
            "Colors are purely visual but help you stay organized when you have many tracks."
        ),
    },
    {
        "id": "track_03",
        "topic": "tracks",
        "text": (
            "Delete a track: click the track to select it, then press Backspace (Delete on Mac). "
            "Confirm the dialog if it appears. To delete multiple tracks, Cmd-click each one "
            "to select them all, then press Backspace. Undo with Cmd+Z if you delete by mistake."
        ),
    },
    {
        "id": "track_04",
        "topic": "tracks",
        "text": (
            "Group tracks: select multiple tracks (Cmd-click each), then press Cmd+G. "
            "They collapse into a single Group Track with a shared volume fader and fold arrow. "
            "Use groups for drums, synths, or any logical set. "
            "Ungroup by selecting the group track and pressing Cmd+Shift+G."
        ),
    },

    # ── Recording ────────────────────────────────────────────────────────────
    {
        "id": "rec_01",
        "topic": "recording",
        "text": (
            "To record audio: select an audio track, click its Arm button (red circle), "
            "set the input source in the track's 'Audio From' dropdown (e.g., Ext. In 1/2), "
            "then press the global Record button in the transport bar (or F9). "
            "A new clip appears in the first available slot. Stop recording with the spacebar."
        ),
    },
    {
        "id": "rec_02",
        "topic": "recording",
        "text": (
            "Count-in before recording: go to Preferences → Record/Warp/Launch → "
            "enable 'Count-In' and set the number of bars. "
            "This gives you time to get ready before the recording actually starts. "
            "The metronome click plays during count-in automatically."
        ),
    },

    # ── Routing & sends ───────────────────────────────────────────────────────
    {
        "id": "route_01",
        "topic": "routing",
        "text": (
            "Return tracks receive signal from any track's Send knob (labeled A, B, C…). "
            "Put shared effects like reverb or delay on a Return track. "
            "Turn up a track's Send A knob to blend that track into Return A's reverb. "
            "This is more efficient than inserting reverb on every track separately."
        ),
    },
    {
        "id": "route_02",
        "topic": "routing",
        "text": (
            "Side-chain compression: on the Compressor device, click the triangle at the top "
            "to expand it, then enable 'Sidechain' and set 'Audio From' to the kick drum track. "
            "The compressor now pumps to the kick rhythm — the classic dance music ducking effect."
        ),
    },

    # ── Instruments ──────────────────────────────────────────────────────────
    {
        "id": "inst_01",
        "topic": "instruments",
        "text": (
            "Operator is Ableton's FM synthesizer. It has 4 oscillators (A, B, C, D) that can "
            "modulate each other. Change the algorithm (how operators connect) in the Algorithm "
            "display. Oscillator A is usually the 'carrier' (what you hear); B, C, D are "
            "'modulators' (add FM harmonics). Increase B's Coarse pitch to create metallic sounds."
        ),
    },
    {
        "id": "inst_02",
        "topic": "instruments",
        "text": (
            "Simpler is a single-sample player. Drag any audio file onto a MIDI track to load it "
            "into Simpler automatically. Use the Start/End knobs to trim the sample, "
            "Loop mode to loop it, and the Transpose knob to pitch it. "
            "Press 'C' in Simpler's top-left to switch to Classic (chromatic) mode."
        ),
    },
    {
        "id": "inst_03",
        "topic": "instruments",
        "text": (
            "Drum Rack is a container that holds up to 128 sample pads. "
            "Drag samples from the Browser onto any pad to assign them. "
            "Each pad has its own pitch, volume, and a mini-chain with insert effects. "
            "Right-click a pad → 'Extract Chain' to edit that drum sound in detail."
        ),
    },

    # ── Effects & plugins ─────────────────────────────────────────────────────
    {
        "id": "fx_01",
        "topic": "effects",
        "text": (
            "Add an effect to a track: open the Browser, click 'Audio Effects', "
            "find the device you want, then double-click it (or drag it) onto the track. "
            "It appears at the bottom in the device chain. "
            "Multiple effects chain left-to-right — order matters (EQ before or after compressor "
            "produces different results)."
        ),
    },
    {
        "id": "fx_02",
        "topic": "effects",
        "text": (
            "Reverb: adds space and depth. Key controls — Decay Time (how long it rings), "
            "Dry/Wet (how much reverb blends in), Pre-Delay (gap before reverb starts — "
            "adds clarity to the dry sound). For vocals, try Decay ~1.5s, Pre-Delay ~20ms, "
            "Dry/Wet ~25%. Use a Return track for reverb shared across multiple instruments."
        ),
    },
    {
        "id": "fx_03",
        "topic": "effects",
        "text": (
            "Delay: repeats the signal at a set interval. Echo and Delay are Ableton's two "
            "main delay devices. Set Sync to On to lock delay time to project BPM (e.g. 1/8 = "
            "eighth-note echo). Feedback controls how many repeats you hear. "
            "Filter the delayed signal with the built-in high-pass filter to keep it from "
            "muddying the low end."
        ),
    },
    {
        "id": "fx_04",
        "topic": "effects",
        "text": (
            "Utility is a small but powerful device. Use it to change volume by dB, "
            "invert a channel's phase (flip polarity), make a stereo signal mono (Width → 0%), "
            "or hard-pan channels. Very useful at the end of effect chains or on the Master track."
        ),
    },

    # ── Clip editing ──────────────────────────────────────────────────────────
    {
        "id": "clip_05",
        "topic": "clips",
        "text": (
            "Consolidate clips: select a range in Arrangement View (click-drag on the timeline), "
            "then press Cmd+J. All clips in the selection become one single clip. "
            "Useful for bouncing a complex arrangement section into a tidy clip. "
            "This does NOT apply effects — use Export or Freeze+Flatten for that."
        ),
    },
    {
        "id": "clip_06",
        "topic": "clips",
        "text": (
            "Split a clip: in Arrangement View, place the playhead where you want to cut, "
            "then press Cmd+E (Split). The clip splits into two separate clips at that point. "
            "Or right-click → Split. Use this to chop up audio, remove a bad section, "
            "or rearrange parts of a recording."
        ),
    },

    # ── Piano Roll / MIDI editing ─────────────────────────────────────────────
    {
        "id": "pr_01",
        "topic": "midi",
        "text": (
            "In the Piano Roll, quantize notes to the grid: select all notes (Cmd+A), "
            "then press Cmd+U to quantize to the current grid setting. "
            "Adjust quantize amount via the % knob that appears — 100% snaps perfectly, "
            "50% moves notes halfway toward the grid (preserves some humanization)."
        ),
    },
    {
        "id": "pr_02",
        "topic": "midi",
        "text": (
            "Draw chords in the Piano Roll: hold Shift while drawing a note to add additional "
            "notes at the same start position. Or select a note and press Shift+Up/Down arrow "
            "to add an interval (semitone). Shift+Ctrl+Up adds an octave above simultaneously."
        ),
    },
    {
        "id": "pr_03",
        "topic": "midi",
        "text": (
            "Note velocity in the Piano Roll: the thin bars at the bottom show velocity "
            "(how hard each note plays, 1–127). Click and drag a velocity bar to change it. "
            "Select multiple notes then drag any bar to move them all relatively. "
            "Random velocity humanizes mechanical-sounding sequences."
        ),
    },

    # ── Export & bounce ───────────────────────────────────────────────────────
    {
        "id": "export_01",
        "topic": "export",
        "text": (
            "Export your mix: go to File → Export Audio/Video (Cmd+Shift+R). "
            "Set 'Rendered Track' to Master to export the full mix. "
            "Choose WAV 24-bit for best quality, or MP3 for sharing. "
            "Enable 'Normalize' if your master is too quiet. "
            "The export renders in real-time unless you freeze CPU-heavy tracks first."
        ),
    },
    {
        "id": "export_02",
        "topic": "export",
        "text": (
            "Stem export (individual tracks): in the Export dialog, change 'Rendered Track' "
            "to 'All Individual Tracks'. Each track exports as its own audio file. "
            "Stems are used for sending tracks to collaborators, remixers, or mastering engineers."
        ),
    },

    # ── Live 12 new features ──────────────────────────────────────────────────
    {
        "id": "live12_01",
        "topic": "live12",
        "text": (
            "MIDI Transformations (Live 12): in the Piano Roll, right-click selected notes "
            "to access transformations — Arpeggiate, Strum, Connect, Ornament, Recombine. "
            "These generate new melodic variations from existing notes. "
            "'Connect' fills gaps between notes with generated passing notes in the current scale."
        ),
    },
    {
        "id": "live12_02",
        "topic": "live12",
        "text": (
            "Scale Mode (Live 12): in the Piano Roll header, enable 'Scale' and choose a root "
            "note + scale type (Major, Minor, Dorian, etc.). Notes outside the scale are "
            "grayed out on the piano keyboard, making it easy to draw only in-key notes. "
            "The scale also applies to Push pad layout and MIDI clip clips globally if set on the Master."
        ),
    },
    {
        "id": "live12_03",
        "topic": "live12",
        "text": (
            "Roar (Live 12): Ableton's new saturation/distortion device. It has three stages "
            "of saturation (each with its own character and drive), a noise generator, and "
            "a built-in filter. Roar can be used subtly for tape warmth or cranked for "
            "aggressive distortion. Try 'Feedback' mode for self-oscillating filter sounds."
        ),
    },
    {
        "id": "live12_04",
        "topic": "live12",
        "text": (
            "Meld (Live 12): a hybrid synthesizer combining wavetable and FM synthesis. "
            "It has two oscillators — each can be in Wavetable, Analog (classical), or FM mode. "
            "Drag on the wavetable display to morph through the wavetable. "
            "Assign macros to automate morphing in real time for evolving pads and leads."
        ),
    },

    # ── MIDI Effects ──────────────────────────────────────────────────────────────
    {
        "id": "mfx_01",
        "topic": "midi_effects",
        "text": (
            "Arpeggiator (MIDI Effect): auto-plays the notes of a held chord in a sequence. "
            "Style sets the note order (Up, Down, Up/Down, Random). Rate sets arpeggiation speed — "
            "sync it to the project BPM for musical results. Gate controls note length (shorter = more staccato). "
            "Transpose lets it shift pitch each cycle for evolving melodic patterns."
        ),
    },
    {
        "id": "mfx_02",
        "topic": "midi_effects",
        "text": (
            "Chord MIDI Effect stacks additional intervals above each note you play. "
            "Add up to six Shift values (in semitones) to turn single notes into full chords automatically. "
            "Shift +4 and +7 gives a major triad; +3 and +7 gives minor. "
            "Combine with Arpeggiator to arpeggiate generated chords for instant melodic complexity."
        ),
    },
    {
        "id": "mfx_03",
        "topic": "midi_effects",
        "text": (
            "Scale MIDI Effect constrains incoming MIDI to a musical scale, "
            "remapping out-of-scale notes to the nearest in-scale note. "
            "Set the Root and the Scale type (Major, Minor, Dorian, Pentatonic, etc.). "
            "Play any notes freely — the Scale effect makes them always sound 'right'. "
            "Great for live improvisation or generative sequences."
        ),
    },
    {
        "id": "mfx_04",
        "topic": "midi_effects",
        "text": (
            "Note Length MIDI Effect controls how long notes play regardless of how long you hold them. "
            "Sync to project time (e.g. 1/8) for rhythmically precise gates. "
            "Combined with a Reverb or long pad sound, short gated notes create the classic 'pump' effect. "
            "Gate value below 100% shortens notes; above 100% makes them overlap (legato)."
        ),
    },
    {
        "id": "mfx_05",
        "topic": "midi_effects",
        "text": (
            "Random MIDI Effect adds controlled randomness to pitch, velocity, or chance. "
            "Chance below 100% randomly silences notes — great for sparse, organic hi-hat patterns. "
            "Set to affect Pitch for slightly out-of-tune notes that feel more human. "
            "Scale the Amount low (1–5 semitones) so randomness enhances rather than destroys the melody."
        ),
    },
    {
        "id": "mfx_06",
        "topic": "midi_effects",
        "text": (
            "Velocity MIDI Effect remaps incoming note velocity. "
            "Use the Out Hi/Low to compress the velocity range (e.g. 80–110) for a more even sound. "
            "Random adds velocity humanization. Drive mode (input multiplied) can make quiet notes louder. "
            "Chain after Arpeggiator to give arpeggio notes a velocity curve — louder on beat 1, softer fills."
        ),
    },

    # ── Follow Actions ───────────────────────────────────────────────────────────
    {
        "id": "follow_01",
        "topic": "follow_actions",
        "text": (
            "Follow Actions tell a clip what to do when it finishes playing — "
            "in Session View only. Options: Stop, Play Again, Play Next, Play Previous, Play First, "
            "Play Last, Play Any, Play Other. Set in the clip's Launch tab. "
            "Chance A and B set probabilities for two different actions, enabling randomized sequences."
        ),
    },
    {
        "id": "follow_02",
        "topic": "follow_actions",
        "text": (
            "Chain clips with Follow Actions to build generative song structures. "
            "Clip A plays once then 'Play Next' to Clip B, Clip B has 80% 'Play Next' and 20% 'Play Any'. "
            "This gives a song that roughly follows a structure but occasionally jumps — "
            "perfect for ambient generative music or game audio that never repeats exactly."
        ),
    },

    # ── Capture & Comping ─────────────────────────────────────────────────────────
    {
        "id": "capture_01",
        "topic": "capture",
        "text": (
            "Capture MIDI (Cmd+Shift+C): Ableton always listens to armed MIDI tracks even when not recording. "
            "If you play something great without recording, press Capture and Live creates a clip "
            "from what you just played — never lose a spontaneous idea again. "
            "Works in both Session and Arrangement View."
        ),
    },
    {
        "id": "comping_01",
        "topic": "comping",
        "text": (
            "Comping (Live 11+): record multiple takes into the Arrangement View with loop recording. "
            "Each pass creates a new Take Lane below the main track. "
            "Click individual regions in the Take Lanes to select the best sections from each take. "
            "Ableton stitches selected sections into a composite clip automatically."
        ),
    },

    # ── Audio to MIDI ─────────────────────────────────────────────────────────────
    {
        "id": "audio2midi_01",
        "topic": "audio_to_midi",
        "text": (
            "Convert audio to MIDI: right-click an audio clip in the Arrangement or Session View and choose "
            "'Convert to New MIDI Track'. Options: Convert Harmony (chords), Convert Melody (monophonic), "
            "Convert Drums (transient detection). Ableton analyses the audio and generates a MIDI clip — "
            "great for transcribing recorded performances or repitching samples."
        ),
    },
    {
        "id": "audio2midi_02",
        "topic": "audio_to_midi",
        "text": (
            "Live 12 MIDI from audio improvements: the Convert Melody option now uses ML to detect pitch "
            "more accurately, including vibrato and portamento. "
            "After conversion, the MIDI clip is fully editable in the Piano Roll. "
            "Load a different instrument on the new MIDI track to instantly retimbre the melody."
        ),
    },

    # ── Groove Pool ──────────────────────────────────────────────────────────────
    {
        "id": "groove_01",
        "topic": "groove",
        "text": (
            "The Groove Pool (Show/Hide Groove Pool in the View menu) applies rhythmic feel to clips. "
            "Drag any .agr groove file or a clip's warp markers onto the Groove Pool, "
            "then drag the groove onto any clip to apply it. "
            "Timing shifts the note timing; Random adds micro-variations; Velocity affects hit strength."
        ),
    },
    {
        "id": "groove_02",
        "topic": "groove",
        "text": (
            "Extract Groove from a clip: drag any audio or MIDI clip into the Groove Pool. "
            "Live analyses its timing and creates a groove template from it. "
            "Apply that groove to other clips to make them swing and feel like the original. "
            "Great for locking new elements to the feel of a drumloop."
        ),
    },

    # ── Push Integration ─────────────────────────────────────────────────────────
    {
        "id": "push_01",
        "topic": "push",
        "text": (
            "Push 2/3 integrates deeply with Ableton Live. In Note mode the 8×8 pad grid plays "
            "notes in a selected scale — the root note is always highlighted in a brighter colour. "
            "The layout repeats every 4 semitones across rows so the same shape always produces "
            "the same interval, making scale-based playing intuitive without knowing theory."
        ),
    },
    {
        "id": "push_02",
        "topic": "push",
        "text": (
            "Push drum sequencer: switch to Drum mode and the grid shows 16 steps per row. "
            "Press pads to place drum hits. Hold a step pad and press note pads to set note length. "
            "Turn an encoder while holding a step to adjust velocity. "
            "Navigate to different 16-step pages with the left/right arrows for longer patterns."
        ),
    },
    {
        "id": "push_03",
        "topic": "push",
        "text": (
            "Browse and load sounds directly on Push: press Browse, turn the encoder to navigate "
            "categories and presets, press the encoder to load. "
            "Push 3 (standalone) can run Ableton without a computer — record ideas, browse library, "
            "mix tracks over USB power. Sync to a full Live session when you're back at the desk."
        ),
    },

    # ── More Devices ─────────────────────────────────────────────────────────────
    {
        "id": "dev_drum_01",
        "topic": "devices",
        "text": (
            "Drum Buss (Audio Effect): a dedicated processor for tightening drum buses. "
            "Transient controls boost attack; Boom adds sub-bass resonance (tune it to the kick pitch); "
            "Crunch adds harmonic drive; Dry/Wet blends the effect. "
            "Insert it on a Drum Rack return or drum group bus for glue and punch without heavy compression."
        ),
    },
    {
        "id": "dev_echo_01",
        "topic": "devices",
        "text": (
            "Echo is Ableton's premium delay. It has separate left/right delay lines (L/R time, sync, filter), "
            "a Modulation section (chorus/wobble on the repeats), a Reverb inside the feedback path, "
            "and a Noise/Gate generator. Set L and R to different sync divisions for wide stereo echoes. "
            "Gate mode only outputs echo when input signal is present — prevents tail buildup."
        ),
    },
    {
        "id": "dev_pedal_01",
        "topic": "devices",
        "text": (
            "Pedal emulates guitar stompbox distortions: Overdrive (warm, tube-like), "
            "Distortion (harder clipping), Fuzz (asymmetric, gated). "
            "Tone control shapes the high-frequency content post-clipping. "
            "Stack Pedal before an amp simulation or Saturator for layered distortion. "
            "Particularly good on bass for adding grit without losing low end."
        ),
    },
    {
        "id": "dev_resonators_01",
        "topic": "devices",
        "text": (
            "Resonators runs the signal through up to five parallel comb filters tuned to musical intervals. "
            "Set the root note (I) and the intervals of II–V relative to it. "
            "Polarity controls phase relationships between resonators — alters the timbre drastically. "
            "Feed noise, transients, or any audio in for pitched metallic textures; "
            "automate the Pitch knob for sweeping resonant effects."
        ),
    },
    {
        "id": "dev_spectral_01",
        "topic": "devices",
        "text": (
            "Spectral Resonator and Spectral Blur (Live 11+) are FFT-based effects. "
            "Spectral Resonator adds pitched resonance to any signal — tune it to a key for harmonic enhancement. "
            "Spectral Blur smears audio in the frequency domain for ghostly, time-stretched textures. "
            "Both have Freeze parameters: Freeze captures the current spectral snapshot indefinitely — "
            "great for ambient drones from drum hits or vocal snippets."
        ),
    },

    # ── Routing Advanced ─────────────────────────────────────────────────────────
    {
        "id": "route_adv_01",
        "topic": "routing",
        "text": (
            "External Instrument device lets you route MIDI out to hardware synths and return their audio "
            "in the same device chain — no separate audio track needed. "
            "Set MIDI To (your interface MIDI port) and Audio From (the input your synth returns on). "
            "Latency compensation is built in. Live treats external hardware like any plugin."
        ),
    },
    {
        "id": "route_adv_02",
        "topic": "routing",
        "text": (
            "Multiple outputs from Drum Rack: click the Chain List button (arrow icon) in the Drum Rack, "
            "then enable 'Audio To' per pad. Each pad can route to its own track for individual compression, "
            "EQ, and send processing. Right-click a pad > 'Extract Chain' to convert it to a full track."
        ),
    },
    {
        "id": "route_adv_03",
        "topic": "routing",
        "text": (
            "Resampling: set any audio track's input to 'Resampling' to record the master output back to a clip. "
            "This bounces your entire mix in real time without exporting. "
            "Use it to capture a complex effects chain or a live performance into a single audio clip — "
            "then manipulate it further as audio."
        ),
    },

    # ── Crossfader & DJ ───────────────────────────────────────────────────────────
    {
        "id": "xfade_01",
        "topic": "crossfader",
        "text": (
            "The Crossfader (Session View mixer) fades between tracks assigned to sides A and B. "
            "Assign any track by clicking the A/B buttons below its volume fader. "
            "Automate the crossfader in Arrangement View for smooth DJ-style transitions. "
            "In Preferences > Record/Warp/Launch, set the crossfader curve (linear, constant power, etc.)."
        ),
    },

    # ── Latency & Performance ────────────────────────────────────────────────────
    {
        "id": "lat_01",
        "topic": "latency",
        "text": (
            "Reduced Latency When Monitoring (Live 11+): right-click any device in the chain and enable "
            "'Reduced Latency'. This bypasses delay compensation for that device only, "
            "reducing monitoring latency for live input at the cost of track alignment. "
            "Useful for performing through a plug-in live while other tracks stay compensated."
        ),
    },
    {
        "id": "lat_02",
        "topic": "latency",
        "text": (
            "Delay Compensation: Ableton automatically compensates for latency introduced by plugins — "
            "the entire mix stays aligned. Check Preferences > Audio > Delay Compensation is on. "
            "High-latency plugins (convolution reverbs) delay the whole chain; check the reported delay "
            "in the plug-in's title bar (ms value). Freeze heavy tracks to reduce total plugin load."
        ),
    },

    # ── Ableton Link ─────────────────────────────────────────────────────────────
    {
        "id": "link_01",
        "topic": "link",
        "text": (
            "Ableton Link (Enable Link in the top bar) syncs tempo and phase across multiple Live instances "
            "or Link-compatible apps (Koala, Loopy Pro, GarageBand) on the same network — "
            "no MIDI cable required. All peers share a common beat clock. "
            "Change tempo on any device and all others follow instantly."
        ),
    },

    # ── Wavetable Synth ──────────────────────────────────────────────────────────
    {
        "id": "wavetable_01",
        "topic": "instruments",
        "text": (
            "Wavetable synthesizer has two oscillators each with a wavetable, sub-oscillator, and noise source. "
            "Drag the Position knob to morph through frames in the wavetable — automate this for evolving timbres. "
            "Matrix modulation: any source (LFO, envelope, velocity, MPE) can route to any target via the matrix. "
            "Enable Poly > Unison for thick detuned voices."
        ),
    },
    {
        "id": "wavetable_02",
        "topic": "instruments",
        "text": (
            "Drift synthesizer (Live 12) is an analogue-modeled synth with intentional imperfections. "
            "Drift amount controls how much each voice drifts in pitch and timbre over time — "
            "higher values give a warm, unstable vintage character. "
            "Two oscillators with classic waveforms, filter, envelopes, LFO, and an Effects section "
            "with built-in chorus, delay, and reverb routing."
        ),
    },

    # ── Clip & Scene Tricks ──────────────────────────────────────────────────────
    {
        "id": "clip_trick_01",
        "topic": "clips",
        "text": (
            "Clip gain (waveform view): the small gain knob in the Clip View adjusts clip volume pre-effects. "
            "Right-click a clip > Normalize to set the gain so the peak hits 0 dB. "
            "Clip gain doesn't add a device — it's metadata on the clip itself, "
            "so it's great for volume-matching imported samples without touching the mixer."
        ),
    },
    {
        "id": "clip_trick_02",
        "topic": "clips",
        "text": (
            "Scene tempo and time signature: right-click any Scene and set a tempo and time signature. "
            "When the scene launches, Live jumps to that tempo and meter — "
            "build a set list where each song section has its own BPM "
            "and transitions happen automatically when you advance to the next scene."
        ),
    },

    # ── Max for Live (expanded) ──────────────────────────────────────────────────
    {
        "id": "m4l_02",
        "topic": "max_for_live",
        "text": (
            "Max for Live LFO device (found in Max for Live > LFO): a free-running modulator "
            "that maps to any parameter in Live via MIDI Map or directly. "
            "Set the Rate (synced or free), Shape (sine, square, saw, random), and Depth. "
            "Drag the 'Map' button to any knob to modulate it continuously — "
            "far more flexible than clip envelope automation."
        ),
    },
    {
        "id": "m4l_03",
        "topic": "max_for_live",
        "text": (
            "Max for Live Envelope Follower: analyses the amplitude of any audio signal and "
            "maps it to any parameter. Classic use: sidechain compress a pad's filter cutoff "
            "from a kick drum — the filter opens on every kick hit without a traditional compressor. "
            "Found in Max for Live > Envelope Follower."
        ),
    },
    {
        "id": "m4l_04",
        "topic": "max_for_live",
        "text": (
            "Max for Live MIDI Monitor shows every incoming MIDI message in real time — "
            "notes, CCs, aftertouch, pitch bend, SysEx. Essential for debugging controller mappings "
            "or understanding what a hardware device is sending. "
            "Place it before other MIDI effects in the chain to inspect raw input."
        ),
    },
    {
        "id": "m4l_05",
        "topic": "max_for_live",
        "text": (
            "Building a M4L patch: double-click a Max device to open the patch editor. "
            "Live objects are prefixed with 'live.' — live.dial, live.button, live.slider create UI controls. "
            "Connect to parameters via live.remote~ or live.path. "
            "Press the lock icon to toggle between edit and performance mode. "
            "Save the patch inside the device to update it everywhere it's used in the project."
        ),
    },
    {
        "id": "m4l_06",
        "topic": "max_for_live",
        "text": (
            "Max for Live Step Sequencer (CV Instrument family): sends rhythmic gate and pitch signals "
            "to hardware synthesizers or modular systems via audio interface DC-coupled outputs. "
            "Max for Live CV Tools (available as a free pack from Ableton) includes CV Instrument, "
            "CV Triggers, CV Clock Out, CV Utility — a complete modular bridge inside Live."
        ),
    },

    # ── More Instruments ─────────────────────────────────────────────────────────
    {
        "id": "inst_analog",
        "topic": "instruments",
        "text": (
            "Analog synthesizer emulates a classic two-oscillator subtractive analogue synth. "
            "OSC 1 and 2 offer Sine, Square, Saw, Tri, Noise. "
            "Two filters (LPF/HPF/BPF/Notch) can run serial or parallel. "
            "Two ADSR envelopes and two LFOs with multiple routing targets. "
            "Drive knob adds input saturation before the filter. Good for basses, leads, and classic pads."
        ),
    },
    {
        "id": "inst_impulse",
        "topic": "instruments",
        "text": (
            "Impulse is an 8-slot drum machine sampler. Each slot holds one sample with its own "
            "pitch, decay, saturation, filter, pan, and volume. "
            "Stretch: on keeps original pitch when Decay changes; off lets decay affect pitch. "
            "Global controls Transpose affect all pads. Impulse responds to MIDI: "
            "pads map to C1–G#1 by default. Load full drum kits from the Browser."
        ),
    },
    {
        "id": "inst_tension",
        "topic": "instruments",
        "text": (
            "Tension models string instruments physically — guitar, bass, harp, violin strings. "
            "Excitator controls how the string is set into motion (bow, hammer, plectrum, blow). "
            "String parameters (stiffness, inharmonicity) tune the overtone character. "
            "Damping and Termination affect how the string stops vibrating. "
            "Use bowing on long decay for cello-like tones; hammer+bright stiffness for piano-like attack."
        ),
    },
    {
        "id": "inst_electric",
        "topic": "instruments",
        "text": (
            "Electric models vintage electric pianos (Rhodes, Wurlitzer-style). "
            "Mallet controls hardness and tone of the hammer strike — softer for warm jazz tones, "
            "harder for bright funk. Tine/Fork is the resonating element; pickups convert vibration to signal. "
            "Damper pedal (sustain CC 64) toggles damping. Add a chorus and tremolo effect for classic Rhodes feel."
        ),
    },
    {
        "id": "inst_collision",
        "topic": "instruments",
        "text": (
            "Collision models physically the collision between two objects — mallet-on-surface. "
            "Mallet section models the striking object (hardness, velocity tracking). "
            "Resonator models the struck object (material, size, decay, pitch). "
            "Great for mallet instruments (marimba, vibraphone), bells, metals, body percussion. "
            "Dual resonators can be in parallel or series for complex timbres."
        ),
    },
    {
        "id": "inst_corpus",
        "topic": "instruments",
        "text": (
            "Corpus (Audio Effect, not instrument) applies the resonance of a physical object to any audio signal. "
            "It is essentially the resonator section of Collision as a standalone effect. "
            "Run a drum loop through Corpus tuned to a note to pitch the transients; "
            "run noise through it for a tuned percussion sound. "
            "Sidechain it from a kick to create a resonant pitched 'thud' effect."
        ),
    },

    # ── More Effects ─────────────────────────────────────────────────────────────
    {
        "id": "fx_vocoder",
        "topic": "effects",
        "text": (
            "Vocoder in Ableton: use the Vocoder MIDI effect on a MIDI track or Vocoder audio effect. "
            "The carrier signal (synthesizer/noise) is shaped by the formants of the modulator signal (voice). "
            "Route a vocal via 'Sidechain > Audio From' and set a synth as the carrier. "
            "More formant bands = clearer intelligibility. Classic robot voice: carrier = sawtooth, "
            "hold chords on keyboard while speaking into the mic."
        ),
    },
    {
        "id": "fx_redux",
        "topic": "effects",
        "text": (
            "Redux applies bit-crushing and sample-rate reduction — the sound of vintage lo-fi samplers. "
            "Bit Depth knob: 24 = clean digital, 8 = noticeable crunch, 4 = extreme lo-fi. "
            "Sample Rate Downsample reduces the effective sample rate for aliasing artefacts. "
            "Mode: Hard clips at quantisation boundaries; Soft rounds edges for a warmer crunch. "
            "Redux is subtle on full mixes but dramatic on individual elements."
        ),
    },
    {
        "id": "fx_vinyl",
        "topic": "effects",
        "text": (
            "Vinyl Distortion emulates the non-linearities of vinyl playback: "
            "Tracing Model adds harmonic distortion from the stylus tracking curves; "
            "Pinch creates odd harmonics at low frequencies (warmth). "
            "Crackle adds vinyl noise — set Density and Volume. "
            "Wear simulates a degraded record. Use on the master bus at low Dry/Wet for lo-fi warmth."
        ),
    },
    {
        "id": "fx_ringmod",
        "topic": "effects",
        "text": (
            "Ring Modulator multiplies the audio signal by a carrier sine wave, producing sum and difference "
            "sidebands — the input pitch disappears and new metallic frequencies appear. "
            "Set Frequency to create dissonant textures; sync it to pitch via MIDI note input. "
            "Fixed Frequency on a melodic line creates a robotic tone. "
            "Low frequencies on the carrier produce tremolo; sub-audio rates produce ring modulation timbres."
        ),
    },
    {
        "id": "fx_freqshift",
        "topic": "effects",
        "text": (
            "Frequency Shifter moves all frequencies up or down by a fixed Hz amount (not semitones). "
            "Shifting 5–20Hz creates subtle Doppler-like motion; larger amounts destroy pitch relationships "
            "for experimental textures. Dual mode splits the signal into two shifters with independent detune "
            "for wide stereo effects. Ring mode outputs only the difference frequency — similar to Ring Modulator."
        ),
    },
    {
        "id": "fx_erosion",
        "topic": "effects",
        "text": (
            "Erosion degrades audio by modulating it with noise or a sine wave. "
            "Wide: broadband noise modulation — high-frequency sizzle and static. "
            "Narrow: sine wave modulation at a specific frequency — aliased digital artefacts. "
            "Use on hi-hats for a crushed, distressed texture; on pads for subtle digital grunge. "
            "Frequency knob targets which range gets eroded most."
        ),
    },
    {
        "id": "fx_gate",
        "topic": "effects",
        "text": (
            "Gate silences the signal when it falls below a threshold. "
            "Threshold sets the level below which the gate closes. "
            "Attack controls how fast the gate opens; Release how fast it closes. "
            "Hold keeps the gate open for a minimum time even if signal drops. "
            "Flip mode inverts the gate — useful for keying effects to the gaps between notes."
        ),
    },
    {
        "id": "fx_limiter",
        "topic": "effects",
        "text": (
            "Limiter is a brick-wall ceiling — nothing passes above the Ceiling value. "
            "Use it as the last device on the Master track to prevent clipping for streaming/distribution. "
            "Set Ceiling to -1.0 dBFS for a small true-peak headroom. "
            "Lookahead (1.5ms default) lets the limiter anticipate transients and react before they clip. "
            "Unlike a compressor, a limiter's ratio is effectively infinite — it's an absolute ceiling."
        ),
    },
    {
        "id": "fx_multiband",
        "topic": "effects",
        "text": (
            "Multiband Dynamics splits the signal into three frequency bands and applies independent "
            "compression/expansion to each. Low, Mid, High bands have their own threshold, ratio, attack, release. "
            "Ideal for mastering: compress lows for tight bass, leave mids fairly open, "
            "gently compress highs for air control. 'Below threshold' mode expands quiet parts upward (upward compression)."
        ),
    },
    {
        "id": "fx_convolution",
        "topic": "effects",
        "text": (
            "Convolution Reverb (available as a M4L device or via third-party) uses impulse responses "
            "recorded from real spaces — concert halls, plates, springs, cathedrals. "
            "The impulse response is convolved with the audio to place it in that exact acoustic space. "
            "Ableton's Hybrid Reverb (Live 11+) combines algorithmic and convolution reverb in one device — "
            "use Convolution for realism and add algorithmic tail for control."
        ),
    },
    {
        "id": "fx_hybrid_reverb",
        "topic": "effects",
        "text": (
            "Hybrid Reverb blends a convolution section (real impulse responses) with an algorithmic section. "
            "ER (Early Reflections) from the IR gives the room's character; "
            "the algorithmic Tail provides a smooth, controllable decay. "
            "Blend knob crossfades between IR and algorithm. "
            "Use IR mode for realistic acoustic spaces; Algorithmic for smooth studio reverbs; "
            "blend both for the best of both worlds."
        ),
    },
    {
        "id": "fx_chorus",
        "topic": "effects",
        "text": (
            "Chorus-Ensemble: Chorus mode doubles the signal with a slightly detuned, delayed copy — "
            "classic tape doubling sound. Amount controls depth of the pitch modulation. "
            "Ensemble mode adds more voices for a richer shimmer (classic 80s strings). "
            "Flanger mode shortens delay time for comb filtering — the jet-engine swoosh effect. "
            "Feedback increases the resonance of the comb filter peaks."
        ),
    },
    {
        "id": "fx_phaser",
        "topic": "effects",
        "text": (
            "Phaser-Flanger device: Phaser mode uses all-pass filters to create frequency-notch sweeps — "
            "a more subtle, swirling effect than flanging. "
            "Poles count controls the number of notches (more poles = richer effect). "
            "Flanger mode creates comb-filter sweeps. Sync the LFO rate to project BPM for rhythmic sweeping. "
            "Both modes have a Feedback (resonance) control that adds intensity."
        ),
    },

    # ── MPE Support ───────────────────────────────────────────────────────────────
    {
        "id": "mpe_01",
        "topic": "midi",
        "text": (
            "MPE (MIDI Polyphonic Expression): supported in Live 11+. Each note gets its own pitch bend, "
            "pressure (aftertouch), and slide channel. Enable on a MIDI track by setting it to receive MPE. "
            "Use with MPE controllers (ROLI Seaboard, Linnstrument, Expressive E Osmose). "
            "Wavetable and Drift are MPE-aware — map per-note slide/pressure to filter cutoff, "
            "vibrato depth, or any parameter for expressive, instrument-like playing."
        ),
    },

    # ── Pitch & Tuning ────────────────────────────────────────────────────────────
    {
        "id": "pitch_01",
        "topic": "effects",
        "text": (
            "Tuner (MIDI or Audio Effect): shows the incoming pitch as cents deviation from equal temperament. "
            "Use on a MIDI track to tune hardware synths or on an audio track to check vocalists and guitars. "
            "The large display reads the nearest note and how sharp/flat the signal is. "
            "Tuner passes audio through unaffected — insert it without altering the signal."
        ),
    },
    {
        "id": "pitch_02",
        "topic": "effects",
        "text": (
            "Pitch (Audio Effect): simple semitone and cent pitch shifting with a Dry/Wet control. "
            "Shift harmonically (whole semitones) for key changes, or a few cents for detuning/widening. "
            "Adding a second track with Pitch set to +5 semitones creates a parallel fifth effect (power chords). "
            "For high-quality vocal pitch correction, use third-party tools like Melodyne or Auto-Tune."
        ),
    },

    # ── Live Performance Tips ─────────────────────────────────────────────────────
    {
        "id": "live_perf_01",
        "topic": "performance",
        "text": (
            "Quantization launch: set Clip Launch Quantization (top of Session View or per-clip) "
            "to 1 Bar so clips always start on a bar boundary — prevents off-beat launches. "
            "Set to 1/8 or 1/16 for tighter, faster transitions. "
            "Hold Shift when clicking a clip to temporarily bypass quantization for immediate launch."
        ),
    },
    {
        "id": "live_perf_02",
        "topic": "performance",
        "text": (
            "CPU monitoring: watch the CPU meter (top right of Live). If it peaks frequently, "
            "increase buffer size (Preferences > Audio > Buffer Size) — 512 or 1024 samples for live sets. "
            "Freeze CPU-heavy tracks before performing. "
            "Disable tracks you won't use. Keep plug-in count low — prefer Ableton's native devices."
        ),
    },
    {
        "id": "live_perf_03",
        "topic": "performance",
        "text": (
            "Safety net: always have a backup Live set and a simple backup audio track. "
            "Route a simple looping backing track on a secondary output in case your main set crashes. "
            "Use two computers with Live Link for resilient live performance. "
            "Save your set with all samples collected (File > Collect All and Save) before gigging."
        ),
    },

    # ── Preferences & Setup ───────────────────────────────────────────────────────
    {
        "id": "prefs_01",
        "topic": "transport",
        "text": (
            "Preferences > Audio: set Sample Rate (44.1kHz standard, 48kHz for video) and Buffer Size. "
            "Lower buffer = lower latency = higher CPU load. "
            "Driver Type on Mac: CoreAudio. On Windows: ASIO (install ASIO4ALL if no dedicated interface). "
            "Always use a dedicated audio interface — built-in soundcards have unacceptable latency."
        ),
    },
    {
        "id": "prefs_02",
        "topic": "browser",
        "text": (
            "Preferences > Library: set User Library location (where your saved presets, racks, samples go). "
            "Add external folders via 'Add Folder' so they appear in the Browser. "
            "Preferences > File > Create Unique File Names prevents overwriting existing exports. "
            "Auto-save (Preferences > File > Save Live Set Backup every X minutes) prevents data loss."
        ),
    },

    # ── Arrangement Tips ──────────────────────────────────────────────────────────
    {
        "id": "arr_04",
        "topic": "arrangement",
        "text": (
            "Tempo automation in Arrangement View: click the Tempo field in the transport "
            "and draw automation in the Automation lane. "
            "Ramp the tempo up or down gradually for buildups and breakdowns. "
            "Use breakpoints for instantaneous BPM changes between sections. "
            "Tempo automation is per-set — each Live Set has its own tempo envelope."
        ),
    },
    {
        "id": "arr_05",
        "topic": "arrangement",
        "text": (
            "Looping and overdubbing in Arrangement: set a loop region (Ctrl+L), enable Arrangement Record. "
            "Each loop pass overdubs new MIDI onto the existing clip rather than replacing it. "
            "For audio, each pass creates a new take lane. "
            "This is the standard method for building up drum patterns, basslines, or chord layers gradually."
        ),
    },

    # ── Dynamic Tube & Cabinet ────────────────────────────────────────────────────
    {
        "id": "fx_dyntube",
        "topic": "effects",
        "text": (
            "Dynamic Tube emulates valve/tube amplifier saturation with dynamic response. "
            "Type A/B/C model different tube topologies (single triode, push-pull, pentode). "
            "Bias knob controls the operating point — high Bias adds warmth at low levels; "
            "low Bias creates dynamic gate-like behaviour at quiet passages. "
            "Use on vocals, bass, or drums for musical saturation that responds to dynamics."
        ),
    },
    {
        "id": "fx_cabinet",
        "topic": "effects",
        "text": (
            "Cabinet emulates guitar speaker cabinets. Choose from 5 cabinet types (4x12, 1x12, etc.) "
            "and 5 microphone types (SM57 dynamic, condenser, ribbon), "
            "each with Near/Far mic placement. "
            "Use on electric guitar amp simulations or to add speaker-cabinet character to synths, bass, or drums. "
            "Combine with Amp and Overdrive for a complete guitar chain."
        ),
    },

    # ── Project Management ────────────────────────────────────────────────────────
    {
        "id": "proj_01",
        "topic": "export",
        "text": (
            "Collect All and Save (File > Collect All and Save): copies all samples and audio files "
            "used in the project into the project folder. "
            "Always do this before sharing a project or moving it to another computer — "
            "without it, Live will show 'file not found' errors for missing samples. "
            "Choose 'Copy' not 'Move' to keep originals in place."
        ),
    },
    {
        "id": "proj_02",
        "topic": "browser",
        "text": (
            "Live packs (.alp files): bundle a complete set with samples, presets, and racks. "
            "Download official packs from Ableton.com/packs or the Push/Live Pack manager. "
            "Third-party packs install the same way — double-click the .alp to import. "
            "Manage installed packs in Preferences > Library. Packs appear in the Browser under 'Packs'."
        ),
    },
    {
        "id": "proj_03",
        "topic": "recording",
        "text": (
            "Render in place: select a clip or range in Arrangement View, right-click > Consolidate. "
            "This flattens all MIDI and effects to a single audio clip — "
            "the most direct way to bounce a complex instrument chain without exporting a file. "
            "The new audio clip is placed exactly where the original was. "
            "Freeze Track is the non-destructive version — it can be unfrozen later."
        ),
    },

    # ── Looper ────────────────────────────────────────────────────────────────
    {
        "id": "looper_01",
        "topic": "recording",
        "text": (
            "Looper (Audio Effect): a real-time loop recorder. "
            "Drag it onto a track. Press the button to Record, again to Overdub (layer on top), "
            "again to Play (stop overdubbing), double-press to Stop, triple-press to Clear. "
            "Sync to Song: loop length locks to a bar count in time with Live's transport. "
            "Reverse plays the loop backwards; 1/2x and 2x pitch-shift the loop down or up an octave."
        ),
    },
    {
        "id": "looper_02",
        "topic": "recording",
        "text": (
            "Looper MIDI control: map the Looper's button to a footswitch (MIDI Learn, Ctrl+M). "
            "Use a sustain pedal (CC64) or any MIDI CC to hands-free control Record/Overdub/Play/Stop. "
            "Drag a Looper's output to its own audio track (Resampling or sending to a new track) "
            "to bounce the loop to a clip when you're happy with it."
        ),
    },

    # ── Resonator ────────────────────────────────────────────────────────────
    {
        "id": "fx_resonator",
        "topic": "effects",
        "text": (
            "Resonator (Audio Effect): adds pitched resonance to any sound using up to five tuned comb filters. "
            "Set the Root Note; the five resonators tune themselves to the intervals you select (octave, fifth, etc.). "
            "Width controls stereo spread across resonators. "
            "Run noise, drums, or voice through it to give unpitched sounds a musical, bell-like tonality."
        ),
    },

    # ── Spectrum Analyser ─────────────────────────────────────────────────────
    {
        "id": "fx_spectrum",
        "topic": "effects",
        "text": (
            "Spectrum (Audio Effect): a real-time FFT spectrum analyser. "
            "Displays the frequency content of the signal as a scrolling graph — "
            "useful for identifying problem frequencies before EQing. "
            "Increase FFT size for higher frequency resolution (slower response). "
            "Avg knob averages readings for a smoother display. "
            "Compare two signals by placing Spectrum on two tracks side-by-side."
        ),
    },

    # ── Punch In/Out & Comping ────────────────────────────────────────────────
    {
        "id": "rec_punch",
        "topic": "recording",
        "text": (
            "Punch In/Out: set an Arrangement loop region over the section to fix, enable 'Punch In' (I) and 'Punch Out' (O) "
            "in the transport. Record starts playing from before the punch-in point and only records within the marked region. "
            "This avoids accidentally overwriting good material on either side of a mistake."
        ),
    },
    {
        "id": "rec_comping",
        "topic": "recording",
        "text": (
            "Comping (Live 11+): record multiple takes with Loop Recording enabled. "
            "Each pass creates a new Take Lane below the track. "
            "Click the Show Takes button (the triangular icon on the clip) to reveal all lanes. "
            "Click-drag inside a lane to select the best region from each take; "
            "Live stitches them together into the main comp lane with automatic crossfades."
        ),
    },

    # ── Session → Arrangement ─────────────────────────────────────────────────
    {
        "id": "session_to_arr",
        "topic": "session",
        "text": (
            "Recording Session to Arrangement: arm the Arrangement Record button (the circle in the transport). "
            "Launch clips and scenes in Session View — Live records every launch as clips in Arrangement View. "
            "When you switch to Arrangement View you see the exact performance captured as audio/MIDI clips. "
            "This is the standard way to turn an improvised Session performance into an Arrangement for final editing."
        ),
    },

    # ── Stem / Multi-Track Export ─────────────────────────────────────────────
    {
        "id": "export_stems",
        "topic": "export",
        "text": (
            "Stem export: select all tracks you want to export, then File > Export Audio/Video. "
            "Choose 'Export Each Track as Separate Audio File' (or for individual clips, render each track solo). "
            "For a true stem export workflow, create a Group Track per stem (Drums, Bass, Synths, Vocals), "
            "then render each Group's output. This gives mix engineers independent stems."
        ),
    },
    {
        "id": "export_multitrack",
        "topic": "export",
        "text": (
            "Multi-track bounce with 'Render as Loop': enables the exported file to loop seamlessly "
            "by including any tail (reverb, delay) within the loop length. "
            "For stems used in DAW collaborations, enable 'Save as Type: Flac' for lossless files "
            "or WAV 24-bit for maximum quality. Include the project tempo in the filename for clarity."
        ),
    },

    # ── Clip Envelope Modes ───────────────────────────────────────────────────
    {
        "id": "clip_env_modes",
        "topic": "clips",
        "text": (
            "Clip warp modes shape how audio is time-stretched: "
            "Beats — for rhythmic material; uses transient analysis and works best for drums. "
            "Tones — for monophonic pitched audio (vocals, bass) with few overtones. "
            "Texture — for dense, textural, or noise-based audio where pitch accuracy is less important. "
            "Re-Pitch — no time-stretching; changes speed (and pitch) like a record player — zero artefacts. "
            "Complex Pro — highest quality for full mixes; set Formants to preserve vocal character."
        ),
    },

    # ── Live 12 MIDI Generation ───────────────────────────────────────────────
    {
        "id": "live12_midi_gen",
        "topic": "midi",
        "text": (
            "Live 12 MIDI Generation: right-click any MIDI clip and choose Generate MIDI. "
            "Live's AI suggests melodic, rhythmic, or chordal ideas based on the clip's existing content "
            "and the current Scale. 'Generate Groove' creates rhythmic pattern variations. "
            "'Transform' mutates the clip with pitch shifts, inversions, or rhythmic displacement. "
            "Results land in a new clip variation — originals are never overwritten."
        ),
    },
    {
        "id": "live12_scale",
        "topic": "midi",
        "text": (
            "Live 12 Scale Mode: set a global scale (e.g. D Dorian) in the transport bar. "
            "All MIDI clips, the Piano Roll, and Push highlight or constrain notes to that scale. "
            "Enable 'Highlight Scale' in the Piano Roll to visually emphasise scale notes. "
            "'Fold' collapses the Piano Roll to show only scale notes — "
            "great for beginners or fast melodic sketching without worrying about wrong notes."
        ),
    },

    # ── Scoring to Video ──────────────────────────────────────────────────────
    {
        "id": "video_scoring",
        "topic": "arrangement",
        "text": (
            "Scoring to video: File > Load Video, or drag a video into the Arrangement. "
            "The video appears in a floating window (View > Video Window). "
            "Use 'Set Song Start Time' to offset Live's timeline from a specific SMPTE timecode. "
            "Sync with external video editors via ReWire or use Export Audio/Video to embed audio in a QuickTime."
        ),
    },
    {
        "id": "video_scrub",
        "topic": "arrangement",
        "text": (
            "Video scrubbing: drag the playhead over a video-linked Arrangement to scrub through footage. "
            "Enable 'Follow' (F) so the timeline tracks playback. "
            "Set Clip Start Offset to align music to a specific hit point in the video. "
            "Use Automation on tempo to push or pull beats to land exactly on visual cuts."
        ),
    },

    # ── Collection Labels ─────────────────────────────────────────────────────
    {
        "id": "collections_01",
        "topic": "browser",
        "text": (
            "Collection labels: in the Browser, right-click any preset, sample, or plugin and assign it "
            "to a coloured Collection (1–6 coloured labels). "
            "Click a collection colour in the left sidebar to filter the Browser to only items with that label. "
            "Use this to tag your favourite synths Red, best drum kits Green, and work-in-progress samples Yellow "
            "for instant access during sessions."
        ),
    },

    # ── MIDI Remote Control ───────────────────────────────────────────────────
    {
        "id": "midi_learn_01",
        "topic": "midi",
        "text": (
            "MIDI Learn: press Ctrl+M (Cmd+M Mac) to enter MIDI Map mode. "
            "Click any control (knob, fader, button) then move a physical controller knob/button — "
            "Live binds them instantly. "
            "Set Min/Max values to constrain the range (e.g. map a fader to 0–100% volume only). "
            "Map the same CC to multiple parameters for one-knob macro control over an entire group of parameters."
        ),
    },
    {
        "id": "midi_learn_02",
        "topic": "midi",
        "text": (
            "Key Mapping: press Ctrl+K (Cmd+K) to enter Key Map mode — same as MIDI Learn but for computer keyboard. "
            "Map keys to Launch Clips, Start/Stop, tap tempo, and more. "
            "Toggle 'Computer Keyboard MIDI Input' (the keyboard icon in the transport) "
            "to switch the keyboard between playing notes and triggering key mappings."
        ),
    },

    # ── Max for Live devices ──────────────────────────────────────────────────
    {
        "id": "m4l_buffer_shuffler",
        "topic": "max_for_live",
        "text": (
            "Buffer Shuffler 2.0 (Max for Live): captures the incoming audio in a buffer and "
            "re-plays segments in randomised or stepped order — creating stutter, glitch, and rearrangement effects. "
            "Divisions set the buffer chunk size. Shuffle controls how much randomisation is applied. "
            "Gate mode silences some chunks for choppy rhythmic gating. Sync to host BPM keeps glitches musical."
        ),
    },
    {
        "id": "m4l_note_echo",
        "topic": "max_for_live",
        "text": (
            "Note Echo (Max for Live MIDI Effect): repeats incoming MIDI notes with a decaying velocity "
            "at a set interval (synced to song tempo). "
            "Pitch knob transposes each successive echo (e.g. +2 semitones each repeat for a rising arpeggio). "
            "Decay reduces velocity with each echo. Pairs well with a sustained pad sound for melodic delay effects."
        ),
    },
    {
        "id": "m4l_convolution_reverb_pro",
        "topic": "max_for_live",
        "text": (
            "Convolution Reverb Pro (Max for Live): loads impulse response files (.wav, .aif) "
            "to place audio in any recorded acoustic space. "
            "Pre-Delay adds separation between dry signal and reverb tail. "
            "ER Mix/Late Mix balance early reflections against late tail. "
            "Use the EQ section to roll off low mud in the reverb tail. "
            "Download free IRs from OpenAIR, EchoThief, or Fokke van Saane's IR collection."
        ),
    },

    # ── Ableton Note ─────────────────────────────────────────────────────────
    {
        "id": "ableton_note",
        "topic": "recording",
        "text": (
            "Ableton Note (iOS/Android mobile app): a companion app for capturing ideas on the go. "
            "Record beats (drum pads), melodic loops (keyboard), samples, and audio. "
            "Export ideas to Live via the User Library (they appear as Project files on desktop). "
            "Note syncs tempo-locked loops; scale mode constrains notes so everything stays in key. "
            "Great for capturing inspiration anywhere and finishing in Live later."
        ),
    },

    # ── Clip Gain ─────────────────────────────────────────────────────────────
    {
        "id": "clip_gain_02",
        "topic": "clips",
        "text": (
            "Clip Gain vs Track Volume: Clip Gain (the yellow triangle in the waveform view) adjusts the "
            "clip's level before it hits the track fader and effects chain. "
            "Use Clip Gain to normalise levels between clips so the track fader is doing consistent work. "
            "This is preferable to gain-staging exclusively at the track level, "
            "especially when clips have wildly different recorded levels."
        ),
    },

    # ── Global Quantisation & Recording ──────────────────────────────────────
    {
        "id": "global_quant",
        "topic": "session",
        "text": (
            "Global Launch Quantisation (the dropdown at top of Session View, default 1 Bar): "
            "controls when clip launches take effect. Set to 'None' for immediate triggering. "
            "Record Quantisation (Preferences > Record/Warp/Launch) snaps incoming MIDI notes "
            "to the nearest grid value as you record — 1/8 is a safe default for most parts."
        ),
    },

    # ── Parallel Compression ─────────────────────────────────────────────────
    {
        "id": "mix_parallel_comp",
        "topic": "mixing",
        "text": (
            "Parallel compression (New York compression): send a drum bus to a Return track. "
            "On the Return track, apply heavy compression (high ratio, fast attack, low threshold). "
            "Blend the heavily compressed Return back with the uncompressed dry drums. "
            "Result: transient punch is preserved (from the dry signal) while sustain and body are boosted "
            "(from the compressed signal). Blend to taste — typically 20–50% wet."
        ),
    },

    # ── Mid/Side Processing ──────────────────────────────────────────────────
    {
        "id": "mix_ms_01",
        "topic": "mixing",
        "text": (
            "Mid/Side (M/S) processing with Utility: insert two Utility devices in a chain. "
            "First Utility: set Width to 0 (mono) — this is the Mid signal. "
            "Or use the Channel Mode dropdown on EQ Eight/Glue Compressor — many Ableton devices "
            "have a built-in M/S mode. M/S lets you EQ or compress the centre of the stereo image "
            "independently from the sides — great for tightening bass in the centre or widening highs."
        ),
    },
    {
        "id": "mix_ms_02",
        "topic": "mixing",
        "text": (
            "Stereo Width with Utility: the Width knob on Utility (0% = mono, 100% = normal stereo, >100% = wider). "
            "Use on synth pads to widen them without phase issues — preferred over a stereo imager plugin. "
            "Use on bass/kick and set Width to 0 to ensure they are mono-compatible (essential for club systems). "
            "Check mono compatibility with the Utility mono button before finalising any mix."
        ),
    },

    # ── LUFS Metering ────────────────────────────────────────────────────────
    {
        "id": "mix_lufs",
        "topic": "mixing",
        "text": (
            "Loudness targets (LUFS) for streaming: "
            "Spotify normalises to -14 LUFS integrated. Apple Music: -16 LUFS. YouTube: -14 LUFS. "
            "Aim for -14 LUFS integrated on your master for streaming so the platform doesn't turn it down. "
            "Use a LUFS meter plugin on the master (or the free Youlean Loudness Meter) to measure. "
            "A true-peak ceiling of -1 dBTP prevents distortion on decode."
        ),
    },

    # ── Pre/Post Fader Sends ─────────────────────────────────────────────────
    {
        "id": "mix_sends",
        "topic": "mixing",
        "text": (
            "Pre-fader vs post-fader sends: right-click any Send knob > Pre Fader. "
            "Post-fader (default): send level follows the channel fader — turn down the track, reverb also quiets. "
            "Pre-fader: send is tapped before the fader — the reverb continues at its level even if the dry track is muted. "
            "Use pre-fader to create a reverb-only blend or to feed a headphone cue mix at fixed levels."
        ),
    },

    # ── Dummy Clips ──────────────────────────────────────────────────────────
    {
        "id": "dummy_clips",
        "topic": "session",
        "text": (
            "Dummy clips: empty MIDI clips placed in Session View slots not to play notes, "
            "but to trigger clip envelope automation (filter sweeps, volume ramps, effect parameter changes). "
            "Draw automation inside the clip envelope. When the dummy clip launches, "
            "the automation fires even though no MIDI notes play — "
            "a powerful way to trigger time-synced parameter changes from Session View."
        ),
    },

    # ── Beat Repeat Deep Dive ────────────────────────────────────────────────
    {
        "id": "beat_repeat_02",
        "topic": "effects",
        "text": (
            "Beat Repeat Chance and Variation: Chance (0–100%) sets the probability that a repeat fires "
            "on any given beat. Variation changes the length of each repeat randomly within the Interval/Offset range. "
            "Set Chance to 50–70% and Variation to 2–3 for organic, not-every-beat stutters — "
            "sounds like a glitchy human performer rather than a quantised effect."
        ),
    },
    {
        "id": "beat_repeat_03",
        "topic": "effects",
        "text": (
            "Beat Repeat Gate vs Mix modes: "
            "Gate mode silences the original signal during a repeat — the repeat replaces the source. "
            "Mix mode layers the repeat on top of the original — creates echo-like layering. "
            "Pitch Decay causes each repeated slice to drop in pitch — produces vinyl-brake effects. "
            "Decay gradually reduces the volume of successive repeats for a natural echo tail."
        ),
    },

    # ── Amp Effect ───────────────────────────────────────────────────────────
    {
        "id": "fx_amp",
        "topic": "effects",
        "text": (
            "Amp (Audio Effect) emulates seven guitar amplifier types: Clean, Boost, Blues, Rock, Lead, Heavy, Bass. "
            "Each has a different EQ character and saturation response. "
            "Gain drives the preamp stage. Bass/Mid/Treble shape the tone. Output controls final level. "
            "Combine with Cabinet effect after Amp for a complete amp + speaker simulation chain. "
            "Works on any audio source — try on drums, bass, or synths for analogue warmth."
        ),
    },

    # ── Live 12 MIDI Transformations ─────────────────────────────────────────
    {
        "id": "live12_midi_tools",
        "topic": "midi",
        "text": (
            "Live 12 MIDI Transformation tools (inside the MIDI clip, top bar): "
            "Arpeggiate — converts held chords into arpeggios with rate/gate/style options. "
            "Strum — staggers simultaneous notes to simulate guitar strumming (up or down, variable speed). "
            "Connect — generates melodic fills between existing notes. "
            "Ornament — adds grace notes and ornaments to selected notes. "
            "All are non-destructive; results land in a new clip variation."
        ),
    },
    {
        "id": "live12_midi_tools2",
        "topic": "midi",
        "text": (
            "Live 12 MIDI Transformation: Echo — adds delay-style repeated notes at a set interval and velocity decay, "
            "entirely within the MIDI domain (before any instrument). "
            "Span — stretches or compresses note durations and timing relationships proportionally. "
            "Recombine — shuffles note pitches while preserving rhythm, or shuffles rhythm while preserving pitch. "
            "All transformations respect the active Scale Mode setting."
        ),
    },

    # ── Macro Variations ─────────────────────────────────────────────────────
    {
        "id": "macro_variations",
        "topic": "devices",
        "text": (
            "Macro Variations (Live 11+, Instrument/Audio/Drum Racks): "
            "the Variations button (star icon) saves snapshots of all eight Macro knob positions. "
            "Save up to 16 named variations per rack. Switch between them in real time for instant preset switching "
            "within a performance — e.g. bass sound variations (dry, filtered, distorted) on one rack."
        ),
    },

    # ── Tab Key & Keyboard Navigation ────────────────────────────────────────
    {
        "id": "keyboard_nav",
        "topic": "transport",
        "text": (
            "Tab key switches between Session View and Arrangement View. "
            "F9 starts/stops recording. Space plays/stops. Shift+Space restarts from the current position. "
            "Ctrl+Z undoes. Ctrl+Shift+Z redoes. "
            "Arrow keys navigate clips in Session View. Enter/Return launches the selected clip. "
            "Ctrl+D duplicates selected clips. Delete removes them."
        ),
    },

    # ── Track & Clip Colour Coding ───────────────────────────────────────────
    {
        "id": "colour_coding",
        "topic": "arrangement",
        "text": (
            "Colour coding tracks and clips: right-click a track header or clip > Assign Colour. "
            "Use a consistent colour system across projects: e.g. drums = orange, bass = red, "
            "chords = blue, leads = green, FX = purple, vocals = yellow. "
            "Colour-coded arrangements are scannable at a glance — especially important during live performance "
            "or collaborative sessions where you need to navigate fast."
        ),
    },

    # ── Sends / Return Tracks ────────────────────────────────────────────────
    {
        "id": "send_return_01",
        "topic": "mixing",
        "text": (
            "Return tracks (A and B by default): shared effects buses. "
            "Every track's Send A/B knob routes signal to the Return track. "
            "Place reverb on Return A — all tracks share one reverb instance instead of one per track. "
            "This is CPU-efficient and creates a cohesive 'room' sound. "
            "Add Return tracks via Create > Insert Return Track. Route multiple sends to the same Return."
        ),
    },

    # ── MIDI Velocity Editor ──────────────────────────────────────────────────
    {
        "id": "midi_velocity_01",
        "topic": "midi",
        "text": (
            "Velocity editor lane: in the MIDI clip view, below the piano roll is a velocity bar graph. "
            "Each bar represents one note's velocity (1–127). "
            "Click and drag a bar to set its velocity. Draw-select multiple bars then drag to scale them all. "
            "Hold Ctrl and drag to scale velocities proportionally from zero. "
            "Right-click a note in the piano roll > Select Notes of Same Pitch to batch-edit one drum hit's dynamics."
        ),
    },
    {
        "id": "midi_velocity_02",
        "topic": "midi",
        "text": (
            "Humanising velocity: select all notes (Ctrl+A) in the piano roll, "
            "then right-click in the velocity lane > Randomise to add subtle variation. "
            "Or draw a velocity envelope with a slight crescendo/decrescendo across a phrase. "
            "Perfectly uniform velocities sound robotic — "
            "a 10–20 unit spread between notes makes MIDI patterns feel performed, not programmed."
        ),
    },

    # ── Group Tracks ──────────────────────────────────────────────────────────
    {
        "id": "group_tracks_01",
        "topic": "mixing",
        "text": (
            "Group tracks (Ctrl+G): select multiple tracks and group them into a single bus track. "
            "The group track has its own fader, pan, and device chain — apply one compressor to all drums at once. "
            "Collapse the group to save screen space. Solo or mute the whole group with one click. "
            "Group tracks also work with Return tracks for complex routing. "
            "Nest groups inside groups for a full stem hierarchy."
        ),
    },

    # ── Instrument Rack Chain Selector ────────────────────────────────────────
    {
        "id": "rack_chain_sel_01",
        "topic": "devices",
        "text": (
            "Instrument Rack Chain Select zones: in an Instrument Rack's Chain list, "
            "each chain has a Zone bar (click the Key/Vel button to show zones). "
            "Key zones split by MIDI note — low notes play chain 1 (piano), high notes play chain 2 (strings). "
            "Velocity zones split by velocity — soft playing triggers an acoustic piano sample, "
            "hard playing triggers an electric piano, enabling dynamic instrument switching from playing harder."
        ),
    },
    {
        "id": "rack_chain_sel_02",
        "topic": "devices",
        "text": (
            "Chain Select macro: the Chain Selector is exposed as a mappable value at the top of the rack. "
            "Map it to a MIDI CC or a Macro knob to switch chains in real time — "
            "turn one knob to morph between a bass guitar, synth bass, and sub bass in the same rack. "
            "Set fade overlap between zones for smooth crossfading instead of hard switching."
        ),
    },

    # ── Drum Rack Individual Outputs ──────────────────────────────────────────
    {
        "id": "drum_rack_outputs",
        "topic": "devices",
        "text": (
            "Drum Rack individual outputs: click 'Show/Hide Send and Return Chains' (the chain icon in the rack). "
            "Each drum pad can be routed to its own audio track: "
            "click the pad's 'Audio To' dropdown and set it to a new track output. "
            "This gives kick, snare, hi-hats, etc. their own mixer channels for individual EQ and compression — "
            "the standard approach for mixing multi-track drums in Live."
        ),
    },

    # ── Simpler Deep Dive ─────────────────────────────────────────────────────
    {
        "id": "simpler_modes_01",
        "topic": "instruments",
        "text": (
            "Simpler has three modes (buttons in the top left of the device): "
            "Classic — the default sampler; pitch-shifts the sample to follow MIDI notes; "
            "supports loop, sustain loop, and warp. "
            "One-Shot — plays the sample once from start to finish regardless of note duration; "
            "good for drum hits, SFX, one-shots. "
            "Slicing — automatically detects transients and maps each slice to its own MIDI note for re-sequencing."
        ),
    },
    {
        "id": "simpler_modes_02",
        "topic": "instruments",
        "text": (
            "Simpler Slicing mode: drag any loop into Simpler, switch to Slice mode. "
            "Live detects transients and maps each slice to ascending MIDI notes. "
            "Use the Slice MIDI Effect (auto-created) to trigger slices in order. "
            "Adjust Sensitivity to add or remove slice points. "
            "Convert to Drum Rack: right-click Simpler > Convert Slices to New Drum Rack "
            "for individual per-pad control of each slice."
        ),
    },

    # ── Sampler ───────────────────────────────────────────────────────────────
    {
        "id": "sampler_01",
        "topic": "instruments",
        "text": (
            "Sampler (the full multi-sample version of Simpler): supports a Sample Zone Map "
            "where different samples trigger at different pitch ranges and velocity layers. "
            "Import multi-samples (e.g. a piano sampled every 3 semitones at soft/medium/hard velocities) "
            "and Sampler auto-detects zones. "
            "Use for realistic acoustic instruments, orchestral libraries, and Kontakt-style instruments built natively in Live."
        ),
    },
    {
        "id": "sampler_02",
        "topic": "instruments",
        "text": (
            "Sampler advanced: the Oscillator section adds a synthesis layer on top of the sample. "
            "The Modulation Matrix lets you map any source (LFO, envelope, MIDI CC, velocity) "
            "to any destination (pitch, filter cutoff, amplitude) — up to six modulation routings. "
            "Loop modes: Loop, Ping-Pong, Warped. Crossfade Loop smooths the loop point for sustained notes. "
            "Right-click Simpler > Convert to Sampler to upgrade a Simpler patch."
        ),
    },

    # ── Arrangement Clip Fades ────────────────────────────────────────────────
    {
        "id": "arr_clip_fades",
        "topic": "arrangement",
        "text": (
            "Clip fades in Arrangement View: hover over the top-left or top-right corner of an audio clip "
            "until the fade cursor appears, then drag to create a fade-in or fade-out. "
            "Hover over the bottom of a fade line to drag a crossfade between two adjacent clips. "
            "Right-click a fade > Fade Type to choose between linear, equal power, and logarithmic curves. "
            "Equal Power is correct for crossfading between unrelated audio; linear for fade-outs to silence."
        ),
    },

    # ── Back to Arrangement ───────────────────────────────────────────────────
    {
        "id": "back_to_arr",
        "topic": "session",
        "text": (
            "Back to Arrangement button (orange button in the transport): appears when Session View clips "
            "are playing over an Arrangement. Session clips override Arrangement playback. "
            "Clicking 'Back to Arrangement' stops all Session clips and returns control to the Arrangement timeline — "
            "the track resumes playing from its Arrangement clips. "
            "Press it during a live set if you accidentally launched a Session clip over your Arrangement."
        ),
    },

    # ── MIDI Clip Loop Brace ──────────────────────────────────────────────────
    {
        "id": "midi_loop_brace",
        "topic": "midi",
        "text": (
            "MIDI clip loop brace: in the Clip View's sample/notes area, "
            "the loop brace (the bar with triangular handles above the note grid) sets the loop region. "
            "Drag the left handle to set Loop Start; right handle for Loop End. "
            "The loop length shows as a numerical value. "
            "Click 'Loop' toggle in the Clip View to enable/disable looping. "
            "Setting a shorter loop brace than the clip length lets you loop just a section of a longer MIDI phrase."
        ),
    },

    # ── Consolidate Clips ─────────────────────────────────────────────────────
    {
        "id": "consolidate_clips",
        "topic": "arrangement",
        "text": (
            "Consolidate clips (Ctrl+J in Arrangement View): merges all selected clips on a track "
            "into one continuous clip. For audio, renders the combined result (with effects) to a new file. "
            "For MIDI, joins the note data into one clip. "
            "Use it to tidy up a fragmented arrangement after heavy editing. "
            "Unlike Freeze, Consolidate is destructive — the original clip boundaries are gone. "
            "Always duplicate the track first if you might want to un-merge."
        ),
    },

    # ── Auto Filter ───────────────────────────────────────────────────────────
    {
        "id": "fx_auto_filter",
        "topic": "effects",
        "text": (
            "Auto Filter: a resonant filter (LP, HP, BP, Notch) with a built-in LFO and envelope follower. "
            "Frequency sets the base cutoff; Resonance adds a peak at the cutoff. "
            "LFO Amount sweeps the cutoff rhythmically (set Rate to a tempo-synced value for filter wobbles). "
            "Envelope Amount makes the filter track the input amplitude — loud passages open the filter. "
            "Classic use: low-pass with high Resonance and a synced LFO for wah-like dubstep bass movement."
        ),
    },

    # ── Saturator ────────────────────────────────────────────────────────────
    {
        "id": "fx_saturator",
        "topic": "effects",
        "text": (
            "Saturator adds harmonic distortion for warmth and character. "
            "Drive pushes the signal into saturation. Output compensates the level increase. "
            "Waveshaper mode: Soft Sine (smooth, valve-like), Medium Curve, Hard Clip (digital crunch), "
            "Sinoid Fold (extreme ring-mod-like foldback). "
            "Color adds high-frequency presence. "
            "Use subtly on bass (Drive 5–10%) for analogue warmth, or harder on synths for aggressive saturation."
        ),
    },

    # ── Overdrive ────────────────────────────────────────────────────────────
    {
        "id": "fx_overdrive",
        "topic": "effects",
        "text": (
            "Overdrive emulates guitar pedal-style soft clipping. "
            "Drive controls gain before clipping. Tone is a tilt EQ (brighter vs warmer). "
            "Feedback adds a mild feedback resonance for added grit. "
            "Softer than Hard Clip in Saturator — Overdrive rounds peaks instead of shearing them. "
            "Use on electric guitars, bass slap transients, or synth leads for a 'pushed' amp feel without full amp simulation."
        ),
    },

    # ── Delay Devices ────────────────────────────────────────────────────────
    {
        "id": "fx_simple_delay",
        "topic": "effects",
        "text": (
            "Simple Delay: two independent delay lines (Left and Right), each with a time and feedback control. "
            "Sync to song tempo with note values (1/4, 1/8, dotted 1/8). "
            "Offset L vs R times for a stereo ping-pong feel without using Ping Pong Delay. "
            "Dry/Wet controls the blend. "
            "Ping Pong Delay: a dedicated device that alternates repeats between left and right channels — "
            "single delay time, one feedback knob, same tempo sync. Simpler setup for classic ping-pong echo."
        ),
    },

    # ── Piano Roll Modes & Fold ───────────────────────────────────────────────
    {
        "id": "piano_roll_modes",
        "topic": "midi",
        "text": (
            "Piano Roll Draw vs Select mode: the pencil icon (Draw) lets you click to create notes; "
            "the arrow icon (Select) lets you click to select existing notes. "
            "Press Ctrl to temporarily switch between modes. "
            "Fold button (the fold icon above the piano keyboard): hides all octaves with no notes, "
            "compressing the view so only the octaves in use are visible — essential for drum editing "
            "where notes span the full range but cluster in specific zones."
        ),
    },
    {
        "id": "piano_roll_tools",
        "topic": "midi",
        "text": (
            "Piano Roll additional tools: "
            "Ctrl+A selects all notes. Shift+click to add to selection. "
            "Hold Alt and drag a note to duplicate it. "
            "Resize a note by dragging its right edge. "
            "Ctrl+click a note to delete it. "
            "Right-click > Select Notes of Same Pitch to select all instances of one drum hit. "
            "Double-click on empty space to create a note at the grid resolution."
        ),
    },

    # ── Gain Staging ─────────────────────────────────────────────────────────
    {
        "id": "gain_staging_01",
        "topic": "mixing",
        "text": (
            "Gain staging: set the level at every stage of the signal chain so each device receives "
            "a healthy signal without clipping. "
            "Rule of thumb: individual tracks should peak around -12 to -6 dBFS before the Master. "
            "The Master fader should rarely need to go above 0 dB if tracks are staged correctly. "
            "Use the Utility device's Gain knob (not the track fader) for clip-level adjustments "
            "to keep the fader at 0 dB for automation reference."
        ),
    },
    {
        "id": "gain_staging_02",
        "topic": "mixing",
        "text": (
            "Headroom and metering: headroom is the space between your average level and 0 dBFS. "
            "Keep 6–10 dB of headroom on the Master before limiting to give the Limiter/Maximiser room to work. "
            "Peak meters show the loudest instantaneous sample; RMS/VU meters show perceived loudness. "
            "A mix that peaks at -6 dBFS with healthy RMS levels will survive mastering better than "
            "a pre-limited mix that's already maximised."
        ),
    },

    # ── Compressor Device ─────────────────────────────────────────────────────
    {
        "id": "compressor_01",
        "topic": "mixing",
        "text": (
            "Compressor device parameters: "
            "Threshold — level above which compression starts. "
            "Ratio — how much gain reduction is applied (4:1 = for every 4 dB over threshold, output increases 1 dB). "
            "Attack — how fast the compressor responds (fast = controls transients; slow = lets attack through). "
            "Release — how fast gain returns to normal (auto-release adapts to the programme material). "
            "Knee — soft knee gradually engages compression near the threshold for transparent results."
        ),
    },
    {
        "id": "compressor_sidechain",
        "topic": "mixing",
        "text": (
            "Compressor sidechain routing: in the Compressor device, click the 'Sidechain' triangle to expand. "
            "Set 'Audio From' to the kick track (or any source). "
            "Now the Compressor on the bass track ducks whenever the kick hits — "
            "classic sidechain pumping for EDM, or transparent bass-kick separation in any genre. "
            "EQ the sidechain signal (enable the EQ section) to only trigger on the kick's low frequencies, "
            "ignoring hi-hats or snare bleed."
        ),
    },

    # ── Save as Default Set ───────────────────────────────────────────────────
    {
        "id": "default_set",
        "topic": "transport",
        "text": (
            "Save Live Set as Default (File > Save Live Set as Default): "
            "every new project opens with this template. "
            "Build your ideal starting state: pre-routed drum bus, master chain (EQ, compressor, limiter, LUFS meter), "
            "colour-coded track groups, preferred audio settings, and a reference track slot. "
            "This saves 5–10 minutes at the start of every session and enforces consistent gain staging habits."
        ),
    },

    # ── MIDI CC Automation ────────────────────────────────────────────────────
    {
        "id": "midi_cc_auto",
        "topic": "midi",
        "text": (
            "MIDI CC automation in clips: in the MIDI Clip View, click the 'E' (Envelopes) box. "
            "Select 'MIDI Ctrl' from the device dropdown and choose a CC number (e.g. CC74 = filter cutoff). "
            "Draw an automation envelope — the CC value changes over time within the clip. "
            "This is clip-bound automation (travels with the clip) rather than track-level automation. "
            "Use it for synth parameter changes that belong to a specific loop, not a fixed Arrangement point."
        ),
    },

    # ── External Hardware Sync ────────────────────────────────────────────────
    {
        "id": "ext_sync_01",
        "topic": "transport",
        "text": (
            "MIDI Clock out: Preferences > Link/Tempo/MIDI > MIDI Ports — enable 'Sync' Output on your MIDI interface port. "
            "Live sends MIDI Clock (24 pulses per quarter note) to any connected hardware sequencer, drum machine, or synth. "
            "The hardware locks to Live's tempo and transport. "
            "Start/Stop messages can also be sent so hardware starts when Live starts. "
            "Use Ableton Link (Preferences > Link) for wireless sync with other computers or iOS/Android apps on the same network."
        ),
    },

    # ── Panning & Stereo Placement ────────────────────────────────────────────
    {
        "id": "panning_01",
        "topic": "mixing",
        "text": (
            "Panning and stereo placement: keep kick, snare, bass, and lead vocal near centre. "
            "Pan supporting elements (guitars, synth layers, hi-hats, pads) left and right to create width. "
            "Rule of thirds: imagine the stereo field in thirds — centre, left-centre, hard left (same on right). "
            "Use Auto Pan (set to LFO off, just as a DC offset) or Utility pan for precise panning. "
            "Always check in mono: if elements disappear, they are phase-cancelling — fix the width before mixing."
        ),
    },

    # ── Glue Compressor ───────────────────────────────────────────────────────
    {
        "id": "glue_comp_01",
        "topic": "mixing",
        "text": (
            "Glue Compressor: a VCA bus compressor modelled on the SSL G-Bus. "
            "Use on drum buses, mix buses, or stem groups to 'glue' multiple tracks into a cohesive sound. "
            "Ratio 2:1 or 4:1, slow attack (30ms) to let transients through, fast release (auto). "
            "Aim for 2–4 dB of gain reduction. "
            "Soft Clip adds gentle saturation above the output ceiling for additional harmonic cohesion."
        ),
    },

    # ── High-Pass Filtering in Mixing ────────────────────────────────────────
    {
        "id": "mix_hpf",
        "topic": "mixing",
        "text": (
            "High-pass filter (HPF) every track that isn't carrying bass energy. "
            "On guitars: HPF around 80–100 Hz. Synth pads: 120 Hz. Vocals: 80–120 Hz. Hi-hats: 200 Hz+. "
            "This removes inaudible low-frequency mud that accumulates across many tracks and clouds the mix. "
            "In EQ Eight, activate the High Pass filter (leftmost band) and roll up until you hear the track thin — "
            "then back off a little."
        ),
    },

    # ── Reference Tracks ─────────────────────────────────────────────────────
    {
        "id": "mix_reference",
        "topic": "mixing",
        "text": (
            "Reference tracks: drag a commercial reference track (same genre) onto a new audio track. "
            "Disable the track from export (right-click > Deactivate Clip on export). "
            "A/B between your mix and the reference by soloing each. "
            "Match levels first (reference tracks are usually louder — reduce their volume to match). "
            "Use EQ Eight in Spectrum mode to visually compare frequency balance, "
            "and match the broad shape of the reference."
        ),
    },

    # ── Auto Pan ──────────────────────────────────────────────────────────────
    {
        "id": "fx_auto_pan",
        "topic": "effects",
        "text": (
            "Auto Pan: an LFO-driven panning and amplitude modulator. "
            "Shape: Sine (smooth), Triangle, Sawtooth, Square (hard). "
            "Rate (synced to tempo): 1/4 creates a quarter-note left-right pan sweep. "
            "Phase controls the offset between L and R channels — 180° = one side peaks as the other dips (full panning). "
            "Offset shifts the pan centre. "
            "Set Shape to Sine with a slow rate for a Leslie rotary speaker tremolo effect on organs."
        ),
    },

    # ── Hot-Swap Presets ──────────────────────────────────────────────────────
    {
        "id": "hotswap_presets",
        "topic": "browser",
        "text": (
            "Hot-swap presets: click the Hot-Swap button (the magnifying glass icon on any device) "
            "or press Q with a device selected. The Browser opens filtered to matching presets. "
            "Press the up/down arrow keys to cycle through presets while the track plays — "
            "each press instantly loads the next preset so you hear it in context. "
            "Press Escape to revert to the original. Press Enter or click to confirm the chosen preset."
        ),
    },

    # ── Browser Preview ───────────────────────────────────────────────────────
    {
        "id": "browser_preview",
        "topic": "browser",
        "text": (
            "Browser sample preview: click any sample in the Browser to select it, "
            "then press Spacebar to pre-listen through your audio output. "
            "Enable 'Preview' in the Browser toolbar (the headphone icon) so clicking a sample auto-plays it. "
            "The Autoplay button (next to Preview) loops the sample automatically. "
            "Enable 'Sync' to preview samples in time with the current tempo — "
            "loops play at the project BPM so you hear exactly how they'll sit in the mix."
        ),
    },

    # ── EQ Eight Channel Modes ────────────────────────────────────────────────
    {
        "id": "eq8_modes",
        "topic": "mixing",
        "text": (
            "EQ Eight channel modes (dropdown in the top-left of the device): "
            "Stereo — one EQ curve affects both channels identically (default). "
            "Left/Right — separate EQ curves for each channel; click L or R to switch which you're editing. "
            "Mid/Side — separate curves for the Mid (mono centre) and Side (stereo difference) signals. "
            "Use M/S mode to cut low-end from the Side (keeps bass mono) or boost high-frequency air only in the Side (wider tops)."
        ),
    },

    # ── Cue / Preview Output ──────────────────────────────────────────────────
    {
        "id": "cue_output",
        "topic": "mixing",
        "text": (
            "Cue/Preview output: Preferences > Audio > Output Config — enable a second stereo pair as the Cue Out. "
            "In the Master section of the mixer, click the headphone icon on any track to route it to the Cue Out "
            "without it hitting the Master — classic DJ monitor cueing. "
            "The Cue Vol knob controls headphone level independently from the Master. "
            "Use to pre-listen Browser previews through headphones while a set plays through speakers."
        ),
    },

    # ── Drum Buss ─────────────────────────────────────────────────────────────
    {
        "id": "drum_buss_01",
        "topic": "effects",
        "text": (
            "Drum Buss: a dedicated drum bus processor combining transient shaping, saturation, and sub-bass. "
            "Transients: Transient Time controls how long the boosted attack is sustained. "
            "Boom: adds sub-bass reinforcement at a tunable frequency (tune to your kick's fundamental). "
            "Crunch: applies mid-range saturation — add sparingly to keep drums punchy without distorting. "
            "Dry/Wet blends the processed and dry signal. Designed to sit on a grouped drum bus."
        ),
    },

    # ── Wavetable Mod Matrix ──────────────────────────────────────────────────
    {
        "id": "wavetable_modmat",
        "topic": "instruments",
        "text": (
            "Wavetable modulation matrix: in the Matrix tab, add up to 12 modulation routings. "
            "Source: Envelope 1/2, LFO 1/2, MIDI (velocity, note, aftertouch, mod wheel), Macro. "
            "Destination: oscillator pitch, wavetable position, filter cutoff, resonance, amp volume, pan. "
            "Amount: positive or negative depth. "
            "Velocity → Filter Cutoff gives classic velocity-sensitive filter brightness; "
            "LFO → Wavetable Position creates animated wavetable scanning."
        ),
    },
    {
        "id": "wavetable_osc",
        "topic": "instruments",
        "text": (
            "Wavetable oscillator section: each oscillator has a wavetable (64 single-cycle waveforms in a table). "
            "Position knob scrubs through the table — automate or modulate this for motion. "
            "Transpose shifts pitch in semitones; Detune in cents. "
            "Sub Osc adds a pure sine one octave below — instant sub bass reinforcement. "
            "FM Amount: oscillator 2 can FM-modulate oscillator 1 for metallic, bell-like timbres. "
            "Load custom wavetables by dragging a WAV file onto the oscillator display."
        ),
    },

    # ── Drum Rack Chain Detail ─────────────────────────────────────────────────
    {
        "id": "drum_rack_chain",
        "topic": "devices",
        "text": (
            "Drum Rack chain detail: each pad is a mini instrument rack chain. "
            "Click a pad and the bottom section shows the chain's device slots — "
            "add Simpler, Impulse, or any instrument + effects per pad. "
            "Send/Return within the rack: pads can send to internal return chains "
            "for a shared reverb or delay that only processes drum sounds from within the rack. "
            "Choke groups: pads in the same Choke Group mute each other (classic hi-hat close/open behaviour)."
        ),
    },

    # ── Follow Actions Probability ─────────────────────────────────────────────
    {
        "id": "follow_action_prob",
        "topic": "session",
        "text": (
            "Follow Action probability: each Follow Action has a Chance A and Chance B (0–100%). "
            "These are relative weights, not absolute percentages — Chance A:50 / Chance B:50 is equal probability. "
            "Chance A:90 / Chance B:10 means Action A happens 90% of the time. "
            "Set Action A to 'Again' (repeat) and Action B to 'Next' with 90/10 split "
            "for a loop that mostly repeats but occasionally advances — perfect for generative live sets."
        ),
    },

    # ── Instrument Rack Layering ──────────────────────────────────────────────
    {
        "id": "inst_rack_layer",
        "topic": "devices",
        "text": (
            "Instrument Rack layering: add multiple chains, each with a different instrument — "
            "all receive the same MIDI note and play simultaneously. "
            "Layer a piano, a pad, and a sub bass in one Instrument Rack for a rich, multi-timbral sound. "
            "Volume-balance each chain with its chain fader. "
            "Add per-chain effects (e.g. reverb on the pad chain only) without affecting the other layers. "
            "This is the primary method for thick, layered sound design in Live."
        ),
    },

    # ── Capture MIDI ──────────────────────────────────────────────────────────
    {
        "id": "capture_midi_01",
        "topic": "midi",
        "text": (
            "Capture MIDI (Cmd/Ctrl+Shift+C): Live continuously buffers the last few minutes of MIDI input, "
            "even when not recording. Press Capture after playing something you forgot to record — "
            "Live creates a clip from the buffered notes, perfectly quantised to the project BPM. "
            "It even back-calculates the tempo if you played freely. "
            "Available in both Session and Arrangement View. One of Live's most-loved workflow features."
        ),
    },

    # ── Automation Modes ──────────────────────────────────────────────────────
    {
        "id": "auto_modes_01",
        "topic": "arrangement",
        "text": (
            "Automation recording modes (the A button in the transport opens automation, "
            "the mode dropdown beside it selects behaviour): "
            "Read — plays back existing automation; ignores controller movement. "
            "Write — records all controller movement, overwriting existing automation throughout playback. "
            "Touch — records only while you hold a control; reverts to existing automation on release. "
            "Latch — starts recording when you touch a control, holds the last value when you release. "
            "Touch is safest for punching in small fixes without destroying surrounding automation."
        ),
    },

    # ── Drawing Automation ────────────────────────────────────────────────────
    {
        "id": "auto_draw_01",
        "topic": "arrangement",
        "text": (
            "Drawing automation in Arrangement View: press A to reveal automation lanes per track. "
            "Click the parameter dropdown (top of the lane) to select which parameter to automate. "
            "Press B to toggle Draw Mode (pencil) — click to place breakpoints, drag to draw freehand. "
            "Right-click a segment between breakpoints to choose its interpolation: Linear, Equal Power, etc. "
            "Hold Alt and drag the middle of a segment to curve it without adding extra breakpoints."
        ),
    },
    {
        "id": "auto_draw_02",
        "topic": "arrangement",
        "text": (
            "Automation editing tips: in select mode (arrow), click a breakpoint to move it. "
            "Shift+click multiple breakpoints to move them as a group. "
            "Ctrl+A selects all breakpoints in the lane. Delete removes selected ones. "
            "Ctrl+drag a breakpoint constrains movement to horizontal or vertical only. "
            "To lock automation to a clip (so it moves with the clip when dragged), "
            "right-click a clip > Clip Envelope Modes > Linked."
        ),
    },

    # ── Track Delay ───────────────────────────────────────────────────────────
    {
        "id": "track_delay_01",
        "topic": "mixing",
        "text": (
            "Track Delay (I/O section — enable via right-click on the header row > Track Delay): "
            "each track has a Delay value in milliseconds. "
            "Positive values push the track later in time. "
            "Negative values advance it — use to compensate for hardware synth or external instrument latency. "
            "If a hardware drum machine sounds consistently late, set its track delay to a negative value "
            "matching the round-trip latency (measure with a click + audio return test)."
        ),
    },

    # ── MIDI Output to Hardware ────────────────────────────────────────────────
    {
        "id": "midi_out_hw",
        "topic": "midi",
        "text": (
            "MIDI output to external hardware: create a MIDI track, set 'MIDI To' to your interface port. "
            "Set the channel to match the hardware's receive channel. "
            "Draw or play MIDI notes — they transmit over MIDI cable or USB to the synth or drum machine. "
            "Use the External Instrument device for a tighter workflow: "
            "it combines MIDI out and audio return in one device so the hardware appears as a native Live instrument "
            "with latency compensation built in."
        ),
    },

    # ── Multiple Audio Outputs ────────────────────────────────────────────────
    {
        "id": "multi_audio_out",
        "topic": "mixing",
        "text": (
            "Multiple audio outputs: Preferences > Audio > Output Config — enable additional output pairs. "
            "On each track's I/O section, set 'Audio To' to the desired pair (Out 3/4, Out 5/6, etc.). "
            "Drums to Out 1/2, bass to Out 3/4, synths to Out 5/6 — "
            "each hits a separate channel on a hardware mixer or FOH desk. "
            "This hybrid setup gives hardware control of individual stems while Live handles sequencing."
        ),
    },

    # ── Arrangement Overview ──────────────────────────────────────────────────
    {
        "id": "arr_overview",
        "topic": "arrangement",
        "text": (
            "Arrangement Overview (the thin strip at the very top of the Arrangement): "
            "shows the entire arrangement at a glance regardless of zoom level. "
            "Click anywhere to jump the playhead to that position. "
            "Drag the shaded region to scroll without losing zoom. "
            "Drag the edges of the shaded region to zoom in or out. "
            "Essential for quick navigation in long arrangements — "
            "jump from intro to chorus instantly without scrolling track by track."
        ),
    },

    # ── Info View ────────────────────────────────────────────────────────────
    {
        "id": "info_view_01",
        "topic": "transport",
        "text": (
            "Info View (View > Info View or the ? icon bottom-left): "
            "shows a one-line description of whatever your cursor is hovering over — "
            "device names, knob functions, button labels, and section names. "
            "Hover any unfamiliar element for an instant contextual explanation. "
            "The text also shows the keyboard shortcut for buttons that have one. "
            "Toggle it off once you know Live well to free up screen space."
        ),
    },

    # ── Scene & Clip Naming ───────────────────────────────────────────────────
    {
        "id": "scene_naming_01",
        "topic": "session",
        "text": (
            "Scene naming: double-click a Scene name (far right of each row in Session View) to rename it. "
            "Name scenes after song sections — Intro, Verse 1, Chorus, Bridge, Drop, Outro. "
            "Right-click a scene > Edit Scene to also set a BPM and time signature that activates on launch. "
            "Named, tempo-set scenes turn Session View into a complete live performance set list "
            "where launching a scene switches BPM automatically."
        ),
    },
    {
        "id": "clip_naming_01",
        "topic": "session",
        "text": (
            "Clip colour-coding: right-click any clip > Assign Colour, or use the Colour Picker at the top of the Clip View. "
            "Consistent colour language across a project makes Session View scannable instantly: "
            "e.g. drums = red, bass = dark blue, chords = green, leads = yellow, FX = purple. "
            "Shift+click multiple clips then assign a colour to batch-colour them in one step. "
            "Colour-coding is even more useful when clips are viewed on Push or a MIDI controller."
        ),
    },

    # ── Convert Audio to MIDI ─────────────────────────────────────────────────
    {
        "id": "audio_to_midi_01",
        "topic": "midi",
        "text": (
            "Convert Audio to MIDI (Live 11+): right-click an audio clip > Convert to MIDI. "
            "Four presets: Melody — extracts a monophonic pitch line (vocals, lead instruments). "
            "Harmony — extracts polyphonic chords (guitar, piano). "
            "Drums — extracts kick/snare/hi-hat transients to a Drum Rack. "
            "Rhythm — extracts rhythmic timing without pitch. "
            "The result is a MIDI clip on a new instrument track — edit, transpose, and rearrange the extracted notes freely."
        ),
    },
    {
        "id": "audio_to_midi_02",
        "topic": "midi",
        "text": (
            "Audio to MIDI quality tips: Convert Audio to MIDI works best on clean, isolated audio. "
            "A piano chord with reverb will produce noisier MIDI than a dry recording. "
            "For drums, use a separated stem (kick-only, snare-only) for cleaner transient detection. "
            "After converting, quantise the MIDI (Ctrl+U) and adjust velocities in the velocity editor "
            "to clean up extraction artefacts before using the clip in a full arrangement."
        ),
    },

    # ── Warp Markers in Depth ─────────────────────────────────────────────────
    {
        "id": "warp_markers_01",
        "topic": "clips",
        "text": (
            "Warp markers: in the Sample tab of the Clip View, double-click the waveform to place a warp marker (yellow triangle). "
            "Drag a warp marker left/right to stretch or compress the audio around that point. "
            "Pin the beats that are correct (double-click to lock a marker) so only the incorrect sections flex. "
            "Use this to fix a drummer who rushed in one bar without affecting the rest of the performance — "
            "a non-destructive alternative to cutting and nudging clips."
        ),
    },
    {
        "id": "warp_markers_02",
        "topic": "clips",
        "text": (
            "Quick warping workflow: Live auto-detects transients and places grey pseudo-warp markers. "
            "Ctrl+click a pseudo-marker to confirm it as a real warp marker. "
            "Right-click between two warp markers > Warp from Here (Straight) to align everything after a point to the grid. "
            "Right-click the waveform > Set 1.1.1 Here to declare a transient as bar 1 beat 1 — "
            "Live aligns its grid to the audio rather than the audio to the grid."
        ),
    },

    # ── Clip Launch Modes ─────────────────────────────────────────────────────
    {
        "id": "clip_launch_modes",
        "topic": "session",
        "text": (
            "Clip launch modes (Clip View > Launch tab > Launch Mode): "
            "Trigger — pressing the button starts the clip; pressing again restarts from the beginning. "
            "Gate — clip plays only while the button/key is held; releases when you let go. "
            "Toggle — first press starts, second press stops (without restarting). "
            "Repeat — holds down and re-triggers the clip at the Launch Quantisation interval for rhythmic stutter. "
            "Gate mode is ideal for one-shot FX stabs and momentary sound effects in live performance."
        ),
    },

    # ── Push 2/3 Workflow ─────────────────────────────────────────────────────
    {
        "id": "push_workflow_01",
        "topic": "performance",
        "text": (
            "Push 2/3 workflow: the 8×8 grid of 64 pads is context-sensitive. "
            "Note Mode: pads map to pitches in the current scale — every pad plays an in-scale note. "
            "Default layout: each row is a 4th higher than the one below (like a guitar). "
            "Session Mode: pads show the Session View clip grid. "
            "Step Sequencer: available when a Drum Rack is selected — each row is a drum hit, each column a 16th-note step. "
            "Press Note/Session/Sequence buttons above the grid to switch modes."
        ),
    },
    {
        "id": "push_workflow_02",
        "topic": "performance",
        "text": (
            "Push 3 standalone mode: Push 3 contains its own CPU and storage — "
            "load a Live Set onto it and perform without a laptop connected. "
            "Connect USB audio interface and MIDI controllers directly to Push 3's USB hub. "
            "Push 3 syncs with Live over Wi-Fi when the laptop is nearby. "
            "The display shows waveforms, device parameters, and the mixer — "
            "full production and performance capability in a portable controller."
        ),
    },

    # ── Freeze & Flatten ──────────────────────────────────────────────────────
    {
        "id": "freeze_flatten_01",
        "topic": "arrangement",
        "text": (
            "Freeze (right-click track > Freeze Track): renders the track to a temporary audio file, "
            "disabling all devices — CPU use drops to near zero for that track. "
            "The track is still editable: unfreeze to get all devices and MIDI back. "
            "Flatten (right-click a frozen track > Flatten): permanently converts the frozen audio to a real audio clip "
            "and removes the original devices — freeing RAM and CPU permanently. Flatten is destructive."
        ),
    },

    # ── File Manager ──────────────────────────────────────────────────────────
    {
        "id": "file_manager_01",
        "topic": "browser",
        "text": (
            "File Manager (File > Manage Files): shows all files used by the current Set. "
            "Missing Files tab: lists samples Live can't locate — click Search to let Live look automatically, "
            "or Locate to manually point to the file. "
            "Unused Files tab: lists samples in the project folder not referenced by the Set — safe to delete. "
            "Packs tab: manage installed Live Packs. "
            "Always run File Manager before archiving or sharing a project."
        ),
    },
]
