# Mask Comparison

Higher IoU is better. The diff panel uses white for overlap, red for
hand-only pixels, and blue for AI-only pixels.

Contact sheet: `assets/generated/light-mask-demo/grounded-sam2-large/compare/mask-contact-sheet.png`

| Mask | IoU | Precision | Recall | Hand px | AI px |
|---|---:|---:|---:|---:|---:|
| terminal | 0.4661 | 0.9093 | 0.4888 | 104478 | 56157 |
| window | 0.5934 | 0.5934 | 1.0000 | 55520 | 93567 |
| status_lamps | 0.0000 | 0.0000 | 0.0000 | 536 | 9729 |
