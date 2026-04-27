# Mask Comparison

Higher IoU is better. The diff panel uses white for overlap, red for
hand-only pixels, and blue for AI-only pixels.

Contact sheet: `/Users/swannzhang/Workspace/AIProjects/TheMoteInTheDust/tools/imagery/mote-comfy-client/assets/generated/light-mask-demo/overnight/clipseg/thr-0.60/compare/mask-contact-sheet.png`

| Mask | IoU | Precision | Recall | Hand px | AI px |
|---|---:|---:|---:|---:|---:|
| terminal | 0.6402 | 0.8666 | 0.7101 | 104478 | 85614 |
| window | 0.6367 | 0.7332 | 0.8287 | 55520 | 62746 |
| status_lamps | 0.0000 | 0.0000 | 0.0000 | 536 | 2441 |
