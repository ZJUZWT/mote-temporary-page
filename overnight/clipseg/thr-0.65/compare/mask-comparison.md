# Mask Comparison

Higher IoU is better. The diff panel uses white for overlap, red for
hand-only pixels, and blue for AI-only pixels.

Contact sheet: `/Users/swannzhang/Workspace/AIProjects/TheMoteInTheDust/tools/imagery/mote-comfy-client/assets/generated/light-mask-demo/overnight/clipseg/thr-0.65/compare/mask-contact-sheet.png`

| Mask | IoU | Precision | Recall | Hand px | AI px |
|---|---:|---:|---:|---:|---:|
| terminal | 0.6268 | 0.8806 | 0.6851 | 104478 | 81282 |
| window | 0.5436 | 0.7277 | 0.6825 | 55520 | 52070 |
| status_lamps | 0.0000 | 0.0000 | 0.0000 | 536 | 1944 |
