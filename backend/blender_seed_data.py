"""
Blender 3D teaching tips — comprehensive knowledge base for ChromaDB.
Covers navigation, modeling, modifiers, materials, rendering, animation,
rigging, sculpting, geometry nodes, UV mapping, lighting, physics,
compositing, and workflow shortcuts.
"""

BLENDER_TIPS = [

    # ── Navigation ──────────────────────────────────────────────────────────────
    {
        "id": "bl_nav_01",
        "app": "blender",
        "topic": "navigation",
        "text": (
            "Orbit: hold Middle Mouse Button and drag. Pan: Shift+Middle Mouse. Zoom: scroll wheel. "
            "Numpad 1/3/7 snap to front/right/top orthographic views. Numpad 5 toggles ortho vs perspective. "
            "Numpad 0 enters Camera View. Numpad 4/6/8/2 rotate the view in 15-degree steps."
        ),
    },
    {
        "id": "bl_nav_02",
        "app": "blender",
        "topic": "navigation",
        "text": (
            "Numpad . (period) frames the selected object. Numpad / isolates it in Local View — "
            "everything else is hidden. Press Numpad / again to exit. "
            "Home key frames the entire scene. This is the fastest way to focus without deselecting anything."
        ),
    },
    {
        "id": "bl_nav_03",
        "app": "blender",
        "topic": "navigation",
        "text": (
            "N key opens the N-Panel (Properties sidebar) on the right of the 3D viewport. "
            "It shows exact Location, Rotation, and Scale for selected objects. "
            "T key toggles the Tool shelf on the left. Both panels have tabs — "
            "add-ons often place their settings here."
        ),
    },
    {
        "id": "bl_nav_04",
        "app": "blender",
        "topic": "navigation",
        "text": (
            "Viewport shading modes (top-right sphere icons): Wireframe (Alt+Z), Solid (Z then Solid), "
            "Material Preview (Z then Material), and Rendered (Z then Rendered). "
            "Use Solid for modeling, Material Preview for shading checks, Rendered for final look. "
            "In Solid mode, hold Alt and click the shading sphere for X-Ray (see-through)."
        ),
    },
    {
        "id": "bl_nav_05",
        "app": "blender",
        "topic": "navigation",
        "text": (
            "Viewport overlays (the two overlapping circles icon in the header) control what is drawn — "
            "toggle face orientation, normals, statistics, wireframe on solid, cavity shading, and more. "
            "Enable Statistics to see vertex/face/triangle counts live — essential for poly budget tracking."
        ),
    },

    # ── Transforms & Object Mode ─────────────────────────────────────────────────
    {
        "id": "bl_xfm_01",
        "app": "blender",
        "topic": "transforms",
        "text": (
            "G = Grab (move), R = Rotate, S = Scale. After pressing a transform key, type an axis letter "
            "to constrain: G Z moves only on Z. Type a number to set exact amount: S X 2 Enter scales X by 2x. "
            "Right-click cancels. Middle-click during a transform snaps the axis to the nearest aligned direction."
        ),
    },
    {
        "id": "bl_xfm_02",
        "app": "blender",
        "topic": "transforms",
        "text": (
            "Pivot point controls the center of rotation/scale. Cycle it with the . (period) key or the "
            "dropdown in the header: Individual Origins rotates each object around its own center; "
            "3D Cursor uses wherever you last clicked (Shift+Right-click to place); Median Point uses "
            "the average of selected items."
        ),
    },
    {
        "id": "bl_xfm_03",
        "app": "blender",
        "topic": "transforms",
        "text": (
            "Snap (magnet icon in header, or Shift+Tab): snap transforms to grid increments, "
            "vertex positions, edge midpoints, or face surfaces. Hold Ctrl during a transform "
            "to snap to grid. The Snap target dropdown controls what the snap point is — "
            "use 'Closest' for vertex snapping, 'Face Project' to slide along surfaces."
        ),
    },
    {
        "id": "bl_xfm_04",
        "app": "blender",
        "topic": "transforms",
        "text": (
            "Apply transforms: Ctrl+A in Object Mode opens the Apply menu. "
            "Apply Location/Rotation/Scale bakes the transform into the mesh data — "
            "always apply Scale before rigging, simulations, or exporting, "
            "because non-applied scale causes unexpected behaviour in physics and child objects."
        ),
    },
    {
        "id": "bl_xfm_05",
        "app": "blender",
        "topic": "transforms",
        "text": (
            "Shift+D duplicates and immediately enters Grab. Alt+D creates a linked duplicate "
            "that shares mesh data — edits to one propagate to all. "
            "Ctrl+J joins multiple selected objects into one. Alt+P clears parent. "
            "Ctrl+P parents selected objects to the active one."
        ),
    },

    # ── Edit Mode & Modeling ─────────────────────────────────────────────────────
    {
        "id": "bl_edit_01",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Tab toggles Object/Edit Mode. In Edit Mode, 1/2/3 (keyboard, not Numpad) switch "
            "Vertex/Edge/Face select. Hold Shift to add select modes simultaneously. "
            "A selects all, Alt+A deselects all. Ctrl+I inverts selection."
        ),
    },
    {
        "id": "bl_edit_02",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Alt+Click selects an edge loop. Ctrl+Alt+Click selects an edge ring (perpendicular loops). "
            "Ctrl+R adds a loop cut — hover to preview the cut location, scroll to add more cuts, "
            "click to confirm position, right-click to center it on the edge."
        ),
    },
    {
        "id": "bl_edit_03",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Ctrl+B bevels selected edges — scroll during bevel to add segments for a smooth curve. "
            "Ctrl+Shift+B bevels vertices instead of edges (vertex bevel). "
            "The V key during bevel switches between offset types. Profile value near 1.0 "
            "gives a convex rounded bevel; 0.0 gives a sharp concave one."
        ),
    },
    {
        "id": "bl_edit_04",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "E extrudes selection along normals. Alt+E opens the Extrude menu for options like "
            "Extrude to Cursor, Extrude Individual Faces (each face extrudes on its own normal), "
            "or Extrude Along Normals. I insets faces — S during inset for individual face mode."
        ),
    },
    {
        "id": "bl_edit_05",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "F fills a face between selected edges or vertices. "
            "Ctrl+F opens the Face menu: Grid Fill converts a ring of edges into an even quad grid — "
            "great for closing circular holes. Grid Fill requires an even number of edges on each side."
        ),
    },
    {
        "id": "bl_edit_06",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "K activates the Knife tool. Click to place cut points, hold Ctrl to snap to midpoints, "
            "hold Z to cut through the back faces too. Enter confirms, Escape cancels. "
            "J (Join) cuts a direct edge between two selected vertices without the knife."
        ),
    },
    {
        "id": "bl_edit_07",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Proportional Editing (O): transforms fall off smoothly to surrounding geometry. "
            "Scroll during the transform to change the falloff radius — blue circle shows the influence area. "
            "Change falloff shape with F6 or the pie after O: Sphere is the most natural, "
            "Sharp gives a tighter, more localized effect."
        ),
    },
    {
        "id": "bl_edit_08",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "M merges vertices (at center, cursor, first, last, or by distance). "
            "Remove doubles/merge by distance: select all (A) then M > By Distance. "
            "Dissolve (Ctrl+X or X > Dissolve) removes edges/faces without leaving holes — "
            "unlike Delete which leaves an open gap."
        ),
    },
    {
        "id": "bl_edit_09",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Alt+S (Shrink/Fatten) moves vertices along their normals — outward or inward uniformly. "
            "Great for fattening organic shapes or adding shell thickness. "
            "Differs from Scale because it respects each vertex's individual normal direction, "
            "preventing the pinching that Scale causes on curved surfaces."
        ),
    },
    {
        "id": "bl_edit_10",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Vertex Groups let you save selections and control modifier/weight influence. "
            "Create groups in Properties > Object Data > Vertex Groups. "
            "Assign selected vertices to a group with a weight value (0–1). "
            "Reference the group by name in modifiers like Armature, Solidify, and Displace "
            "to restrict their effect to specific regions."
        ),
    },
    {
        "id": "bl_edit_11",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Face Normals indicate which way a face is pointing — critical for rendering and export. "
            "Enable Overlay > Face Orientation to see blue (outward) vs red (inward/flipped) faces. "
            "Select all faces (A) then Mesh > Normals > Recalculate Outside (Shift+N) to fix them all. "
            "Alt+N opens a normals menu for custom normal editing."
        ),
    },
    {
        "id": "bl_edit_12",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Loop Tools (built-in add-on, enable in Preferences > Add-ons): adds Relax, Space, Circle, "
            "and other operations to the Right-Click menu in Edit Mode. "
            "Relax smooths vertex positions while preserving topology. "
            "Circle projects selected vertices onto a perfect circle — very useful for clean circular holes."
        ),
    },

    # ── Modifiers ───────────────────────────────────────────────────────────────
    {
        "id": "bl_mod_01",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Subdivision Surface smooths without adding base mesh polygons. "
            "Ctrl+1/2/3 in Object Mode sets viewport subdivision level. "
            "Keep base mesh quad-dominant — triangles and n-gons cause pinching under subdivision. "
            "Crease edges (Shift+E in Edit Mode, value 1.0) to preserve sharp edges without extra loops."
        ),
    },
    {
        "id": "bl_mod_02",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Mirror modifier: duplicates geometry across X/Y/Z axis. Enable Clipping to weld center vertices "
            "and prevent crossing. Enable Bisect to remove existing geometry on the mirror side. "
            "Model only one side; Mirror handles the other. Apply before rigging or baking."
        ),
    },
    {
        "id": "bl_mod_03",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Array modifier repeats the object N times with an offset. "
            "Use Relative Offset (multiples of object bounding box) or Constant Offset (exact units). "
            "Combine with a Curve modifier to bend the array along a path — "
            "perfect for chains, fences, necklaces, or stadium seating."
        ),
    },
    {
        "id": "bl_mod_04",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Boolean modifier subtracts, adds, or intersects another mesh. "
            "Set Operand Object to a second mesh, choose Difference/Union/Intersect. "
            "Use the Exact solver (Blender 3+) for cleaner results. "
            "Both meshes must be manifold (watertight, no open edges). "
            "Hide the cutter object after using it — don't delete, or the modifier breaks."
        ),
    },
    {
        "id": "bl_mod_05",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Solidify adds thickness to thin geometry. Offset controls direction (1 = outward, -1 = inward). "
            "Enable Fill Rim to close the edge. Even Thickness compensates for curves. "
            "Good for architectural panels, walls, and fabric objects that start as flat planes."
        ),
    },
    {
        "id": "bl_mod_06",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Bevel modifier bevels all edges (or those with a bevel weight) non-destructively. "
            "Limit Method > Angle lets you set the threshold — only edges sharper than that angle get beveled. "
            "Use Limit Method > Vertex Group to restrict bevel to specific edges. "
            "Far better than manually beveling before the mesh is final."
        ),
    },
    {
        "id": "bl_mod_07",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Shrinkwrap modifier projects one mesh onto the surface of another. "
            "Modes: Nearest Surface Point keeps each vertex at the closest point; "
            "Project casts along an axis. Essential for retopology — "
            "draw clean quad topology over a high-res sculpt and Shrinkwrap it to the surface."
        ),
    },
    {
        "id": "bl_mod_08",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Decimate reduces polygon count without manual retopology. "
            "Collapse mode merges vertices by a ratio (0.5 = 50% fewer faces). "
            "Un-Subdivide reverses subdivision. Planar collapses coplanar faces. "
            "Good for LODs or reducing imported high-poly meshes for real-time use."
        ),
    },
    {
        "id": "bl_mod_09",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Lattice modifier: add a Lattice object (Shift+A > Lattice), select the mesh, "
            "add the Lattice modifier and set the Object to your lattice. "
            "Edit the lattice points to deform the mesh smoothly without touching its topology. "
            "Ideal for squash-and-stretch animation or general shape adjustments."
        ),
    },
    {
        "id": "bl_mod_10",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Displace modifier displaces vertices along their normals using a texture. "
            "Assign a texture (e.g. a noise texture) in the modifier and control the strength. "
            "Use with a Subdivision Surface below it in the stack for enough geometry to show detail. "
            "Great for terrain, rough surfaces, and procedural displacement."
        ),
    },
    {
        "id": "bl_mod_11",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Multiresolution modifier (Multires) is the sculpting equivalent of Subdivision Surface. "
            "Add it before sculpting at high resolution. Subdivide levels to add detail, "
            "then Reshape / Apply Base to propagate changes between levels. "
            "Unlike Dyntopo, Multires preserves clean quad topology — "
            "better for characters that will be rigged."
        ),
    },
    {
        "id": "bl_mod_12",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Modifier stack order matters significantly. A common correct order: "
            "Mirror → Armature → Subdivision Surface. "
            "Mirror before Armature means one bone deforms both sides. "
            "Subdivision after Armature gives smooth deformation on the final smooth mesh. "
            "Drag modifiers in the stack to reorder them."
        ),
    },

    # ── Materials & Shading ──────────────────────────────────────────────────────
    {
        "id": "bl_mat_01",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Principled BSDF covers most real-world surfaces. Key inputs: "
            "Base Color (surface color), Metallic (0 = plastic/skin/wood, 1 = metal), "
            "Roughness (0 = mirror-smooth, 1 = fully matte), IOR (1.45 for glass/plastic, 1.33 for water), "
            "Alpha (transparency), Subsurface (wax/skin light scattering)."
        ),
    },
    {
        "id": "bl_mat_02",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Image Texture node: Shift+A > Texture > Image Texture. Connect Color to Base Color. "
            "Set Colorspace: sRGB for albedo/color maps, Non-Color for normal/roughness/metallic/AO maps. "
            "Getting the colorspace wrong on data maps causes washed-out or over-bright results."
        ),
    },
    {
        "id": "bl_mat_03",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Normal maps need a Normal Map node between the texture and shader. "
            "Chain: Image Texture (Non-Color) → Normal Map node → Normal input on Principled BSDF. "
            "The Normal Map node converts tangent-space blue/purple pixel data into actual normals. "
            "Skipping it produces completely wrong lighting."
        ),
    },
    {
        "id": "bl_mat_04",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Ctrl+Shift+Click any shader node to preview just its output in the Solid/Material Preview viewport — "
            "a yellow dot appears on the node. Click elsewhere to reset. "
            "M mutes a node (bypasses it without deleting). Ctrl+Shift+Click the Material Output "
            "to restore full material view."
        ),
    },
    {
        "id": "bl_mat_05",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Texture Coordinate node controls how textures are mapped: UV (requires UV unwrap), "
            "Object (object-space, good for procedural tiles), "
            "Generated (0–1 over the bounding box), Camera. "
            "Pair with a Mapping node (Shift+A > Vector > Mapping) to control scale, rotation, and offset."
        ),
    },
    {
        "id": "bl_mat_06",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Procedural textures: Noise Texture (organic randomness), Voronoi (cellular/stone), "
            "Wave Texture (wood grain, stripes), Musgrave (fractal terrain/clouds). "
            "Chain them through a ColorRamp node to remap the 0–1 output to any color range or contrast. "
            "ColorRamp is one of the most useful nodes — use it constantly for material control."
        ),
    },
    {
        "id": "bl_mat_07",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Mix Shader blends two complete shaders by a factor. MixRGB mixes colors. "
            "Use a Mix Shader with a mask (e.g. a Noise Texture through a ColorRamp as the Factor) "
            "to blend two different materials — dirty paint over rust, for example. "
            "Layer multiple Mix Shaders for complex multi-material effects."
        ),
    },
    {
        "id": "bl_mat_08",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Emission shader makes a surface glow and emit light (in Cycles). "
            "Use a pure Emission node for screen/light surfaces, or Mix Shader to blend emission "
            "with a Principled BSDF for subtle self-illumination. "
            "In EEVEE, also enable Bloom (Render Properties > Bloom) to see the glow effect."
        ),
    },
    {
        "id": "bl_mat_09",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Material slots: one object can have multiple materials assigned to different faces. "
            "In Edit Mode, select faces, pick a material slot (Properties > Material), "
            "click Assign. Use this for objects with distinct surface zones — "
            "a car body (paint) + windows (glass) + trim (chrome) in one mesh."
        ),
    },
    {
        "id": "bl_mat_10",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Node Groups: select a set of nodes (including their links), press Ctrl+G to group them. "
            "The group appears as a single node and can be reused across materials. "
            "Expose inputs/outputs by dragging sockets to the Group Input/Output nodes. "
            "Edit the group by pressing Tab on it, or in the Node Groups editor."
        ),
    },

    # ── Lighting ─────────────────────────────────────────────────────────────────
    {
        "id": "bl_light_01",
        "app": "blender",
        "topic": "lighting",
        "text": (
            "Light types: Point (omnidirectional bulb), Spot (cone — adjust Spot Size and Blend), "
            "Area (rectangular/square soft light, like a softbox), Sun (parallel rays, simulates daylight). "
            "Area lights give the softest, most realistic shadows for studio setups. "
            "All lights have Energy (watts in Cycles) — don't be afraid of high values (1000+ W)."
        ),
    },
    {
        "id": "bl_light_02",
        "app": "blender",
        "topic": "lighting",
        "text": (
            "HDRI world lighting: in the World Properties, set Surface to Background, "
            "plug an Environment Texture node into the Color, and load an .hdr or .exr panorama. "
            "HDRIs provide realistic ambient lighting and reflections simultaneously. "
            "Sites like Poly Haven offer free high-quality HDRIs. "
            "Control HDRI rotation with a Texture Coordinate > Mapping node chain."
        ),
    },
    {
        "id": "bl_light_03",
        "app": "blender",
        "topic": "lighting",
        "text": (
            "Three-point lighting setup: Key light (main, brighter, 45° side), "
            "Fill light (opposite side, dimmer, reduces harsh shadows), "
            "Rim/Back light (behind the subject, separates it from background). "
            "Use Area lights for all three. Start: Key at 1000W, Fill at 200W, Rim at 500W."
        ),
    },

    # ── Camera ───────────────────────────────────────────────────────────────────
    {
        "id": "bl_cam_01",
        "app": "blender",
        "topic": "camera",
        "text": (
            "Numpad 0 enters Camera View. Press N > View > Lock Camera to View to navigate inside "
            "camera view without exiting it. Camera Properties: Focal Length (50mm = natural, "
            "wider = more distortion), Clip Start/End, Depth of Field. "
            "Press Ctrl+Numpad 0 to make the selected camera the active camera."
        ),
    },
    {
        "id": "bl_cam_02",
        "app": "blender",
        "topic": "camera",
        "text": (
            "Depth of Field: in Camera Properties, enable Depth of Field and set F-Stop "
            "(smaller = more blur). Set the Focus Object to a mesh to track focus dynamically, "
            "or set the Focus Distance manually. In Cycles you'll see bokeh blobs on out-of-focus highlights. "
            "In EEVEE, enable Depth of Field in the Render Properties."
        ),
    },

    # ── Rendering ───────────────────────────────────────────────────────────────
    {
        "id": "bl_rend_01",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "Cycles is ray-traced — photorealistic, physically accurate, slower. "
            "EEVEE is rasterized — real-time speed, great for stylized work and fast iteration. "
            "Switch in Render Properties > Render Engine. "
            "Cycles GPU rendering: set to GPU Compute in Render Properties — often 10x faster than CPU."
        ),
    },
    {
        "id": "bl_rend_02",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "F12 renders current frame. Ctrl+F12 renders animation. F11 shows last render. "
            "Set output path and format in Properties > Output before rendering animations — "
            "save as PNG image sequence rather than video: if a render crashes, "
            "you keep completed frames and resume from where it stopped."
        ),
    },
    {
        "id": "bl_rend_03",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "Cycles denoising: Render Properties > Sampling > Denoise. "
            "OptiX (NVIDIA) or OpenImageDenoise (any hardware) removes noise at lower sample counts. "
            "Adaptive Sampling (Render Properties > Sampling) auto-stops each pixel when "
            "its noise falls below the threshold — massive time saving on complex scenes."
        ),
    },
    {
        "id": "bl_rend_04",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "Render Region: in the viewport (Numpad 0 camera view), press Ctrl+B and drag a box — "
            "only that area renders. Ctrl+Alt+B clears it. Use this to test a specific part "
            "of the frame without waiting for the full render. "
            "Also reduce resolution % in Output Properties for quick tests."
        ),
    },
    {
        "id": "bl_rend_05",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "Render Passes (View Layer Properties > Passes): output Diffuse, Specular, Shadow, "
            "AO, Depth, Normal, and more as separate images. Combine them in the Compositor "
            "for full non-destructive control over the final image — adjust shadows without re-rendering, "
            "tweak specular highlights, add atmospheric depth with the Z pass."
        ),
    },
    {
        "id": "bl_rend_06",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "EEVEE requires baked probes for accurate reflections and global illumination. "
            "Add a Reflection Cubemap object near reflective surfaces and an Irradiance Volume over the scene. "
            "Then Render Properties > Indirect Lighting > Bake Indirect Lighting. "
            "Without baking, EEVEE reflections are a flat screen-space approximation."
        ),
    },

    # ── Sculpting ───────────────────────────────────────────────────────────────
    {
        "id": "bl_sculpt_01",
        "app": "blender",
        "topic": "sculpting",
        "text": (
            "Switch to Sculpt Mode from the mode dropdown. F adjusts brush radius, Shift+F adjusts strength. "
            "Hold Shift to smooth. Ctrl inverts the brush (push in instead of pull out). "
            "X toggles symmetry on the X axis. Key brushes: Draw, Clay Strips (adds flat clay layers), "
            "Grab (moves geometry), Smooth, Crease, Inflate, Blob, Snake Hook."
        ),
    },
    {
        "id": "bl_sculpt_02",
        "app": "blender",
        "topic": "sculpting",
        "text": (
            "Dyntopo (Dynamic Topology): enable in Sculpt Mode header. Adds mesh detail automatically as you paint, "
            "so you never run out of resolution mid-stroke. Set Detail Size smaller for finer geometry. "
            "Constant Detail maintains uniform polygon size across the mesh. "
            "Disable Dyntopo before rigging — it creates chaotic, non-manifold topology."
        ),
    },
    {
        "id": "bl_sculpt_03",
        "app": "blender",
        "topic": "sculpting",
        "text": (
            "Remesh (Ctrl+R in Sculpt Mode, or Object Data Properties > Remesh): "
            "rebuilds the mesh with clean, uniform voxels. Smaller voxel size = more detail = heavier mesh. "
            "Remesh before adding fine detail on a new shape to get clean topology. "
            "After remeshing, sculpt large forms first, then remesh smaller for detail."
        ),
    },
    {
        "id": "bl_sculpt_04",
        "app": "blender",
        "topic": "sculpting",
        "text": (
            "Face Sets: paint colored regions on the mesh (Ctrl+W creates a face set from a visible region). "
            "Face sets allow masking — hide all but one face set to sculpt isolated areas. "
            "Press H to hide the face set under cursor; Alt+H to show all. "
            "Use them as a non-destructive selection system throughout sculpting."
        ),
    },
    {
        "id": "bl_sculpt_05",
        "app": "blender",
        "topic": "sculpting",
        "text": (
            "Masking (M to paint mask, Ctrl+I to invert): masked areas are protected from all brush strokes. "
            "Box Mask (B) and Lasso Mask available in the toolbar. "
            "Mask by Normal or Curvature via the Mask menu for targeted isolation. "
            "Convert a mask to a Face Set with Mask > Mask to Face Set."
        ),
    },

    # ── UV Mapping ───────────────────────────────────────────────────────────────
    {
        "id": "bl_uv_01",
        "app": "blender",
        "topic": "uv_mapping",
        "text": (
            "In Edit Mode, select all faces (A), press U for the UV Mapping menu. "
            "Unwrap follows marked seams (the most control). Smart UV Project packs islands automatically. "
            "Cylinder/Sphere/Box Projection for simple regular shapes. "
            "Open a UV Editor (change panel type to UV Editor) to see and edit the result."
        ),
    },
    {
        "id": "bl_uv_02",
        "app": "blender",
        "topic": "uv_mapping",
        "text": (
            "Mark Seams: select edges in Edit Mode where you want the UV map to split, "
            "then Ctrl+E > Mark Seam (turns red). Think of seams as where you'd cut a cardboard box open. "
            "For a character: seams along the back of limbs, inside armpits, under the chin — "
            "places hidden from camera view. Then A > U > Unwrap."
        ),
    },
    {
        "id": "bl_uv_03",
        "app": "blender",
        "topic": "uv_mapping",
        "text": (
            "In the UV Editor, use the same transform keys (G, R, S) to move/rotate/scale UV islands. "
            "Average Island Scale (UV menu) normalizes all islands to the same texel density. "
            "Pack Islands arranges them to fill the 0–1 UV space efficiently. "
            "Stitch (V) merges islands at shared seams."
        ),
    },
    {
        "id": "bl_uv_04",
        "app": "blender",
        "topic": "uv_mapping",
        "text": (
            "UDIM tiles (multi-tile UVs): place UV islands beyond the 0–1 tile into adjacent tiles (1001, 1002…). "
            "In Image Texture node, enable UDIM and load a UDIM sequence. "
            "Allows much higher texture resolution for characters by spreading detail across multiple 4K or 8K tiles."
        ),
    },

    # ── Animation ───────────────────────────────────────────────────────────────
    {
        "id": "bl_anim_01",
        "app": "blender",
        "topic": "animation",
        "text": (
            "Insert keyframe: hover over any value in the Properties panel and press I, "
            "or hover in the 3D viewport and press I > LocRotScale. "
            "Yellow highlights mean the property has a keyframe on the current frame. "
            "Green means it's keyed but the current frame is between keyframes."
        ),
    },
    {
        "id": "bl_anim_02",
        "app": "blender",
        "topic": "animation",
        "text": (
            "Graph Editor shows F-curves — the interpolation path between keyframes. "
            "Select keyframes and press T to change interpolation: Bezier (smooth easing), "
            "Linear (constant speed), Constant (instant jump). "
            "Drag handles on Bezier keyframes to shape the ease-in/ease-out curve. "
            "Flat handles = slow start and slow end; angled = fast through."
        ),
    },
    {
        "id": "bl_anim_03",
        "app": "blender",
        "topic": "animation",
        "text": (
            "Dope Sheet shows all keyframes as diamond icons on a timeline. "
            "Select all keys on a channel and scale (S) to retime the animation. "
            "Copy (Ctrl+C) and paste (Ctrl+V) keyframes. "
            "Action Editor (dropdown inside Dope Sheet) manages named animation actions — "
            "create separate Walk, Run, Jump actions for one armature."
        ),
    },
    {
        "id": "bl_anim_04",
        "app": "blender",
        "topic": "animation",
        "text": (
            "Shape Keys (Properties > Object Data > Shape Keys): morph targets for facial animation or deformation. "
            "Add a Basis shape (the neutral mesh), then add more keys and sculpt/move vertices for each expression. "
            "Animate the Value slider (0–1) on each shape key. "
            "Corrective shape keys fix skinning artifacts at specific joint angles."
        ),
    },
    {
        "id": "bl_anim_05",
        "app": "blender",
        "topic": "animation",
        "text": (
            "Drivers: link any property to any other property or a custom expression. "
            "Right-click any value > Add Driver. In the Driver editor, set type to Scripted Expression "
            "for formulas, or Average Value to mirror another property. "
            "Classic use: drive a shape key from a bone rotation to auto-correct skin around a joint."
        ),
    },
    {
        "id": "bl_anim_06",
        "app": "blender",
        "topic": "animation",
        "text": (
            "NLA (Non-Linear Animation) Editor: convert your action to an NLA strip (push down button in Dope Sheet). "
            "Stack, layer, and blend strips from different actions without merging them. "
            "Set blend mode and influence to mix actions (Walk + WaveHand simultaneously). "
            "Scale strips to retime entire actions non-destructively."
        ),
    },
    {
        "id": "bl_anim_07",
        "app": "blender",
        "topic": "animation",
        "text": (
            "Preview range: set start/end markers (P to set, Alt+P to clear in timeline) to loop playback "
            "over a specific section. Set the project frame range in Output Properties. "
            "Timeline markers (M key): place named markers at important frames — "
            "right-click to rename, drag to move."
        ),
    },

    # ── Rigging ─────────────────────────────────────────────────────────────────
    {
        "id": "bl_rig_01",
        "app": "blender",
        "topic": "rigging",
        "text": (
            "Add an armature: Shift+A > Armature. In Edit Mode, E extrudes bones. "
            "Name bones precisely (e.g. 'upper_arm.L') — Blender's Symmetrize (Armature menu) "
            "mirrors bones and weight data from .L to .R automatically. "
            "Connected bones share a head/tail; Ctrl+click to extrude disconnected bones."
        ),
    },
    {
        "id": "bl_rig_02",
        "app": "blender",
        "topic": "rigging",
        "text": (
            "Parent mesh to armature: select mesh, Shift-click armature, Ctrl+P > With Automatic Weights. "
            "Blender calculates bone influence per vertex via a heat map algorithm. "
            "Results are usually good for simple shapes; complex meshes may need manual weight painting cleanup."
        ),
    },
    {
        "id": "bl_rig_03",
        "app": "blender",
        "topic": "rigging",
        "text": (
            "Weight Paint mode: shows bone influence as a color gradient (red = full, blue = none). "
            "Select the armature in Pose Mode, Shift-click the mesh, switch to Weight Paint. "
            "Use Add/Subtract/Blur brushes to refine influence. "
            "Ctrl+click on a bone in the viewport while in Weight Paint to switch the active bone."
        ),
    },
    {
        "id": "bl_rig_04",
        "app": "blender",
        "topic": "rigging",
        "text": (
            "Inverse Kinematics (IK): in Pose Mode, select the tip bone, add a Bone Constraint > Inverse Kinematics. "
            "Set Target to an IK target bone. Chain Length controls how many bones are solved. "
            "IK lets you position a hand or foot and have the arm/leg solve automatically — "
            "far easier than rotating every joint individually."
        ),
    },
    {
        "id": "bl_rig_05",
        "app": "blender",
        "topic": "rigging",
        "text": (
            "Bone Constraints (Pose Mode > Properties > Bone Constraints): "
            "Copy Rotation mirrors rotation from one bone to another. "
            "Track To makes a bone always point at a target. "
            "Stretch To scales a bone to always reach a target — great for IK stretch effects. "
            "Limit Rotation/Location prevents bones from moving beyond anatomical ranges."
        ),
    },

    # ── Geometry Nodes ───────────────────────────────────────────────────────────
    {
        "id": "bl_gn_01",
        "app": "blender",
        "topic": "geometry_nodes",
        "text": (
            "Add a Geometry Nodes modifier in Properties > Modifier. Click New to create a node graph. "
            "All geometry flows: Group Input → processing nodes → Group Output. "
            "Everything is non-destructive and fully procedural. "
            "Press N in the Geometry Node editor for the node panel — expose inputs as modifier parameters."
        ),
    },
    {
        "id": "bl_gn_02",
        "app": "blender",
        "topic": "geometry_nodes",
        "text": (
            "Distribute Points on Faces generates a point cloud on a mesh surface. "
            "Connect to Instance on Points to place objects at each point. "
            "Add Random Value nodes to randomize each instance's scale, rotation, and transform. "
            "This is the node-based particle/scatter system — replaces old Particle System for many tasks."
        ),
    },
    {
        "id": "bl_gn_03",
        "app": "blender",
        "topic": "geometry_nodes",
        "text": (
            "Mesh to Curve and Curve to Mesh: convert mesh edges to splines, then sweep a profile along them. "
            "Example: draw a path as a curve, create a pipe cross-section profile, "
            "connect Curve to Mesh to generate a clean pipe or cable along any path. "
            "Change the profile curve at any time — the pipe updates instantly."
        ),
    },
    {
        "id": "bl_gn_04",
        "app": "blender",
        "topic": "geometry_nodes",
        "text": (
            "Attribute nodes let you read and write per-element data (position, normal, UV, custom). "
            "Named Attribute node reads any attribute by name. Store Named Attribute writes one. "
            "Use this to carry custom data through the node tree — "
            "e.g. store a curvature mask to drive per-instance color variation."
        ),
    },

    # ── Compositing ─────────────────────────────────────────────────────────────
    {
        "id": "bl_comp_01",
        "app": "blender",
        "topic": "compositing",
        "text": (
            "Blender's Compositor (editor type: Compositor) processes renders post-production. "
            "Enable Use Nodes. The Render Layers node feeds all render passes. "
            "Add Color Balance, Glare, Lens Distortion, and Blur nodes to grade and stylize. "
            "Composite node is the final output. Viewer node previews any intermediate point."
        ),
    },
    {
        "id": "bl_comp_02",
        "app": "blender",
        "topic": "compositing",
        "text": (
            "Glare node adds bloom, streaks, or fog glow to bright areas. "
            "Set type to Fog Glow for a soft cinematic bloom, Streaks for sci-fi lens flares. "
            "Threshold controls which luminance value starts glowing — "
            "lower threshold = more of the image glows. "
            "Combine with a Color Balance node before Glare to control the warm/cool tint."
        ),
    },

    # ── Physics ─────────────────────────────────────────────────────────────────
    {
        "id": "bl_phys_01",
        "app": "blender",
        "topic": "physics",
        "text": (
            "Rigid Body: select a mesh, Properties > Physics > Rigid Body. "
            "Type Active = falls and collides. Passive = stationary collider (floor, walls). "
            "Shape: Convex Hull is fastest; Mesh is accurate but slow. "
            "Press Space (or bake via Scene > Rigid Body World > Bake) to run the simulation. "
            "Cache baking is required before rendering."
        ),
    },
    {
        "id": "bl_phys_02",
        "app": "blender",
        "topic": "physics",
        "text": (
            "Cloth simulation: Physics > Cloth. Presets like Cotton, Denim, Silk adjust stiffness and mass. "
            "Pin groups: assign a Vertex Group as the Pin Group to hold parts of the cloth fixed "
            "(e.g. collar/shoulders stay on a character). "
            "Add a Collision modifier to the character body so cloth doesn't pass through it."
        ),
    },
    {
        "id": "bl_phys_03",
        "app": "blender",
        "topic": "physics",
        "text": (
            "Fluid simulation (Mantaflow): add a domain object (large cube around the scene), "
            "set it to Fluid > Domain > Liquid. Add emitter objects with Fluid > Flow. "
            "Bake Data first (generates caches), then Bake Mesh for the final surface. "
            "Resolution Divisions controls quality — start at 32 for fast previews, 64+ for final."
        ),
    },
    {
        "id": "bl_phys_04",
        "app": "blender",
        "topic": "physics",
        "text": (
            "Particles (emitter): Physics > Particle System > Emitter. "
            "Frame Start/End controls when emission begins/ends. Lifetime = frames each particle lives. "
            "Render tab: set render as Object to instance a mesh per particle (e.g. rocks, debris). "
            "Physics tab: add Collision modifier to objects that particles should bounce off."
        ),
    },

    # ── Curves & Text ────────────────────────────────────────────────────────────
    {
        "id": "bl_curve_01",
        "app": "blender",
        "topic": "curves",
        "text": (
            "Add a Bezier curve: Shift+A > Curve > Bezier. In Edit Mode, E extrudes new points. "
            "V changes handle type: Auto, Vector (sharp corners), Aligned, Free. "
            "Set the curve Bevel Depth in Object Data Properties for instant tube/rope geometry — "
            "no need for a separate Geometry Nodes setup for simple cables."
        ),
    },
    {
        "id": "bl_curve_02",
        "app": "blender",
        "topic": "curves",
        "text": (
            "Text objects: Shift+A > Text. In Edit Mode, type directly. "
            "Object Data Properties > Font: load any .ttf/.otf font. "
            "Extrude and Bevel for 3D lettering. Convert to mesh (Alt+C or Object > Convert > Mesh) "
            "for further editing. Text follows a curve path by setting Curve > Text on Curve."
        ),
    },

    # ── Collections & Scene Management ──────────────────────────────────────────
    {
        "id": "bl_coll_01",
        "app": "blender",
        "topic": "collections",
        "text": (
            "Collections organize objects in the Outliner (like layers/groups). "
            "M moves selected objects to a collection. "
            "Collections can be hidden per viewport or render independently. "
            "View Layer settings let you exclude entire collections from render — "
            "useful for proxy/low-res versions or switching between scene variants."
        ),
    },
    {
        "id": "bl_coll_02",
        "app": "blender",
        "topic": "collections",
        "text": (
            "Linked Libraries: link or append assets from another .blend file. "
            "File > Link imports objects/materials/node groups that stay linked to the source file. "
            "File > Append copies them locally. Linking is better for large projects — "
            "update the source .blend and all linked scenes inherit the changes automatically."
        ),
    },

    # ── Workflow & Shortcuts ─────────────────────────────────────────────────────
    {
        "id": "bl_short_01",
        "app": "blender",
        "topic": "shortcuts",
        "text": (
            "F3 (or Spacebar depending on keymap) opens the operator search. "
            "Type any command to find and run it — faster than hunting through menus. "
            "Ctrl+Z undo, Ctrl+Shift+Z redo. Undo history is per-mode — "
            "undoing in Edit Mode doesn't affect Object Mode history and vice versa."
        ),
    },
    {
        "id": "bl_short_02",
        "app": "blender",
        "topic": "shortcuts",
        "text": (
            "H hides selected objects/elements, Alt+H reveals all, Shift+H hides everything except selected. "
            "In Edit Mode these apply per-element within the mesh. "
            "To isolate one object in the outliner, click its eye icon. "
            "Use visibility restrictions (camera icon in Outliner) to exclude from render without hiding in viewport."
        ),
    },
    {
        "id": "bl_short_03",
        "app": "blender",
        "topic": "shortcuts",
        "text": (
            "Ctrl+L selects all linked geometry (connected to the currently selected element). "
            "P separates selected elements into a new object. "
            "Ctrl+J joins multiple selected objects into one mesh. "
            "These three shortcuts are the core of 'mesh surgery' — split and join at will."
        ),
    },

    # ── Performance & Baking ─────────────────────────────────────────────────────
    {
        "id": "bl_perf_01",
        "app": "blender",
        "topic": "performance",
        "text": (
            "Simplify (Render Properties > Simplify): cap subdivision levels during viewport "
            "and render separately. Viewport max subdivision 2, Render max 4 saves significant RAM. "
            "Also limits particle/hair count during viewport navigation. "
            "Enable only when working with heavy scenes."
        ),
    },
    {
        "id": "bl_perf_02",
        "app": "blender",
        "topic": "performance",
        "text": (
            "Baking: Cycles can bake Diffuse, Roughness, Normal, AO, and other passes from a high-poly mesh "
            "down to a texture on a low-poly mesh. Set up Selected to Active in the Bake panel, "
            "select low-poly, Shift-select high-poly, set Extrusion distance, click Bake. "
            "The resulting normal map gives the low-poly the appearance of the high-poly in real time."
        ),
    },
    {
        "id": "bl_perf_03",
        "app": "blender",
        "topic": "performance",
        "text": (
            "Render test strips: use Ctrl+B to draw a render region in camera view for quick spot-checks. "
            "Set resolution to 25% in Output Properties for even faster iterations. "
            "Hold Ctrl while clicking Render Image to render without opening the render window "
            "(result still goes to the Render Result slot, viewable with F11)."
        ),
    },

    # ── Node Wrangler Add-on ─────────────────────────────────────────────────────
    {
        "id": "bl_nw_01",
        "app": "blender",
        "topic": "node_wrangler",
        "text": (
            "Node Wrangler is a built-in add-on (Preferences > Add-ons > Node Wrangler) that massively speeds up "
            "shader and compositing work. Key shortcuts: Ctrl+Shift+Click to preview any node output, "
            "Ctrl+T to add a Texture Coordinate + Mapping node pair, "
            "Ctrl+Shift+T to load a full PBR texture set from a folder (auto-creates all texture nodes)."
        ),
    },
    {
        "id": "bl_nw_02",
        "app": "blender",
        "topic": "node_wrangler",
        "text": (
            "More Node Wrangler shortcuts: Alt+Click on a link to disconnect it quickly. "
            "Shift+P frames selected nodes in a labeled box (good for organization). "
            "Ctrl+RightClick and drag to cut through multiple links at once — faster than clicking each link. "
            "Alt+Shift+D duplicates the active node with all its settings."
        ),
    },

    # ── Rigify Add-on ────────────────────────────────────────────────────────────
    {
        "id": "bl_rigify_01",
        "app": "blender",
        "topic": "rigify",
        "text": (
            "Rigify (built-in add-on, enable in Preferences) generates production-ready control rigs. "
            "Add > Armature > Human (Meta-Rig) places a template skeleton. Align its bones to your character "
            "in Edit Mode, then press Generate Rig in the Armature Properties. "
            "Rigify creates a full FK/IK rig with bone layers, pole targets, stretch, and IK-FK switching."
        ),
    },
    {
        "id": "bl_rigify_02",
        "app": "blender",
        "topic": "rigify",
        "text": (
            "Rigify IK/FK switching: in the generated rig's N-panel (Rig Main Properties tab) "
            "each limb has an IK/FK slider (0 = IK, 1 = FK). "
            "IK is better for animation with ground contact (feet, hands on surfaces). "
            "FK is better for free-swinging limbs (waving, running arms). "
            "Snap IK to FK (and vice versa) using the bone layer snap buttons."
        ),
    },

    # ── Grease Pencil ────────────────────────────────────────────────────────────
    {
        "id": "bl_gp_01",
        "app": "blender",
        "topic": "grease_pencil",
        "text": (
            "Grease Pencil is a 2D animation system inside Blender's 3D space. "
            "Add > Grease Pencil > Blank to start. Switch to Draw Mode to paint strokes. "
            "Strokes live on Layers (like Photoshop layers) with keyframes on the timeline. "
            "Materials control stroke fill and line color. The result exists in 3D and can cast shadows, "
            "receive lighting, and be combined with 3D geometry."
        ),
    },
    {
        "id": "bl_gp_02",
        "app": "blender",
        "topic": "grease_pencil",
        "text": (
            "Grease Pencil animation: each layer has its own timeline. "
            "Insert keyframes with I in Draw mode. Strokes interpolate between keyframes "
            "using the Interpolate tool (Shift+Ctrl+E) to generate in-between frames automatically. "
            "Use the Dopesheet > Grease Pencil mode to manage timing across all layers."
        ),
    },
    {
        "id": "bl_gp_03",
        "app": "blender",
        "topic": "grease_pencil",
        "text": (
            "Convert 3D objects to Grease Pencil: select a mesh > Object > Convert > Grease Pencil. "
            "Conversely, trace over a 3D object in Draw Mode to create a stylized 2D look. "
            "Add a Line Art modifier to a Grease Pencil object to automatically generate "
            "clean outlines from any 3D mesh — the foundation of cel-shaded / toon renders."
        ),
    },

    # ── Hair & Fur ───────────────────────────────────────────────────────────────
    {
        "id": "bl_hair_01",
        "app": "blender",
        "topic": "hair",
        "text": (
            "Geometry Nodes hair (Blender 3.3+): add a Curves object, enable a Hair Generate node in Geometry Nodes. "
            "Use Surface Deform or snap to a mesh surface for root placement. "
            "Comb, Trim, and Smooth nodes style the curves procedurally. "
            "This replaces the old Particle Hair system — better control, non-destructive, and renders in Cycles/EEVEE."
        ),
    },
    {
        "id": "bl_hair_02",
        "app": "blender",
        "topic": "hair",
        "text": (
            "Old Particle Hair (still supported): Physics > Particle System > Hair. "
            "In Edit mode (enable hair particle editing in header) use comb, smooth, add, cut, and length brushes. "
            "Children settings multiply hair count for rendering without placing each strand manually. "
            "Material settings on the particle system control hair color and reflectivity."
        ),
    },

    # ── Color Management ─────────────────────────────────────────────────────────
    {
        "id": "bl_color_01",
        "app": "blender",
        "topic": "color_management",
        "text": (
            "Render Properties > Color Management > View Transform: "
            "AgX (Blender 4.0+) is the modern default — better highlights handling and film-like roll-off. "
            "Filmic (pre-4.0 default) is still excellent. Standard is flat and only useful for pixel-art. "
            "AgX avoids the blown-out neon look that Standard produces on bright saturated colors."
        ),
    },
    {
        "id": "bl_color_02",
        "app": "blender",
        "topic": "color_management",
        "text": (
            "Exposure and Gamma in Render > Color Management control scene brightness and contrast globally. "
            "Exposure brightens without blowing out highlights (unlike just boosting light energy). "
            "Look (Low/Medium/High Contrast presets) applies an S-curve — "
            "High Contrast gives a punchy cinematic feel; None/Low is good for product renders needing clean whites."
        ),
    },
    {
        "id": "bl_color_03",
        "app": "blender",
        "topic": "color_management",
        "text": (
            "For accurate color work, use a calibrated monitor and enable display color correction. "
            "In the viewport header, set the display device (sRGB for standard monitors). "
            "When texturing, use the Compositor to add a Color Balance or Curves node before the Output — "
            "this grades the final render independently of the 3D scene materials."
        ),
    },

    # ── More Modifiers ───────────────────────────────────────────────────────────
    {
        "id": "bl_mod_weld",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Weld modifier merges vertices within a set distance — the non-destructive version of "
            "Merge by Distance. Useful when Boolean or Array operations produce near-duplicate vertices "
            "that aren't perfectly overlapping. Set Merge Distance to a small value (0.001) "
            "and it cleans up the mesh automatically every time you adjust upstream modifiers."
        ),
    },
    {
        "id": "bl_mod_screw",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Screw modifier revolves a profile curve around an axis to create lathe objects — "
            "bowls, vases, columns, bottles. Draw the profile as a half-cross-section curve, "
            "add Screw, set Axis to Z (or Y), set Angle to 360° and Steps for smoothness. "
            "Change Screw value to add a thread offset for spirals and threads."
        ),
    },
    {
        "id": "bl_mod_skin",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Skin modifier generates a mesh skin around edges and vertices — great for quick organic shapes. "
            "Create a simple vertex/edge skeleton with Ctrl+RightClick, add Skin modifier. "
            "Ctrl+A in Edit Mode adjusts the radius at each vertex (like a pipe thickness). "
            "Combine with Subdivision Surface above it for a smooth organic result from just a few edges."
        ),
    },
    {
        "id": "bl_mod_wireframe",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Wireframe modifier converts faces into wireframe tubes along every edge. "
            "Thickness sets tube diameter. Enable Replace Original to replace the solid mesh entirely. "
            "Even Thickness corrects for non-uniform scaling. "
            "Combine with a transparent material for stylized X-ray / cage renders."
        ),
    },

    # ── Smooth Shading & Normals ─────────────────────────────────────────────────
    {
        "id": "bl_smooth_01",
        "app": "blender",
        "topic": "shading",
        "text": (
            "Right-click a mesh > Shade Smooth to interpolate normals across faces for a smooth appearance "
            "without adding geometry. Right-click > Shade Flat reverts to faceted look. "
            "Shade Smooth by Angle (Blender 4.1+) only smooths edges below a threshold angle — "
            "automatically keeps sharp hard edges without manual edge marking."
        ),
    },
    {
        "id": "bl_smooth_02",
        "app": "blender",
        "topic": "shading",
        "text": (
            "Auto Smooth (Object Data > Normals > Auto Smooth): enable and set the Angle. "
            "Edges sharper than the angle stay hard; shallower edges are smooth-shaded. "
            "60° is a good default for hard surface models. "
            "Mark Sharp (Ctrl+E > Mark Sharp in Edit Mode) on specific edges to force them hard "
            "regardless of the Auto Smooth angle."
        ),
    },

    # ── Texture Painting ─────────────────────────────────────────────────────────
    {
        "id": "bl_texpaint_01",
        "app": "blender",
        "topic": "texture_painting",
        "text": (
            "Texture Paint mode lets you paint directly onto the mesh in 3D. "
            "Create a new Image in the UV Editor first, then assign it to a material's Image Texture node. "
            "In Texture Paint mode, use brushes (Draw, Soften, Smear, Clone, Fill) to paint. "
            "F adjusts brush size, Shift+F adjusts strength. Hold Ctrl to pick a color from the mesh."
        ),
    },
    {
        "id": "bl_texpaint_02",
        "app": "blender",
        "topic": "texture_painting",
        "text": (
            "Stencil texture painting: enable Texture > Stencil in the brush settings and load an image. "
            "The stencil appears as an overlay — paint through it to stamp the texture onto the mesh. "
            "RightClick+drag to move the stencil, Shift+RightClick to rotate, Ctrl+RightClick to scale. "
            "Useful for adding logos, labels, or tiling detail to curved surfaces."
        ),
    },

    # ── Physics: Force Fields & Soft Body ────────────────────────────────────────
    {
        "id": "bl_ff_01",
        "app": "blender",
        "topic": "physics",
        "text": (
            "Force Fields affect particles, hair, cloth, and soft body simulations. "
            "Shift+A > Force Field > Wind, Vortex, Turbulence, Magnetic, etc. "
            "Wind pushes in one direction (great for blowing hair/cloth). "
            "Turbulence adds random motion. Vortex swirls around an axis — good for tornado/smoke effects. "
            "Set Strength and Falloff to control influence radius."
        ),
    },
    {
        "id": "bl_softbody_01",
        "app": "blender",
        "topic": "physics",
        "text": (
            "Soft Body simulation makes a mesh deform as if made of elastic material. "
            "Physics > Soft Body. Goal Stiffness controls how strongly vertices return to their rest position — "
            "0 = fully jelly-like, 1 = rigid. Edges > Spring controls how much the mesh resists stretching. "
            "Add a Collision object so the soft body bounces and deforms around it."
        ),
    },

    # ── Compositing: Cryptomatte & Passes ────────────────────────────────────────
    {
        "id": "bl_comp_crypto",
        "app": "blender",
        "topic": "compositing",
        "text": (
            "Cryptomatte (View Layer > Passes > Cryptomatte): generates masks per object, material, or asset "
            "automatically during render. In the Compositor, use the Cryptomatte node to pick "
            "which object to mask with just a click — no manual object ID setup needed. "
            "Enables per-object color grading, isolation, and compositing in post."
        ),
    },
    {
        "id": "bl_comp_shadow",
        "app": "blender",
        "topic": "compositing",
        "text": (
            "Shadow Catcher: enable 'Shadow Catcher' in Object Properties > Visibility. "
            "The object becomes invisible but catches and displays shadows from other objects — "
            "essential for compositing 3D renders over photos. "
            "The shadow blends with the photo background, making 3D objects appear to sit on a real surface."
        ),
    },

    # ── Asset Library ────────────────────────────────────────────────────────────
    {
        "id": "bl_asset_01",
        "app": "blender",
        "topic": "asset_library",
        "text": (
            "Asset Library: mark any object, material, or node group as an Asset (right-click > Mark as Asset). "
            "Set an Asset Library path in Preferences > File Paths > Asset Libraries. "
            "Browse all assets in the Asset Browser editor type — drag them directly into any scene. "
            "Blender's default Pose Library also uses the Asset system for storing and blending poses."
        ),
    },

    # ── Rendering: Holdout & Light Linking ───────────────────────────────────────
    {
        "id": "bl_holdout_01",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "Holdout shader: assign a Holdout node as the surface material to make an object punch a hole "
            "in the render — showing the alpha/transparent background behind it. "
            "Use this to create masks for compositing: a Holdout sphere around a character cuts out "
            "a clean shape for layering effects in post-production."
        ),
    },
    {
        "id": "bl_lightlink_01",
        "app": "blender",
        "topic": "lighting",
        "text": (
            "Light Linking (Blender 4.1+): control which objects a specific light illuminates or excludes. "
            "In the light's Properties > Visibility > Light Linking, include or exclude specific objects. "
            "A key light illuminates only the character; a rim light illuminates only the hair. "
            "Gives fine-grained artistic control without needing separate render layers."
        ),
    },

    # ── Freestyle ────────────────────────────────────────────────────────────────
    {
        "id": "bl_freestyle_01",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "Freestyle (Render Properties > Freestyle): adds non-photorealistic line art overlaid on the render. "
            "Line Sets control which edges are drawn (crease, outline, material boundary, contour). "
            "Line Style controls color, thickness, texture, and chaining. "
            "Great for architectural drawings, comic-book aesthetics, or technical illustration looks."
        ),
    },

    # ── Python Scripting ─────────────────────────────────────────────────────────
    {
        "id": "bl_py_01",
        "app": "blender",
        "topic": "scripting",
        "text": (
            "Blender has a built-in Python console (change editor to Python Console). "
            "bpy is the Blender Python module — everything you can do via the UI, you can script. "
            "bpy.data accesses all scene data (objects, materials, meshes). "
            "bpy.ops runs operators (bpy.ops.mesh.subdivide()). "
            "Hover over any UI button and the tooltip shows the Python expression for that action."
        ),
    },
    {
        "id": "bl_py_02",
        "app": "blender",
        "topic": "scripting",
        "text": (
            "Text Editor > Templates > Python > Addon Tutorial gives a minimal add-on scaffold. "
            "Write scripts in the Text Editor and press Run Script. "
            "Use the Info Editor to see the Python equivalent of recent UI actions — "
            "a perfect way to learn what bpy call corresponds to a menu item you just used."
        ),
    },

    # ── View Layers ──────────────────────────────────────────────────────────────
    {
        "id": "bl_viewlayer_01",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "View Layers let you render the same scene multiple times with different object sets "
            "and pass configurations. Add view layers in the Scene Properties > View Layers panel. "
            "Exclude whole Collections per view layer. Combine in the Compositor: "
            "Character on one layer, Environment on another, VFX on a third — composite them independently."
        ),
    },

    # ── Motion Tracking ──────────────────────────────────────────────────────────
    {
        "id": "bl_track_01",
        "app": "blender",
        "topic": "motion_tracking",
        "text": (
            "Motion Tracking (Movie Clip Editor): load footage, place tracking markers on distinct features, "
            "then Track > Track Scene to solve the camera motion. "
            "Set up a Floor and Origin constraint in the 3D scene, "
            "then Link Empty to Clip to place objects that stick to the real-world surface. "
            "Used to integrate 3D renders into live-action footage."
        ),
    },

    # ── Topology & Quad-Flow ───────────────────────────────────────────────────
    {
        "id": "bl_topo_01",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Topology fundamentals: always model in quads (four-sided polygons). "
            "Quads subdivide cleanly and deform predictably for animation. "
            "Triangles and N-gons cause shading artefacts and break subdivision. "
            "Use Mesh Analysis (Overlay > Face Orientation, Mesh Analysis) to visualise problem areas. "
            "Alt+J converts triangles to quads; Ctrl+T converts quads to triangles."
        ),
    },
    {
        "id": "bl_topo_02",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Poles in topology: a 3-pole is a vertex with 3 edges, a 5-pole has 5. "
            "Ideal vertices are 4-valent (4 edges). Poles are necessary at corners and to redirect edge flow, "
            "but place them in low-deformation areas (away from joints, mouth corners, eye corners). "
            "Excessive poles cause pinching under subdivision — keep them deliberate and minimal."
        ),
    },
    {
        "id": "bl_topo_03",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Edge loops for character topology: "
            "rings of quads should follow the muscles and tension lines of the face or body. "
            "Eye socket: concentric rings around the eye. Mouth: rings around the lips. "
            "This ensures clean deformation when the character smiles, blinks, or speaks. "
            "Reference anatomical muscle maps when planning edge flow for organic characters."
        ),
    },

    # ── Hard Surface Modeling ─────────────────────────────────────────────────
    {
        "id": "bl_hardsurface_01",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Hard surface workflow: use support loops (edge loops added close to a sharp edge) "
            "before applying Subdivision Surface to keep corners sharp. "
            "Alternatively, use Mark Sharp (Edge > Mark Sharp) and a Bevel modifier set to 'Weight' mode "
            "to control bevel width per-edge with Ctrl+Shift+B in the Bevel Weight slider."
        ),
    },
    {
        "id": "bl_hardsurface_02",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Boolean workflow for hard surface: use Boolean modifier (Union, Difference, Intersect) "
            "to cut holes and combine shapes non-destructively. "
            "Keep cutters as separate objects and toggle their visibility with H. "
            "After applying a Boolean, run 'Limited Dissolve' (Mesh > Merge > Limited Dissolve) "
            "to clean up unnecessary topology inside the boolean region."
        ),
    },
    {
        "id": "bl_hardsurface_03",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Bridge Edge Loops: select two open edge loops on separate parts of a mesh, "
            "then Edge > Bridge Edge Loops (Ctrl+E > Bridge Edge Loops). "
            "Creates a smooth bridge of faces between them. "
            "Use for connecting arm to body, tube ends, or filling a gap between two separate shapes. "
            "The Number of Cuts option adds loops to the bridge for better curvature."
        ),
    },
    {
        "id": "bl_hardsurface_04",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "PolyBuild tool (T panel in Edit Mode, or Shift+W): "
            "a retopology-focused tool that lets you click to add faces one by one over a reference mesh. "
            "Drag from an edge to extrude a face; Ctrl+click to delete a face. "
            "Use it on a projected surface (Shrinkwrap modifier active) to re-draw clean topology "
            "over a high-poly sculpt."
        ),
    },

    # ── Object Constraints ────────────────────────────────────────────────────
    {
        "id": "bl_constr_01",
        "app": "blender",
        "topic": "rigging",
        "text": (
            "Object constraints (Properties > Object Constraint Properties): "
            "Copy Location makes one object always stay at the same position as a target. "
            "Copy Transform copies both location, rotation, and scale. "
            "These are non-destructive — the object still has its own transforms underneath. "
            "Use influence slider (0–1) to partially blend the constrained transform."
        ),
    },
    {
        "id": "bl_constr_02",
        "app": "blender",
        "topic": "rigging",
        "text": (
            "Floor constraint: prevents an object from going below a target surface. "
            "Use it on a character foot to prevent foot-floor penetration when animating manually. "
            "Track To constraint makes an object always face another (like a camera facing an Empty). "
            "Limit Distance constraint keeps an object within or outside a radius of its target."
        ),
    },
    {
        "id": "bl_constr_03",
        "app": "blender",
        "topic": "animation",
        "text": (
            "Follow Path constraint: attach an object to a Bezier curve and it will travel along it. "
            "Set the curve's path duration in Object Data > Path Animation. "
            "Enable 'Fixed Position' and keyframe 'Offset' for manual control of position along the path. "
            "Enable 'Follow Curve' so the object rotates to face the direction of travel."
        ),
    },

    # ── Bone Constraints & Custom Shapes ─────────────────────────────────────
    {
        "id": "bl_bone_01",
        "app": "blender",
        "topic": "rigging",
        "text": (
            "IK pole target: IK solvers tend to flip when the limb is straight. "
            "Add an Empty in front of the knee/elbow, then in Pose Mode add an IK constraint to the shin/forearm bone "
            "and set the Pole Target to that Empty. The Pole Angle (usually 0 or -90) orients the flip direction. "
            "Now the limb always bends consistently toward the pole."
        ),
    },
    {
        "id": "bl_bone_02",
        "app": "blender",
        "topic": "rigging",
        "text": (
            "Custom bone shapes (Bone Viewport Display): any mesh can replace the default bone octahedron. "
            "In Pose Mode, select a bone, go to Bone Properties > Viewport Display > Custom Object "
            "and pick a mesh (circle, arrow, widget). "
            "Scale the mesh to control display size — it does not affect rig behaviour. "
            "Creates professional-looking rigs with visible, colour-coded controls."
        ),
    },
    {
        "id": "bl_bone_03",
        "app": "blender",
        "topic": "rigging",
        "text": (
            "B-Bones (Bendy Bones): subdivide a bone into segments that bend along a curved path. "
            "In Bone Properties set Segments (e.g. 8) and Ease In/Out. "
            "Used for spine, tail, or tentacle rigs where you want smooth curvature from a single bone. "
            "Each B-Bone is controlled by its endpoints — add Scale handles for full curve control."
        ),
    },

    # ── Walk Cycle Animation ──────────────────────────────────────────────────
    {
        "id": "bl_walkcycle",
        "app": "blender",
        "topic": "animation",
        "text": (
            "Walk cycle structure: Contact (feet apart, heel hits) → Down (body lowers) → Passing (one leg vertical) → Up (body rises). "
            "Key frames: Contact at 1 and 13 (half cycle), mirror the second half. "
            "Keep root bone rising on Up frames (+Y) and dipping on Down frames for body bounce. "
            "Arms swing opposite to legs — right arm forward when left leg forward."
        ),
    },
    {
        "id": "bl_anim_nla",
        "app": "blender",
        "topic": "animation",
        "text": (
            "NLA (Non-Linear Animation) Editor: bake Actions (walk, run, idle) as strips and combine them. "
            "Push an Action down to NLA with the push-down button in the Action Editor. "
            "Strips can be scaled, blended with influence weights, and looped. "
            "Use Blend Mode 'Replace' or 'Add' to layer idle breathing on top of a walk cycle."
        ),
    },

    # ── Metaballs ─────────────────────────────────────────────────────────────
    {
        "id": "bl_meta_01",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Metaballs (Add > Meta > Ball/Tube/Plane/Ellipsoid/Cube): organic blobs that melt together "
            "when they get close. The Threshold (Object Data) controls how far apart they need to be to merge. "
            "Resolution (Viewport/Render) controls surface smoothness. "
            "Great for blob characters, liquid simulations as proxies, or organic forms before retopology."
        ),
    },

    # ── Volume & OpenVDB ──────────────────────────────────────────────────────
    {
        "id": "bl_volume_01",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "Volume Objects: Add > Volume > Empty Volume, then add a Volume Scatter/Volume Absorption shader. "
            "Load an OpenVDB file (smoke, fire, cloud) with the Volume Data Properties. "
            "Cycles renders volumes accurately; EEVEE needs an approximation with Volumetric settings in the render panel. "
            "Use a Noise Texture mapped to density for procedural fog or clouds."
        ),
    },
    {
        "id": "bl_volume_02",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "Principled Volume shader: all-in-one PBR volume shader. "
            "Color controls scattering color, Density controls thickness, "
            "Emission Strength adds self-illumination (fire). "
            "Anisotropy (-1 to 1): positive values scatter light forward (beam effects), "
            "negative backward (back-scattered fog). Temperature drives fire colour mapping."
        ),
    },

    # ── Ocean Modifier ────────────────────────────────────────────────────────
    {
        "id": "bl_ocean_01",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Ocean Modifier: add it to a high-subdivision plane to simulate animated ocean waves. "
            "Resolution controls detail. Wind Velocity and Wave Scale control wave energy. "
            "Choppiness adds breaking wave tips. Enable Foam and connect the Foam output "
            "to a mix shader for whitecap foam on the material. "
            "Bake the ocean to disk for faster playback."
        ),
    },

    # ── Mesh Analysis Tools ───────────────────────────────────────────────────
    {
        "id": "bl_meshanalysis_01",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Mesh Analysis Overlay (Edit Mode > Overlays > Mesh Analysis): "
            "Distortion shows how far quads deviate from flat (blue=flat, red=bent). "
            "Thickness finds thin regions. Sharp shows angles above a threshold. "
            "Use 'Face Orientation' overlay (blue=outward, red=inward normals) to spot flipped normals "
            "before export — flipped normals cause invisible faces in game engines."
        ),
    },
    {
        "id": "bl_meshanalysis_02",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Finding doubles: in Edit Mode, select all (A), then Mesh > Merge > By Distance (Alt+M > By Distance). "
            "Adjust the Merge Distance to weld overlapping vertices. "
            "Also check for non-manifold geometry: Select > Select All by Trait > Non-Manifold "
            "highlights edges with more than two faces (impossible for solid 3D printing or games)."
        ),
    },

    # ── Advanced Snapping ─────────────────────────────────────────────────────
    {
        "id": "bl_snap_02",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Advanced snapping: enable Snap (Shift+Tab or magnet icon). "
            "Type: Face Project — the moved object projects onto the surface of other meshes (retopology). "
            "Type: Face Nearest — snaps to nearest face point. "
            "Enable 'Project Individual Elements' to snap each vertex in a selection independently. "
            "Align Rotation to Target rotates the object to match the target face's normal."
        ),
    },

    # ── Edit Mode Advanced Tools ──────────────────────────────────────────────
    {
        "id": "bl_edit_gridfill",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Grid Fill (Face > Grid Fill, or Ctrl+F > Grid Fill): select an open edge loop "
            "and fill it with an evenly spaced grid of quads. "
            "Ideal for filling the top of a cylinder or any circular/rectangular hole cleanly. "
            "Span and Offset control the grid alignment. "
            "Much cleaner than F (Fill Face) which creates an N-gon."
        ),
    },
    {
        "id": "bl_edit_tris2quads",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Tris to Quads (Face > Tris to Quads, or Alt+J): converts triangulated meshes back to quads. "
            "Adjust the Max Angle threshold — lower values are stricter. "
            "Often needed after importing FBX/OBJ from game assets or photogrammetry scans. "
            "Poke Faces (Face > Poke Faces) does the opposite: splits every polygon into triangles from its center."
        ),
    },

    # ── Simulation Nodes (Geometry Nodes) ────────────────────────────────────
    {
        "id": "bl_simnodes_01",
        "app": "blender",
        "topic": "geometry_nodes",
        "text": (
            "Simulation Zones (Blender 3.6+): two nodes bracket a zone — Simulation Input and Simulation Output. "
            "Geometry passed through the zone is retained between frames, enabling particle-like simulations "
            "entirely inside Geometry Nodes. "
            "Use for procedural snow accumulation, growing structures, fluid-like spreading, "
            "or any effect that needs memory of previous frames."
        ),
    },

    # ── Light Paths & Motion Blur ─────────────────────────────────────────────
    {
        "id": "bl_lightpath_01",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "Light Path node in Cycles: outputs whether a ray is camera, shadow, reflection, or transmission. "
            "Use 'Is Camera Ray' to make an emissive plane appear as pure white in the final image "
            "but not contribute light (fake HDRI light in the background). "
            "'Is Shadow Ray' lets you make objects cast shadows but remain invisible to the camera."
        ),
    },
    {
        "id": "bl_motionblur_01",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "Motion Blur (Render Properties > Motion Blur): enable for cinematic realism. "
            "Shutter value controls how long the 'shutter' is open per frame — 0.5 = half-frame (standard film). "
            "Higher values = more blur. In Cycles, Steps controls quality of the blur effect. "
            "Per-object motion blur can be disabled in Object Properties > Visibility > Motion Blur."
        ),
    },
    {
        "id": "bl_ambientocclusion",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "Ambient Occlusion in shaders: use the Ambient Occlusion node in the shader editor "
            "to bake contact shadows into a texture. Samples controls quality. "
            "In the Render Properties, enabling Ambient Occlusion adds a global AO pass (Cycles/EEVEE). "
            "For baking: select the target mesh, add an Image Texture node, and in Render > Bake, choose AO."
        ),
    },

    # ── Audio in Blender ─────────────────────────────────────────────────────
    {
        "id": "bl_audio_01",
        "app": "blender",
        "topic": "animation",
        "text": (
            "Audio in Blender: add a sound strip in the Video Sequence Editor (Add > Sound). "
            "In Scene Properties > Audio, set the output device and format. "
            "Add a Speaker object (Add > Speaker) in the 3D scene and link an audio file "
            "for 3D spatial audio in Cycles and EEVEE. Animate the Speaker's position for moving audio sources."
        ),
    },
    {
        "id": "bl_audio_02",
        "app": "blender",
        "topic": "animation",
        "text": (
            "Sync to Audio: in Timeline > Playback > Sync, set to 'AV-sync' so animation plays in sync with the audio track. "
            "Bake Sound to F-Curves (Graph Editor > Key > Bake Sound to F-Curves): "
            "analyse an audio track and drive an object's scale, position, or material value "
            "with the audio amplitude — classic reactive animation effect."
        ),
    },

    # ── Video Sequence Editor ─────────────────────────────────────────────────
    {
        "id": "bl_vse_01",
        "app": "blender",
        "topic": "compositing",
        "text": (
            "Video Sequence Editor (VSE): a non-linear video editor built into Blender. "
            "Add > Movie, Image, Sound, Scene strips. "
            "Stack strips vertically — higher channels take priority. "
            "Cross effect strip creates a fade between two clips. "
            "Render the final video from the VSE by setting the output to MP4/H.264 in Output Properties."
        ),
    },
    {
        "id": "bl_vse_02",
        "app": "blender",
        "topic": "compositing",
        "text": (
            "VSE effects: Color Balance strip for grading (Lift/Gamma/Gain). "
            "Blur strip for defocus. Glow for light bleed. "
            "Transform strip to resize or reposition without cutting. "
            "Speed Control strip to ramp speed: set factor < 1 for slow motion, > 1 for fast. "
            "Use the Preview panel with split-screen to compare color grades."
        ),
    },

    # ── Preferences & Auto-Save ───────────────────────────────────────────────
    {
        "id": "bl_prefs_01",
        "app": "blender",
        "topic": "shortcuts",
        "text": (
            "Blender Preferences (Edit > Preferences): "
            "Interface > Resolution Scale adjusts UI size for HiDPI screens. "
            "Keymap: switch between Blender and Industry Standard keymap (like Maya/3ds Max). "
            "System: set GPU compute for Cycles (CUDA/OptiX for NVIDIA, HIP for AMD, Metal for Apple Silicon). "
            "Enable all needed add-ons (Rigify, Node Wrangler, etc.) under Add-ons tab."
        ),
    },
    {
        "id": "bl_prefs_02",
        "app": "blender",
        "topic": "shortcuts",
        "text": (
            "Auto-save and recovery: Blender auto-saves to a temp file every 2 minutes by default. "
            "Recover last session: File > Recover > Last Session. "
            "Recover auto-save: File > Recover > Auto Save — choose the most recent file. "
            "Increase auto-save interval or count in Preferences > Save & Load > Auto Save. "
            "Always save manually before renders or major edits with Ctrl+S."
        ),
    },

    # ── Add-ons Deep Dive ─────────────────────────────────────────────────────
    {
        "id": "bl_addon_looptools",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "LoopTools add-on (built-in, enable in Preferences > Add-ons): "
            "right-click in Edit Mode > LoopTools. "
            "Relax: smooths selected vertices while keeping topology. "
            "Circle: projects selected vertices onto a perfect circle (great for circular holes). "
            "Curve: fits selected edges to a smooth curve. Space: equalises spacing between selected vertices."
        ),
    },
    {
        "id": "bl_addon_extraobj",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Extra Objects add-on (Add > Mesh > Extra Objects): adds Math Function surfaces (Klein bottle, torus knot), "
            "pipe joints, gears, diamonds, and more. "
            "Useful for mechanical parts and mathematical visualisations. "
            "Enable in Preferences > Add-ons > search 'Extra Objects'."
        ),
    },

    # ── More UV Mapping ───────────────────────────────────────────────────────
    {
        "id": "bl_uv_05",
        "app": "blender",
        "topic": "uv_mapping",
        "text": (
            "UV Live Unwrap: enable in Edit Mode top header (UV > Live Unwrap). "
            "Every time you move a seam or pin a vertex (P to pin, Alt+P to unpin) the unwrap updates in real time. "
            "This interactive workflow lets you immediately see how seam placement affects the UV layout "
            "without repeatedly pressing U > Unwrap."
        ),
    },
    {
        "id": "bl_uv_06",
        "app": "blender",
        "topic": "uv_mapping",
        "text": (
            "Packing UVs: in the UV Editor, UV > Pack Islands arranges all UV islands "
            "to fill the UV space efficiently, minimising wasted texture space. "
            "Average Island Scale first (UV > Average Island Scale) so all islands match texel density. "
            "Use the 'Margin' value to add padding between islands and prevent bleeding in game engines."
        ),
    },

    # ── More Lighting ─────────────────────────────────────────────────────────
    {
        "id": "bl_lighting_05",
        "app": "blender",
        "topic": "lighting",
        "text": (
            "IES light profiles: import real-world IES photometric files for physically accurate area lights. "
            "Add > Light > Area, then in Object Data Properties > Light > Shape, enable 'IES Texture' "
            "and load the .ies file. Produces accurate beam patterns for architectural visualisation. "
            "Many IES files are freely available from lighting manufacturers."
        ),
    },
    {
        "id": "bl_lighting_06",
        "app": "blender",
        "topic": "lighting",
        "text": (
            "HDRI rotation: in the Shader Editor (World), connect an Environment Texture node "
            "to a Mapping node, then to a Texture Coordinate node (Object or Generated). "
            "Animating or adjusting the Mapping Rotation Z value rotates the HDRI "
            "to control which direction the sun or key light comes from — no need to rotate the scene."
        ),
    },

    # ── More Sculpting ────────────────────────────────────────────────────────
    {
        "id": "bl_sculpt_06",
        "app": "blender",
        "topic": "sculpting",
        "text": (
            "Cloth Brush (Sculpt Mode): simulates fabric-like deformation on the mesh surface. "
            "Brush Size determines the 'cloth zone'. Stroke: Dots gives gravity folds; Anchored stretches from a fixed pin. "
            "Great for creating realistic fabric, capes, draped cloth, or soft skin folds without a physics simulation."
        ),
    },
    {
        "id": "bl_sculpt_07",
        "app": "blender",
        "topic": "sculpting",
        "text": (
            "Elastic Deform brush: creates volume-preserving smooth deformation — "
            "pulling the mesh moves surrounding geometry naturally, like pulling taffy. "
            "Best for organic reshaping of body parts or creature features "
            "without losing volume (unlike the Grab brush which simply moves verts in an arc)."
        ),
    },

    # ── Grease Pencil Extra ───────────────────────────────────────────────────
    {
        "id": "bl_gp_04",
        "app": "blender",
        "topic": "grease_pencil",
        "text": (
            "Grease Pencil modifiers: Subdivide adds smoothness to strokes. "
            "Simplify reduces vertex count. Noise adds organic jitter for hand-drawn feel. "
            "Array duplicates strokes in a pattern. "
            "Lineart modifier auto-generates line art from 3D scene geometry "
            "as Grease Pencil strokes — perfect for stylised cel shading without a render pass."
        ),
    },

    # ── Empties ───────────────────────────────────────────────────────────────
    {
        "id": "bl_empty_01",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Empties (Add > Empty): invisible objects used as transform targets, rig controllers, or group pivots. "
            "Parent multiple objects to an Empty to move them as a group while keeping their relative positions. "
            "Empty > Image displays a reference image as a billboard in the viewport — "
            "ideal for modelling over concept art or orthographic blueprints."
        ),
    },

    # ── Principled BSDF Deep Dive ─────────────────────────────────────────────
    {
        "id": "bl_pbsdf_01",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Principled BSDF key parameters: "
            "Base Color — the albedo (diffuse colour). "
            "Metallic — 0 for dielectrics (plastic, wood), 1 for metals. "
            "Roughness — 0 = mirror-smooth, 1 = fully diffuse. "
            "IOR (Index of Refraction) — 1.45 glass, 1.33 water, 1.5 plastic. "
            "Alpha — transparency (use Blend Mode 'Alpha Blend' in Material Settings for correct rendering)."
        ),
    },
    {
        "id": "bl_pbsdf_02",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Principled BSDF advanced: "
            "Subsurface — simulates light scattering inside a translucent material (skin, wax, marble). "
            "Set Subsurface Color to a warm red-pink and Subsurface Radius controls scatter depth per RGB channel. "
            "Clearcoat — adds a secondary glossy layer on top (car paint lacquer, polished wood). "
            "Sheen — simulates micro-fibre roughness (velvet, fabric). "
            "Transmission — for glass/water; combine with IOR and low Roughness."
        ),
    },
    {
        "id": "bl_pbsdf_03",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Specular vs Metallic: for non-metals, Metallic = 0 and Specular controls the highlight intensity. "
            "Most real-world non-metals have Specular around 0.5 (the default). "
            "Specular Tint blends the specular highlight toward the Base Color (coloured plastics). "
            "For metals, Metallic = 1, set Base Color to the metal tint, and Roughness to control polish."
        ),
    },

    # ── Normal Maps ───────────────────────────────────────────────────────────
    {
        "id": "bl_normalmap_01",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Normal maps in Blender: add an Image Texture node, load the normal map, "
            "set its Color Space to 'Non-Color' (critical — prevents sRGB gamma correction destroying the map). "
            "Connect the Color output to a Normal Map node, then connect Normal Map output to the Normal input "
            "of Principled BSDF. The Normal Map node's Space should be 'Tangent' for standard baked maps."
        ),
    },
    {
        "id": "bl_normalmap_02",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Baking normal maps: create a high-poly and low-poly version of the mesh. "
            "Select both, with low-poly active last. In Render Properties > Bake, choose 'Normal'. "
            "Enable 'Selected to Active' and set Extrusion (cage size) so the ray hits the high-poly. "
            "The result captures the high-poly surface detail as a texture for the low-poly — "
            "used in all game-ready assets to fake surface complexity cheaply."
        ),
    },

    # ── Shape Keys & Drivers ──────────────────────────────────────────────────
    {
        "id": "bl_shapekey_01",
        "app": "blender",
        "topic": "animation",
        "text": (
            "Shape Keys (Object Data Properties > Shape Keys): "
            "Basis is the rest state. Add new keys and sculpt or move vertices — "
            "each key stores the delta from Basis. "
            "Value slider (0–1) blends between Basis and the shape. "
            "Used for facial expressions (smile, blink, phonemes) and mechanical deformations (car door opening)."
        ),
    },
    {
        "id": "bl_shapekey_02",
        "app": "blender",
        "topic": "animation",
        "text": (
            "Relative vs Absolute Shape Keys: Relative (default) adds each shape's delta on top of Basis — "
            "multiple shapes can combine. Absolute (pin icon) transitions between shapes as the Evaluation Time changes — "
            "good for a walk cycle stored as progressive key poses. "
            "Corrective shape keys fix skin-weighting artefacts at specific joint angles by adding a corrective delta "
            "driven by a bone rotation."
        ),
    },
    {
        "id": "bl_drivers_01",
        "app": "blender",
        "topic": "animation",
        "text": (
            "Drivers: right-click any property > Add Driver. "
            "In the Driver panel (Graph Editor > Drivers view), set the source (a bone rotation, object location, custom property). "
            "Type: Average Value averages the source; Min/Max/Sum combine multiple sources. "
            "Scripted Expression: write a Python expression (e.g. 'var * 2') for custom math. "
            "Example: drive a shape key value from a bone's Y rotation to auto-correct a bulging elbow."
        ),
    },

    # ── Weight Painting ───────────────────────────────────────────────────────
    {
        "id": "bl_weightpaint_01",
        "app": "blender",
        "topic": "rigging",
        "text": (
            "Weight Painting (Ctrl+Tab in Object Mode > Weight Paint): "
            "blue = 0 (no influence), red = 1 (full influence). "
            "Select the armature and the mesh (Shift+click), enter Weight Paint Mode on the mesh. "
            "Click a bone in the viewport (or select from the Vertex Group list) to paint its influence. "
            "Use Blur brush to smooth hard weight transitions at joints."
        ),
    },
    {
        "id": "bl_weightpaint_02",
        "app": "blender",
        "topic": "rigging",
        "text": (
            "Normalize All (Weights > Normalize All): ensures all vertex weights for each vertex sum to 1. "
            "Without this, a vertex might be influenced 100% by Shoulder AND 100% by Spine — causing double translation. "
            "Lock a vertex group before normalising to preserve its weights and only adjust others. "
            "Gradient weight painting (Weight Gradient tool) paints a smooth weight ramp from 1 to 0 across a selection."
        ),
    },

    # ── Particles (Classic) ───────────────────────────────────────────────────
    {
        "id": "bl_particles_01",
        "app": "blender",
        "topic": "physics",
        "text": (
            "Particle System (Object Properties > Particles > New): "
            "Emitter type: emits geometry (spheres, objects) over time from the mesh surface. "
            "Hair type: grows static strands from the surface — used for hair, grass, fur before Geometry Nodes Hair. "
            "Emission Number sets total particle count. Start/End frames control emission timing. "
            "Lifetime sets how many frames each particle lives."
        ),
    },
    {
        "id": "bl_particles_02",
        "app": "blender",
        "topic": "physics",
        "text": (
            "Particle rendering: in the Render panel of the Particle Settings, choose what each particle looks like: "
            "Halo (dot), Object (instance a mesh), Collection (randomly instance from a collection). "
            "Use 'Render > Object' with a tree model to scatter trees across a terrain. "
            "Enable 'Rotation' and 'Random Rotation' so each instance has a unique orientation. "
            "Geometry Nodes particles (Points > Instance) are now preferred for new projects."
        ),
    },

    # ── Mantaflow Fluid ───────────────────────────────────────────────────────
    {
        "id": "bl_fluid_01",
        "app": "blender",
        "topic": "physics",
        "text": (
            "Mantaflow liquid simulation: "
            "1) Create a Domain (box that contains the sim — Physics > Fluid > Type: Domain, Liquid). "
            "2) Create a Flow object (Physics > Fluid > Type: Flow, Flow Type: Liquid, Inflow). "
            "3) Create an Effector (solid object fluid hits — Type: Effector). "
            "Bake the simulation (Domain > Cache > Bake All). "
            "Increase Resolution Divisions for more detail (but exponentially slower)."
        ),
    },
    {
        "id": "bl_smoke_01",
        "app": "blender",
        "topic": "physics",
        "text": (
            "Mantaflow fire/smoke simulation: same Domain > Flow > Effector structure as liquid. "
            "Set Flow Type to Fire, Smoke, or Fire + Smoke. "
            "Domain type: Gas. Use the Shader Editor with a Principled Volume to shade smoke (grey density) "
            "and fire (yellow/orange emission). Bake and render in Cycles for best results. "
            "Temperature controls fire rise speed; Vorticity adds turbulent swirling."
        ),
    },

    # ── Rigid Body ────────────────────────────────────────────────────────────
    {
        "id": "bl_rigid_01",
        "app": "blender",
        "topic": "physics",
        "text": (
            "Rigid Body physics: select an object, Physics > Rigid Body > Type: Active (moves with physics). "
            "Type: Passive (static collider). "
            "Bake the simulation via Scene > Rigid Body World > Bake to Keyframes. "
            "Collision Shape: Convex Hull is fast and accurate for convex objects; Mesh is exact but slow. "
            "Friction and Bounciness control material properties."
        ),
    },

    # ── Cycles Denoising ─────────────────────────────────────────────────────
    {
        "id": "bl_denoise_01",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "Cycles denoising: enable in Render Properties > Sampling > Denoise. "
            "Denoiser options: OpenImageDenoise (CPU-based, very high quality), OptiX (NVIDIA GPU, very fast). "
            "Add a Denoise node in the Compositor for frame-by-frame denoising with the Albedo and Normal passes — "
            "significantly better than the integrated per-sample denoiser for animation. "
            "Use Render Passes > Diffuse Direct/Indirect for targeted denoising."
        ),
    },

    # ── EEVEE Specifics ───────────────────────────────────────────────────────
    {
        "id": "bl_eevee_01",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "EEVEE vs Cycles: EEVEE is a real-time rasterizer — renders in seconds but uses screen-space approximations. "
            "Cycles is a path-tracer — physically accurate light, slower. "
            "Use EEVEE for: motion graphics, stylised looks, product visualisation where speed matters. "
            "Use Cycles for: photorealistic interiors, caustics, sub-surface scattering accuracy, VFX."
        ),
    },
    {
        "id": "bl_eevee_02",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "EEVEE quality settings: "
            "Ambient Occlusion: adds contact shadows between nearby surfaces. "
            "Bloom: adds glow to bright areas (enable under Render Properties > Bloom). "
            "Screen Space Reflections (SSR): enables reflections visible in camera (not true ray-traced). "
            "Shadows: increase Cascade Size and Cube Size for sharper shadows. "
            "Sample count: increase for cleaner temporal anti-aliasing."
        ),
    },

    # ── Viewport Shading Modes ────────────────────────────────────────────────
    {
        "id": "bl_viewport_01",
        "app": "blender",
        "topic": "navigation",
        "text": (
            "Viewport shading modes (top-right sphere icons or Z key pie menu): "
            "Wireframe — see through the mesh. Solid — flat shading with studio lighting (fast). "
            "Material Preview — shows materials with an HDRI (no render needed, uses Workbench engine). "
            "Rendered — live viewport render (Cycles or EEVEE). "
            "In Solid mode, click the dropdown to switch between Matcap (artistic lighting spheres) and Studio."
        ),
    },

    # ── Render Passes & EXR ──────────────────────────────────────────────────
    {
        "id": "bl_renderpasses_01",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "Render Passes: enable in View Layer Properties > Passes. "
            "Combined = final image. Diffuse Direct/Indirect = diffuse light only. "
            "Glossy Direct/Indirect = specular. AO = ambient occlusion. Shadow = shadows alone. "
            "Normal = surface normals. Vector = motion vectors (for motion blur in compositing). "
            "Connecting all passes to a File Output node in the Compositor saves them as separate EXR layers."
        ),
    },
    {
        "id": "bl_exr_01",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "Multi-Layer EXR: set Output Format to OpenEXR MultiLayer in Output Properties. "
            "All enabled render passes are saved into one EXR file. "
            "Import into Nuke, DaVinci Fusion, or After Effects for professional compositing. "
            "In the Compositor, use an Image node to load it back and a Render Layers node "
            "to access individual passes for grading, re-lighting, or fixing only specific passes."
        ),
    },

    # ── Curve Objects ─────────────────────────────────────────────────────────
    {
        "id": "bl_curve_03",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Curve objects (Add > Curve > Bezier/NURBS): vector-based paths editable with control points. "
            "Bezier: each point has handles (V for handle type: Free, Aligned, Vector, Auto). "
            "In the Object Data (Curve) panel: Bevel > Round adds a circular cross-section (tube/cable). "
            "Set Bevel Depth and Resolution for tube thickness and smoothness. "
            "Alt+C converts a curve to a mesh. Ctrl+Alt+C converts the mesh back to a curve."
        ),
    },
    {
        "id": "bl_curve_04",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "NURBS curves/surfaces: smoother than Bezier for organic shapes but less controllable. "
            "Add > Surface > NURBS Sphere/Cylinder for smooth mathematical surfaces. "
            "Use NURBS curves as path guides for the Array + Curve modifier combo: "
            "Array offset driven by a NURBS/Bezier path makes cables, chains, and fences follow any curve precisely."
        ),
    },

    # ── Text Objects ──────────────────────────────────────────────────────────
    {
        "id": "bl_text_01",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Text objects (Add > Text): create editable 3D text. Tab to enter Edit Mode and type. "
            "In Object Data > Font, load any .ttf/.otf font file. "
            "Extrude adds depth; Bevel rounds the extrude edges. "
            "Size, Line Dist, and Spacing control the layout. "
            "Convert to Mesh (Alt+C) to edit individual letters as geometry and add further modelling."
        ),
    },

    # ── Separate & Join ───────────────────────────────────────────────────────
    {
        "id": "bl_separate_join",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Separate (P in Edit Mode): splits selected geometry into its own object. "
            "Options: Selection (selected faces/verts), By Material (splits each material into its own object), "
            "By Loose Parts (splits disconnected meshes). "
            "Join (Ctrl+J in Object Mode): merges all selected objects into one mesh — "
            "the active object's name and origin are used. Destructive operation; use with care."
        ),
    },

    # ── Grease Pencil 2D Animation ────────────────────────────────────────────
    {
        "id": "bl_gp_05",
        "app": "blender",
        "topic": "grease_pencil",
        "text": (
            "Grease Pencil 2D animation: switch to 2D Animation workspace. "
            "Draw strokes in Draw Mode. In the Dope Sheet (Grease Pencil > Dope Sheet), "
            "each stroke lives on a frame. Insert new frame (I) and redraw to animate. "
            "Enable Onion Skinning (overlay) to ghost previous/next frames — "
            "set Before (blue) and After (orange) count so you see multiple frames at once for smooth in-betweening."
        ),
    },
    {
        "id": "bl_gp_06",
        "app": "blender",
        "topic": "grease_pencil",
        "text": (
            "Grease Pencil interpolation: in the Dope Sheet, select two keyframes and go to "
            "Grease Pencil > Interpolate > Interpolate Sequence. "
            "Blender generates in-between frames automatically by morphing stroke positions. "
            "Works best when both keyframes have the same number of strokes with matching point counts. "
            "Used for quick rough animation without drawing every frame."
        ),
    },

    # ── Cloth Simulation ──────────────────────────────────────────────────────
    {
        "id": "bl_cloth_01",
        "app": "blender",
        "topic": "physics",
        "text": (
            "Cloth simulation: add Physics > Cloth to a mesh. "
            "Quality Steps: higher = more accurate but slower (8–15 for detailed cloth). "
            "Pin Group: create a vertex group, paint it 1.0 where cloth is pinned (e.g. shoulder seam), "
            "then set it as the Pin Group — that region stays fixed while the rest falls. "
            "Collision: enable Self-Collision to prevent cloth passing through itself."
        ),
    },
    {
        "id": "bl_cloth_02",
        "app": "blender",
        "topic": "physics",
        "text": (
            "Cloth presets: Blender includes presets (Cotton, Denim, Leather, Rubber, Silk). "
            "Access via the preset dropdown in Cloth Properties. "
            "Stiffness (Tension, Compression, Shear) controls how the fabric resists stretching and bending. "
            "Air Viscosity damps the cloth oscillation — high value for underwater or heavy material feel. "
            "Always bake the cache before rendering (Cloth > Cache > Bake)."
        ),
    },

    # ── EEVEE vs Cycles Decision ──────────────────────────────────────────────
    {
        "id": "bl_engine_choice",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "Choosing a render engine: "
            "Cycles: use for photorealism — accurate global illumination, caustics, SSS, volumetrics. "
            "EEVEE Next (Blender 4.2+): much closer to Cycles quality with real-time performance. "
            "Workbench: for quick technical previews, matcaps, and wireframe renders. "
            "Third-party: LuxCore (spectral), Octane, Redshift, Arnold for studios with specific requirements."
        ),
    },

    # ── Blender 4.x Features ─────────────────────────────────────────────────
    {
        "id": "bl_4x_viewport_comp",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "Viewport Compositor (Blender 4.0+): apply compositor nodes directly in the 3D Viewport "
            "without a full render. Enable in Viewport Shading dropdown > Compositor > Camera. "
            "Nodes like Glare, Color Correction, Vignette apply in real time as you work. "
            "Faster iteration than re-rendering to check compositing effects — "
            "then finalise with the full Compositor for production output."
        ),
    },
    {
        "id": "bl_4x_hair_bsdf",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Principled Hair BSDF (Blender 4.0+): physically-based hair shader. "
            "Melanin controls hair darkness (0 = white/blonde, 1 = black). "
            "Melanin Redness shifts toward red/auburn. "
            "Roughness controls highlight sharpness. "
            "Coat adds a second highlight layer (cuticle gloss). "
            "Connect a gradient texture to Melanin for natural root-to-tip color variation."
        ),
    },

    # ── Separating & Joining ─────────────────────────────────────────────────
    {
        "id": "bl_performance_02",
        "app": "blender",
        "topic": "performance",
        "text": (
            "Blender performance tips: "
            "Simplify (Render Properties > Simplify): globally cap Subdivision Surface levels during viewport and render. "
            "Statistics overlay: View > Overlays > Statistics shows vertex/face/object count — watch for polygon budget. "
            "Use Instancing (Object Properties > Instancing > Faces/Verts) for repeating objects: "
            "one mesh, many displayed — viewport and render cost is only one object."
        ),
    },

    # ── Shader Nodes: Textures ────────────────────────────────────────────────
    {
        "id": "bl_shader_noise",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Noise Texture node: generates procedural fractal noise. "
            "Scale controls zoom level; Detail adds more octaves of noise (more complexity, slower). "
            "Roughness controls how jagged vs smooth the noise is. Distortion warps the noise internally. "
            "Connect Color output to Base Color for rocky/cloudy surfaces; to Roughness for uneven shininess; "
            "to a Bump node for procedural surface detail without baking."
        ),
    },
    {
        "id": "bl_shader_voronoi",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Voronoi Texture node: generates cell-pattern noise — like cracked mud, reptile scales, or stone tiles. "
            "Feature: F1 gives cell centres (spotty); Distance to Edge gives the lines between cells (cracks). "
            "Scale controls cell density. Randomness at 0 gives uniform grid, at 1 gives organic variation. "
            "Use Distance to Edge as a mask for cavity/crevice effects or grunge maps."
        ),
    },
    {
        "id": "bl_shader_colorramp",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Color Ramp node: maps a 0–1 value (like a texture's greyscale output) to a custom gradient. "
            "Use it to posterise a noise texture into hard zones (black→white with a sharp stop). "
            "Essential for: turning a Voronoi distance into clean cell outlines, "
            "remapping roughness falloff, adding colour variation to a procedural material, "
            "or controlling where a mix happens across a surface."
        ),
    },
    {
        "id": "bl_shader_texcoord",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Texture Coordinate node: controls how a texture is mapped to the surface. "
            "UV — uses the mesh's UV map (most common for baked or image textures). "
            "Object — maps relative to the object's local space (moves with the object, good for procedurals). "
            "Generated — maps to the bounding box (0–1 in each axis, ignores UV layout). "
            "Camera — maps based on camera view (for screen-space effects). "
            "Always connect through a Mapping node to control position/rotation/scale."
        ),
    },
    {
        "id": "bl_shader_mapping",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Mapping node: transforms texture coordinates with Location, Rotation, and Scale. "
            "Connect Texture Coordinate > Mapping > Image Texture for full control. "
            "Scale Z to 0.5 to stretch a texture; Rotation Z to 45° to rotate the pattern. "
            "Animating the Location values makes a texture scroll across the surface — "
            "used for moving water, conveyor belts, or animated fire UVs."
        ),
    },
    {
        "id": "bl_shader_mix",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Mix Shader: blends two shaders together by a Factor (0 = first shader, 1 = second shader). "
            "Use a texture or Fresnel node as the Factor for surface-dependent blending. "
            "Example: mix a Glossy shader with a Diffuse shader using a Noise texture as the factor "
            "to get a material that's shiny in some areas and matte in others. "
            "Add Shader: adds two shaders' contributions together (useful for emissive + diffuse combos)."
        ),
    },
    {
        "id": "bl_shader_fresnel",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Fresnel node: outputs 0 at surfaces facing the camera, 1 at grazing angles. "
            "Real-world surfaces are more reflective at glancing angles (wet road, car paint). "
            "Use as a Factor in a Mix Shader to blend a rough diffuse (head-on) with a glossy (edges). "
            "Layer Weight node's Facing output does the same; its Fresnel output is IOR-aware like Principled BSDF."
        ),
    },

    # ── True Displacement ─────────────────────────────────────────────────────
    {
        "id": "bl_displacement_01",
        "app": "blender",
        "topic": "materials",
        "text": (
            "True displacement in Cycles (vs Bump): connect a texture to the Displacement input of the Material Output node. "
            "In Material Properties > Settings > Surface, set Displacement to 'Displacement and Bump' (or 'Displacement Only'). "
            "Enable Adaptive Subdivision: add a Subdivision Surface modifier set to Simple, "
            "then in Render Properties > Subdivision enable 'Dicing Rate' — Cycles subdivides dynamically "
            "to the pixel level, giving real geometry displacement without a high-poly mesh."
        ),
    },
    {
        "id": "bl_bump_01",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Bump mapping vs Normal mapping vs Displacement: "
            "Bump — fake shading trick using a greyscale height map; zero geometry change, fastest. "
            "Normal map — encodes surface normals in RGB; more accurate than bump, still no geometry. "
            "Displacement — actually moves vertices; looks correct at silhouettes, slowest. "
            "Use Bump/Normal for game-ready assets; Displacement for film/arch-viz close-ups where silhouette accuracy matters."
        ),
    },

    # ── Multi-Resolution Modifier ─────────────────────────────────────────────
    {
        "id": "bl_multires_01",
        "app": "blender",
        "topic": "sculpting",
        "text": (
            "Multi-Resolution modifier: like Subdivision Surface but stores sculpt detail at each level. "
            "Add it to a mesh, subdivide to level 2–3, sculpt broad forms. "
            "Subdivide again to level 5–6, sculpt fine detail. Switch between levels to edit at different scales. "
            "Bake the high-res detail down to a normal map for the low-res base mesh. "
            "This is the traditional (pre-Geometry Nodes) film character sculpt pipeline."
        ),
    },

    # ── Compositing: Glare ────────────────────────────────────────────────────
    {
        "id": "bl_comp_glare",
        "app": "blender",
        "topic": "compositing",
        "text": (
            "Glare node in the Compositor: adds bloom, fog glow, or light streaks to bright areas of the render. "
            "Type: Fog Glow — soft bloom around bright areas. Streaks — star-like light rays (use for sun/lamps). "
            "Simple Star — 4-pointed star glow. Mix value controls blend with the original image. "
            "Feed only the Glossy or Emission render pass into Glare for a controlled effect "
            "rather than glowing the entire image."
        ),
    },
    {
        "id": "bl_comp_colbal",
        "app": "blender",
        "topic": "compositing",
        "text": (
            "Color Balance node (CDL — Color Decision List): classic Lift/Gamma/Gain colour grading. "
            "Lift adjusts shadows (raise to add a colour tint to blacks). "
            "Gamma adjusts midtones. Gain adjusts highlights. "
            "For a cinematic look: lift slightly toward blue-green (teal shadows), "
            "push gain slightly warm (orange highlights) — the classic teal-and-orange grade."
        ),
    },
    {
        "id": "bl_comp_lensdist",
        "app": "blender",
        "topic": "compositing",
        "text": (
            "Lens Distortion node: adds barrel distortion (bulge), pincushion distortion (pinch), "
            "chromatic aberration (Dispersion), and jitter. "
            "Distortion: positive = barrel (wide-angle look), negative = pincushion (telephoto look). "
            "Dispersion separates RGB channels at edges — adds a photographic lens fringe. "
            "Combine with Glare, Color Balance, and a subtle Vignette (Ellipse Mask > Invert > Multiply) "
            "for a full cinematic post-processing pipeline."
        ),
    },

    # ── Graph Editor F-Curves ─────────────────────────────────────────────────
    {
        "id": "bl_fcurve_01",
        "app": "blender",
        "topic": "animation",
        "text": (
            "Graph Editor F-Curve handle types (V key in Graph Editor): "
            "Free — handles move independently, any shape. "
            "Aligned — handles stay opposite, smooth tangent. "
            "Vector — linear handles, sharp corners. "
            "Auto — Blender auto-smooths handles (good default). "
            "Auto Clamped — like Auto but prevents overshoot past keyframe values (prevents bouncing above/below targets)."
        ),
    },
    {
        "id": "bl_fcurve_02",
        "app": "blender",
        "topic": "animation",
        "text": (
            "F-Curve extrapolation (Channel > Extrapolation Mode): "
            "Constant — value holds after the last keyframe (nothing moves after the animation ends). "
            "Linear — continues the slope beyond keyframes (good for continuous spinning). "
            "Cyclic (Modifier > Cycles): loops the animation between first and last keyframe — "
            "set Before and After to 'Repeat' for a seamless looping animation without duplicating keyframes."
        ),
    },

    # ── Face Sets ─────────────────────────────────────────────────────────────
    {
        "id": "bl_facesets_01",
        "app": "blender",
        "topic": "sculpting",
        "text": (
            "Face Sets in Sculpt Mode: Ctrl+W draws a face set region by painting. "
            "Each face set gets a unique colour. Hold Alt while sculpting to mask everything except the active face set. "
            "Use Ctrl+Alt+W to expand/shrink face sets. "
            "Face sets let you isolate a face region (e.g. just the nose) and sculpt there without affecting the rest of the mesh — "
            "a faster alternative to masking for blocked-out sculpting."
        ),
    },

    # ── Edit Mode Tools ───────────────────────────────────────────────────────
    {
        "id": "bl_inset_01",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Inset Faces (I key in Edit Mode): shrinks each selected face inward by a set amount, "
            "creating a border loop around it. "
            "Thickness controls inset distance. Depth extrudes the inset up/down simultaneously. "
            "Enable 'Individual' (I while using Inset) to inset each face independently rather than as a group. "
            "Foundation technique for panel lines, windows, recesses, and hard-surface detailing."
        ),
    },
    {
        "id": "bl_knifeproject_01",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Knife Project (Edit Mode > Mesh > Knife Project): projects the silhouette of another object's edges "
            "onto the active mesh, cutting new edges along the projected shape. "
            "Select the cutter object first (in Object Mode), then Shift+click the target, enter Edit Mode, "
            "then Mesh > Knife Project. Great for cutting logos, complex shapes, or technical curves onto a surface."
        ),
    },
    {
        "id": "bl_spin_01",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Spin tool (Edit Mode > Toolbar > Spin, or Alt+click on a profile): "
            "rotates selected geometry around the 3D cursor, duplicating it each step. "
            "Used to lathe-turn a profile curve into a revolution solid (wine glass, vase, wheel arch). "
            "Steps controls how many duplicated segments are created. "
            "Angle 360° makes a full revolution; less for partial arcs like an arch or cup handle."
        ),
    },

    # ── Import/Export ─────────────────────────────────────────────────────────
    {
        "id": "bl_export_fbx",
        "app": "blender",
        "topic": "performance",
        "text": (
            "FBX export for game engines (File > Export > FBX): "
            "Scale: set to 0.01 if importing into Unreal Engine (which uses centimetres); Unity uses 1. "
            "Apply Transform: enable to bake the object's transform before export. "
            "Mesh: triangulate on export for game engines. "
            "Armature: check 'Add Leaf Bones' only if required by the target engine. "
            "Disable 'Add Leaf Bones' for Unreal rigs."
        ),
    },
    {
        "id": "bl_export_gltf",
        "app": "blender",
        "topic": "performance",
        "text": (
            "glTF/GLB export (File > Export > glTF 2.0): the standard for web, AR/VR, and real-time engines. "
            "GLB is a single binary file (embed textures); glTF is a JSON + separate texture files. "
            "Format: glTF Separate for editing pipelines; GLB for distribution. "
            "Include all PBR maps (Base Color, Roughness, Metallic, Normal) — glTF 2.0 is fully PBR. "
            "Draco compression (enable in export panel) dramatically reduces file size for web delivery."
        ),
    },
    {
        "id": "bl_export_alembic",
        "app": "blender",
        "topic": "performance",
        "text": (
            "Alembic (.abc) export (File > Export > Alembic): the VFX industry standard for animated geometry caches. "
            "Exports baked vertex positions per frame — no armature or modifiers, just raw deformed mesh. "
            "Used to hand off simulations (cloth, fluid, softbody, hair) to other DCCs (Houdini, Maya, Nuke). "
            "Frame Range controls which frames bake. 'Triangulate' ensures compatibility with all importers."
        ),
    },

    # ── Shrinkwrap Modifier ───────────────────────────────────────────────────
    {
        "id": "bl_shrinkwrap_01",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Shrinkwrap modifier: projects a mesh onto the surface of a target object. "
            "Mode: Nearest Surface Point — every vertex moves to the closest point on the target. "
            "Project — projects along the mesh's normals (use for decals or surface details that follow curvature). "
            "Wrap Method: Above Surface keeps a small offset so the mesh floats above the target. "
            "Essential for retopology (combined with Face Snapping) and for attaching clothing to a character body."
        ),
    },

    # ── Proportional Editing ──────────────────────────────────────────────────
    {
        "id": "bl_propedit_01",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Proportional Editing (O key in Edit Mode): when enabled, moving/rotating/scaling selected vertices "
            "also affects nearby unselected vertices, with influence falling off by distance. "
            "Scroll the mouse wheel while transforming to adjust the influence radius (shown as a circle in the viewport). "
            "Essential for organic surface shaping — push a small section of a terrain or face without hard boundaries."
        ),
    },
    {
        "id": "bl_propedit_02",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Proportional Editing falloff types (dropdown in the header bar while O is on): "
            "Smooth — gentle bell-curve falloff (most natural). Sphere — spherical influence. "
            "Root — influence drops quickly, then levels. Sharp — aggressive falloff, tight influence area. "
            "Linear — constant slope. Random — random displacement within the radius (organic noise). "
            "Constant — all vertices in the radius move equally (like moving a selection with no falloff)."
        ),
    },

    # ── Loop Cut and Slide ────────────────────────────────────────────────────
    {
        "id": "bl_loopcut_01",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Loop Cut and Slide (Ctrl+R in Edit Mode): hover over an edge and a yellow ring previews "
            "where the new loop will be cut. Click to confirm, then slide the loop along the face. "
            "Scroll the mouse wheel before clicking to add multiple parallel cuts at once. "
            "Right-click or press Escape after the first click to place the cut exactly at the midpoint. "
            "This is the primary way to add edge loops for support loops or topology refinement."
        ),
    },

    # ── Bevel Deep Dive ───────────────────────────────────────────────────────
    {
        "id": "bl_bevel_02",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Bevel (Ctrl+B): drag to bevel selected edges. Scroll wheel adds segments (more rounded bevel). "
            "V while bevelling switches to Vertex Bevel (Ctrl+Shift+B), which chamfers vertices. "
            "Profile value (in the redo panel, F9): 0.5 = round, 0 = flat, 1 = sharp concave. "
            "Clamp Overlap prevents bevels from overlapping adjacent edges on tight geometry. "
            "Bevel Weight (edge property) + Bevel modifier's 'Weight' limit method = per-edge bevel control."
        ),
    },

    # ── 3D Cursor ─────────────────────────────────────────────────────────────
    {
        "id": "bl_3dcursor_01",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "3D Cursor (Shift+RMB to place): Blender's universal reference point. "
            "Shift+S opens the Snap pie menu: 'Cursor to Selected' snaps the cursor to the selection centre; "
            "'Cursor to World Origin' resets it to 0,0,0. "
            "Use the cursor as the pivot point (,) so objects rotate or scale around the cursor location. "
            "Add > Object places new objects at the cursor. "
            "Object > Set Origin > Origin to 3D Cursor moves the origin without moving geometry."
        ),
    },

    # ── Set Origin ────────────────────────────────────────────────────────────
    {
        "id": "bl_setorigin_01",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Set Origin (right-click in Object Mode > Set Origin): "
            "Origin to Geometry — moves the origin to the geometric centre of the mesh. "
            "Origin to 3D Cursor — places the origin at the cursor. "
            "Geometry to Origin — moves the geometry so the existing origin is at its centre. "
            "The origin is the pivot point for transforms and the object's positional reference in the scene. "
            "Misaligned origins cause problems with modifiers, constraints, and parenting."
        ),
    },

    # ── Rip ───────────────────────────────────────────────────────────────────
    {
        "id": "bl_rip_01",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Rip (V in Edit Mode): tears selected vertices/edges apart, creating a gap in the mesh. "
            "The rip follows the mouse direction. "
            "Alt+V (Rip Fill) rips and immediately fills the gap with new faces. "
            "Use to open a seam in a mesh (e.g. split a cylinder along one side to unfold it flat), "
            "or to create panels and panel lines in hard surface modelling."
        ),
    },

    # ── Image Texture Node ────────────────────────────────────────────────────
    {
        "id": "bl_imagetext_01",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Image Texture node: the foundation of texture-mapped materials. "
            "Open the image file (PNG, JPEG, EXR, TIFF). "
            "Color Space: set to sRGB for colour maps (Base Color, Emission), Non-Color for data maps "
            "(Normal, Roughness, Metallic, AO, Displacement) — critical to avoid incorrect gamma correction. "
            "Interpolation: Linear for most use; Closest for pixel art. "
            "Extension: Repeat (tile), Clip (black outside UV 0–1), Extend (stretch last pixel)."
        ),
    },

    # ── Emission Shader ───────────────────────────────────────────────────────
    {
        "id": "bl_emission_01",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Emission shader: makes a surface emit light. Connect to the Surface input of Material Output "
            "(or mix with Principled BSDF via Add Shader for a glowing material). "
            "In Cycles, Emission objects are actual light sources — "
            "high Strength makes them light the scene. "
            "In EEVEE, enable 'Bloom' in render settings for glowing halos. "
            "Use a Blackbody node (temperature in Kelvin) as the Emission Color for physically accurate light colours."
        ),
    },

    # ── Transparent BSDF ─────────────────────────────────────────────────────
    {
        "id": "bl_transparent_01",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Transparent BSDF: passes rays straight through the surface with no refraction — "
            "use for alpha-cutout materials (leaves, hair cards, chain-link fence). "
            "Mix with Diffuse/Principled using a Texture Alpha as the factor: "
            "black areas become transparent, white areas are opaque. "
            "In Material Settings set Blend Mode to 'Alpha Clip' (hard cutout) or 'Alpha Blend' (soft edges). "
            "For true glass refraction, use Principled BSDF with Transmission instead."
        ),
    },

    # ── Material Slots ────────────────────────────────────────────────────────
    {
        "id": "bl_matslots_01",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Multiple materials on one object: in Material Properties, click + to add material slots. "
            "Assign different materials to different faces: in Edit Mode, select faces, "
            "pick the slot in the Material Properties panel, click Assign. "
            "Use this for a car body (paint + glass + chrome) or character (skin + clothing + eyes) "
            "all as one mesh with multiple material slots."
        ),
    },

    # ── Vertex Groups ─────────────────────────────────────────────────────────
    {
        "id": "bl_vertgroups_01",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Vertex Groups (Object Data Properties > Vertex Groups): named collections of vertices with a weight (0–1). "
            "Create a group, select vertices in Edit Mode, click Assign with a weight. "
            "Used by: Armature modifier (controls bone influence), Particle Systems (emit only from a group), "
            "Solidify modifier (variable thickness), Displacement modifier, and many others. "
            "Click Select/Deselect to quickly re-select all vertices in a group."
        ),
    },

    # ── X-Mirror ─────────────────────────────────────────────────────────────
    {
        "id": "bl_xmirror_01",
        "app": "blender",
        "topic": "sculpting",
        "text": (
            "X-Mirror (header toggle in Sculpt Mode and Weight Paint): "
            "any brush stroke on the right side of the mesh automatically mirrors to the left, "
            "and vice versa — requires topology to be perfectly symmetrical. "
            "In Edit Mode, Mesh > Symmetrize copies one half over the other to establish symmetry before sculpting. "
            "X-Mirror saves enormous time on faces, bodies, vehicles, or anything bilaterally symmetrical."
        ),
    },

    # ── Geometry Nodes: Core Nodes ────────────────────────────────────────────
    {
        "id": "bl_gn_instpoints",
        "app": "blender",
        "topic": "geometry_nodes",
        "text": (
            "Instance on Points node: takes a set of points and places an instance of a geometry on each. "
            "Connect a Distribute Points on Faces node (which scatters points over a mesh surface) "
            "into the Points socket, and an Object Info node (pointing to a tree/rock/grass object) "
            "into the Instance socket. Rotation and Scale inputs randomise each instance. "
            "This replaces the old Particle System for object scattering."
        ),
    },
    {
        "id": "bl_gn_joingeom",
        "app": "blender",
        "topic": "geometry_nodes",
        "text": (
            "Join Geometry node: merges multiple geometry streams into one. "
            "Use when you've generated several separate geo streams (walls, floors, roofs) "
            "and need to output them as a single object. "
            "Also used to combine the original geometry with instanced geometry. "
            "Join Geometry is the node equivalent of Ctrl+J (Join) in Object Mode, but non-destructive."
        ),
    },
    {
        "id": "bl_gn_setpos",
        "app": "blender",
        "topic": "geometry_nodes",
        "text": (
            "Set Position node: overrides the position of each point/vertex in a geometry. "
            "Offset input adds a vector to the existing position (use for displacement effects). "
            "Position input completely replaces the position. "
            "Connect a Noise Texture (or math nodes) to Offset to procedurally displace a surface. "
            "Enable a Selection socket to only move specific points (e.g. only those above a height threshold)."
        ),
    },
    {
        "id": "bl_gn_attr",
        "app": "blender",
        "topic": "geometry_nodes",
        "text": (
            "Store Named Attribute node: saves a calculated value (float, vector, boolean, color) "
            "as a named attribute on the geometry so it can be reused later in the graph "
            "or accessed by a material via the Attribute node. "
            "Example: store a procedural 'dirt' mask as 'dirt_weight' attribute, "
            "then read it in the shader with Attribute > dirt_weight to drive a mix between clean and dirty materials."
        ),
    },

    # ── Color Management: AgX ─────────────────────────────────────────────────
    {
        "id": "bl_agx_01",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "AgX color management (Blender 4.0+, Render Properties > Color Management > View Transform): "
            "AgX replaces Filmic as the default. AgX handles very bright highlights more naturally — "
            "no more orange/magenta blooming on overexposed areas. "
            "Punchy look preset increases contrast and saturation. "
            "Still use Filmic if working on projects started in earlier Blender versions to maintain consistency."
        ),
    },

    # ── Bone Collections ──────────────────────────────────────────────────────
    {
        "id": "bl_bonecoll_01",
        "app": "blender",
        "topic": "rigging",
        "text": (
            "Bone Collections (Blender 4.0+ — replaced old Bone Layers): "
            "in Armature Properties > Bone Collections, create named collections (e.g. FK Controls, IK Controls, Deform). "
            "Assign bones to collections in Pose Mode via Bone Properties > Relations > Collections. "
            "Toggle collection visibility with the eye icon. "
            "This lets animators hide deform bones and only see clean control widgets."
        ),
    },

    # ── Smart UV Project ──────────────────────────────────────────────────────
    {
        "id": "bl_smartuv_01",
        "app": "blender",
        "topic": "uv_mapping",
        "text": (
            "Smart UV Project (U > Smart UV Project in Edit Mode): automatically unwraps the mesh "
            "by splitting it at sharp angles above a set Island Margin. "
            "No seam placement needed. Not ideal for character UVs (many small islands) "
            "but perfect for architectural objects, props, and baking AO where UV layout quality is less critical. "
            "Angle Limit controls where splits occur — lower values = more pieces, more coverage."
        ),
    },

    # ── Follow Active Quads ───────────────────────────────────────────────────
    {
        "id": "bl_followquads_01",
        "app": "blender",
        "topic": "uv_mapping",
        "text": (
            "Follow Active Quads (U > Follow Active Quads): unwraps a grid of quads following the active face's orientation. "
            "Best for regular grid-like surfaces: roads, walls, floors, belts, fabric with a clear weave direction. "
            "Select the grid of faces, make one face active (the one with the correct orientation), "
            "then apply Follow Active Quads. Even Columns/Rows option straightens the UV grid."
        ),
    },

    # ── Firefly Reduction ─────────────────────────────────────────────────────
    {
        "id": "bl_firefly_01",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "Firefly reduction in Cycles: bright single-pixel artefacts ('fireflies') come from light path variance. "
            "Clamp Direct and Clamp Indirect (Render > Light Paths > Clamping): "
            "set both to a value like 4–10 to clip any sample brighter than that threshold. "
            "Lower values remove fireflies but also reduce physical accuracy of bright caustics. "
            "Increasing samples also helps. Using the Denoiser can blend away remaining fireflies post-render."
        ),
    },

    # ── Render Output Settings ────────────────────────────────────────────────
    {
        "id": "bl_renderout_01",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "Render output settings (Output Properties): "
            "Resolution X/Y: set to 1920×1080 (Full HD), 3840×2160 (4K), or any custom size. "
            "Resolution % scales the render for fast previews (50% = quarter of pixels). "
            "Frame Range sets start/end frames for animation. "
            "Frame Rate: 24fps (film), 25fps (PAL), 30fps (NTSC/web), 60fps (game/sports). "
            "File Format: PNG (lossless still), JPEG (compressed still), FFmpeg Video (animation, set codec to H.264)."
        ),
    },

    # ── Mirror Modifier ───────────────────────────────────────────────────────
    {
        "id": "bl_mirror_mod",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Mirror modifier: duplicates the mesh across X, Y, or Z axis, always in sync. "
            "Model only one half — the modifier creates the other half automatically. "
            "Clipping: prevents vertices from crossing the mirror axis — keeps seam closed. "
            "Merge: welds the mirrored seam vertices within the Merge Limit distance. "
            "Apply the modifier only when the mesh is fully finished; until then it stays fully editable and non-destructive."
        ),
    },
    {
        "id": "bl_mirror_mod2",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Mirror modifier workflow: add the Mirror modifier before a Subdivision Surface modifier "
            "in the stack (modifiers apply top-to-bottom). "
            "Enable X axis (and optionally Y for full bilateral symmetry on face models). "
            "If the mesh is off-centre, use 'Mirror Object' — set an Empty at the world origin as the mirror pivot "
            "so the mirror line is exactly at the object's intended centre, not the origin."
        ),
    },

    # ── Decimate Modifier ─────────────────────────────────────────────────────
    {
        "id": "bl_decimate_01",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Decimate modifier: reduces polygon count. "
            "Collapse mode: merges vertices to reach a target Ratio (1.0 = unchanged, 0.1 = 10% of original polys). "
            "Un-Subdivide: reverses subdivision, keeping a cleaner quad topology than Collapse. "
            "Planar: merges faces within an angle threshold — removes unnecessary loops on flat surfaces. "
            "Used to generate LODs (Levels of Detail) for game engines from high-poly sculpts."
        ),
    },

    # ── Array Modifier Deep Dive ──────────────────────────────────────────────
    {
        "id": "bl_array_02",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Array modifier deep dive: Count controls how many copies. "
            "Relative Offset: each copy is offset by a multiple of the object's own dimensions (X=1 = no gap, X=1.1 = 10% gap). "
            "Constant Offset: adds a fixed world-space distance. "
            "Object Offset: positions each copy relative to another object — rotate/move that object to create a circular or curved array. "
            "Merge: welds overlapping vertices between copies. "
            "Stack Array + Curve modifier to distribute copies along a path."
        ),
    },

    # ── Solidify Modifier ─────────────────────────────────────────────────────
    {
        "id": "bl_solidify_02",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Solidify modifier: gives thickness to a flat surface (a plane, shell, or imported CAD surface). "
            "Thickness is the extrusion depth. Offset: -1 extrudes inward, 0 extrudes both ways, +1 outward. "
            "Even Thickness: compensates for curved surfaces so thickness remains uniform around bends. "
            "Fill Rim: caps the open edges with faces. "
            "Material Offset: assigns the rim a different material slot than the main surface."
        ),
    },

    # ── Subdivision Surface Modifier ──────────────────────────────────────────
    {
        "id": "bl_subdiv_02",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Subdivision Surface modifier: subdivides every quad into four, smoothing the mesh. "
            "Levels Viewport: how many subdivisions show in the 3D view (keep at 1–2 to stay interactive). "
            "Levels Render: how many subdivisions at render time (2–3 for most work, 4+ for close-ups). "
            "Catmull-Clark (default): smooths the surface. Simple: subdivides without smoothing (for displacement). "
            "Ctrl+1/2/3 in Object Mode sets the viewport level directly."
        ),
    },

    # ── Shader Nodes: Map Range & Math ────────────────────────────────────────
    {
        "id": "bl_maprange_01",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Map Range node: remaps a value from one input range to a custom output range. "
            "From Min/Max: the input's expected range. To Min/Max: the desired output range. "
            "Example: a Noise Texture outputs 0–1, but you want a roughness value between 0.3 and 0.7 — "
            "set From 0–1, To 0.3–0.7. "
            "Clamp checkbox prevents output exceeding the To range. "
            "Interpolation types include Linear, Stepped, Smoothstep, Smoother Step."
        ),
    },
    {
        "id": "bl_mathnode_01",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Math node: performs arithmetic on scalar values inside shader graphs. "
            "Operations: Add, Subtract, Multiply, Divide, Power, Log, Sqrt, Abs, Min, Max, Round, Modulo, Sine, Cosine, etc. "
            "Use to combine, scale, or offset any value. "
            "Vector Math node does the same for 3D vectors: Add, Subtract, Dot Product, Cross Product, Normalize, Length. "
            "Both nodes are fundamental building blocks for any procedural material."
        ),
    },

    # ── Shader Nodes: More Textures ────────────────────────────────────────────
    {
        "id": "bl_wave_tex",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Wave Texture node: generates sine-wave stripe patterns. "
            "Type: Bands (stripes) or Rings (concentric circles). "
            "Direction: X, Y, Z, or Diagonal for band orientation. "
            "Distortion adds noise to warp the waves (making wood grain with Distortion 2–5 and Bands). "
            "Scale controls stripe frequency; Detail adds extra noise octaves. "
            "Connect to Base Color for stylised patterns, or to Roughness for anisotropic-like variation."
        ),
    },
    {
        "id": "bl_gradient_tex",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Gradient Texture node: outputs a linear, quadratic, diagonal, radial, quadratic sphere, or spherical gradient. "
            "Use with a Texture Coordinate node (Object space) to make a smooth gradient across the object's bounding box. "
            "Classic uses: blend two colours top-to-bottom (sky), create a spherical vignette, "
            "or drive a Mix Shader factor for a material that changes across the object's height."
        ),
    },
    {
        "id": "bl_brick_tex",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Brick Texture node: procedural brick/tile pattern. "
            "Color1/Color2 controls alternate brick colours; Mortar sets the grout colour. "
            "Scale controls brick size. Mortar Size controls joint width. Mortar Smooth softens the edge. "
            "Squash adjusts the brick aspect ratio. "
            "Output 'Color' gives the brick pattern; 'Fac' gives a black/white mask (1 = brick, 0 = mortar) "
            "useful for adding bump only to the brick surface, not the joints."
        ),
    },

    # ── Transparent Background Render ─────────────────────────────────────────
    {
        "id": "bl_transparent_bg",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "Transparent background render: Render Properties > Film > Transparent (enable checkbox). "
            "With this on, the background is rendered as alpha instead of the world colour/HDRI. "
            "Output must be PNG (or EXR) to preserve the alpha channel — JPEG discards alpha. "
            "Use to composite renders over different backgrounds in Photoshop, After Effects, or Figma "
            "without needing to key out the background."
        ),
    },

    # ── Dope Sheet vs Timeline ────────────────────────────────────────────────
    {
        "id": "bl_dopesheet_01",
        "app": "blender",
        "topic": "animation",
        "text": (
            "Timeline vs Dope Sheet: "
            "Timeline — a simple horizontal strip showing current frame, playback controls, and keyframe markers. "
            "Dope Sheet — shows all keyframes for all selected objects as diamond shapes on a grid. "
            "Select and move keyframes in the Dope Sheet to retime animation. "
            "Summary mode shows a single row per object. Action Editor mode (dropdown top-left) shows one action at a time. "
            "Use the Dope Sheet for editing timing; Graph Editor for editing value curves."
        ),
    },

    # ── Named Actions ─────────────────────────────────────────────────────────
    {
        "id": "bl_actions_01",
        "app": "blender",
        "topic": "animation",
        "text": (
            "Named Actions (Action Editor — select from the Dope Sheet header dropdown): "
            "each set of keyframes is an 'Action'. Give it a name (e.g. 'Walk', 'Run', 'Idle'). "
            "Click New to create a fresh action. Click the Browse button to switch between saved actions. "
            "Push actions down to the NLA Editor for blending. "
            "Actions with no NLA users are deleted when Blender closes unless you enable the Fake User (F button)."
        ),
    },

    # ── Blender Unit System ───────────────────────────────────────────────────
    {
        "id": "bl_units_01",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Blender unit system (Scene Properties > Units): "
            "None — Blender units (1 BU = arbitrary). "
            "Metric — real-world metres. Set Length to Metres; Unit Scale 1.0. "
            "Imperial — feet and inches. "
            "For architecture: 1 BU = 1 metre (Unit Scale 1.0). For characters: 1 BU = 1 cm (Unit Scale 0.01). "
            "Correct unit scale matters for physics simulations, lighting intensity, and camera lens calculations."
        ),
    },

    # ── Custom Transform Orientations ─────────────────────────────────────────
    {
        "id": "bl_customori_01",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Custom Transform Orientations: select a face or edge that defines the desired axis, "
            "then in the Transform Orientation dropdown (viewport header, or the '+' in the Transform Orientation panel) "
            "click '+' to create a custom orientation aligned to that selection. "
            "Now you can move/rotate along an angled surface's local axes. "
            "Essential for modelling on angled geometry, like cutting grooves on a bevelled corner."
        ),
    },

    # ── Fill (F Key) ─────────────────────────────────────────────────────────
    {
        "id": "bl_fill_key",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Fill (F key in Edit Mode): context-sensitive face/edge creation. "
            "Two vertices selected: creates an edge between them. "
            "Three or more vertices in a loop: creates a face (N-gon). "
            "An open edge loop: fills it with a face (use Grid Fill for clean quads on circular loops). "
            "Alt+F (Beauty Fill): fills with triangles and tries to create the most even triangulation. "
            "F is the quickest way to manually close holes in a mesh."
        ),
    },

    # ── Lattice Object ────────────────────────────────────────────────────────
    {
        "id": "bl_lattice_01",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Lattice (Add > Lattice): a cage of control points that deforms any object inside it. "
            "Add a Lattice modifier to your mesh and set the Lattice as the Object. "
            "Edit the lattice points (Tab into edit mode on the Lattice) to push/pull the deformed mesh without touching its topology. "
            "Great for package design (bending a box), character squash-and-stretch, or bulk-deforming a complex prop."
        ),
    },

    # ── Hook Modifier ────────────────────────────────────────────────────────
    {
        "id": "bl_hook_01",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Hook modifier: attaches selected vertices to an object (usually an Empty or bone). "
            "Select vertices in Edit Mode, then Ctrl+H > Hook to New Object. "
            "Moving the Empty moves those vertices with it. "
            "Strength controls how tightly the vertices follow the hook (0 = unaffected, 1 = fully controlled). "
            "Use for: attaching cloth corners to control points, driving mesh deformations from rig bones, "
            "or interactive product configurator deformations."
        ),
    },

    # ── Append vs Link ────────────────────────────────────────────────────────
    {
        "id": "bl_append_link",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Append vs Link from external .blend files (File > Append / File > Link): "
            "Append: copies the selected data (object, material, collection) into the current file — "
            "fully independent, edits don't affect the source file. "
            "Link: references the external file — changes to the source update all files that link to it. "
            "Link is the production pipeline standard: update a character rig in one file, "
            "all scene files that link it see the update automatically."
        ),
    },

    # ── Edge Slide ────────────────────────────────────────────────────────────
    {
        "id": "bl_edgeslide_01",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Edge Slide (GG in Edit Mode): slides a selected edge loop along the surrounding faces "
            "without leaving the surface — unlike G which moves freely in space. "
            "Move the mouse to slide 0–1 (or negative). "
            "C while sliding clamps to 0–1 range. Alt+C toggles clamping off for over-sliding. "
            "Even mode (E while sliding) distributes the edges evenly across the face. "
            "Essential for repositioning a support loop without changing the silhouette."
        ),
    },

    # ── Shortest Path Select ──────────────────────────────────────────────────
    {
        "id": "bl_pathselect_01",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Shortest Path Select (Ctrl+click in Edit Mode): selects the shortest path of edges "
            "between the active element and the clicked element. "
            "Works on vertices, edges, and faces. "
            "Topological Distance follows the mesh topology; Geodesic Distance follows surface geometry. "
            "Use to quickly select a stripe of faces across a curved surface for a panel line, "
            "or to select a loop section without manually Shift+clicking every element."
        ),
    },

    # ── Merge Options ────────────────────────────────────────────────────────
    {
        "id": "bl_merge_full",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Merge (M key in Edit Mode) full options: "
            "At Center — merges selected vertices to their average position. "
            "At Cursor — merges to the 3D cursor location. "
            "At First — to the first selected vertex. At Last — to the last. "
            "Collapse — merges each edge independently to its midpoint (useful for collapsing edge loops). "
            "By Distance — same as the Alt+M > By Distance shortcut, welds overlapping verts within a threshold."
        ),
    },

    # ── Edge Loop vs Ring ─────────────────────────────────────────────────────
    {
        "id": "bl_loopring_01",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Edge Loop vs Edge Ring selection: "
            "Alt+click an edge: selects the Edge Loop (follows the edge path around the mesh, perpendicular to polygons). "
            "Ctrl+Alt+click an edge: selects the Edge Ring (parallel edges running through the same row of faces). "
            "Loop is for selecting a continuous band; Ring is for selecting a row of parallel edges across faces. "
            "Converting a Ring to a Loop: select the ring, then Ctrl+E > Edge Loops from Ring."
        ),
    },

    # ── Extrude Along Normals ─────────────────────────────────────────────────
    {
        "id": "bl_extrude_normals",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Extrude Along Normals (Alt+E > Extrude Faces Along Normals, or Shift+Ctrl+N shortcut): "
            "extrudes each selected face along its own normal vector rather than a single global direction. "
            "Essential for adding raised surface detail uniformly on curved surfaces — "
            "buttons on a sphere, scales on a creature, rivets on armour. "
            "Offset Even keeps the extrusion thickness consistent regardless of face angle."
        ),
    },

    # ── Checker Deselect ─────────────────────────────────────────────────────
    {
        "id": "bl_checker_desel",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Checker Deselect (Select > Checker Deselect): alternates the selection across a loop or ring — "
            "selects every other element. "
            "Deselected number and Selected number control the pattern ratio. "
            "Classic use: select an edge loop, apply Checker Deselect, then delete faces to create a grate or grid pattern. "
            "Also useful for adding detail only every N edges on a dense mesh."
        ),
    },

    # ── Select Similar ────────────────────────────────────────────────────────
    {
        "id": "bl_select_similar",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Select Similar (Shift+G in Edit Mode): selects all elements that share a property with the active one. "
            "In Face mode: Coplanar, Material, Area, Sides (triangles, quads, N-gons). "
            "In Edge mode: Length, Direction, Face Angle, Bevel Weight. "
            "In Vertex mode: Vertex Groups, Amount of Connecting Edges. "
            "Threshold controls how similar elements need to be. "
            "Use 'Sides > Triangles' to find and select all tris in a mesh for cleanup."
        ),
    },

    # ── Shader to RGB ─────────────────────────────────────────────────────────
    {
        "id": "bl_shader_to_rgb",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Shader to RGB node (EEVEE only): converts a shader's rendered output into a color value "
            "usable in further math nodes — enabling toon/cel shading. "
            "Connect a Diffuse BSDF into Shader to RGB, then run the Color output through a Color Ramp "
            "with hard posterised steps (3–4 colours) to get a flat cartoon shading look. "
            "Works in EEVEE; Cycles uses Light Path node workarounds for toon shading instead."
        ),
    },

    # ── GN: Distribute Points on Faces ────────────────────────────────────────
    {
        "id": "bl_gn_distrib",
        "app": "blender",
        "topic": "geometry_nodes",
        "text": (
            "Distribute Points on Faces node: scatters points across a mesh surface. "
            "Mode Random: uniform random distribution. Density sets points per square metre. "
            "Mode Poisson Disk: enforces a minimum distance between points (no clumping). "
            "Density Attribute: use a texture or vertex weight to control where points appear — "
            "dense grass in valleys, sparse on hilltops. "
            "Feed the output Points into Instance on Points to scatter objects."
        ),
    },

    # ── GN: Curve ↔ Mesh ─────────────────────────────────────────────────────
    {
        "id": "bl_gn_curve_mesh",
        "app": "blender",
        "topic": "geometry_nodes",
        "text": (
            "Curve to Mesh node: sweeps a profile curve along a path curve to create a 3D surface — "
            "pipes, roads, cables, mouldings. Profile Input: any closed curve shape (circle, rectangle). "
            "Fill Caps: closes the ends. "
            "Mesh to Curve node: converts mesh edges to a curve — extract edges for use in curve nodes. "
            "Resample Curve node: redistributes curve points at a fixed count or spacing — "
            "essential before instancing along a curve for even distribution."
        ),
    },

    # ── Light Groups (Cycles) ─────────────────────────────────────────────────
    {
        "id": "bl_lightgroups_01",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "Light Groups (Cycles, Blender 3.5+): assign lights to named groups in Object Properties > Light Group. "
            "Enable 'Use Light Groups' in View Layer Properties. "
            "Each group renders as a separate pass (LightGroup_Key, LightGroup_Fill, LightGroup_Rim). "
            "In compositing, adjust only the key light's brightness without re-rendering — "
            "a huge time-saver for lighting revisions in production."
        ),
    },

    # ── Character Animation Pipeline ──────────────────────────────────────────
    {
        "id": "bl_anim_pipeline",
        "app": "blender",
        "topic": "animation",
        "text": (
            "Character animation pipeline stages: "
            "1. Blocking — rough poses on key frames (1s, 5s, 10s apart), spaced like stop-motion. Set interpolation to Constant. "
            "2. Rough spline — change to Bezier curves, add in-between poses for major arcs. "
            "3. Refine — work through each body part (hips, spine, arms, face) adding overlap and follow-through. "
            "4. Polish — fine-tune curves in the Graph Editor, add secondary motion (hair, clothing, fingers). "
            "Never go to step 4 before step 2 is approved — polish is wasted on unapproved blocking."
        ),
    },

    # ── A.N.T. Landscape ──────────────────────────────────────────────────────
    {
        "id": "bl_ant_landscape",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "A.N.T. Landscape add-on (built-in, enable in Preferences > Add-ons > Landscape): "
            "Add > Mesh > Landscape generates a procedural terrain mesh. "
            "Noise Type: Perlin, Marble, Wood, etc. Scale, Height, and Offset control terrain shape. "
            "Strata adds rocky layering. Refresh randomises the seed. "
            "Apply a displacement-based material to add micro-detail without increasing base poly count."
        ),
    },

    # ── Sapling Tree Generator ────────────────────────────────────────────────
    {
        "id": "bl_sapling_01",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Sapling Tree Generator (built-in, enable in Preferences > Add-ons > Sapling): "
            "Add > Curve > Sapling Tree Generator creates a procedural tree as Bezier curves. "
            "Levels controls trunk → branch → sub-branch depth. "
            "Length and Radius taper per level. "
            "Leaves: enable and set leaf object (any mesh). "
            "Convert to mesh (Alt+C) after generation. "
            "Animate with wind: add Curve modifier with a Wind force field for swaying branches."
        ),
    },

    # ── Object Visibility ─────────────────────────────────────────────────────
    {
        "id": "bl_visibility_01",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Object visibility controls: H hides selected objects in the viewport (Alt+H shows all). "
            "In the Outliner, each object has three icon toggles: eye (viewport visibility), "
            "cursor (selectability), camera (render visibility). "
            "Click the camera icon to exclude an object from renders while keeping it visible in the viewport. "
            "Disable selectability for background reference objects so you don't accidentally select them."
        ),
    },

    # ── Pose Library (Blender 4+) ─────────────────────────────────────────────
    {
        "id": "bl_pose_lib",
        "app": "blender",
        "topic": "rigging",
        "text": (
            "Pose Library (Blender 4.0+, Asset Library based): in Pose Mode, create a pose, "
            "then mark it as an Asset (Object > Asset > Mark as Asset). "
            "It appears in the Asset Browser as a pose thumbnail. "
            "Drag a pose from the Asset Browser onto the rig to apply it. "
            "Hold Ctrl while dragging to blend the pose at a custom strength (0–100%). "
            "Store full-body poses, hand shapes, and facial expressions as reusable library assets."
        ),
    },

    # ── Rigify Deep Dive ──────────────────────────────────────────────────────
    {
        "id": "bl_rigify_03",
        "app": "blender",
        "topic": "rigging",
        "text": (
            "Rigify advanced setup: after generating a rig, the 'rig_ui.py' script creates bone layer panels. "
            "IK/FK switch: the generated rig includes an IK↔FK slider per limb — "
            "set to IK for posing, FK for follow-through and arcs. "
            "Rigify generates a clean deform skeleton (DEF- bones) separate from control bones — "
            "export only the DEF bones to game engines with the Rigify export add-on. "
            "Refit the meta-rig to match your character before generating."
        ),
    },

    # ── Command Line Rendering ────────────────────────────────────────────────
    {
        "id": "bl_cmdline_render",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "Command line rendering: run Blender headless for batch renders on a server or render farm. "
            "blender -b my_scene.blend -o //output/frame_ -f 1 renders frame 1. "
            "-a renders the entire frame range. "
            "-s 10 -e 50 renders frames 10–50. "
            "-t 0 uses all CPU cores. "
            "Redirect stdout to a log file (blender ... > render.log) to monitor progress remotely. "
            "This is the standard approach for overnight or cloud renders."
        ),
    },

    # ── Object Info Node ──────────────────────────────────────────────────────
    {
        "id": "bl_objinfo_01",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Object Info node: outputs per-object data usable in shaders. "
            "Random — a unique 0–1 float per object instance; feed into a Color Ramp to give each scattered "
            "instance a unique colour without separate materials. "
            "Object Index — an integer set in Object Properties > Relations > Pass Index; "
            "isolate specific objects in compositing with the ID Mask node. "
            "Location — the object's world position; drive material variation by height (snow above Y=2)."
        ),
    },

    # ── Timeline Markers ──────────────────────────────────────────────────────
    {
        "id": "bl_markers_01",
        "app": "blender",
        "topic": "animation",
        "text": (
            "Timeline markers (M key in Timeline or Dope Sheet): adds a named marker at the current frame. "
            "Double-click a marker to rename it — label scene cuts, sync points, or shot names. "
            "Markers appear across all animation editors for cross-editor navigation. "
            "Bind a marker to a camera: select the camera + marker, then Ctrl+B — "
            "the camera activates on that frame. The standard way to cut between cameras in an animated sequence."
        ),
    },

    # ── Render Border ─────────────────────────────────────────────────────────
    {
        "id": "bl_renderborder_01",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "Render Border (Ctrl+B in the 3D Viewport): draw a rectangle to render only that sub-region. "
            "Renders only those pixels — massively faster for testing lighting or shading in one corner. "
            "Enable 'Render Region' in Render Properties to make it stick across sessions. "
            "Ctrl+Alt+B clears the border and returns to full-frame rendering. "
            "Works in both Cycles and EEVEE; also applies to Viewport Render (Ctrl+F12)."
        ),
    },

    # ── Normals Overlay ───────────────────────────────────────────────────────
    {
        "id": "bl_normals_overlay",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Normals overlay (Edit Mode > Overlays > Normals): "
            "displays lines showing which direction each face/vertex normal points. "
            "Face Normals shows one line per face centre; Vertex Normals shows one per vertex. "
            "Size slider controls display length. "
            "Enable Face Orientation (also in Overlays) — blue faces point outward, red faces are flipped. "
            "Fix flipped normals: select all (A) then Mesh > Normals > Recalculate Outside (Shift+N)."
        ),
    },

    # ── Lock Camera to View ───────────────────────────────────────────────────
    {
        "id": "bl_lock_cam",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "Lock Camera to View (N panel > View > Lock Camera to View): "
            "navigating the viewport while in Camera View (Numpad 0) moves the actual camera. "
            "Orbit, pan, and zoom to frame the perfect shot, then disable the lock when finished. "
            "The camera's position and rotation update live — "
            "far more intuitive than transforming the camera object with G/R. "
            "Remember to disable Lock Camera to View before regular viewport navigation."
        ),
    },

    # ── F3 Operator Search ────────────────────────────────────────────────────
    {
        "id": "bl_f3_search",
        "app": "blender",
        "topic": "shortcuts",
        "text": (
            "Operator Search (F3 in Blender keymap, Spacebar in Industry Standard): "
            "search every available Blender operator by name. "
            "Type any partial name — 'loop cut', 'recalculate', 'apply modifier', 'grid fill' — and press Enter. "
            "Recent operators appear at the top for quick repeat access. "
            "The fastest route to any function you can't remember the exact menu location for, "
            "and shows the keyboard shortcut alongside each result."
        ),
    },

    # ── Quick Favourites ──────────────────────────────────────────────────────
    {
        "id": "bl_quick_fav",
        "app": "blender",
        "topic": "shortcuts",
        "text": (
            "Quick Favourites (Q key in any editor): a personal shortcut menu you populate yourself. "
            "Hover any menu item and press Ctrl+U (or right-click > Add to Quick Favourites) to add it. "
            "Press Q to open your menu instantly from anywhere in that editor. "
            "Ideal for operations used constantly but lacking default shortcuts: "
            "Recalculate Normals, Tris to Quads, Smart UV Project, Shade Smooth, Apply All Transforms."
        ),
    },

    # ── Color Attributes / Vertex Colors ──────────────────────────────────────
    {
        "id": "bl_vertcol_01",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Color Attributes (Object Data Properties > Color Attributes): "
            "paint per-vertex or per-face-corner color data directly on the mesh in Vertex Paint mode. "
            "Access in shaders via the Attribute node — enter the color attribute name in the Name field. "
            "Uses: hand-painted foliage color variation, AO approximation, damage/weathering masks, "
            "or stylised flat-color-per-region rendering without UV maps or image textures."
        ),
    },

    # ── Knife Tool ────────────────────────────────────────────────────────────
    {
        "id": "bl_knife_01",
        "app": "blender",
        "topic": "modeling",
        "text": (
            "Knife tool (K in Edit Mode): click to place cut points, click again to extend, Enter to confirm, Esc to cancel. "
            "C snaps the cut angle to 45° increments. "
            "Z cuts through to back faces (not just visible geometry). "
            "Ctrl snaps to edge midpoints. "
            "E starts a new disconnected cut. "
            "Use for adding arbitrary edge loops, cutting specific shapes into a face, "
            "or retopologising by tracing over imported geometry."
        ),
    },

    # ── Depth of Field ────────────────────────────────────────────────────────
    {
        "id": "bl_dof_01",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "Depth of Field (Camera Object Data > Depth of Field): "
            "Focus Object: pick a scene object — the camera stays focused on it as it moves. "
            "Focus Distance: set manually in metres if no focus object. "
            "F-Stop: lower values = shallower depth of field, more bokeh blur (f/1.4 = very blurry, f/11 = sharp). "
            "In Cycles, Aperture Blades sets the bokeh polygon shape (6 = hexagonal bokeh). "
            "In EEVEE, set Bokeh Max Size in the Depth of Field render settings."
        ),
    },

    # ── Camera Focal Length vs Sensor ────────────────────────────────────────
    {
        "id": "bl_camera_lens",
        "app": "blender",
        "topic": "rendering",
        "text": (
            "Camera focal length and sensor size: in Camera Object Data, Focal Length (mm) determines field of view. "
            "24mm = wide angle (architectural, environmental — some perspective distortion). "
            "50mm = natural/neutral (closest to human eye perspective). "
            "85–135mm = telephoto (compressed perspective, flatters portraits, isolates subjects). "
            "Sensor Size affects the crop factor — use Sensor Fit 'Auto' for standard 35mm equivalents. "
            "Shorter focal lengths exaggerate depth; longer ones compress it."
        ),
    },

    # ── GN Group Input/Output ─────────────────────────────────────────────────
    {
        "id": "bl_gn_group_01",
        "app": "blender",
        "topic": "geometry_nodes",
        "text": (
            "Geometry Nodes Group Input/Output: every node tree has Group Input and Group Output nodes. "
            "Drag a socket from Group Input to expose it as a modifier parameter in the Properties panel — "
            "add a Float input named 'Scale' and designers can adjust it without opening the node editor. "
            "Create a reusable node group: select nodes, press Ctrl+G to group them. "
            "Tab enters the group; Tab again exits. The group appears as a single node, reusable anywhere."
        ),
    },

    # ── Particle Hair Children ────────────────────────────────────────────────
    {
        "id": "bl_hair_children",
        "app": "blender",
        "topic": "physics",
        "text": (
            "Particle hair children: in the Children panel of the Particle System, "
            "set Type to Interpolated (smooth children following parent paths) or Simple (radiate from strand roots). "
            "Count sets how many children per parent. "
            "Use 50–200 parents but 10–50 children per parent for dense, realistic fur without "
            "the overhead of 10,000 individual hair strands. "
            "Roughness and Kink add variation and curl to child strands independently of parents."
        ),
    },

    # ── Data Transfer Modifier ────────────────────────────────────────────────
    {
        "id": "bl_datatransfer_01",
        "app": "blender",
        "topic": "modifiers",
        "text": (
            "Data Transfer modifier: copies mesh data from a source object to the active object. "
            "Face Corner Data > Custom Normals: copies sharp/smooth normal data — "
            "fix shading artefacts on a retopologised mesh by transferring normals from the high-poly original. "
            "UV Maps: transfer UV layout from one mesh to another with matching geometry. "
            "Vertex Groups: propagate weight data from a reference mesh. "
            "Enable 'Apply on Spline' for curves. Click Generate Data Layers to initialise target data."
        ),
    },

    # ── Toon Outline Trick ────────────────────────────────────────────────────
    {
        "id": "bl_toon_outline",
        "app": "blender",
        "topic": "materials",
        "text": (
            "Cel-shaded outline with Solidify modifier: add a Solidify modifier to the character mesh. "
            "Set Thickness to a small negative value (e.g. -0.02). Enable 'Flip Normals'. "
            "Assign a pure black material to the 'Shell' material slot. "
            "The inside-out shell appears as a black outline around the character from any camera angle. "
            "Works in both EEVEE and Cycles without Freestyle — extremely lightweight outline method."
        ),
    },
]
