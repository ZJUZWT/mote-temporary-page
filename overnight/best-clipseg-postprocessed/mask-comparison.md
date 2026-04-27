# Mask Comparison

Higher IoU is better. The diff panel uses white for overlap, red for
hand-only pixels, and blue for AI-only pixels.

Contact sheet: `assets/generated/light-mask-demo/overnight/best-clipseg-postprocessed/mask-contact-sheet.png`

| Mask | IoU | Precision | Recall | Hand px | AI px |
|---|---:|---:|---:|---:|---:|
| terminal | 0.6907 | 0.8214 | 0.8128 | 104478 | 103374 |
| window | 0.7315 | 0.7329 | 0.9976 | 55520 | 75573 |
| status_lamps | 0.0090 | 0.0090 | 0.9496 | 536 | 56838 |
