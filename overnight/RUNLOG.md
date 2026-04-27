# Overnight Light Mask Runlog

Stop by: 2026-04-26 10:00 Asia/Shanghai.

## 2026-04-26 01:15 CST - Startup Check

- project_entry_file: `AGENTS.md`
- roadmap_lane: `tools` + `assets`
- boundaries: no commit, no push, no curated `assets/` writes
- hook evidence: `.agent/hook-events.jsonl` contains nearby automatic `SessionStart`
  rows; caveat is that no pre-session baseline row was captured.
- context read:
  - `docs/process/overnight-image-optimization-handoff.md`
  - `docs/roadmap/current-state.md`
  - `docs/roadmap/loss-register.md`
  - `tools/imagery/mote-comfy-client/docs/LIGHTMAP_SEGMENTATION_CN.md`
  - `docs/knowledge/tools/best-practices.md`
  - `docs/knowledge/tools/quality-fixes.md`
  - `docs/knowledge/infra/reflection-loop.md`

## 2026-04-26 01:16 CST - Baseline Harness

Command:

```bash
python3 scripts/compare_masks.py --out assets/generated/light-mask-demo/overnight/baseline
```

Output path:

- `assets/generated/light-mask-demo/overnight/baseline/`
- contact sheet:
  `assets/generated/light-mask-demo/overnight/baseline/mask-contact-sheet.png`

Metrics:

| Mask | IoU | Precision | Recall | Judgment |
|---|---:|---:|---:|---|
| terminal | 0.6504 | 0.8567 | 0.7298 | keep as baseline |
| window | 0.6621 | 0.7211 | 0.8901 | keep as baseline |
| status_lamps | 0.0000 | 0.0000 | 0.0000 | reject |

Note: handoff command used `python`; local shell has only `python3`.

## 2026-04-26 01:20 CST - CLIPSeg Cache Repair

Observed blocker:

- `CIDAS/clipseg-rd64-refined` cache existed but model weights were incomplete.
- Cache size was about 1.5 MB.
- `model.safetensors` blob was present only as a 0B `.incomplete` file.
- Running the existing CLIPSeg script stalled without growing the incomplete
  file.

Repair:

```bash
HF_HUB_DISABLE_XET=1 hf download CIDAS/clipseg-rd64-refined model.safetensors --cache-dir ~/.cache/huggingface/hub
```

Result:

- downloaded `model.safetensors` into the Hugging Face cache
- subsequent CLIPSeg load succeeded with `local_files_only=True`

Judgment: keep. This makes the CLIPSeg baseline repeatable on this Mac.

## 2026-04-26 01:26 CST - CLIPSeg Threshold Sweep

Model:

- `CIDAS/clipseg-rd64-refined`
- local cache only after repair

Prompts:

- terminal: `glowing computer screen and terminal monitor`
- window: `round window with bright outside light`
- status_lamps: `small status lamps and indicator lights`

Outputs:

- `assets/generated/light-mask-demo/overnight/clipseg/thr-0.45/`
- `assets/generated/light-mask-demo/overnight/clipseg/thr-0.50/`
- `assets/generated/light-mask-demo/overnight/clipseg/thr-0.55/`
- `assets/generated/light-mask-demo/overnight/clipseg/thr-0.60/`
- `assets/generated/light-mask-demo/overnight/clipseg/thr-0.65/`

Each threshold directory contains:

- `masks/`
- `compare/mask-comparison.csv`
- `compare/mask-comparison.md`
- `compare/mask-contact-sheet.png`

Metrics:

| Threshold | Mask | IoU | Precision | Recall | Judgment |
|---:|---|---:|---:|---:|---|
| 0.45 | terminal | 0.6651 | 0.8332 | 0.7672 | keep |
| 0.45 | window | 0.6517 | 0.6848 | 0.9309 | retry |
| 0.45 | status_lamps | 0.0000 | 0.0000 | 0.0000 | reject |
| 0.50 | terminal | 0.6599 | 0.8460 | 0.7500 | retry |
| 0.50 | window | 0.6649 | 0.7045 | 0.9221 | keep |
| 0.50 | status_lamps | 0.0000 | 0.0000 | 0.0000 | reject |
| 0.55 | terminal | 0.6504 | 0.8567 | 0.7298 | baseline |
| 0.55 | window | 0.6621 | 0.7211 | 0.8901 | baseline |
| 0.55 | status_lamps | 0.0000 | 0.0000 | 0.0000 | reject |
| 0.60 | terminal | 0.6402 | 0.8666 | 0.7101 | reject |
| 0.60 | window | 0.6367 | 0.7332 | 0.8287 | reject |
| 0.60 | status_lamps | 0.0000 | 0.0000 | 0.0000 | reject |
| 0.65 | terminal | 0.6268 | 0.8806 | 0.6851 | reject |
| 0.65 | window | 0.5436 | 0.7277 | 0.6825 | reject |
| 0.65 | status_lamps | 0.0000 | 0.0000 | 0.0000 | reject |

Current best:

- terminal: threshold 0.45, IoU 0.6651
- window: threshold 0.50, IoU 0.6649
- status_lamps: no useful CLIPSeg result

Judgment: CLIPSeg is keep for rough large emitters, reject for tiny status
lamps, and not sufficient for receiver `influence_map` generation.

## 2026-04-26 01:28 CST - Best CLIPSeg Composite

Command:

```bash
python3 scripts/compare_masks.py --out assets/generated/light-mask-demo/overnight/best-clipseg --case terminal=masks/terminal-mask.png=overnight/clipseg/thr-0.45/masks/ai-terminal-screen-mask.png --case window=masks/window-mask.png=overnight/clipseg/thr-0.50/masks/ai-round-window-mask.png --case status_lamps=masks/status-lamps.png=overnight/clipseg/thr-0.45/masks/ai-small-lights-mask.png
```

Output path:

- `assets/generated/light-mask-demo/overnight/best-clipseg/`
- contact sheet:
  `assets/generated/light-mask-demo/overnight/best-clipseg/mask-contact-sheet.png`

Metrics:

| Mask | IoU | Precision | Recall | Judgment |
|---|---:|---:|---:|---|
| terminal | 0.6651 | 0.8332 | 0.7672 | keep |
| window | 0.6649 | 0.7045 | 0.9221 | keep |
| status_lamps | 0.0000 | 0.0000 | 0.0000 | reject |

Judgment: best current CLIPSeg review surface. It improves terminal slightly
over baseline and window slightly over baseline, but does not reduce the tiny
emitter loss.

## 2026-04-26 01:28 CST - Status Lamp Prompt Sweep

Model:

- `CIDAS/clipseg-rd64-refined`
- local cache only

Prompts tested:

- `small status lamps and indicator lights`
- `small white indicator lights`
- `tiny glowing lamps`
- `small circular light sources`
- `bright dots and indicator lamps`
- `little glowing bulbs on machinery`

Thresholds:

- 0.35
- 0.45
- 0.55
- 0.65

Output path:

- `assets/generated/light-mask-demo/overnight/clipseg-status-prompt-sweep/`

Best observed result:

- prompt: `tiny glowing lamps`
- threshold: 0.35
- mask:
  `assets/generated/light-mask-demo/overnight/clipseg-status-prompt-sweep/tiny-glowing-lamps/thr-0.35/masks/ai-small-lights-mask.png`
- contact sheet:
  `assets/generated/light-mask-demo/overnight/clipseg-status-prompt-sweep/tiny-glowing-lamps/thr-0.35/compare/mask-contact-sheet.png`
- IoU: 0.0090
- precision: 0.0090
- recall: 0.9496

Judgment: reject. The high recall comes from a very broad false-positive mask,
not useful tiny emitter localization. CLIPSeg prompt tuning does not repair
status lamps.

## 2026-04-26 01:29 CST - Large Emitter Prompt Sweep

Model:

- `CIDAS/clipseg-rd64-refined`
- local cache only

Targets:

- terminal
- window

Thresholds:

- 0.35 through 0.70 in 0.05 steps

Output path:

- `assets/generated/light-mask-demo/overnight/clipseg-large-emitter-sweep/`

Best terminal result:

- prompt: `computer terminal screen`
- threshold: 0.35
- mask:
  `assets/generated/light-mask-demo/overnight/clipseg-large-emitter-sweep/terminal/computer-terminal-screen/thr-0.35/masks/ai-terminal-screen-mask.png`
- contact sheet:
  `assets/generated/light-mask-demo/overnight/clipseg-large-emitter-sweep/terminal/computer-terminal-screen/thr-0.35/compare/mask-contact-sheet.png`
- IoU: 0.6826
- precision: 0.8049
- recall: 0.8180
- judgment: keep

Best window result:

- prompt: `large circular window on the right`
- threshold: 0.60
- mask:
  `assets/generated/light-mask-demo/overnight/clipseg-large-emitter-sweep/window/large-circular-window-on-the-right/thr-0.60/masks/ai-round-window-mask.png`
- contact sheet:
  `assets/generated/light-mask-demo/overnight/clipseg-large-emitter-sweep/window/large-circular-window-on-the-right/thr-0.60/compare/mask-contact-sheet.png`
- IoU: 0.6897
- precision: 0.7038
- recall: 0.9718
- judgment: keep

Best combined review surface:

- `assets/generated/light-mask-demo/overnight/best-clipseg-large-emitters/`
- contact sheet:
  `assets/generated/light-mask-demo/overnight/best-clipseg-large-emitters/mask-contact-sheet.png`

Combined metrics:

| Mask | IoU | Precision | Recall | Judgment |
|---|---:|---:|---:|---|
| terminal | 0.6826 | 0.8049 | 0.8180 | keep |
| window | 0.6897 | 0.7038 | 0.9718 | keep |
| status_lamps | 0.0090 | 0.0090 | 0.9496 | reject |

Judgment: keep for large emitter segmentation. This beats the original
baseline for terminal and window, but it confirms CLIPSeg is the wrong tool for
tiny status lamps.

## 2026-04-26 01:30 CST - Alternative Model/GPU Check

Local Python dependencies:

- `sam2`: missing
- `segment_anything`: missing
- `groundingdino`: missing
- `timm`: missing
- `accelerate`: available

Hugging Face cache:

- no Florence, GroundingDINO, SAM, or SAM2 cache found

ComfyUI:

- API reachable at `http://192.168.1.4:8188`
- device: NVIDIA GeForce RTX 4080
- segmentation-related node search found background-removal nodes, but no
  Florence, GroundingDINO, CLIPSeg, SAM, or SAM2 node.

Judgment: do not start a Florence/GroundingDINO/SAM2 path tonight without a
clearer dependency plan. It would require new installs and model downloads,
while the current highest-value result is already a repeatable CLIPSeg baseline
for large emitters.

## 2026-04-26 01:32 CST - CLIPSeg Postprocess Sweep

Inputs:

- terminal:
  `assets/generated/light-mask-demo/overnight/clipseg-large-emitter-sweep/terminal/computer-terminal-screen/thr-0.35/masks/ai-terminal-screen-mask.png`
- window:
  `assets/generated/light-mask-demo/overnight/clipseg-large-emitter-sweep/window/large-circular-window-on-the-right/thr-0.60/masks/ai-round-window-mask.png`

Operations tested:

- raw
- erosion/dilation/opening/closing, 1-3 iterations
- keep largest connected components
- fill holes
- fill holes then erosion
- open then close

Output path:

- `assets/generated/light-mask-demo/overnight/clipseg-postprocess-sweep/`

Best terminal postprocess:

- operation: `fill-then-erosion-2`
- mask:
  `assets/generated/light-mask-demo/overnight/clipseg-postprocess-sweep/terminal/fill-then-erosion-2/masks/ai-terminal-screen-mask.png`
- contact sheet:
  `assets/generated/light-mask-demo/overnight/clipseg-postprocess-sweep/terminal/fill-then-erosion-2/compare/mask-contact-sheet.png`
- IoU: 0.6907
- precision: 0.8214
- recall: 0.8128
- judgment: keep

Best window postprocess:

- operation: `fill-then-erosion-2`
- mask:
  `assets/generated/light-mask-demo/overnight/clipseg-postprocess-sweep/window/fill-then-erosion-2/masks/ai-round-window-mask.png`
- contact sheet:
  `assets/generated/light-mask-demo/overnight/clipseg-postprocess-sweep/window/fill-then-erosion-2/compare/mask-contact-sheet.png`
- IoU: 0.7315
- precision: 0.7329
- recall: 0.9976
- judgment: keep

Best combined postprocessed review surface:

- `assets/generated/light-mask-demo/overnight/best-clipseg-postprocessed/`
- contact sheet:
  `assets/generated/light-mask-demo/overnight/best-clipseg-postprocessed/mask-contact-sheet.png`

Combined metrics:

| Mask | IoU | Precision | Recall | Judgment |
|---|---:|---:|---:|---|
| terminal | 0.6907 | 0.8214 | 0.8128 | keep |
| window | 0.7315 | 0.7329 | 0.9976 | keep |
| status_lamps | 0.0090 | 0.0090 | 0.9496 | reject |

Judgment: keep for large emitters. The postprocess is simple and repeatable:
fill holes, then erode twice. It should not be used for tiny status lamps.

## 2026-04-26 01:34 CST - Fine Postprocess Sweep

Purpose:

- confirm the best large-emitter parameters with a finer grid
- keep the model path fixed and vary only threshold plus fill/erosion

Fixed prompts:

- terminal: `computer terminal screen`
- window: `large circular window on the right`

Output path:

- `assets/generated/light-mask-demo/overnight/clipseg-fine-postprocess-sweep/`

Best terminal result:

- threshold: 0.325
- operation: `fill-then-erosion-3`
- mask:
  `assets/generated/light-mask-demo/overnight/clipseg-fine-postprocess-sweep/terminal/thr-0.325/fill-then-erosion-3/masks/ai-terminal-screen-mask.png`
- contact sheet:
  `assets/generated/light-mask-demo/overnight/clipseg-fine-postprocess-sweep/terminal/thr-0.325/fill-then-erosion-3/compare/mask-contact-sheet.png`
- IoU: 0.6999
- precision: 0.8671
- recall: 0.7840
- judgment: keep

Best window result:

- threshold: 0.600
- operation: `fill-then-erosion-6`
- mask:
  `assets/generated/light-mask-demo/overnight/clipseg-fine-postprocess-sweep/window/thr-0.600/fill-then-erosion-6/masks/ai-round-window-mask.png`
- contact sheet:
  `assets/generated/light-mask-demo/overnight/clipseg-fine-postprocess-sweep/window/thr-0.600/fill-then-erosion-6/compare/mask-contact-sheet.png`
- IoU: 0.8626
- precision: 0.9098
- recall: 0.9433
- judgment: keep

Best combined fine review surface:

- `assets/generated/light-mask-demo/overnight/best-clipseg-fine-postprocessed/`
- contact sheet:
  `assets/generated/light-mask-demo/overnight/best-clipseg-fine-postprocessed/mask-contact-sheet.png`

Combined metrics:

| Mask | IoU | Precision | Recall | Judgment |
|---|---:|---:|---:|---|
| terminal | 0.6999 | 0.8671 | 0.7840 | keep |
| window | 0.8626 | 0.9098 | 0.9433 | keep |
| status_lamps | 0.0090 | 0.0090 | 0.9496 | reject |

Judgment: keep. This is the strongest result so far for large emitter masks.
The status lamp result remains rejected and should not be promoted.
