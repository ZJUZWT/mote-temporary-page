# Mask Comparison

Higher IoU is better. The diff panel uses white for overlap, red for
hand-only pixels, and blue for AI-only pixels.

Contact sheet: `assets/generated/light-mask-demo/grounded-sam2-prompt-sweep/compare/mask-contact-sheet.png`

| Mask | IoU | Precision | Recall | Hand px | AI px |
|---|---:|---:|---:|---:|---:|
| terminal_monitor | 0.4874 | 0.8772 | 0.5232 | 104478 | 62313 |
| terminal_panel | 0.5007 | 0.8589 | 0.5456 | 104478 | 66373 |
| terminal_screen | 0.4814 | 0.8945 | 0.5104 | 104478 | 59616 |
| window_porthole | 0.5344 | 0.5344 | 1.0000 | 55520 | 103894 |
| window_bright | 0.6244 | 0.6244 | 1.0000 | 55520 | 88911 |
| window_opening | 0.5391 | 0.5391 | 1.0000 | 55520 | 102992 |
