# Lightmap Demo

This generated experiment tests whether a still image can become a low-frame,
web-driven scene through masks and influence maps.

## Open

From the super-repo root:

```bash
python3 -m http.server 8765 --directory tools/imagery/mote-comfy-client/assets/generated/light-mask-demo
```

Then open:

```text
http://127.0.0.1:8765/index.html
```

Direct map views also work:

```text
http://127.0.0.1:8765/index.html?view=window
http://127.0.0.1:8765/index.html?view=monitor
```

## What To Check

- `window map`: the round exterior light affects the window, floor patch,
  ceiling bounce, and right wall.
- `monitor map`: the display mostly affects the screen, desk, and nearby wall.
- `lamp map`: small status lights stay local.
- `shadow map`: ambient occlusion darkens corners and the underside of the
  desk.
- `final`: the canvas recomposes the base image with those weights every frame.
- `final lighting -> draft lightmaps from masks`: the canvas uses derived
  per-light influence maps, so mask-derived lightmaps feed the final result
  instead of only appearing as review layers.
- `2x2 layers -> Lightmaps`: the top-left final remains animated while the
  other cells show per-light influence maps and a packed RGB lightmap preview.
- `2x2 layers -> Object Masks`: review object masks for interaction and
  highlight boundaries, separate from light influence.

## Model

The experiment separates four concepts:

1. `semantic_mask`: the object or surface itself.
2. `emitter_mask`: the visible source of light.
3. `influence_map`: the receiving pixels affected by that source.
4. `runtime_weight`: the current intensity used by the web renderer.

Segmentation can help with the first two. The third needs scene reasoning,
manual paint, or a constrained AI-assisted pass.

## Draft Lightmap Test

Regenerate the current low-cost lightmaps from AI object/emitter masks:

```bash
cd tools/imagery/mote-comfy-client
python scripts/generate_draft_lightmaps.py --demo-dir assets/generated/light-mask-demo
```

Outputs live in:

```text
assets/generated/light-mask-demo/draft-lightmaps/
```

This is not a G-buffer renderer. It is a recheckable bridge between
`emitter_mask` and `lightmap`: masks locate light sources, and explicit receiver
rules produce per-light influence maps. A real G-buffer route would use depth,
normal, albedo/material, and object IDs to compute lighting instead of storing
per-light influence directly.
