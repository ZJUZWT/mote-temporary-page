# Mask Comparison

Higher IoU is better. The diff panel uses white for overlap, red for
hand-only pixels, and blue for AI-only pixels.

Contact sheet: `assets/generated/light-mask-demo/overnight/best-clipseg-large-emitters/mask-contact-sheet.png`

| Mask | IoU | Precision | Recall | Hand px | AI px |
|---|---:|---:|---:|---:|---:|
| terminal | 0.6826 | 0.8049 | 0.8180 | 104478 | 106181 |
| window | 0.6897 | 0.7038 | 0.9718 | 55520 | 76654 |
| status_lamps | 0.0090 | 0.0090 | 0.9496 | 536 | 56838 |
