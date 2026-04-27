# Mask Comparison

Higher IoU is better. The diff panel uses white for overlap, red for
hand-only pixels, and blue for AI-only pixels.

Contact sheet: `assets/generated/light-mask-demo/grounded-sam2-large-largest/compare/mask-contact-sheet.png`

| Mask | IoU | Precision | Recall | Hand px | AI px |
|---|---:|---:|---:|---:|---:|
| terminal | 0.4809 | 0.8898 | 0.5114 | 104478 | 60049 |
| window | 0.5934 | 0.5934 | 1.0000 | 55520 | 93567 |
| status_lamps | 0.0000 | 0.0000 | 0.0000 | 536 | 12504 |
