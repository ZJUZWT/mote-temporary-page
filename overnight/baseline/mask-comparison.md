# Mask Comparison

Higher IoU is better. The diff panel uses white for overlap, red for
hand-only pixels, and blue for AI-only pixels.

Contact sheet: `assets/generated/light-mask-demo/overnight/baseline/mask-contact-sheet.png`

| Mask | IoU | Precision | Recall | Hand px | AI px |
|---|---:|---:|---:|---:|---:|
| terminal | 0.6504 | 0.8567 | 0.7298 | 104478 | 89002 |
| window | 0.6621 | 0.7211 | 0.8901 | 55520 | 68526 |
| status_lamps | 0.0000 | 0.0000 | 0.0000 | 536 | 3027 |
