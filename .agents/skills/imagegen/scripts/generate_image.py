#!/usr/bin/env python3

import argparse
import base64
import os
from pathlib import Path

from openai import OpenAI


SUPPORTED_SIZES = {
    "1024x1024",
    "1024x1536",
    "1536x1024",
    "auto",
}


def normalize_size(size: str) -> str:
    """
    Some APIs only support a limited size set.
    Keep the script stable by mapping unsupported requested ratios
    to the closest supported size.
    """
    aliases = {
        "1:1": "1024x1024",
        "square": "1024x1024",

        "2:3": "1024x1536",
        "portrait": "1024x1536",
        "vertical": "1024x1536",
        "9:16": "1024x1536",

        "3:2": "1536x1024",
        "landscape": "1536x1024",
        "horizontal": "1536x1024",
        "16:9": "1536x1024",
        "youtube": "1536x1024",
        "thumbnail": "1536x1024",
    }

    normalized = aliases.get(size.lower(), size)

    if normalized not in SUPPORTED_SIZES:
        print(f"Warning: unsupported size '{size}', using 'auto' instead.")
        return "auto"

    return normalized


def main():
    parser = argparse.ArgumentParser(
        description="Generate an image with the OpenAI image generation API."
    )

    parser.add_argument(
        "--prompt",
        required=True,
        help="Image prompt.",
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Output image path, e.g. generated/image_001.png.",
    )

    parser.add_argument(
        "--size",
        default="1024x1536",
        help="Image size or ratio. Examples: 1024x1024, 1024x1536, 1536x1024, 1:1, 2:3, 9:16, 16:9.",
    )

    parser.add_argument(
        "--quality",
        default="high",
        choices=["low", "medium", "high", "auto"],
        help="Image quality. Default: high.",
    )

    parser.add_argument(
        "--background",
        default="auto",
        choices=["auto", "opaque", "transparent"],
        help="Background type. Default: auto.",
    )

    parser.add_argument(
        "--model",
        default="gpt-5",
        help="Main Responses API model.",
    )

    args = parser.parse_args()

    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Add it as an environment variable or secret. "
            "Do not paste the API key directly into this repository."
        )

    size = normalize_size(args.size)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    client = OpenAI()

    response = client.responses.create(
        model=args.model,
        input=args.prompt,
        tools=[
            {
                "type": "image_generation",
                "size": size,
                "quality": args.quality,
                "background": args.background,
            }
        ],
        tool_choice={"type": "image_generation"},
    )

    image_b64 = None

    for item in response.output:
        if item.type == "image_generation_call":
            image_b64 = item.result
            break

    if not image_b64:
        raise RuntimeError("No image was generated.")

    output_path.write_bytes(base64.b64decode(image_b64))

    print(f"Saved image: {output_path}")
    print(f"Size used: {size}")
    print(f"Quality used: {args.quality}")


if __name__ == "__main__":
    main()
