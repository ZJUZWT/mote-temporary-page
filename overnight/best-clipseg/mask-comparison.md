# Mask Comparison

Higher IoU is better. The diff panel uses white for overlap, red for
hand-only pixels, and blue for AI-only pixels.

Contact sheet: `assets/generated/light-mask-demo/overnight/best-clipseg/mask-contact-sheet.png`

| Mask | IoU | Precision | Recall | Hand px | AI px |
|---|---:|---:|---:|---:|---:|
| terminal | 0.6651 | 0.8332 | 0.7672 | 104478 | 96202 |
| window | 0.6649 | 0.7045 | 0.9221 | 55520 | 72665 |
| status_lamps | 0.0000 | 0.0000 | 0.0000 | 536 | 4500 |
