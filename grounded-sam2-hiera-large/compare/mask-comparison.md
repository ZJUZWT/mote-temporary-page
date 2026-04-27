# Mask Comparison

Higher IoU is better. The diff panel uses white for overlap, red for
hand-only pixels, and blue for AI-only pixels.

Contact sheet: `assets/generated/light-mask-demo/grounded-sam2-hiera-large/compare/mask-contact-sheet.png`

| Mask | IoU | Precision | Recall | Hand px | AI px |
|---|---:|---:|---:|---:|---:|
| terminal | 0.4850 | 0.8535 | 0.5290 | 104478 | 64758 |
| window | 0.5454 | 0.5454 | 1.0000 | 55520 | 101804 |
| status_lamps | 0.0000 | 0.0000 | 0.0000 | 536 | 13353 |
