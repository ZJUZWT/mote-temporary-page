# Mask Comparison

Higher IoU is better. The diff panel uses white for overlap, red for
hand-only pixels, and blue for AI-only pixels.

Contact sheet: `/Users/swannzhang/Workspace/AIProjects/TheMoteInTheDust/tools/imagery/mote-comfy-client/assets/generated/light-mask-demo/overnight/clipseg/thr-0.50/compare/mask-contact-sheet.png`

| Mask | IoU | Precision | Recall | Hand px | AI px |
|---|---:|---:|---:|---:|---:|
| terminal | 0.6599 | 0.8460 | 0.7500 | 104478 | 92617 |
| window | 0.6649 | 0.7045 | 0.9221 | 55520 | 72665 |
| status_lamps | 0.0000 | 0.0000 | 0.0000 | 536 | 3738 |
