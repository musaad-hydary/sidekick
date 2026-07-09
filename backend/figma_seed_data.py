"""
Figma teaching tips — comprehensive knowledge base for ChromaDB.
Covers components, auto layout, variables, prototyping, frames, styles,
vectors, text, dev handoff, plugins, collaboration, design systems,
accessibility, and workflow shortcuts.
"""

FIGMA_TIPS = [

    # ── Components & Variants ───────────────────────────────────────────────────
    {
        "id": "fig_comp_01",
        "app": "figma",
        "topic": "components",
        "text": (
            "Create a component: select a frame or group, press Ctrl+Alt+K (Mac: ⌘+Option+K). "
            "A purple diamond marks the master component. "
            "Instances placed anywhere in the file stay linked — master changes propagate automatically. "
            "Right-click any instance > Go to Main Component to jump back to the master."
        ),
    },
    {
        "id": "fig_comp_02",
        "app": "figma",
        "topic": "components",
        "text": (
            "Double-click an instance to enter it and edit overrideable content (text, fill, nested instances) "
            "without breaking the link. Press Escape to exit. "
            "Override a specific fill: click the layer inside the instance and change its color — "
            "the master's color now shows a mixed/override indicator. "
            "Right-click > Reset All Overrides to restore master defaults."
        ),
    },
    {
        "id": "fig_comp_03",
        "app": "figma",
        "topic": "components",
        "text": (
            "Variants group multiple states (Default, Hover, Disabled, Active, Focused) into one Component Set. "
            "Select all state components, click 'Combine as variants' in the right panel. "
            "Add Variant Properties (State, Size, Theme) to create a structured matrix. "
            "Switch variants per instance via the dropdown in the Properties panel — no detaching needed."
        ),
    },
    {
        "id": "fig_comp_04",
        "app": "figma",
        "topic": "components",
        "text": (
            "Component Properties (Figma 2022+): add Boolean, Text, and Instance Swap properties to a master. "
            "Boolean toggles sub-layers on/off per instance (e.g. show/hide a leading icon). "
            "Text property lets consumers change a label from the Properties panel without entering the instance. "
            "Instance Swap lets you pick an icon from a library within a button component."
        ),
    },
    {
        "id": "fig_comp_05",
        "app": "figma",
        "topic": "components",
        "text": (
            "Nested components: place component instances inside a master component. "
            "When the nested master updates, all parents also update. "
            "Example: an icon component nested in a button component — swap the icon globally "
            "by updating the icon master, or per-instance by swapping the nested instance."
        ),
    },
    {
        "id": "fig_comp_06",
        "app": "figma",
        "topic": "components",
        "text": (
            "Component organization: group masters on a dedicated page (e.g. '🧩 Components') "
            "separate from your design pages. Wrap related components in frames with clear names. "
            "Figma uses the frame hierarchy as the component category path — "
            "'Buttons/Primary', 'Buttons/Secondary' appear grouped in the Assets panel."
        ),
    },
    {
        "id": "fig_comp_07",
        "app": "figma",
        "topic": "components",
        "text": (
            "Detach Instance (Ctrl+Alt+B) breaks the link to the master and converts to a plain group. "
            "Only do this when you truly need a one-off variation that should never update again. "
            "Prefer overrides and boolean properties — detaching makes maintenance much harder "
            "and is one of the most common causes of messy Figma files."
        ),
    },

    # ── Auto Layout ─────────────────────────────────────────────────────────────
    {
        "id": "fig_al_01",
        "app": "figma",
        "topic": "auto_layout",
        "text": (
            "Add auto layout: select a frame or group and press Shift+A. "
            "Children stack horizontally or vertically with a consistent gap. "
            "Set Direction, Gap between items, and Padding (top/right/bottom/left) in the right panel. "
            "Children reorder just by dragging them — the layout adjusts automatically."
        ),
    },
    {
        "id": "fig_al_02",
        "app": "figma",
        "topic": "auto_layout",
        "text": (
            "Sizing in auto layout — three modes for each axis: "
            "Hug Contents resizes the frame to wrap its children tightly. "
            "Fill Container stretches a child to fill all available space in the layout direction. "
            "Fixed keeps a set dimension regardless of content. "
            "Combining Hug on the container with Fill on a child gives flexible-width layouts."
        ),
    },
    {
        "id": "fig_al_03",
        "app": "figma",
        "topic": "auto_layout",
        "text": (
            "Absolute Position within auto layout: select a layer inside the frame, "
            "toggle 'Absolute position' in the right panel (or Ctrl+Alt+A on Mac). "
            "The layer floats out of the layout flow and can be placed freely inside the container. "
            "Use this for badges, close buttons, or decorative elements that must overlay content."
        ),
    },
    {
        "id": "fig_al_04",
        "app": "figma",
        "topic": "auto_layout",
        "text": (
            "Wrap mode (horizontal auto layout): enable Wrap in the Layout section. "
            "Items wrap to the next row when they exceed the container width — "
            "just like CSS flexbox wrap. Set Min/Max width on the container for responsive behavior. "
            "Use for tag clouds, chip groups, or any layout that should flow across multiple lines."
        ),
    },
    {
        "id": "fig_al_05",
        "app": "figma",
        "topic": "auto_layout",
        "text": (
            "Min and Max width/height on auto layout children (2023+): "
            "set a minimum width so a button never shrinks below its comfortable tap target, "
            "and a maximum so it doesn't grow wider than a column. "
            "Combined with Fill Container this gives responsive behavior — "
            "the element grows to fill but stops at the max."
        ),
    },
    {
        "id": "fig_al_06",
        "app": "figma",
        "topic": "auto_layout",
        "text": (
            "Nested auto layouts are the foundation of any component: "
            "a Card component might be a vertical auto layout (image + content area), "
            "where content is a horizontal auto layout (avatar + text stack), "
            "and text stack is another vertical auto layout (name + subtitle). "
            "Each layer handles one axis — the whole thing is fully responsive with no manual positioning."
        ),
    },
    {
        "id": "fig_al_07",
        "app": "figma",
        "topic": "auto_layout",
        "text": (
            "Spacing between items: hold Alt while dragging a child in an auto layout to set "
            "its individual spacing — overrides the global gap just for that item. "
            "For most consistent designs, use a single global gap and control spacing "
            "with padding on sub-containers rather than per-item overrides."
        ),
    },

    # ── Variables & Design Tokens ────────────────────────────────────────────────
    {
        "id": "fig_var_01",
        "app": "figma",
        "topic": "variables",
        "text": (
            "Variables (Figma 2023+) store reusable values: Color, Number, String, Boolean. "
            "Open with Edit > Local Variables. Bind any fill, stroke, padding, gap, corner radius, "
            "or size field to a variable — a change to the variable updates every bound element instantly."
        ),
    },
    {
        "id": "fig_var_02",
        "app": "figma",
        "topic": "variables",
        "text": (
            "Variable Modes let one collection hold multiple value sets. "
            "A Colors collection with Light and Dark modes lets you assign one variable to a fill, "
            "then switch the entire frame to Dark mode and all bound fills update. "
            "Apply modes per-frame — use Light for most of the file and Dark on specific screens."
        ),
    },
    {
        "id": "fig_var_03",
        "app": "figma",
        "topic": "variables",
        "text": (
            "Number variables drive spacing and sizing: define a spacing scale (4, 8, 12, 16, 24, 32) "
            "as variables named spacing/sm, spacing/md, etc. Bind auto layout padding and gap to them. "
            "If the design direction changes from 8pt to 10pt grid, you change one value "
            "and every component updates. This is the foundation of a proper spacing system."
        ),
    },
    {
        "id": "fig_var_04",
        "app": "figma",
        "topic": "variables",
        "text": (
            "Boolean variables control component logic in prototypes. "
            "Bind a boolean variable to a conditional visibility layer (show/hide) — "
            "then in the prototype, use 'Set variable' actions to toggle it on click. "
            "This enables state-driven interactions: a toggle switch that actually stays toggled "
            "as you navigate the prototype."
        ),
    },
    {
        "id": "fig_var_05",
        "app": "figma",
        "topic": "variables",
        "text": (
            "Variables vs Styles: Styles (colors, text, effects) are great for static shared values "
            "that don't need modes or logical variation. Variables are better when you need "
            "semantic token aliasing (color/primary → blue/500), multiple modes (Light/Dark), "
            "or prototype interactivity. For most modern design systems, prefer variables for color."
        ),
    },

    # ── Frames & Constraints ──────────────────────────────────────────────────────
    {
        "id": "fig_frame_01",
        "app": "figma",
        "topic": "frames",
        "text": (
            "Frames (F key or A key) are the core containers. Unlike groups, frames have: "
            "their own background, clip content, constraints, auto layout, layout grids, and scroll behavior. "
            "Always prefer frames over groups for any structural container. "
            "Use Ctrl+Alt+G (Mac: ⌘+Option+G) to wrap a selection in a frame instantly."
        ),
    },
    {
        "id": "fig_frame_02",
        "app": "figma",
        "topic": "frames",
        "text": (
            "Constraints (right panel > Constraints section) control how a layer reacts when its parent resizes. "
            "Left & Right stretches horizontally (CSS width: 100%). "
            "Center pins to the center horizontally. "
            "Top & Bottom stretches vertically. "
            "Scale resizes proportionally. Combine to build responsive layouts without auto layout."
        ),
    },
    {
        "id": "fig_frame_03",
        "app": "figma",
        "topic": "frames",
        "text": (
            "Clip Content (right panel checkbox): when on, children outside the frame boundary are hidden — "
            "like CSS overflow: hidden. When off, children can spill out visibly. "
            "Use Clip Content on scroll containers (cards, modals, image thumbnails). "
            "Turn it off for tooltips, dropdown menus, or shadows that extend outside the frame."
        ),
    },
    {
        "id": "fig_frame_04",
        "app": "figma",
        "topic": "frames",
        "text": (
            "Prototype scroll: select a frame, set scroll behavior in the Prototype tab to Horizontal, "
            "Vertical, or Both. Set the frame to a smaller fixed size (e.g. 375×812 phone) — "
            "content inside that extends beyond the frame becomes scrollable in the prototype viewer. "
            "Fixed elements (nav bars, FABs): set their position to 'Fixed' in the prototype scroll section."
        ),
    },

    # ── Styles ──────────────────────────────────────────────────────────────────
    {
        "id": "fig_style_01",
        "app": "figma",
        "topic": "styles",
        "text": (
            "Create a Style: click + next to Fill, Text, Effect, or Layout Grid in the right panel. "
            "Name it descriptively (Primary/500, Heading/H1, Shadow/Card). "
            "Editing the style propagates to all elements using it. "
            "Styles are scoped to the file; publish via Assets panel > Publish to share across files."
        ),
    },
    {
        "id": "fig_style_02",
        "app": "figma",
        "topic": "styles",
        "text": (
            "Text styles store the full typographic definition: font family, size, weight, "
            "line height, letter spacing, and paragraph spacing. "
            "Apply text styles to all text layers — never set type ad hoc. "
            "When a type decision changes (e.g. body size from 16px to 15px), "
            "edit the style once and every text layer using it updates."
        ),
    },
    {
        "id": "fig_style_03",
        "app": "figma",
        "topic": "styles",
        "text": (
            "Effect styles: save drop shadows, inner shadows, and blurs as reusable styles. "
            "Name them semantically: Shadow/Raised, Shadow/Overlay, Blur/Frosted. "
            "A card might use Shadow/Raised; a modal scrim uses Blur/Frosted. "
            "One change to the style updates every card and modal in the file."
        ),
    },
    {
        "id": "fig_style_04",
        "app": "figma",
        "topic": "styles",
        "text": (
            "Swap libraries: when migrating from an old component library to a new one, "
            "use Main Menu > Libraries > Swap Library. "
            "Figma automatically replaces all instances and styles from the old library "
            "with their equivalents from the new one — much faster than manually re-linking components."
        ),
    },

    # ── Prototyping ──────────────────────────────────────────────────────────────
    {
        "id": "fig_proto_01",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Switch to Prototype tab. Hover an element to reveal the blue hotspot handle — "
            "drag it to any frame to create a navigation link. "
            "Set Trigger (On Click, On Hover, On Drag, After Delay, Key/Gamepad), "
            "Action (Navigate To, Open Overlay, Swap Overlay, Scroll To, Set Variable), "
            "and Animation (Smart Animate, Slide, Push, Dissolve, etc.)."
        ),
    },
    {
        "id": "fig_proto_02",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Smart Animate automatically tweens matching layers between two frames. "
            "Name layers identically on both frames (e.g. 'Card'). "
            "Figma interpolates position, size, rotation, opacity, and corner radius. "
            "Works best when the same component appears in both frames in different states — "
            "the tween makes interactions feel native and polished."
        ),
    },
    {
        "id": "fig_proto_03",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Overlays let you show modals, drawers, tooltips, and menus without replacing the whole screen. "
            "In the prototype connection, change Navigate To → Open Overlay. "
            "Set Position to Center (modal), Manual (anchored to click position), or a fixed edge. "
            "Close Overlay action or click-outside-to-close option removes it."
        ),
    },
    {
        "id": "fig_proto_04",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "After Delay trigger: auto-advances to the next frame after N milliseconds. "
            "Use for splash screens, loading states, success confirmations, or guided tours. "
            "Combine with Dissolve animation for elegant auto-fade transitions. "
            "Set a long delay (3000ms) for onboarding steps the user reads before moving on."
        ),
    },
    {
        "id": "fig_proto_05",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Interactive Components (Figma 2022+): add prototype connections inside a component itself. "
            "A checkbox can toggle its own state (Unchecked → Checked) on click — "
            "every instance in the prototype exhibits this behaviour without you wiring each one manually. "
            "Enable in the component's own Prototype tab. Works within variant sets."
        ),
    },
    {
        "id": "fig_proto_06",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Variable-driven prototypes: use Set Variable action to change a variable on interaction. "
            "Bind layer visibility to a Boolean variable — the element shows/hides based on variable state. "
            "Chain multiple Set Variable actions in one interaction to update multiple states at once. "
            "This replaces workarounds like stacked variant combinations for complex stateful flows."
        ),
    },
    {
        "id": "fig_proto_07",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Present prototype: Ctrl+Alt+Enter (Mac: ⌘+Option+Enter) enters presentation mode. "
            "Choose a device frame, background color, and starting frame in the prototype settings. "
            "Share a prototype link (Share > Anyone with link can view) to send to stakeholders — "
            "they see and interact with it in a browser without a Figma account."
        ),
    },

    # ── Vectors & Shapes ─────────────────────────────────────────────────────────
    {
        "id": "fig_vec_01",
        "app": "figma",
        "topic": "vectors",
        "text": (
            "Pen tool (P): click for corner points, click+drag for Bezier curves. "
            "Enter or double-click the last point to finish an open path. "
            "Click the first point to close a path. "
            "Double-click any vector on the canvas to enter Vector Edit mode and adjust individual anchor points."
        ),
    },
    {
        "id": "fig_vec_02",
        "app": "figma",
        "topic": "vectors",
        "text": (
            "Vector networks: unlike traditional path tools, Figma allows multiple paths branching "
            "from a single anchor point without separate layers. "
            "This makes icon construction more flexible — draw a star burst or complex symbol "
            "as one vector network rather than multiple combined paths."
        ),
    },
    {
        "id": "fig_vec_03",
        "app": "figma",
        "topic": "vectors",
        "text": (
            "Boolean operations: Union (merges shapes), Subtract (cuts top shape from bottom), "
            "Intersect (keeps only overlap), Exclude (keeps non-overlapping areas). "
            "Select two or more overlapping shapes and pick from the toolbar dropdown. "
            "Flatten (Ctrl+E) converts the boolean result to a single editable vector permanently."
        ),
    },
    {
        "id": "fig_vec_04",
        "app": "figma",
        "topic": "vectors",
        "text": (
            "Anchor point types in Vector Edit mode: click a point and use the toolbar buttons to switch: "
            "Mirrored (smooth symmetric handle), Disconnected (independent handles), "
            "Asymmetric (different lengths, same direction), Corner (no handles, sharp). "
            "You can also drag a handle while holding Alt to break the mirroring and create asymmetric curves."
        ),
    },
    {
        "id": "fig_vec_05",
        "app": "figma",
        "topic": "vectors",
        "text": (
            "Strokes have advanced options: Open the Stroke section > three dots for advanced settings. "
            "Position: Inside, Center, Outside (like CSS box-sizing). "
            "Cap style: Butt, Round, Square. Join style: Miter, Round, Bevel. "
            "Dashed strokes: enable Dashes and set Dash length and Gap. "
            "Stroke endpoints can be dragged to trim/extend in vector edit mode."
        ),
    },

    # ── Text & Typography ────────────────────────────────────────────────────────
    {
        "id": "fig_text_01",
        "app": "figma",
        "topic": "text",
        "text": (
            "T creates text. Click for auto-width (grows with content). "
            "Click-drag to create a fixed-width text box. "
            "In the right panel, set text resize to: Auto Width, Auto Height (fixed width, grows vertically), "
            "or Fixed (clips text). Use Auto Height for body text in cards so the card grows with content."
        ),
    },
    {
        "id": "fig_text_02",
        "app": "figma",
        "topic": "text",
        "text": (
            "Line height controls vertical spacing between lines. Letter spacing adjusts horizontal tracking. "
            "Paragraph spacing adds space between paragraphs (after pressing Enter). "
            "In long-form text, line height ~140–160% of font size improves readability. "
            "These values are all available in text styles — define them once."
        ),
    },
    {
        "id": "fig_text_03",
        "app": "figma",
        "topic": "text",
        "text": (
            "Mixed typography in one text layer: highlight specific characters with the text cursor, "
            "then change their weight, color, or size in the right panel. "
            "Use this for inline emphasis (bold keyword in a sentence) without splitting into multiple text layers. "
            "Inspect in Dev Mode shows per-run text properties for engineering handoff."
        ),
    },
    {
        "id": "fig_text_04",
        "app": "figma",
        "topic": "text",
        "text": (
            "Text truncation: set a text box to Fixed size, then switch Overflow to Truncate — "
            "text that doesn't fit shows an ellipsis (…). "
            "Use this in list items, table cells, or anywhere text length is unpredictable. "
            "Truncation is a prototype-only visual; call it out explicitly in dev specs."
        ),
    },
    {
        "id": "fig_text_05",
        "app": "figma",
        "topic": "text",
        "text": (
            "Variable fonts: some fonts (Inter, Roboto Flex, etc.) expose weight/width/slant as continuous axes. "
            "Figma exposes these as sliders in the text panel when a variable font is selected. "
            "Animate font weight in a prototype using a number variable bound to the weight axis — "
            "creates expressive transitions like a label getting bolder on selection."
        ),
    },

    # ── Images & Fills ───────────────────────────────────────────────────────────
    {
        "id": "fig_fill_01",
        "app": "figma",
        "topic": "fills",
        "text": (
            "Image fills: drag an image file onto a shape to fill it, or add an Image fill via the Fill section. "
            "Fill modes: Fill (covers the shape, may crop), Fit (shows entire image, may letterbox), "
            "Crop (lets you reposition inside the shape), Tile (repeats). "
            "Double-click an image fill thumbnail in the Fill section to enter Crop mode and reposition."
        ),
    },
    {
        "id": "fig_fill_02",
        "app": "figma",
        "topic": "fills",
        "text": (
            "Gradient fills: Linear, Radial, Angular, Diamond. "
            "Click any color stop on the gradient bar to change its color/opacity. "
            "Drag stops to reposition. Add new stops by clicking on the bar. "
            "Rotate a linear gradient by dragging the line endpoint in the canvas gradient editor. "
            "Layer multiple gradient fills with different blend modes for complex background effects."
        ),
    },
    {
        "id": "fig_fill_03",
        "app": "figma",
        "topic": "fills",
        "text": (
            "Blend modes on fills and layers: Normal, Multiply, Screen, Overlay, Color Dodge, Color Burn, "
            "Luminosity, etc. Apply per-fill (in the fill row) or per-layer (at the top of the right panel). "
            "Multiply darkens: use a dark gradient with Multiply to add a text-shadow effect over a photo. "
            "Screen lightens: use for light overlays without bleaching to white."
        ),
    },

    # ── Effects ──────────────────────────────────────────────────────────────────
    {
        "id": "fig_effect_01",
        "app": "figma",
        "topic": "effects",
        "text": (
            "Drop Shadow: offset X/Y, blur radius, spread, color+opacity. "
            "Use small blur (2–4px), low offset (0–2px), low opacity (15–25%) for subtle elevation. "
            "Stack multiple drop shadows to simulate ambient + directional lighting. "
            "Inner Shadow creates a debossed/pressed look — useful for input fields and toggle troughs."
        ),
    },
    {
        "id": "fig_effect_02",
        "app": "figma",
        "topic": "effects",
        "text": (
            "Background Blur blurs content behind a layer — frosted glass effect. "
            "Works only when the layer itself has some transparency (reduce fill opacity). "
            "Layer Blur blurs the layer itself and its children. "
            "Use Background Blur for modals, tooltips, and navigation bars over content. "
            "Performance note: background blur is GPU-intensive — avoid stacking many blurred layers."
        ),
    },

    # ── Layout Grids ────────────────────────────────────────────────────────────
    {
        "id": "fig_grid_01",
        "app": "figma",
        "topic": "layout_grids",
        "text": (
            "Add a layout grid: click + in the Layout Grid section in the right panel on any frame. "
            "Grid type: Grid (uniform squares), Column (vertical bands), Row (horizontal bands). "
            "Toggle visibility with Ctrl+Shift+4. Multiple grids can coexist on one frame — "
            "layer a column grid and a base-8 square grid for maximum snapping flexibility."
        ),
    },
    {
        "id": "fig_grid_02",
        "app": "figma",
        "topic": "layout_grids",
        "text": (
            "Column grid for responsive web: 12 columns with a margin and gutter. "
            "Common values: 375px mobile (4 cols, 16px margin, 8px gutter), "
            "768px tablet (8 cols, 24px margin, 16px gutter), "
            "1440px desktop (12 cols, 80px margin, 24px gutter). "
            "Design on these grids so developers can translate column spans directly to CSS Grid."
        ),
    },
    {
        "id": "fig_grid_03",
        "app": "figma",
        "topic": "layout_grids",
        "text": (
            "8-point grid: a square grid with 8px cells. Set all spacing, padding, and sizing to multiples of 8. "
            "This gives visual rhythm and aligns naturally with most component libraries and CSS defaults. "
            "Use 4px for micro-spacing within components (icon-to-label gap, border-to-content padding). "
            "Grid snapping (View > Snap to Grid) makes placement effortless."
        ),
    },

    # ── Developer Handoff ────────────────────────────────────────────────────────
    {
        "id": "fig_dev_01",
        "app": "figma",
        "topic": "handoff",
        "text": (
            "Dev Mode (Shift+D): toggle for developers. Shows px values, spacing, font specs, "
            "and code snippets (CSS, iOS Swift, Android Compose) for every selected element. "
            "Mark frames as 'Ready for development' to signal the design is finalized. "
            "Developers can comment, inspect, and export without ever editing the design."
        ),
    },
    {
        "id": "fig_dev_02",
        "app": "figma",
        "topic": "handoff",
        "text": (
            "Export assets: select any layer, click + next to Export in the right panel. "
            "Set scale (1x, 2x, 3x for mobile), format (PNG for rasters, SVG for vectors, "
            "WebP for optimized web, PDF for print). "
            "Layers marked as exportable are surfaced to developers in Dev Mode. "
            "Click Export [name] to download immediately, or Ctrl+Shift+E for a batch export dialog."
        ),
    },
    {
        "id": "fig_dev_03",
        "app": "figma",
        "topic": "handoff",
        "text": (
            "Copy CSS: right-click a selected layer → Copy/Paste as → Copy as CSS. "
            "Figma outputs relevant properties: dimensions, border-radius, colors, "
            "box-shadow, font, flex layout direction, and padding for auto layout frames. "
            "Copy as SVG works for vector shapes and icons. Copy as PNG copies a rasterized image."
        ),
    },
    {
        "id": "fig_dev_04",
        "app": "figma",
        "topic": "handoff",
        "text": (
            "Sections (Figma 2023+): draw a section (S key) to group frames on the canvas. "
            "Sections appear as collapsible groups in Dev Mode, making it easy for developers to find "
            "all screens for a specific user flow. Mark individual sections as ready — "
            "partial handoffs become possible without marking the whole file."
        ),
    },
    {
        "id": "fig_dev_05",
        "app": "figma",
        "topic": "handoff",
        "text": (
            "Inspect panel details: when a developer selects a layer in Inspect (or Dev Mode), "
            "they see the computed value, not the raw style — distances between elements, "
            "not the variable name. Show them the design token mapping separately in documentation, "
            "or use a Tokens Studio plugin that exports variable-to-token mappings."
        ),
    },

    # ── Collaboration ────────────────────────────────────────────────────────────
    {
        "id": "fig_collab_01",
        "app": "figma",
        "topic": "collaboration",
        "text": (
            "Multiplayer: multiple people can edit the same file simultaneously. "
            "See each collaborator as a colored cursor with their avatar. "
            "Click their avatar in the toolbar to follow their view. "
            "Cmd+Click their avatar enters observation mode — you follow without them knowing."
        ),
    },
    {
        "id": "fig_collab_02",
        "app": "figma",
        "topic": "collaboration",
        "text": (
            "Comments (C key): click anywhere on the canvas to leave a pinned comment. "
            "@mention teammates to notify them. Resolve comments when addressed — "
            "use the filter to show only unresolved. "
            "In prototype mode, comments appear at the canvas coordinates and are visible to stakeholders."
        ),
    },
    {
        "id": "fig_collab_03",
        "app": "figma",
        "topic": "collaboration",
        "text": (
            "Share settings: Share > Can Edit or Can View. "
            "View-only links let stakeholders inspect, comment, download assets, and view prototypes "
            "without the ability to modify anything. "
            "To share a single frame: right-click it > Copy Link to Selection — "
            "the link opens the file centred on that frame."
        ),
    },
    {
        "id": "fig_collab_04",
        "app": "figma",
        "topic": "collaboration",
        "text": (
            "Version history: Main Menu > File > Show Version History (Ctrl+Alt+S). "
            "Figma auto-saves versions every 30 minutes and on significant changes. "
            "Click any version to preview it. Restore a version to roll back the entire file. "
            "Name important milestones manually (right-click a version > Name This Version) — "
            "'Before rebrand', 'Client approved v2', etc."
        ),
    },
    {
        "id": "fig_collab_05",
        "app": "figma",
        "topic": "collaboration",
        "text": (
            "Branching (Figma Pro): create a branch from a file to experiment safely. "
            "The branch is a full copy of the file — make changes, preview them, "
            "then merge back into the main file or discard. "
            "Ideal for major redesigns, A/B explorations, or client alternatives "
            "without touching the production design file."
        ),
    },

    # ── Shortcuts ───────────────────────────────────────────────────────────────
    {
        "id": "fig_short_01",
        "app": "figma",
        "topic": "shortcuts",
        "text": (
            "Shape tools: R = Rectangle, O = Ellipse, L = Line, P = Pen, T = Text, F/A = Frame, V = Select. "
            "Hold Shift while drawing to constrain to square or circle. "
            "Hold Alt while drawing to create from center outward. "
            "Ctrl+drag a shape to duplicate without entering the tool."
        ),
    },
    {
        "id": "fig_short_02",
        "app": "figma",
        "topic": "shortcuts",
        "text": (
            "Layer operations: Ctrl+G = Group, Ctrl+Shift+G = Ungroup, Ctrl+Alt+G = Frame selection. "
            "Ctrl+[ = send backward, Ctrl+] = bring forward. "
            "Ctrl+Shift+[ = send to back, Ctrl+Shift+] = bring to front. "
            "Ctrl+D = duplicate in place. Alt+drag = duplicate and move in one gesture."
        ),
    },
    {
        "id": "fig_short_03",
        "app": "figma",
        "topic": "shortcuts",
        "text": (
            "Ctrl+/ (Mac: ⌘+/) opens Quick Actions — search any command, navigate to pages, "
            "run recently used plugins, or jump to any named layer. "
            "This is the most powerful shortcut in Figma — learn it first and save minutes every session."
        ),
    },
    {
        "id": "fig_short_04",
        "app": "figma",
        "topic": "shortcuts",
        "text": (
            "Zoom: Ctrl+0 = fit page, Ctrl+1 = 100%, Ctrl+Shift+H = fit selection to viewport. "
            "+ / - zoom in and out. Hold Space to pan (hand tool) from any other tool. "
            "Ctrl+R = rename selected layer. "
            "Ctrl+Alt+C = copy properties (fill, stroke, effects) to paste with Ctrl+Alt+V onto another layer."
        ),
    },
    {
        "id": "fig_short_05",
        "app": "figma",
        "topic": "shortcuts",
        "text": (
            "Selection shortcuts: hold Ctrl to click-select through stacked layers. "
            "Hold Shift to add/remove from selection. "
            "Double-click enters a group or component. Escape goes up one level. "
            "Ctrl+A selects all top-level layers on the page. "
            "Right-click > Select Layer to pick a specific layer under the cursor from a list."
        ),
    },
    {
        "id": "fig_short_06",
        "app": "figma",
        "topic": "shortcuts",
        "text": (
            "Nudge values: arrow keys move by 1px. Shift+Arrow moves by 10px (customisable in settings). "
            "Ctrl+arrow keys resize the selection by 1px in that direction. "
            "For consistent nudging, set Big Nudge to 8px in Figma Preferences > Nudge Amount "
            "to match your 8pt grid system."
        ),
    },

    # ── Pages & File Organization ────────────────────────────────────────────────
    {
        "id": "fig_org_01",
        "app": "figma",
        "topic": "organization",
        "text": (
            "Pages act as separate canvases within a file. Use them to separate: "
            "Cover page (file thumbnail), Design (the working screens), "
            "Components (master library page), Archive (old versions), "
            "Explorations (rough ideas). Prefix page names with emoji for quick visual scanning — "
            "📱 Design, 🧩 Components, 🗃 Archive."
        ),
    },
    {
        "id": "fig_org_02",
        "app": "figma",
        "topic": "organization",
        "text": (
            "Layer naming conventions: descriptive names (Card/Product, Nav/TopBar) appear in Inspect, "
            "code export, and the Assets panel. Name every layer — avoid 'Frame 42' or 'Rectangle 7'. "
            "Batch rename: select multiple layers, Ctrl+R, use search/replace syntax [✦] or numbered sequences. "
            "Good names make the file usable for any team member without guidance."
        ),
    },
    {
        "id": "fig_org_03",
        "app": "figma",
        "topic": "organization",
        "text": (
            "Sections (S key or from the toolbar) group related frames on the canvas with a label. "
            "Use sections per user flow: Onboarding, Home, Product Detail, Checkout. "
            "Sections show up as collapsible groups in the Layers panel and Dev Mode — "
            "making large files navigable for developers and reviewers."
        ),
    },

    # ── Accessibility ────────────────────────────────────────────────────────────
    {
        "id": "fig_a11y_01",
        "app": "figma",
        "topic": "accessibility",
        "text": (
            "Color contrast: text needs 4.5:1 ratio against its background for AA compliance, "
            "3:1 for large text (18pt+ or 14pt+ bold). Use the Contrast plugin or Stark to check. "
            "Never rely on color alone to convey information — add icons, labels, or patterns. "
            "Check your design in Grayscale (Accessibility > Simulate) to catch color-only issues."
        ),
    },
    {
        "id": "fig_a11y_02",
        "app": "figma",
        "topic": "accessibility",
        "text": (
            "Focus order for prototypes: in the Prototype tab, enable 'Set prototype starting frame' "
            "and define the keyboard tab order using the flow arrows. "
            "Mark layers as accessible and set their ARIA roles and labels in the Layers panel "
            "accessibility options — engineers can read these in Dev Mode for implementation guidance."
        ),
    },

    # ── Plugins ─────────────────────────────────────────────────────────────────
    {
        "id": "fig_plugin_01",
        "app": "figma",
        "topic": "plugins",
        "text": (
            "Open Plugin Manager from Main Menu > Plugins > Manage Plugins (or Ctrl+/). "
            "Essential plugins: Iconify (150,000+ icons in-canvas), Unsplash (free photos), "
            "Content Reel (realistic placeholder names, avatars, data), "
            "Stark (accessibility checker), Tokens Studio (design token management), "
            "Figma to Code (export to React/HTML/Tailwind)."
        ),
    },
    {
        "id": "fig_plugin_02",
        "app": "figma",
        "topic": "plugins",
        "text": (
            "Automate repetitive tasks with plugins: "
            "Similayer selects all layers matching specific properties (same color, same font size). "
            "Find and Replace searches text across the entire file. "
            "Batch Styler applies or replaces styles across many elements at once. "
            "These save hours on large-file maintenance or rebrand work."
        ),
    },

    # ── Design Systems ───────────────────────────────────────────────────────────
    {
        "id": "fig_ds_01",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "A design system in Figma has: a token/variable layer (colors, spacing, typography values), "
            "a styles layer (named styles bound to variables), "
            "a component library (published masters), and documentation. "
            "Build these in a separate Design System file and publish the library — "
            "all product files link to it as a dependency."
        ),
    },
    {
        "id": "fig_ds_02",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Publish a library: in the Assets panel (Ctrl+Alt+O), click the book icon > Publish. "
            "Team members open their files, go to Assets > Libraries, and enable your library. "
            "All published components and styles appear in their Assets panel. "
            "Updates to the library surface as a 'Library updates available' banner in consuming files."
        ),
    },
    {
        "id": "fig_ds_03",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Color token naming: use semantic names rather than values. "
            "Bad: #0066FF. Good: color/brand/primary, color/text/default, color/surface/card. "
            "The semantic layer (Primary) references a primitive (Blue/500) via variable aliasing. "
            "In Dark mode, Primary still means the right blue — it just resolves to a different primitive value."
        ),
    },
    {
        "id": "fig_ds_04",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Spacing scale example: define spacing primitives (spacing/1=4px, spacing/2=8px, spacing/3=12px, "
            "spacing/4=16px, spacing/5=24px, spacing/6=32px, spacing/8=48px, spacing/10=64px). "
            "Bind component padding and gap to these. Changing spacing/4 from 16px to 14px — "
            "every component using it tightens simultaneously."
        ),
    },
    {
        "id": "fig_ds_05",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Component base + modifier pattern: create a base component with all possible slots, "
            "then use Boolean properties to hide/show slots per instance. "
            "Example: a List Item component has Icon (Boolean), Avatar (Boolean), "
            "Supporting text (Boolean), Trailing element (Boolean). "
            "One master component, infinite combinations — no separate variants for each combination."
        ),
    },

    # ── Import & Export ──────────────────────────────────────────────────────────
    {
        "id": "fig_export_01",
        "app": "figma",
        "topic": "export",
        "text": (
            "Import files: drag .fig, .sketch, .svg, .png, .jpg, or .pdf onto the Figma canvas or into the browser tab. "
            ".sketch imports with reasonable fidelity (some effects may differ). "
            ".svg imports as fully editable vector layers. "
            ".pdf imports each page as a frame (non-editable but inspectable)."
        ),
    },
    {
        "id": "fig_export_02",
        "app": "figma",
        "topic": "export",
        "text": (
            "Batch export: Ctrl+Shift+E opens the Export dialog listing all layers marked for export. "
            "Review and export them all at once as a ZIP. "
            "This is the standard handoff workflow: mark all icons and images for export, "
            "then hand developers the ZIP. They can also trigger their own exports from Dev Mode."
        ),
    },

    # ── FigJam ──────────────────────────────────────────────────────────────────
    {
        "id": "fig_fj_01",
        "app": "figma",
        "topic": "figjam",
        "text": (
            "FigJam is Figma's whiteboard product — accessible from the Figma dashboard by creating a new FigJam file. "
            "Use it for brainstorming, user journey mapping, retros, and team workshops. "
            "Sticky notes (S), shapes, connectors, stamps, and freehand drawing are built in. "
            "Participants can join and collaborate in real time with no Figma account needed for invited guests."
        ),
    },
    {
        "id": "fig_fj_02",
        "app": "figma",
        "topic": "figjam",
        "text": (
            "FigJam connectors (C key): click and drag from any shape's edge to create a directed arrow. "
            "Double-click a connector to add a label. Change connector style (straight, elbow, curved) "
            "in the right panel. Use connectors to build flowcharts, system diagrams, or user flows "
            "alongside the designs in FigJam."
        ),
    },
    {
        "id": "fig_fj_03",
        "app": "figma",
        "topic": "figjam",
        "text": (
            "Embed Figma designs in FigJam: paste a Figma file link into FigJam and it embeds as a live preview. "
            "Click the embed to jump to the Figma file. Use this to reference screens while mapping "
            "user journeys or annotating design decisions on a whiteboard. "
            "Both files stay in sync — the embed always shows the latest version."
        ),
    },

    # ── Advanced Prototyping Techniques ──────────────────────────────────────────
    {
        "id": "fig_proto_adv_01",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "On Drag interaction: set trigger to 'On Drag' and action to 'Navigate To' with a Slide animation. "
            "This creates swipeable card stacks, carousels, and drawer interactions. "
            "Combine with 'Swap Overlay' for a drawer that slides in from the side "
            "and can be dismissed by dragging back."
        ),
    },
    {
        "id": "fig_proto_adv_02",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Conditional logic with variables: use 'Conditional' action type on a trigger. "
            "Set the condition (If variable X equals Y) and define separate actions for true/false paths. "
            "Example: If cart_count > 0, navigate to Checkout; else show an empty cart modal. "
            "This enables branching prototype flows that feel like real apps."
        ),
    },
    {
        "id": "fig_proto_adv_03",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Number variable increments: use 'Set variable' with an expression like cart_count + 1 "
            "on an Add to Cart button. Display the variable in a text layer bound to it. "
            "The cart badge number increments with each click in the prototype — "
            "no multiple frame duplication required."
        ),
    },
    {
        "id": "fig_proto_adv_04",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Prototype starting point and flows: click a frame (not inside it) and in the Prototype tab "
            "click '+' next to Flows to name this frame as a flow starting point. "
            "Multiple flows let you share direct links to specific sections of the prototype — "
            "share the Onboarding flow link with the UX researcher and the Checkout flow with the PM."
        ),
    },

    # ── Advanced Text & Typography ────────────────────────────────────────────────
    {
        "id": "fig_typo_01",
        "app": "figma",
        "topic": "text",
        "text": (
            "OpenType features: click the three dots (...) next to the font name in the right panel "
            "to access OpenType options — ligatures, tabular numbers, stylistic sets, small caps, etc. "
            "Enable Tabular Numbers for tables and data displays so number columns align perfectly. "
            "Enable Ligatures for headings that use typographic ligatures (fi, fl, ff combinations)."
        ),
    },
    {
        "id": "fig_typo_02",
        "app": "figma",
        "topic": "text",
        "text": (
            "Baseline alignment in mixed-size text: when you have an icon and a label at different sizes "
            "in an auto layout row, align them by Baseline in the auto layout alignment options. "
            "This aligns the bottom of each element's text baseline — "
            "far more precise than center alignment for mixed type sizes."
        ),
    },
    {
        "id": "fig_typo_03",
        "app": "figma",
        "topic": "text",
        "text": (
            "Responsive text sizing: use Min/Max width on a text layer's parent auto layout frame "
            "combined with Fill Container on the text to make body text that reflows naturally. "
            "For fluid type, use variables with different values per breakpoint mode — "
            "switch the frame's mode between Mobile and Desktop to see text resize."
        ),
    },

    # ── Advanced Components & Slots ───────────────────────────────────────────────
    {
        "id": "fig_comp_slot_01",
        "app": "figma",
        "topic": "components",
        "text": (
            "Slot pattern: create a generic container component with an empty auto layout frame as a 'slot'. "
            "Other components can be dropped into the slot using Instance Swap property. "
            "Example: a Modal component with a Content slot — swap in a Form, Confirmation, or Media component "
            "without duplicating the modal chrome (header, footer, overlay)."
        ),
    },
    {
        "id": "fig_comp_slot_02",
        "app": "figma",
        "topic": "components",
        "text": (
            "Preferred values for Instance Swap: in the master component, click an Instance Swap property, "
            "then add 'Preferred Values' — a curated list of which components make sense in that slot. "
            "Designers using the component see a filtered picker with only the valid options, "
            "preventing misuse and documenting design intent at the component level."
        ),
    },

    # ── Performance & Large Files ────────────────────────────────────────────────
    {
        "id": "fig_perf_01",
        "app": "figma",
        "topic": "performance",
        "text": (
            "Large file performance: avoid putting every screen in one file. "
            "Split by product area (Onboarding, Core Product, Settings) or by design phase. "
            "Flatten complex illustration layers (Ctrl+E) to reduce node count. "
            "Rasterize complex vector art (right-click > Flatten) — reduces memory without changing appearance. "
            "Detach or archive unused pages."
        ),
    },
    {
        "id": "fig_perf_02",
        "app": "figma",
        "topic": "performance",
        "text": (
            "Image optimization in Figma: imported images are stored in their original resolution. "
            "Right-click an image > Set Image Fill > re-export at 2x for Retina and use that. "
            "Avoid placing full-resolution 10MB photos directly — resize them in a photo editor first. "
            "Use WebP format for web projects (smaller file size, same quality)."
        ),
    },
    {
        "id": "fig_perf_03",
        "app": "figma",
        "topic": "performance",
        "text": (
            "Hidden layers still consume memory. Periodically review the Layers panel for invisible layers "
            "that are no longer needed and delete them. "
            "Use Plugins > Clean Document (or similar) to find orphaned components, empty frames, "
            "and detached instances that bloat the file. Run this before handing off to development."
        ),
    },

    # ── Figma AI ────────────────────────────────────────────────────────────────
    {
        "id": "fig_ai_01",
        "app": "figma",
        "topic": "ai_features",
        "text": (
            "Figma AI (2024+) features: Rename Layers automatically renames all selected layers with "
            "descriptive names based on their visual content. "
            "Generate Copy fills placeholder text with context-appropriate copy (button labels, headings, body). "
            "Remove Background removes the background from images in one click. "
            "Access AI features from the right-click menu or the toolbar."
        ),
    },
    {
        "id": "fig_ai_02",
        "app": "figma",
        "topic": "ai_features",
        "text": (
            "Figma AI component suggestions: select a loose group of elements and AI suggests "
            "which existing component from your library it matches — prompting you to replace it "
            "with the proper component instance. Keeps files consistent without manually auditing every screen."
        ),
    },

    # ── Responsive Design Strategies ─────────────────────────────────────────────
    {
        "id": "fig_resp_01",
        "app": "figma",
        "topic": "responsive",
        "text": (
            "Breakpoint strategy: design Mobile (375px), Tablet (768px), and Desktop (1440px) frames. "
            "Use the same components across all — only layout changes (column count, spacing, font size). "
            "Variable modes for spacing and type size let you switch a frame's breakpoint mode "
            "and see the whole layout reflow using token-bound values."
        ),
    },
    {
        "id": "fig_resp_02",
        "app": "figma",
        "topic": "responsive",
        "text": (
            "Min/Max sizing on auto layout frames (right panel > Size dropdown > Min/Max): "
            "set max-width on a content container (e.g. 1200px) and center it — "
            "the container grows to fill the frame but stops at max width, just like CSS max-width + margin: auto. "
            "Combine with Fill Container on the outer frame to simulate a centered web layout at any breakpoint."
        ),
    },

    # ── Design QA & Annotation ───────────────────────────────────────────────────
    {
        "id": "fig_qa_01",
        "app": "figma",
        "topic": "design_qa",
        "text": (
            "Annotation plugins: Figma has no built-in annotation system (as of 2024). "
            "Use Annotations by Figma (official plugin) or Redline/Lingo to add numbered notes, "
            "spacing arrows, and measurements directly on the canvas. "
            "Annotations should document constraints, states, and behaviors that aren't obvious from the design."
        ),
    },
    {
        "id": "fig_qa_02",
        "app": "figma",
        "topic": "design_qa",
        "text": (
            "Design QA checklist before handoff: all layers named meaningfully, "
            "all text using styles or variables, all colors using styles or variables, "
            "no detached instances, export assets marked, prototype covers all main flows and edge cases, "
            "accessibility contrast checked, components use auto layout (not fixed positioning). "
            "Use a shared Checklist component in each screen's annotations."
        ),
    },

    # ── Tokens Studio ────────────────────────────────────────────────────────────
    {
        "id": "fig_tokens_01",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Tokens Studio (plugin): manages design tokens as JSON synced to a Git repo (GitHub, GitLab). "
            "Define primitive and semantic tokens in JSON, sync to Figma, "
            "and engineer teams can pull the same JSON directly into their codebase. "
            "Tokens Studio bridges the design–engineering gap for spacing, color, and typography tokens "
            "better than Figma Variables alone (which don't yet export to code natively)."
        ),
    },

    # ── Storybook & Engineering Workflow ─────────────────────────────────────────
    {
        "id": "fig_eng_01",
        "app": "figma",
        "topic": "engineering_workflow",
        "text": (
            "Figma ↔ Storybook workflow: use the Storybook Connect plugin to embed live Storybook stories "
            "alongside Figma components. Engineers see the live code component next to the design spec. "
            "Designers see if their component has been built. "
            "This closes the loop: design changes prompt component updates, and vice versa."
        ),
    },
    {
        "id": "fig_eng_02",
        "app": "figma",
        "topic": "engineering_workflow",
        "text": (
            "CSS Grid and Flexbox mapping: auto layout horizontal = CSS flexbox row. "
            "Auto layout vertical = CSS flexbox column. "
            "Hug Contents = width/height: fit-content. Fill Container = flex: 1. "
            "Fixed size = explicit width/height. Gap in auto layout = gap in CSS. "
            "Document this mapping in your design system so engineers translate directly."
        ),
    },

    # ── Advanced Fills & Overlays ────────────────────────────────────────────────
    {
        "id": "fig_adv_fill_01",
        "app": "figma",
        "topic": "fills",
        "text": (
            "Video fills (Figma 2023+): add a video file as a fill on any frame or shape. "
            "The video plays in the prototype viewer automatically. "
            "Use this for app preview screens with hero video, loading animations, or video ads mockups. "
            "Supported formats: MP4. Video fills are not exported — they're prototype-only."
        ),
    },
    {
        "id": "fig_adv_fill_02",
        "app": "figma",
        "topic": "fills",
        "text": (
            "Noise and grain fill: Figma doesn't have a built-in noise texture, "
            "but you can add grain via a PNG noise overlay layer set to Overlay or Soft Light blend mode "
            "at low opacity (5–15%). This adds a tactile, slightly analog feel to flat designs. "
            "Export the noise tile from Figma Community or generate it with the Noise & Texture plugin."
        ),
    },

    # ── Interaction Design Patterns ──────────────────────────────────────────────
    {
        "id": "fig_ixd_01",
        "app": "figma",
        "topic": "interaction_patterns",
        "text": (
            "Bottom sheet / drawer pattern: place the sheet content below the screen frame, "
            "then use On Drag > Navigate To with a Smart Animate upward to reveal it. "
            "A drag handle affordance at the top of the sheet signals interactivity. "
            "Add an 'On Drag Down' connection back to the original frame to close it."
        ),
    },
    {
        "id": "fig_ixd_02",
        "app": "figma",
        "topic": "interaction_patterns",
        "text": (
            "Tab bar navigation pattern: each tab button links to a different frame. "
            "The destination frames all have the same tab bar component with the corresponding tab active. "
            "Use 'Swap Overlay' if you want the tab bar to stay fixed while only the content area changes — "
            "avoids the entire screen sliding on tab switches."
        ),
    },
    {
        "id": "fig_ixd_03",
        "app": "figma",
        "topic": "interaction_patterns",
        "text": (
            "Skeleton loading screens: duplicate a content frame and replace all text and images "
            "with gray rectangle placeholders of the same size. "
            "Use After Delay (1000–2000ms) to transition from the skeleton to the loaded state. "
            "This is the industry standard for communicating load states — "
            "more effective than spinners because users can see the layout before content arrives."
        ),
    },
    {
        "id": "fig_ixd_04",
        "app": "figma",
        "topic": "interaction_patterns",
        "text": (
            "Toast / snackbar notifications: design a notification banner as a component. "
            "Use Open Overlay with position 'Bottom Center' and an After Delay trigger to auto-dismiss it. "
            "Combine with Smart Animate for the slide-up appearance. "
            "The overlay appears over any screen without needing a separate frame for each state."
        ),
    },

    # ── Touch Targets & Accessibility Sizes ───────────────────────────────────
    {
        "id": "fig_touch_01",
        "app": "figma",
        "topic": "accessibility",
        "text": (
            "Minimum touch target size: Apple HIG recommends 44×44pt; Google Material 3 recommends 48×48dp. "
            "Even if the visual element (icon, text) is smaller, its tap zone must meet these minimums. "
            "In Figma, design the hit area as a transparent background layer inside the component, "
            "sized to 44×44px, so developers can reference the correct clickable region."
        ),
    },
    {
        "id": "fig_touch_02",
        "app": "figma",
        "topic": "accessibility",
        "text": (
            "WCAG color contrast requirements: AA level requires 4.5:1 ratio for normal text, 3:1 for large text (18px+ or 14px+ bold). "
            "AAA level requires 7:1 for normal text. "
            "In Figma, use the built-in Color Blindness simulator (View > Color Blindness) "
            "and third-party plugins like 'Contrast' or 'A11y - Color Contrast Checker' to verify all text meets WCAG."
        ),
    },
    {
        "id": "fig_touch_03",
        "app": "figma",
        "topic": "accessibility",
        "text": (
            "Focus indicators: every interactive element must have a visible focus ring for keyboard navigation (WCAG 2.4.7). "
            "Design focus states for every component — typically a 2px offset ring in the brand accent color. "
            "Use Figma's interactive components to create a Focus variant so developers can see exactly how focus should look on each element."
        ),
    },

    # ── Dark Mode Design ──────────────────────────────────────────────────────
    {
        "id": "fig_darkmode_01",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Dark mode colour system: avoid pure black (#000000) backgrounds — use dark grays (#121212–#1E1E1E). "
            "Don't simply invert light mode colors; instead design a separate elevation system: "
            "the higher a surface, the lighter its shade (Material Design elevation model). "
            "Define dark variants of every color token (background/surface/on-surface/primary/error) "
            "and switch them with Figma Variables in a dedicated 'dark' mode collection."
        ),
    },
    {
        "id": "fig_darkmode_02",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Shadows in dark mode: drop shadows are nearly invisible on dark backgrounds. "
            "Replace with a lighter elevation overlay (a white fill at low opacity, e.g. 8–16%). "
            "Strokes (1px, low opacity) can also define elevation layers. "
            "Use Figma Variables to map `shadow-color` to a different value in dark mode "
            "so a single component token handles both themes."
        ),
    },

    # ── RTL & Internationalisation ────────────────────────────────────────────
    {
        "id": "fig_rtl_01",
        "app": "figma",
        "topic": "accessibility",
        "text": (
            "RTL (Right-to-Left) layout support for Arabic, Hebrew, Persian: "
            "select all text and change the text direction to 'Right' in the Text panel. "
            "Mirror Auto Layout direction by setting it to 'Right to Left' in the Auto Layout settings. "
            "Icons that imply direction (arrows, play buttons, caret) should be flipped; "
            "icons that don't (clock, search magnifier) stay the same."
        ),
    },
    {
        "id": "fig_i18n_01",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Internationalisation text expansion: German and Finnish text can be 30–40% longer than English; "
            "RTL languages need mirrored layouts. "
            "Design with content-driven Auto Layout so strings expand without breaking layouts. "
            "Test your components with longer strings using the 'Content Reel' or 'Lorem ipsum' plugin. "
            "Set Min Width on text containers so they expand gracefully."
        ),
    },

    # ── Motion & Easing ───────────────────────────────────────────────────────
    {
        "id": "fig_easing_01",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Easing curves in Smart Animate: in the transition panel, click the curve icon to open the easing editor. "
            "Ease Out (fast start, slow end) for elements entering the screen — feels natural as they slow into place. "
            "Ease In (slow start, fast end) for elements leaving — mimics real acceleration. "
            "Linear feels robotic; always use easing for UI motion. "
            "Duration: 150–300ms for micro-interactions; 300–500ms for larger transitions."
        ),
    },
    {
        "id": "fig_easing_02",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Spring animations in Figma: available in the transition settings as 'Spring' type. "
            "Stiffness controls how rigid the spring is (high = fast snap), "
            "Damping controls how quickly oscillation dies (low damping = bouncy). "
            "Spring animations feel more physical and alive than cubic-bezier easing. "
            "Use for interactive elements like toggles, checkboxes, and pull-to-refresh indicators."
        ),
    },

    # ── Figma Slides ─────────────────────────────────────────────────────────
    {
        "id": "fig_slides_01",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Figma Slides: a native presentation tool inside Figma. "
            "Create a presentation from a File > New Slides file type. "
            "Frames become slides; you can embed live Figma design frames directly in a slide. "
            "Present in browser or full-screen via Presentation Mode. "
            "Collaborators can join the presentation live and see the presenter's slide in real time."
        ),
    },
    {
        "id": "fig_slides_02",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Embedding live prototypes in Figma Slides: insert a Figma frame as an interactive embed. "
            "Viewers can click through the prototype within the slide presentation — "
            "no need to switch tabs when demoing to stakeholders. "
            "Great for design reviews where you show context slides alongside interactive prototype demos."
        ),
    },

    # ── Presentation Mode ─────────────────────────────────────────────────────
    {
        "id": "fig_present_01",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Presentation Mode (⌘/Ctrl+P or the Play button): shows a prototype in full screen. "
            "Arrow keys navigate between connected frames. "
            "R restarts the prototype. "
            "Hold Z to enter zoom mode and click to focus on details. "
            "Share a presentation link (Share > Share Prototype) for stakeholders who don't have Figma accounts — "
            "they can comment on specific frames via the URL."
        ),
    },

    # ── Multi-File Library Architecture ──────────────────────────────────────
    {
        "id": "fig_library_02",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Multi-file library architecture for large teams: "
            "split a design system into separate Figma files — Foundations (colors, type, spacing), "
            "Components (atoms, molecules), Patterns (organisms, templates). "
            "Each file publishes its own library. Product files subscribe only to the layers they need. "
            "Updating a Foundations change only requires republishing that file, "
            "reducing merge conflicts and review scope."
        ),
    },
    {
        "id": "fig_library_03",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Library update notifications: when a published component changes, "
            "all files using it see a notification in the Assets panel with a blue dot. "
            "Click 'Review and Update' to see a diff of what changed before accepting. "
            "Reject updates to specific components to pin a file to an older version while others update."
        ),
    },

    # ── Icon System Workflow ──────────────────────────────────────────────────
    {
        "id": "fig_icons_01",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Icon system best practices: all icons should be the same base size (e.g. 24×24) "
            "with a consistent visual weight (stroke width, fill vs outline). "
            "Set the icon as a component and add a 'size' variant (16/20/24/32) using scale. "
            "Always flatten SVG paths inside the icon and set 'Fill' rather than 'Stroke' — "
            "strokes don't scale perfectly and export inconsistently."
        ),
    },
    {
        "id": "fig_icons_02",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "SVG import from Illustrator: paste or use File > Place Image. "
            "Figma imports SVG groups as frames. "
            "Always 'Detach' and 'Flatten' imported SVGs before publishing as components — "
            "nested groups from Illustrator retain layer names that pollute your component structure. "
            "Check for mixed fill/stroke paths and convert strokes to fills (Object > Expand Appearance in AI first)."
        ),
    },
    {
        "id": "fig_icons_03",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Icon swapping with component properties: create one icon slot in a component. "
            "Add a 'Component Property > Instance Swap' pointing to your icon set. "
            "Designers can swap any icon without unlocking the component. "
            "Name icon components with a consistent prefix (e.g. 'icon/arrow-right') "
            "so they all appear together in the swap panel dropdown."
        ),
    },

    # ── Typography Scale ──────────────────────────────────────────────────────
    {
        "id": "fig_typo_09",
        "app": "figma",
        "topic": "typography",
        "text": (
            "Type scale: use a modular scale ratio (e.g. 1.25 Major Third or 1.333 Perfect Fourth) "
            "to create harmonious font sizes. Start with a base size (16px), multiply by ratio for larger steps. "
            "Common scales: 12/14/16/20/24/32/40/48. "
            "Define each step as a Figma Text Style so every size is available from the style picker."
        ),
    },
    {
        "id": "fig_typo_10",
        "app": "figma",
        "topic": "typography",
        "text": (
            "Line height and letter spacing: "
            "body text: line height 1.5× font size (e.g. 24px for 16px text). "
            "Headings: tighter, around 1.1–1.2×. "
            "Letter spacing for small caps or UI labels: +2–5% (positive tracking). "
            "Large display text: -1% to -2% (negative tracking for tightness). "
            "These are perceptual rules, not absolutes — test with real content at real sizes."
        ),
    },

    # ── Device Frames ─────────────────────────────────────────────────────────
    {
        "id": "fig_frames_05",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Device frames: in the Design panel with a Frame selected, "
            "scroll to 'Frame > Device' to overlay a device mockup (iPhone 15, Pixel 7, MacBook, etc.) "
            "around your frame in presentation mode. "
            "This adds the device hardware chrome automatically — no need to import phone frame assets. "
            "Enable 'Mirror' in Presentation Mode to show the device on an iPhone via the Figma Mirror app."
        ),
    },

    # ── Multi-Page Navigation Prototyping ─────────────────────────────────────
    {
        "id": "fig_proto_12",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Multi-page navigation in a prototype: set a Flow Starting Point on each top-level screen. "
            "Connect screens across pages using the prototype arrow and selecting the destination page frame. "
            "This lets a single prototype file span mobile (one page) and tablet (another page) flows "
            "without duplicating all your component instances."
        ),
    },

    # ── Component Documentation ───────────────────────────────────────────────
    {
        "id": "fig_compdoc_01",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Component documentation with annotations: use the 'Annotations' feature (Design > Annotations) "
            "to mark spacing, component names, and interaction notes directly on a design — "
            "visible in Dev Mode without cluttering the design layer. "
            "Third-party plugins like 'Figma Tokens' or 'EightShapes Specs' auto-generate spec sheets "
            "with all spacing, color, and typography values extracted."
        ),
    },
    {
        "id": "fig_compdoc_02",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Component playground frames: create a dedicated page named 'Playground' in your library file. "
            "Show each component's variants, states, and composition examples in a grid. "
            "Add text annotations explaining when to use each variant. "
            "This serves as living documentation — whenever the component updates, the playground "
            "automatically reflects the change because it uses real component instances."
        ),
    },

    # ── Missing Fonts & SVG Workflow ──────────────────────────────────────────
    {
        "id": "fig_fonts_01",
        "app": "figma",
        "topic": "typography",
        "text": (
            "Missing fonts: Figma shows a red highlight on text with fonts not installed locally. "
            "Install the Figma Font Installer app (desktop) to load all system fonts. "
            "For files using commercial fonts (brand typefaces), download the font files and install them locally. "
            "Or use 'Substitute Font' in the missing font dialog to replace them with an available fallback "
            "for review purposes without permanently changing the design."
        ),
    },

    # ── Figma API Basics ──────────────────────────────────────────────────────
    {
        "id": "fig_api_01",
        "app": "figma",
        "topic": "dev_handoff",
        "text": (
            "Figma REST API: access any file's structure at GET /v1/files/{file_key}. "
            "Retrieve image renders at /v1/images/{file_key}?ids={node_id}. "
            "Personal Access Tokens are created in Settings > Account > Personal Access Tokens. "
            "The API is read-only for most endpoints — useful for automating documentation generation, "
            "extracting design tokens, or building Figma → code sync tools."
        ),
    },

    # ── Figma Shortcuts (more) ────────────────────────────────────────────────
    {
        "id": "fig_shortcuts_07",
        "app": "figma",
        "topic": "shortcuts",
        "text": (
            "Essential Figma shortcuts: "
            "Ctrl/Cmd+D = duplicate in place, Ctrl+Alt+C = copy properties, Ctrl+Alt+V = paste properties. "
            "Ctrl+E = flatten selection to a single vector. "
            "Ctrl+Shift+E = export selected (opens export panel). "
            "Ctrl+G = group, Ctrl+Alt+G = ungroup. "
            "Hold Option/Alt while dragging = duplicate while moving."
        ),
    },
    {
        "id": "fig_shortcuts_08",
        "app": "figma",
        "topic": "shortcuts",
        "text": (
            "Quick style shortcuts: "
            "B = fill with solid color (opens fill picker). "
            "Ctrl+Shift+H = flip horizontal, Ctrl+Shift+V = flip vertical. "
            "Ctrl+[ and Ctrl+] = send backward/forward. Ctrl+Alt+[ and Ctrl+Alt+] = send to back/front. "
            "Shift+drag corner to scale proportionally. "
            "Hold Ctrl while resizing to resize from center."
        ),
    },

    # ── Variable-Driven Prototypes ────────────────────────────────────────────
    {
        "id": "fig_varproto_01",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Variable conditionals in prototypes (Figma Variables): "
            "set a number variable 'step' to 0. On a Next button, add a 'Set Variable' action: step = step + 1. "
            "On each frame, add a 'Conditional' node: if step == 1, navigate to Step 2 frame. "
            "This creates branching logic and multi-step flows without duplicating frames for every state."
        ),
    },

    # ── Design QA (more) ─────────────────────────────────────────────────────
    {
        "id": "fig_qa_03",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Design token audit: use the 'Variables / Tokens' section in Dev Mode to inspect which tokens "
            "are applied to each element. If a design uses a hardcoded hex instead of a token, "
            "it will show as a raw value without a token name — a red flag during QA. "
            "Run a plugin like 'Find and Replace' or 'Similayer' to batch-fix hardcoded values."
        ),
    },
    {
        "id": "fig_qa_04",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Alignment QA: select all elements on a frame and use 'Tidy Up' (right-click) "
            "or the Align panel to check for misaligned items. "
            "Figma's 'Highlight pixel-misaligned objects' (Preferences > Snap to pixel grid) "
            "flags any element not sitting on whole-pixel boundaries — critical for raster rendering clarity."
        ),
    },

    # ── FigJam Additional ─────────────────────────────────────────────────────
    {
        "id": "fig_figjam_04",
        "app": "figma",
        "topic": "figjam",
        "text": (
            "FigJam templates: start from a library of templates (retrospectives, flow diagrams, mind maps, "
            "journey maps, concept maps, Kanban boards). "
            "Customize them for your team and save as a private template. "
            "Share a FigJam board link for async brainstorming — participants add sticky notes "
            "with reactions (thumbs-up, heart, question mark) without needing a Figma license."
        ),
    },

    # ── Performance (Figma file) ───────────────────────────────────────────────
    {
        "id": "fig_perf_04",
        "app": "figma",
        "topic": "performance",
        "text": (
            "Optimise a large Figma file: "
            "delete unused components and styles (Assets panel > right-click unused items). "
            "Rasterize complex vector elements you won't edit (right-click > Flatten). "
            "Split a monolithic file into multiple pages or separate files for different product areas. "
            "Avoid stacking many large images — compress them to WebP/JPEG before importing."
        ),
    },
    {
        "id": "fig_perf_05",
        "app": "figma",
        "topic": "performance",
        "text": (
            "Vector path simplification: complex paths imported from Illustrator may have hundreds of points. "
            "Select the path, then Edit > Simplify Path (Ctrl+Alt+K) to reduce anchor count. "
            "Simplification threshold controls how closely the result matches the original. "
            "Fewer path points = faster Figma rendering and smaller file size."
        ),
    },

    # ── Copy as CSS / React ───────────────────────────────────────────────────
    {
        "id": "fig_copy_css",
        "app": "figma",
        "topic": "dev_handoff",
        "text": (
            "Copy as CSS: right-click any element > Copy/Paste As > Copy as CSS. "
            "Figma outputs all visual properties (width, height, background, border-radius, "
            "box-shadow, font-size, etc.) as CSS. "
            "In Dev Mode, the right panel shows code snippets in CSS, iOS (Swift), and Android (XML/Compose). "
            "Use these as a starting point — they capture the visual spec even if the exact code needs adaptation."
        ),
    },
    {
        "id": "fig_copy_react",
        "app": "figma",
        "topic": "dev_handoff",
        "text": (
            "Copy as React / Tailwind: third-party plugins (Anima, Builder.io, Locofy) translate "
            "Figma frames into React JSX + Tailwind or CSS Modules. "
            "Results require cleanup but capture structure, spacing, and styles accurately. "
            "For design systems, this bridges the gap between Figma components and production code components — "
            "keep both in sync with a token-based workflow."
        ),
    },

    # ── Dev Mode Deep Dive ────────────────────────────────────────────────────
    {
        "id": "fig_devmode_01",
        "app": "figma",
        "topic": "dev_handoff",
        "text": (
            "Dev Mode (Shift+D to toggle): a dedicated view for engineers with measurement overlays, "
            "code snippets, and asset export. Click any element to see all its properties in code. "
            "Hover over two elements while holding Alt to see the distance between them (spacing/padding). "
            "Dev Mode is read-only — engineers can inspect without accidentally moving things."
        ),
    },
    {
        "id": "fig_devmode_02",
        "app": "figma",
        "topic": "dev_handoff",
        "text": (
            "Dev Mode 'Ready for Dev' sections: designers can mark specific frames or sections as "
            "'Ready for Development' (right-click > Mark as Ready for Development). "
            "Engineers filter the file to only see Ready frames — reduces confusion about which designs are final. "
            "Section notes in Dev Mode let designers add context and implementation hints directly on the design."
        ),
    },

    # ── Branching & Merging ───────────────────────────────────────────────────
    {
        "id": "fig_branch_01",
        "app": "figma",
        "topic": "collaboration",
        "text": (
            "Branching (Organization/Enterprise plan): duplicate a file into a Branch "
            "(File > Create Branch). Edit the branch independently — a 'B' badge appears on the file. "
            "When ready, request a review and merge back into the Main file. "
            "Merging shows a diff of component and style changes so reviewers can approve or reject individual changes. "
            "Prevents breaking main while experimenting with major redesigns."
        ),
    },
    {
        "id": "fig_branch_02",
        "app": "figma",
        "topic": "collaboration",
        "text": (
            "Branch review: use the 'Review Changes' panel before merging. "
            "Accept or reject each changed component individually — "
            "you don't have to merge everything from a branch. "
            "Branch history is preserved even after merging, so you can reference what changed and why. "
            "This workflow mirrors Git pull requests for design files."
        ),
    },

    # ── Figma Community ───────────────────────────────────────────────────────
    {
        "id": "fig_community_01",
        "app": "figma",
        "topic": "shortcuts",
        "text": (
            "Figma Community (community.figma.com): thousands of free files, UI kits, icon sets, "
            "design systems, and templates shared by the community. "
            "Click 'Duplicate to your Drafts' to get an editable copy. "
            "Search for app-specific UI kits (iOS 17, Material 3, Windows 11) to start with platform-accurate components. "
            "Community plugins and widgets are installed directly from the Community tab inside Figma."
        ),
    },

    # ── Nudge Amount Preferences ──────────────────────────────────────────────
    {
        "id": "fig_nudge_01",
        "app": "figma",
        "topic": "shortcuts",
        "text": (
            "Nudge amounts: arrow keys move elements by 1px (small nudge). "
            "Shift+arrow moves by 8px (big nudge). "
            "Change the big nudge value in Preferences > Big Nudge — "
            "set it to your design grid spacing (8 or 10) for grid-aligned movement. "
            "Consistent nudge values ensure spacing tokens are respected when adjusting layout manually."
        ),
    },

    # ── Cursor Types ──────────────────────────────────────────────────────────
    {
        "id": "fig_cursor_01",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Cursor types in prototypes: in the Prototype connection settings, change the cursor style "
            "shown when a user hovers over an interactive element: Default (arrow), Hand (pointer), "
            "Text (I-beam), Zoom (magnifier). "
            "Set to Hand for buttons and links to signal clickability. "
            "These cursor hints appear during prototype presentation and in the published prototype URL."
        ),
    },

    # ── Rulers & Guides ───────────────────────────────────────────────────────
    {
        "id": "fig_guides_01",
        "app": "figma",
        "topic": "shortcuts",
        "text": (
            "Rulers and guides: show rulers with Shift+R. "
            "Drag from the ruler onto the canvas to create a guide line. "
            "Double-click a guide to set its exact position numerically. "
            "Drag a guide back to the ruler to delete it. "
            "View > Guides to toggle guide visibility. "
            "Guides are per-page and don't appear in exports — they're layout helpers only."
        ),
    },

    # ── Scroll Position in Prototypes ────────────────────────────────────────
    {
        "id": "fig_scroll_01",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Scroll position preserve: in the prototype connection, enable 'Maintain Scroll Position' "
            "so the destination frame remembers scroll offset when navigating back. "
            "This prevents the jarring jump back to the top when a user goes to a detail page and returns. "
            "Works for vertical and horizontal scroll frames."
        ),
    },

    # ── Figma Desktop App ─────────────────────────────────────────────────────
    {
        "id": "fig_desktop_01",
        "app": "figma",
        "topic": "shortcuts",
        "text": (
            "Figma Desktop app advantages over web: "
            "local font access without the Font Installer extension, "
            "quicker keyboard shortcuts (no browser shortcut conflicts), "
            "offline mode (limited — opens recently synced files). "
            "The desktop app is Electron-based — same rendering as web. "
            "Figma Mirror (iOS/Android) connects to the desktop app over the same Wi-Fi network "
            "to preview designs on a real device in real time."
        ),
    },

    # ── Import from Sketch ────────────────────────────────────────────────────
    {
        "id": "fig_sketch_import",
        "app": "figma",
        "topic": "shortcuts",
        "text": (
            "Importing from Sketch: File > Import and select a .sketch file. "
            "Figma imports pages, artboards, symbols (as components), and text styles. "
            "Limitations: some Sketch plugins and non-standard effects don't translate. "
            "Check imported symbols — they may need names normalised to match your component structure. "
            "After importing, run the 'Symbol Organizer' plugin to clean up the component page."
        ),
    },

    # ── Plugin Development ────────────────────────────────────────────────────
    {
        "id": "fig_plugin_dev_01",
        "app": "figma",
        "topic": "dev_handoff",
        "text": (
            "Figma Plugin API basics: plugins are JavaScript/TypeScript running in a sandboxed iframe. "
            "The plugin manifest.json defines the plugin name, permissions, and entry points. "
            "Access the document via figma.currentPage and figma.selection. "
            "Create nodes with figma.createFrame(), figma.createText(), etc. "
            "Use figma.ui.postMessage / onmessage for UI ↔ plugin communication. "
            "Test locally with Desktop app > Plugins > Development > Import plugin from manifest."
        ),
    },

    # ── Figma for VS Code ─────────────────────────────────────────────────────
    {
        "id": "fig_vscode_01",
        "app": "figma",
        "topic": "dev_handoff",
        "text": (
            "Figma for VS Code extension: install from the VS Code marketplace. "
            "Open a Figma file directly inside VS Code — browse layers, inspect properties, copy CSS. "
            "Link Figma components to code components for bi-directional navigation. "
            "Access design tokens and variables from the code side without switching apps. "
            "Particularly useful for teams maintaining a design system with a companion component library."
        ),
    },

    # ── Working Offline ───────────────────────────────────────────────────────
    {
        "id": "fig_offline_01",
        "app": "figma",
        "topic": "collaboration",
        "text": (
            "Working offline in Figma: the Desktop app caches recently opened files. "
            "If you lose internet, you can continue editing — changes queue locally and sync when reconnected. "
            "The web app has no offline mode. "
            "If multiple editors make conflicting edits offline and then sync, "
            "Figma uses a CRDT (conflict-free replicated data type) to merge non-conflicting changes automatically."
        ),
    },

    # ── Prototype Hidden State / Hover ────────────────────────────────────────
    {
        "id": "fig_proto_hover",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Show on hover interaction: set a component to have a Default and Hover variant. "
            "In the prototype panel, add a 'While Hovering' trigger > 'Change To' the Hover variant. "
            "This simulates CSS :hover states in prototypes — tooltips, button highlights, navigation dropdowns. "
            "Combine with Smart Animate for smooth fade/scale transitions on hover."
        ),
    },

    # ── Multiplayer & Emoji Reactions ─────────────────────────────────────────
    {
        "id": "fig_collab_06",
        "app": "figma",
        "topic": "collaboration",
        "text": (
            "Multiplayer cursors: all editors in a file appear as named cursors in real time. "
            "Click any collaborator's avatar (top right) to jump to their viewport. "
            "Emoji reactions: press E during a presentation to react with an emoji that floats on screen — "
            "useful for live design reviews. 'Spotlight' mode pins your viewport to the presenter's for guided walkthroughs."
        ),
    },

    # ── Image Fill Modes & Adjustments ────────────────────────────────────────
    {
        "id": "fig_image_fill_01",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Image fill modes: select any shape and add a Fill of type Image. "
            "Fill — scales to cover the shape, crops edges (like CSS background-size: cover). "
            "Fit — scales to fit entirely inside, shows empty space on sides (like contain). "
            "Crop — lets you drag the image to reposition within the shape manually. "
            "Tile — tiles the image repeatedly (good for patterns and textures)."
        ),
    },
    {
        "id": "fig_image_adj_01",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Image adjustments in Figma: click an image fill > Adjustments (the sliders icon). "
            "Control Exposure (brightness), Contrast, Saturation, Temperature (warm/cool), and Tint. "
            "Highlights and Shadows sliders give Lightroom-style selective tone control. "
            "These are non-destructive — the original image file is unchanged. "
            "Use to unify varied photo styles across a design without pre-editing in Photoshop."
        ),
    },

    # ── Masking with Images ───────────────────────────────────────────────────
    {
        "id": "fig_mask_01",
        "app": "figma",
        "topic": "vectors",
        "text": (
            "Masking in Figma: place the mask shape below the content to be masked in the layer panel. "
            "Select both, then right-click > Use as Mask (or Ctrl/Cmd+Alt+M). "
            "The shape's outline clips the content above it — only what's inside the shape is visible. "
            "Any shape works as a mask (rectangle, circle, custom vector). "
            "The mask is identified by a circle icon in the layer panel."
        ),
    },
    {
        "id": "fig_mask_02",
        "app": "figma",
        "topic": "vectors",
        "text": (
            "Alpha mask: place an image with transparency (PNG) as the mask shape. "
            "The alpha channel of the image determines what shows through — "
            "white = fully visible, black = fully hidden, grey = semi-transparent. "
            "Use a gradient PNG as a mask to create soft-edge image fade-outs "
            "without needing a dedicated alpha channel in the original photo."
        ),
    },

    # ── Variables by Type ─────────────────────────────────────────────────────
    {
        "id": "fig_var_number",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Number variables: store spacing, radius, opacity, or sizing values as reusable tokens. "
            "Create in the Variables panel > Number. "
            "Bind to any numeric property: corner radius, width, height, opacity, stroke width. "
            "Define spacing tokens (spacing/4 = 4, spacing/8 = 8, spacing/16 = 16) and "
            "apply them to padding values in Auto Layout for system-wide spacing control."
        ),
    },
    {
        "id": "fig_var_string",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "String variables: store text content as tokens. "
            "Bind a string variable to a text layer's content. "
            "Create multiple modes — e.g. English/French/German — and each mode stores the translated string. "
            "Switching the active mode updates all bound text layers simultaneously — "
            "the fastest way to prototype localisation across an entire design without duplicating frames."
        ),
    },
    {
        "id": "fig_var_boolean",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Boolean variables: true/false values that control layer visibility. "
            "Create a Boolean variable and bind it to a layer's visibility toggle (in the Layers panel). "
            "In a prototype, use 'Set Variable' action to toggle the boolean — "
            "the bound layer shows or hides without needing separate component variants for every show/hide state. "
            "Massively reduces component bloat for show/hide interactions."
        ),
    },
    {
        "id": "fig_var_vs_styles",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Variables vs Styles — when to use each: "
            "Styles (colors, text, effects): apply a fixed value by name — best for design-time reuse. "
            "Variables: store a value that can change across modes (light/dark, desktop/mobile, locale) — best for theming. "
            "If a color needs to change in dark mode, use a Color Variable, not a Style. "
            "Styles can reference Variables — publish a Style that points to a Variable for the best of both."
        ),
    },

    # ── Prototype Interaction Triggers ────────────────────────────────────────
    {
        "id": "fig_trigger_delay",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "After Delay trigger: fires a transition automatically after a set millisecond delay. "
            "Use it for auto-advancing onboarding slides, dismissing a toast after 3 seconds, "
            "or showing a loading skeleton before revealing content. "
            "Set the delay in the Prototype panel after choosing 'After Delay' as the trigger. "
            "Combine with Back navigation to loop back to a starting frame."
        ),
    },
    {
        "id": "fig_trigger_hover",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Mouse Enter / Mouse Leave triggers: "
            "Mouse Enter fires when the cursor enters the element's bounding box. "
            "Mouse Leave fires when it exits. "
            "Use to show a tooltip on Mouse Enter and hide it on Mouse Leave. "
            "Combine with Change To (variant) for dropdown menus that open on hover and close when the cursor leaves."
        ),
    },
    {
        "id": "fig_trigger_key",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Key/Gamepad trigger: fires on a specific keyboard key press. "
            "Select an element, add interaction > Trigger: Key/Gamepad > type the key (e.g. Escape, Enter, Arrow Left). "
            "Use to prototype keyboard-driven interactions: dismiss a modal on Escape, "
            "navigate a gallery with arrow keys, or submit a form on Enter. "
            "Works inside the prototype viewer — not just in the editor."
        ),
    },
    {
        "id": "fig_trigger_scroll",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Scroll Into View trigger: fires when the user scrolls an element into the viewport within a scrollable frame. "
            "Use for lazy-load animations — a card that fades in as the user scrolls down to it. "
            "Combine with Smart Animate (opacity 0 → 1, or translateY 20px → 0) for reveal-on-scroll effects. "
            "The triggering element must be inside a scrollable frame (overflow: scroll)."
        ),
    },

    # ── SVG Export ────────────────────────────────────────────────────────────
    {
        "id": "fig_export_svg",
        "app": "figma",
        "topic": "export",
        "text": (
            "SVG export best practices: select a vector layer or component > Export > SVG. "
            "Enable 'Include ID Attribute' so engineers can target individual SVG elements in CSS/JS. "
            "Flatten the vector first (Ctrl+E) to merge all paths — reduces SVG complexity. "
            "Outline all text (Type > Outline Stroke) before SVG export so fonts don't need to be installed on the viewer's system. "
            "Check exported SVGs in a browser or SVGOMG to verify and compress."
        ),
    },

    # ── FigJam: Timer & Dot Voting ────────────────────────────────────────────
    {
        "id": "fig_figjam_timer",
        "app": "figma",
        "topic": "figjam",
        "text": (
            "FigJam Timer: click the Timer widget (or add via Widgets panel) for time-boxed workshop activities. "
            "Set a countdown for brainstorming rounds, affinity mapping, or voting sessions. "
            "The timer is visible to all participants simultaneously. "
            "Pair with a 2-minute timer for silent brainstorming (everyone writes stickies alone) "
            "then open discussion — reduces groupthink."
        ),
    },
    {
        "id": "fig_figjam_voting",
        "app": "figma",
        "topic": "figjam",
        "text": (
            "Dot voting in FigJam: add the Voting widget (Widgets > Voting). "
            "Each participant gets a set number of votes (dots) to place on stickies or ideas. "
            "Results are tallied automatically — the ideas with the most dots rise to the top. "
            "Use after a brainstorm to democratically prioritise without a facilitator bottleneck. "
            "Combine with Timer to keep the voting round time-boxed."
        ),
    },

    # ── Proportional Scaling ──────────────────────────────────────────────────
    {
        "id": "fig_scale_k",
        "app": "figma",
        "topic": "shortcuts",
        "text": (
            "Scale tool (K key): proportionally scales a frame or component including all its contents, "
            "fonts, stroke widths, corner radii, and effects — unlike dragging the corner handle "
            "which only resizes the container. "
            "Use Scale (K) when resizing a finished component or frame to a new size without distortion. "
            "Type a target width/height numerically in the toolbar while in Scale mode."
        ),
    },

    # ── Clip Content ──────────────────────────────────────────────────────────
    {
        "id": "fig_clip_content",
        "app": "figma",
        "topic": "frames",
        "text": (
            "Clip Content (frame property in the Design panel): when enabled, anything outside the frame's bounds is hidden. "
            "When disabled, child layers can extend beyond the frame and remain visible — "
            "useful for tooltips, dropdowns, and overlapping card shadows that should 'hang over' the container. "
            "Toggle it with the 'Clip content' checkbox in the Frame section of the right panel. "
            "Auto Layout frames always clip content by default."
        ),
    },

    # ── PDF Export ────────────────────────────────────────────────────────────
    {
        "id": "fig_export_pdf",
        "app": "figma",
        "topic": "export",
        "text": (
            "PDF export: select one or more frames > Export > PDF. "
            "Each frame becomes a page in the PDF — order follows the left-to-right, "
            "top-to-bottom position of frames on the canvas. "
            "PDF export is vector-based for shapes and text (sharp at any scale) "
            "but rasterises complex fills and effects. "
            "Great for print handoffs, specification documents, or sharing with stakeholders who don't have Figma access."
        ),
    },

    # ── Aspect Ratio Lock ─────────────────────────────────────────────────────
    {
        "id": "fig_aspect_ratio",
        "app": "figma",
        "topic": "frames",
        "text": (
            "Aspect ratio lock: click the chain link icon between W and H in the Design panel to lock the aspect ratio. "
            "Changing either dimension now proportionally scales the other. "
            "Hold Shift while dragging a corner to temporarily lock aspect ratio without clicking the lock. "
            "For images: when resized with the lock on, they scale without stretching. "
            "Unlock to freely resize width and height independently."
        ),
    },

    # ── Text Resizing Modes ───────────────────────────────────────────────────
    {
        "id": "fig_textresize_01",
        "app": "figma",
        "topic": "typography",
        "text": (
            "Text resizing modes (right-click a text layer or use the Design panel): "
            "Auto Width — the box grows horizontally as you type; never wraps. Use for single labels. "
            "Auto Height — fixed width, box grows vertically to fit content. Use for paragraphs in fixed-width containers. "
            "Fixed Size — neither dimension changes; text clips if it overflows. Use when the text container must stay a fixed size. "
            "Setting the wrong mode causes invisible overflow or broken layouts when content changes."
        ),
    },

    # ── Lists in Text ─────────────────────────────────────────────────────────
    {
        "id": "fig_textlist_01",
        "app": "figma",
        "topic": "typography",
        "text": (
            "Bulleted and numbered lists: in the Text panel, click the List Style icons (bullet or numbered). "
            "Indentation: Tab indents a list item; Shift+Tab outdents. "
            "Paragraph Indent offsets the first line of each paragraph. "
            "List items in Figma are plain text with list styling — not separate components. "
            "For complex nested lists in design specs, use an Auto Layout frame with individual text layers instead."
        ),
    },

    # ── Paragraph Spacing ─────────────────────────────────────────────────────
    {
        "id": "fig_paraspc_01",
        "app": "figma",
        "topic": "typography",
        "text": (
            "Paragraph spacing: in the Text panel (the advanced text options, ↗ icon), "
            "Paragraph Spacing adds space after each paragraph break (Enter/Return). "
            "This is separate from Line Height, which controls space between lines within a paragraph. "
            "A common rule: Paragraph Spacing should be roughly 1.5–2× the Line Height "
            "so paragraph breaks are clearly visible compared to regular line spacing."
        ),
    },

    # ── Instance Overrides ────────────────────────────────────────────────────
    {
        "id": "fig_resetinst_01",
        "app": "figma",
        "topic": "components",
        "text": (
            "Reset instance overrides: right-click a component instance > Reset All Overrides "
            "to remove all local changes and restore the instance to the main component's default state. "
            "Or right-click a specific property (fill, text, etc.) > Reset to Main Component "
            "to reset only that property. "
            "Use when an instance has drifted far from the main component and you want to start clean."
        ),
    },
    {
        "id": "fig_detachinst_01",
        "app": "figma",
        "topic": "components",
        "text": (
            "Detach instance (Ctrl/Cmd+Alt+B): breaks the link between an instance and its main component. "
            "The instance becomes a plain group/frame — no longer updates when the main component changes. "
            "Use when you need to make edits not possible within the component system, "
            "or when exploring a one-off design direction. "
            "Detaching is irreversible — consider duplicating the instance first."
        ),
    },
    {
        "id": "fig_gotomain_01",
        "app": "figma",
        "topic": "components",
        "text": (
            "Go to main component: right-click an instance > Go to Main Component (or the arrow icon in the Design panel). "
            "Jumps the viewport to the main component, selecting it — useful for editing the source when working "
            "in a file where components are on a dedicated 'Components' page. "
            "After editing, use the back arrow in the toolbar to return to where you were."
        ),
    },

    # ── Fixed Position in Scroll ───────────────────────────────────────────────
    {
        "id": "fig_fixedpos_01",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Fixed position in scrollable frames: select a layer inside a scrollable frame "
            "and enable 'Fix position when scrolling' in the Design panel (Prototype > Scroll Behavior). "
            "The layer stays fixed on screen while content beneath it scrolls — "
            "used for sticky navigation bars, floating action buttons, bottom tab bars, and cookie banners. "
            "Requires the parent frame to have 'Clip Content' on and a scroll direction set."
        ),
    },

    # ── Overlay Position Options ──────────────────────────────────────────────
    {
        "id": "fig_overlay_pos",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Overlay position options (in prototype Open Overlay settings): "
            "Center — centred over the triggering frame. Top Left/Right — anchored to a corner. "
            "Bottom Center — modal sheets, toasts, snackbars. Manual — drag to set exact position. "
            "Relative to Frame — positions relative to the triggering element's location. "
            "Close When Clicking Outside: enable for modal dialogs; disable for persistent overlays like drawers."
        ),
    },

    # ── Token Taxonomy ────────────────────────────────────────────────────────
    {
        "id": "fig_token_tax",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Token taxonomy — three-tier architecture: "
            "1) Global tokens: raw values (color/blue/500 = #3B82F6, spacing/4 = 4px). "
            "2) Alias tokens: semantic names referencing globals (color/interactive/primary = color/blue/500). "
            "3) Component tokens: component-specific references (button/background = color/interactive/primary). "
            "Components only consume alias or component tokens — never raw globals. "
            "This enables brand theming by only changing the alias layer, not every component."
        ),
    },

    # ── Multi-Brand Theming ───────────────────────────────────────────────────
    {
        "id": "fig_multibrand_01",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Multi-brand theming with Figma Variable modes: create a Variable collection 'Brand'. "
            "Add modes: Brand A, Brand B, Brand C. "
            "Each mode stores different values for the same tokens (primary color, logo, font family). "
            "Apply a mode to a frame: right-click the frame > Apply Variable Mode > Brand A. "
            "The entire frame — all components using those variables — updates to Brand A's values instantly. "
            "One component library, infinite brand expressions."
        ),
    },

    # ── Effect & Grid Styles ──────────────────────────────────────────────────
    {
        "id": "fig_effect_style",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Effect styles: save a drop shadow, inner shadow, or blur as a named style. "
            "Click the + next to Effects in the Design panel. "
            "Apply the same shadow to any element — when the style updates, all instances update. "
            "Grid styles: save a layout grid (columns, rows, or grid) as a named style "
            "and apply it to multiple frames. Changing the grid style updates all frames at once."
        ),
    },

    # ── Content Reel Plugin ───────────────────────────────────────────────────
    {
        "id": "fig_contentreel",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Content Reel plugin: inserts realistic dummy data into text layers and frames. "
            "Provides names, emails, phone numbers, addresses, job titles, avatars, and company names. "
            "Select a text layer and apply a data type — the layer fills with realistic content. "
            "For lists, select multiple layers and apply in bulk to fill an entire component list at once. "
            "Realistic data reveals layout problems that 'Lorem Ipsum' hides (long names, edge cases)."
        ),
    },

    # ── Autoflow Plugin ───────────────────────────────────────────────────────
    {
        "id": "fig_autoflow",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Autoflow plugin: automatically draws flow arrows between frames based on your prototype connections. "
            "Run it after building a prototype to generate a user-flow diagram on top of your designs. "
            "Arrows are live — updating prototype connections and re-running Autoflow updates the diagram. "
            "Use it for stakeholder presentations to show navigation structure without a separate diagram tool."
        ),
    },

    # ── Video Fills ───────────────────────────────────────────────────────────
    {
        "id": "fig_videofill",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Video fills: select any shape or frame > Fill > + > choose Video. "
            "Upload an MP4 file as a fill — the video plays in the frame during prototype preview. "
            "Use for: animated onboarding illustrations, video player mockups, background motion. "
            "Videos loop by default. Combine with prototype interactions to play/pause on click. "
            "Video fills export as static frames in PDF/image export — only animate in prototype mode."
        ),
    },

    # ── Publishing Partial Libraries ──────────────────────────────────────────
    {
        "id": "fig_pubpartial",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Publishing partial libraries: when publishing a library (Assets > Publish), "
            "you can hide specific components from the published set by right-clicking a component > "
            "'Hide when publishing' — the component still exists in the file but doesn't appear "
            "in other files' Asset panels. "
            "Use this for WIP components, internal helper layers, or components not ready for team use."
        ),
    },

    # ── Auto Layout Spacing Modes ─────────────────────────────────────────────
    {
        "id": "fig_al_spacing",
        "app": "figma",
        "topic": "components",
        "text": (
            "Auto Layout spacing modes: click the spacing value between items to toggle modes. "
            "Packed — items sit together at one end (left, center, or right aligned). "
            "Space Between — items are distributed evenly with equal gaps (like CSS justify-content: space-between). "
            "Fixed spacing — a set gap between every item. "
            "Combine Space Between with Fill Container children for fully responsive layouts."
        ),
    },

    # ── Hug / Fill / Fixed Sizing ────────────────────────────────────────────
    {
        "id": "fig_sizing_modes",
        "app": "figma",
        "topic": "components",
        "text": (
            "Sizing modes in Auto Layout (W and H dropdowns): "
            "Hug Contents — the container shrinks/grows to fit its children (like width: fit-content in CSS). "
            "Fill Container — the child expands to fill its parent Auto Layout frame (like flex: 1). "
            "Fixed — the dimension stays at the set pixel value regardless of content. "
            "Mixing Hug (parent) with Fill (child) is how you build fully responsive, content-driven layouts."
        ),
    },

    # ── Version History ───────────────────────────────────────────────────────
    {
        "id": "fig_version_hist",
        "app": "figma",
        "topic": "collaboration",
        "text": (
            "Version history (File > Show Version History, or Ctrl/Cmd+Alt+S to save a named version): "
            "Figma auto-saves versions every 30 minutes. "
            "Click any version in the sidebar to preview it. Click 'Restore this version' to roll back. "
            "Save a named version before major changes: a snapshot you can always return to. "
            "Version history is retained for 30 days on Starter, indefinitely on Professional/Organization plans."
        ),
    },

    # ── Retina Export ─────────────────────────────────────────────────────────
    {
        "id": "fig_retina_export",
        "app": "figma",
        "topic": "export",
        "text": (
            "Retina / HiDPI export: in the Export panel, click '+' to add export sizes. "
            "Add 1x (standard), 2x (retina), 3x (iPhone Pro). "
            "Set a Suffix — '2x' automatically appends '@2x' to the filename (e.g. icon@2x.png). "
            "Export All at once to get all sizes in one click. "
            "For Android: use 1x/1.5x/2x/3x/4x with MDPI/HDPI/XHDPI/XXHDPI/XXXHDPI suffixes."
        ),
    },

    # ── Figma AI ──────────────────────────────────────────────────────────────
    {
        "id": "fig_ai_03",
        "app": "figma",
        "topic": "shortcuts",
        "text": (
            "Figma AI — Make Designs: describe a UI in plain text and Figma generates a wireframe or design. "
            "Select a frame and use 'Make designs' from the AI panel. "
            "The AI uses your existing component library to populate designs with your actual components. "
            "Results are editable Figma layers — use as a starting point, not a final output. "
            "Also available: 'Rename Layers' (AI renames all layers semantically based on content), "
            "and 'Replace Content' (swaps placeholder text/images with contextually relevant content)."
        ),
    },
    {
        "id": "fig_ai_04",
        "app": "figma",
        "topic": "shortcuts",
        "text": (
            "Figma AI — visual search and generation: "
            "search your design file by describing what you're looking for ('blue button', 'empty state illustration'). "
            "Generate images directly in Figma: select a shape, right-click > Fill with AI Image, describe the image. "
            "Edit with AI: select a vector or image and ask it to change style, colour, or content. "
            "AI features are available in the right-click menu and the Resources panel."
        ),
    },

    # ── Prototype Device & Background Settings ────────────────────────────────
    {
        "id": "fig_proto_device_bg",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Prototype device and background settings: in the Prototype tab with no element selected, "
            "set the Device (iPhone 15, Pixel 8, MacBook — overlays the hardware chrome around your prototype), "
            "Model (specific colour/finish), and Orientation (portrait/landscape). "
            "Background Color sets the canvas colour behind the prototype frames in the preview. "
            "These settings only apply in Presentation Mode — they don't affect the design canvas."
        ),
    },

    # ── Sections for Organisation ─────────────────────────────────────────────
    {
        "id": "fig_sections_02",
        "app": "figma",
        "topic": "collaboration",
        "text": (
            "Sections as organisational units: Sections (S key to create) group frames on the canvas. "
            "Name a Section 'Flows', 'Components', 'Archive' to create visual regions in a large file. "
            "Sections appear in the Layers panel as collapsible groups. "
            "Dev Mode: mark a Section as 'Ready for Development' to batch-flag all frames inside it. "
            "Sections can also be used in version history to show what changed inside a specific area."
        ),
    },

    # ── Variable Collection Scoping ───────────────────────────────────────────
    {
        "id": "fig_var_scope",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Variable collection scoping: when creating a variable, set its Scope "
            "(which properties it appears in) — Color, Corner Radius, Font Size, Line Height, etc. "
            "Scoping prevents a spacing variable from accidentally appearing in a colour picker "
            "and reduces clutter in the variable assignment dropdowns. "
            "Library variables (published from a library file) are available in all files subscribed to that library; "
            "Local variables are only available within the current file."
        ),
    },

    # ── Preferred Values for Variants ─────────────────────────────────────────
    {
        "id": "fig_preferred_val",
        "app": "figma",
        "topic": "components",
        "text": (
            "Preferred values for instance swap: right-click a component > Edit Preferred Values. "
            "Choose which variants of another component appear first in the swap dropdown. "
            "Example: a Card component has an 'icon' slot — set preferred values to only show icon components, "
            "not every component in the library. "
            "This dramatically speeds up designer workflow when swapping components in a large library."
        ),
    },

    # ── Embed Figma in Notion / Confluence ────────────────────────────────────
    {
        "id": "fig_embed_01",
        "app": "figma",
        "topic": "collaboration",
        "text": (
            "Embed Figma in Notion, Confluence, or any tool supporting oEmbed: "
            "copy the Figma file or frame URL, paste it in Notion — it auto-embeds as an interactive preview. "
            "Viewers can pan and zoom the design directly in Notion without opening Figma. "
            "In Confluence, use the Figma macro (install from Atlassian Marketplace). "
            "Embeds always show the live version — as the design updates, the embed updates automatically."
        ),
    },

    # ── Page Organisation ─────────────────────────────────────────────────────
    {
        "id": "fig_pages_01",
        "app": "figma",
        "topic": "shortcuts",
        "text": (
            "Page organisation strategy for large files: "
            "Cover — a visual thumbnail of the file's purpose (shown in the file browser). "
            "📐 Components — all published components live here. "
            "🎨 Styles & Tokens — color/text style references. "
            "📱 Flows — actual design screens by flow or feature. "
            "🗄️ Archive — deprecated designs kept for reference. "
            "Consistent page naming across files makes navigation predictable for the whole team."
        ),
    },

    # ── Figma Inspect vs Dev Mode ─────────────────────────────────────────────
    {
        "id": "fig_inspect_01",
        "app": "figma",
        "topic": "dev_handoff",
        "text": (
            "Inspect panel (available to all viewers, even without Dev Mode access): "
            "click any layer to see its properties — dimensions, colours, fonts, effects, and code snippets. "
            "Dev Mode (Shift+D) is a superset of Inspect with richer code output, "
            "token names (not just values), and the 'Ready for Dev' workflow. "
            "Teams on Starter plan use Inspect; Professional/Organization teams use Dev Mode for full handoff."
        ),
    },

    # ── Naming Conventions ────────────────────────────────────────────────────
    {
        "id": "fig_naming_01",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Component naming conventions: use '/' as a grouping separator — "
            "'Button/Primary/Large', 'Button/Secondary/Small' creates a nested folder structure in the Assets panel. "
            "Keep names consistent with code: if the React component is '<ButtonPrimary>', name it 'Button/Primary'. "
            "Prefix with '_' (e.g. '_Base Button') to hide internal helper components from the published library. "
            "Consistent naming is the single biggest factor in how usable a design system library is."
        ),
    },

    # ── Working with Illustrations ────────────────────────────────────────────
    {
        "id": "fig_illustration_01",
        "app": "figma",
        "topic": "vectors",
        "text": (
            "Working with illustrations in Figma: import SVG illustrations and flatten them (Ctrl+E) "
            "to simplify the layer structure. "
            "For colour-themeable illustrations, keep fills as separate layers and bind them to color variables. "
            "For static illustrations, flatten to a single vector to reduce layer count. "
            "Use 'Ungroup' (Ctrl+Shift+G) after SVG import to access individual paths. "
            "Large SVGs with thousands of nodes can slow Figma — simplify paths before import."
        ),
    },

    # ── Conditional Variants ──────────────────────────────────────────────────
    {
        "id": "fig_cond_variant",
        "app": "figma",
        "topic": "components",
        "text": (
            "Conditional visibility in components: add a Boolean property to a component "
            "and bind it to a layer's visibility. "
            "Example: 'Show Icon' boolean property — when true, the icon layer is visible; when false, hidden. "
            "This eliminates the need for separate 'with icon' and 'without icon' variants, "
            "cutting the variant count and keeping the component set manageable."
        ),
    },

    # ── Quick Actions ─────────────────────────────────────────────────────────
    {
        "id": "fig_quick_actions",
        "app": "figma",
        "topic": "shortcuts",
        "text": (
            "Quick Actions (Cmd+/ on Mac, Ctrl+/ on Windows): opens Figma's command palette. "
            "Type any action name — 'add auto layout', 'flip horizontal', 'export', 'detach' — "
            "and press Enter to run it without navigating menus. "
            "Also searches plugins, components, and recent files. "
            "The fastest way to run any Figma feature, especially ones you don't use often enough to memorise the shortcut. "
            "Also accessible via the search icon in the toolbar."
        ),
    },

    # ── Find and Replace ──────────────────────────────────────────────────────
    {
        "id": "fig_find_replace",
        "app": "figma",
        "topic": "shortcuts",
        "text": (
            "Find and Replace (Cmd/Ctrl+H): search for any text string across the entire file "
            "and replace it globally. Options: Match Case, Whole Word. "
            "Use it to update button labels, replace placeholder text with real copy, "
            "or find all instances of a brand name change across hundreds of frames at once. "
            "Find only (Cmd/Ctrl+F) highlights all matching text layers in the Layers panel without replacing."
        ),
    },

    # ── Selection Colors Panel ────────────────────────────────────────────────
    {
        "id": "fig_sel_colors",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Selection colors: when multiple elements are selected, the Design panel shows "
            "a 'Selection colors' section listing every unique fill and stroke color used within the selection. "
            "Click any swatch to change all elements using that color simultaneously — "
            "perfect for batch-replacing an off-brand color across a complex illustration or component. "
            "Also shows the count of elements using each color, helping you audit inconsistencies."
        ),
    },

    # ── Frame vs Group vs Section ─────────────────────────────────────────────
    {
        "id": "fig_frame_group_sec",
        "app": "figma",
        "topic": "frames",
        "text": (
            "Frame vs Group vs Section: "
            "Frame (F) — a clipping container with layout properties (constraints, Auto Layout, clip content, scroll). Use for UI screens and components. "
            "Group (G) — a loose collection with no intrinsic bounds; children determine the bounding box. No layout features. Use for temporary groupings. "
            "Section (S) — a canvas-level organisational wrapper with a label and Dev Mode status. No layout properties. Use for file organisation only."
        ),
    },

    # ── Creating & Publishing Styles ──────────────────────────────────────────
    {
        "id": "fig_create_style",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Creating styles: select a layer with the desired property, click the four-dot grid icon "
            "next to Fill/Stroke/Text/Effect/Grid in the Design panel, then click '+' to save as a style. "
            "Name it clearly (e.g. 'Brand/Primary', 'Text/Body/Regular'). "
            "Publishing: open the Assets panel > Libraries icon > Publish. "
            "Once published, all files in your team workspace can use these styles. "
            "Edit the source style to update it everywhere it's used."
        ),
    },

    # ── Plugin Management ─────────────────────────────────────────────────────
    {
        "id": "fig_plugin_mgmt",
        "app": "figma",
        "topic": "shortcuts",
        "text": (
            "Plugin management: Main menu > Plugins > Manage Plugins. "
            "Pin frequently used plugins so they appear at the top of the Plugins menu. "
            "Run recent plugins with Cmd+Option+P (re-runs the last used plugin instantly). "
            "Remove unused plugins to keep the menu clean. "
            "Update plugins: Figma updates them automatically, but check the Community page for changelogs. "
            "Assign a plugin to a keyboard shortcut via Quick Actions > search plugin name."
        ),
    },

    # ── Comments Workflow ─────────────────────────────────────────────────────
    {
        "id": "fig_comments_01",
        "app": "figma",
        "topic": "collaboration",
        "text": (
            "Comments workflow: press C to enter comment mode, click anywhere to add a comment, "
            "@mention a teammate to notify them. "
            "Reply to a comment to start a thread. "
            "Resolve a comment (✓ check) when the change is made — it hides from the canvas but stays in history. "
            "Filter comments: show Only Unresolved, or filter by page/author. "
            "Comments are visible in Presentation Mode for stakeholder review."
        ),
    },

    # ── Handoff Link ──────────────────────────────────────────────────────────
    {
        "id": "fig_handoff_link",
        "app": "figma",
        "topic": "dev_handoff",
        "text": (
            "Direct frame link for handoff: right-click any frame > Copy/Paste as > Copy Link. "
            "The URL includes the node ID, so it opens Figma directly to that frame. "
            "Share this link with engineers so they land on exactly the right screen in Dev Mode. "
            "Add ?mode=dev to the URL to open it directly in Dev Mode. "
            "Works for any layer — components, sections, or individual elements."
        ),
    },

    # ── Spell Check ───────────────────────────────────────────────────────────
    {
        "id": "fig_spellcheck",
        "app": "figma",
        "topic": "shortcuts",
        "text": (
            "Spell check: Main menu > View > Spell Check (or Cmd+Option+; on Mac). "
            "Underlines misspelled words in red across all text layers in the file. "
            "Click an underline to see suggestions; click a suggestion to apply the fix. "
            "Change the spell check language in Preferences > Language. "
            "Particularly useful before client presentations or design handoff — "
            "typos in designs erode trust more than visual imperfections."
        ),
    },

    # ── Design Token Export Plugins ───────────────────────────────────────────
    {
        "id": "fig_token_export",
        "app": "figma",
        "topic": "design_systems",
        "text": (
            "Design token export plugins: "
            "Tokens Studio (formerly Figma Tokens): edit tokens as JSON, sync to GitHub/GitLab/URL. "
            "Style Dictionary integration: export tokens in formats consumable by any platform (CSS custom properties, Swift, Kotlin, JSON). "
            "Figma Variables Export plugin: exports all variables as a JSON token file. "
            "This is the standard approach for bridging design → code with a single source of truth for all design decisions."
        ),
    },

    # ── Figma to Code Plugins ─────────────────────────────────────────────────
    {
        "id": "fig_to_code",
        "app": "figma",
        "topic": "dev_handoff",
        "text": (
            "Figma to code plugins: "
            "Anima: exports React, Vue, HTML+CSS from Figma frames with reasonable accuracy. "
            "Builder.io: generates React + Tailwind with live code preview inside Figma. "
            "Locofy: auto-generates responsive React/Next.js with component detection. "
            "None produce production-ready code, but all dramatically reduce boilerplate setup time. "
            "Best used for design system scaffolding, not final implementation."
        ),
    },

    # ── Prototype Starting Frame ───────────────────────────────────────────────
    {
        "id": "fig_proto_start",
        "app": "figma",
        "topic": "prototyping",
        "text": (
            "Prototype starting frame and flows: in the Prototype tab, click on a frame "
            "and click '+ Flow starting point' to mark it as an entry point. "
            "Name the flow (e.g. 'Onboarding', 'Checkout'). "
            "A file can have multiple flows — each represents a separate user journey. "
            "When sharing the prototype URL, add #flow-name to the URL to open a specific flow directly. "
            "Flows are listed in the Prototype panel for quick access."
        ),
    },

    # ── Annotating for Accessibility ──────────────────────────────────────────
    {
        "id": "fig_a11y_annot",
        "app": "figma",
        "topic": "accessibility",
        "text": (
            "Accessibility annotations: use the Figma Accessibility Annotation Kit (free Community file) "
            "to mark up designs for engineers. Add annotations for: "
            "reading order (numbered tab stops), landmark regions, aria labels for icon-only buttons, "
            "heading levels (H1–H6), and interactive state descriptions. "
            "These annotations live on a dedicated 'A11y' page and are not part of the visual design — "
            "they document the intended accessible experience for implementation."
        ),
    },

    # ── Multi-Edit Instances ───────────────────────────────────────────────────
    {
        "id": "fig_multi_edit",
        "app": "figma",
        "topic": "components",
        "text": (
            "Multi-edit instances: select multiple instances of the same component — "
            "changes apply to all simultaneously. "
            "Text, fill overrides, and nested layer properties all update in bulk. "
            "Mixed values across the selection show as dashes; editing sets all to the new value. "
            "Use Cmd/Ctrl+click to build a selection across frames. "
            "Fastest way to update a repeated element (e.g. change 20 card titles at once) "
            "without touching the main component."
        ),
    },

    # ── Custom File Cover ─────────────────────────────────────────────────────
    {
        "id": "fig_file_cover",
        "app": "figma",
        "topic": "shortcuts",
        "text": (
            "Custom file thumbnail: create a frame named exactly 'Cover' (case-sensitive) on any page. "
            "Figma uses it as the file's preview image in the dashboard, team, and shared links. "
            "Design a clear cover showing the file name, version number, and a key screen or component. "
            "Recommended size: 1920×1080 or any 16:9 ratio. "
            "Update it whenever the file's scope changes — it's the first thing teammates see."
        ),
    },

    # ── Text Case Transformations ─────────────────────────────────────────────
    {
        "id": "fig_text_case",
        "app": "figma",
        "topic": "typography",
        "text": (
            "Text case transformations: in the advanced text options (... icon in the Text panel) "
            "choose Original, UPPERCASE, lowercase, Title Case, or Small Caps. "
            "These transform the rendered display without changing the underlying text content — "
            "revert to Original at any time. "
            "Use UPPERCASE for button labels as a visual style choice, "
            "so the actual text content stays in sentence case and is easy to change later."
        ),
    },

    # ── Boolean Operations Deep Dive ──────────────────────────────────────────
    {
        "id": "fig_boolean_ops",
        "app": "figma",
        "topic": "vectors",
        "text": (
            "Boolean operations (select two+ shapes > toolbar or Arrange menu): "
            "Union — merges into one shape, overlaps become filled. "
            "Subtract — removes the top shape's silhouette from the bottom (use for cutouts, holes). "
            "Intersect — keeps only the overlapping area. "
            "Exclude — keeps only non-overlapping areas. "
            "All are non-destructive groups — double-click to edit originals. "
            "Flatten (Cmd/Ctrl+E) permanently merges into a single vector path."
        ),
    },

    # ── Export Settings Persistence ───────────────────────────────────────────
    {
        "id": "fig_export_preset",
        "app": "figma",
        "topic": "export",
        "text": (
            "Export settings persist per layer: configure an export (PNG @2x, SVG, PDF) once "
            "and those settings are saved with the layer permanently. "
            "Copy export settings to other layers: Cmd+C on the source, "
            "select destinations, Cmd+Alt+V (Paste Properties) — transfers all export configs at once. "
            "Standardise icon export settings across a whole library in one paste operation."
        ),
    },

    # ── Multiple Fills Stacking ───────────────────────────────────────────────
    {
        "id": "fig_multi_fill",
        "app": "figma",
        "topic": "vectors",
        "text": (
            "Multiple fills: click the '+' on the Fill section repeatedly to add multiple fills to one layer. "
            "Each fill has its own blend mode and opacity — stack a gradient over a solid colour, "
            "a noise texture over a gradient, or a semi-transparent tint over an image. "
            "Fills render top-to-bottom (top fill on top). "
            "Use a Linear gradient at low opacity over a solid brand colour to add subtle depth without a separate layer. "
            "Combine with multiple strokes for complex visual layering on a single shape."
        ),
    },

    # ── Stroke Options ────────────────────────────────────────────────────────
    {
        "id": "fig_stroke_opts",
        "app": "figma",
        "topic": "vectors",
        "text": (
            "Stroke options (expand the Stroke section in the Design panel): "
            "Position: Inside (within the shape bounds), Centre (straddles the edge), Outside (outside the bounds). "
            "Dashed stroke: toggle the dash icon to set Dash length and Gap length in px. "
            "Cap: Butt (flat end), Round (rounded end), Square (extended flat). "
            "Join: Miter (sharp corner), Round (rounded corner), Bevel (clipped corner). "
            "Advanced stroke settings let you design dividers, borders, and dashed outlines precisely."
        ),
    },

    # ── Corner Smoothing / Squircle ───────────────────────────────────────────
    {
        "id": "fig_corner_smooth",
        "app": "figma",
        "topic": "vectors",
        "text": (
            "Corner smoothing (the % field next to Corner Radius): applies iOS-style 'squircle' smoothing "
            "to rounded corners. At 0% you get standard circular corners (CSS border-radius). "
            "At 100% you get a continuous curvature curve — the same shape used by iOS app icons, "
            "Apple's design language, and most modern mobile UI. "
            "Set corner radius to ~22% of the frame size and smoothing to 60% to match the iOS app icon shape exactly."
        ),
    },

    # ── Constraints Deep Dive ─────────────────────────────────────────────────
    {
        "id": "fig_constraints_02",
        "app": "figma",
        "topic": "frames",
        "text": (
            "Constraints control how a layer behaves when its parent frame resizes. "
            "Left/Right/Top/Bottom: pins the layer's edge to that side — maintains a fixed margin. "
            "Left and Right together: layer stretches horizontally with the frame (like width: 100%). "
            "Center: layer stays centred regardless of frame size. "
            "Scale: layer resizes proportionally — useful for decorative elements that should scale with the frame. "
            "Set constraints correctly on every layer before sharing a responsive design with engineers."
        ),
    },
]
