from __future__ import annotations

import argparse
from pathlib import Path

import torch
from PIL import Image
from transformers import CLIPSegForImageSegmentation, CLIPSegProcessor


def normalize_mask(logits: torch.Tensor, threshold: float) -> Image.Image:
    values = torch.sigmoid(logits).detach().cpu()
    values = (values - values.min()) / (values.max() - values.min() + 1e-6)
    mask = (values > threshold).to(torch.uint8) * 255
    return Image.fromarray(mask.numpy(), mode="L")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--threshold", type=float, default=0.55)
    args = parser.parse_args()

    image = Image.open(args.input).convert("RGB")
    prompts = {
        "ai-terminal-screen-mask.png": "glowing computer screen and terminal monitor",
        "ai-round-window-mask.png": "round window with bright outside light",
        "ai-small-lights-mask.png": "small status lamps and indicator lights",
    }

    processor = CLIPSegProcessor.from_pretrained("CIDAS/clipseg-rd64-refined")
    model = CLIPSegForImageSegmentation.from_pretrained("CIDAS/clipseg-rd64-refined")
    model.eval()

    output_dir = Path(args.out)
    output_dir.mkdir(parents=True, exist_ok=True)

    texts = list(prompts.values())
    inputs = processor(text=texts, images=[image] * len(texts), return_tensors="pt", padding=True)

    with torch.inference_mode():
        outputs = model(**inputs)

    for filename, logits in zip(prompts.keys(), outputs.logits):
        mask = normalize_mask(logits, args.threshold)
        mask = mask.resize(image.size, Image.Resampling.BILINEAR)
        mask.save(output_dir / filename)
        print(output_dir / filename)


if __name__ == "__main__":
    main()
