# Mask Comparison

Higher IoU is better. The diff panel uses white for overlap, red for
hand-only pixels, and blue for AI-only pixels.

Contact sheet: `assets/generated/light-mask-demo/overnight/best-clipseg-fine-postprocessed/mask-contact-sheet.png`

| Mask | IoU | Precision | Recall | Hand px | AI px |
|---|---:|---:|---:|---:|---:|
| terminal | 0.6999 | 0.8671 | 0.7840 | 104478 | 94460 |
| window | 0.8626 | 0.9098 | 0.9433 | 55520 | 57566 |
| status_lamps | 0.0090 | 0.0090 | 0.9496 | 536 | 56838 |
