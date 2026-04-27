# Mask Comparison

Higher IoU is better. The diff panel uses white for overlap, red for
hand-only pixels, and blue for AI-only pixels.

Contact sheet: `/Users/swannzhang/Workspace/AIProjects/TheMoteInTheDust/tools/imagery/mote-comfy-client/assets/generated/light-mask-demo/overnight/clipseg/thr-0.45/compare/mask-contact-sheet.png`

| Mask | IoU | Precision | Recall | Hand px | AI px |
|---|---:|---:|---:|---:|---:|
| terminal | 0.6651 | 0.8332 | 0.7672 | 104478 | 96202 |
| window | 0.6517 | 0.6848 | 0.9309 | 55520 | 75464 |
| status_lamps | 0.0000 | 0.0000 | 0.0000 | 536 | 4500 |
