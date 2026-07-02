#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Overlay exact text on an image with a solid/translucent backing box.

Use this when generated slide images contain wrong Chinese glyphs, incorrect
labels, or page-number issues but the rest of the slide is visually acceptable.
"""

from __future__ import annotations

import argparse
import os
import platform
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WINDOWS_FONT_CANDIDATES = [
    r"C:\Windows\Fonts\msyhbd.ttc",
    r"C:\Windows\Fonts\msyh.ttc",
    r"C:\Windows\Fonts\simhei.ttf",
    r"C:\Windows\Fonts\simsun.ttc",
    r"C:\Windows\Fonts\arialuni.ttf",
]

MAC_FONT_CANDIDATES = [
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/STHeiti Light.ttc",
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/Library/Fonts/Arial Unicode.ttf",
    "/Library/Fonts/NotoSansCJK-Regular.ttc",
    "/Library/Fonts/Noto Sans CJK SC.ttc",
]

LINUX_FONT_CANDIDATES = [
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
    "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/noto/NotoSansSC-Regular.otf",
    "/usr/share/fonts/truetype/arphic/uming.ttc",
    "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]


def parse_box(value: str) -> tuple[int, int, int, int]:
    parts = [int(p.strip()) for p in value.split(",")]
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("box must be x1,y1,x2,y2")
    x1, y1, x2, y2 = parts
    if x2 <= x1 or y2 <= y1:
        raise argparse.ArgumentTypeError("box must have x2>x1 and y2>y1")
    return x1, y1, x2, y2


def parse_rgba(value: str) -> tuple[int, int, int, int]:
    parts = [int(p.strip()) for p in value.split(",")]
    if len(parts) not in (3, 4):
        raise argparse.ArgumentTypeError("color must be r,g,b or r,g,b,a")
    if len(parts) == 3:
        parts.append(255)
    if any(p < 0 or p > 255 for p in parts):
        raise argparse.ArgumentTypeError("color values must be 0-255")
    return tuple(parts)  # type: ignore[return-value]


def candidate_fonts() -> list[str]:
    system = platform.system().lower()
    if system == "windows":
        candidates = WINDOWS_FONT_CANDIDATES + MAC_FONT_CANDIDATES + LINUX_FONT_CANDIDATES
    elif system == "darwin":
        candidates = MAC_FONT_CANDIDATES + WINDOWS_FONT_CANDIDATES + LINUX_FONT_CANDIDATES
    else:
        candidates = LINUX_FONT_CANDIDATES + MAC_FONT_CANDIDATES + WINDOWS_FONT_CANDIDATES

    extra = os.environ.get("PPT_VISUAL_REBUILDER_FONT")
    if extra:
        candidates.insert(0, extra)
    return candidates


def find_font(explicit: str | None) -> str:
    if explicit:
        path = Path(explicit)
        if path.exists():
            return str(path)
        raise FileNotFoundError(f"Specified font not found: {explicit}")

    for candidate in candidate_fonts():
        if Path(candidate).exists():
            return candidate

    raise FileNotFoundError(
        "No Chinese-capable font found. Install Microsoft YaHei, Noto Sans CJK, "
        "SimHei, PingFang, or Arial Unicode; or pass --font <path>."
    )


def text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0], box[3] - box[1]


def main() -> None:
    parser = argparse.ArgumentParser(description="Overlay exact text on an image.")
    parser.add_argument("--input", required=True, help="Input image path")
    parser.add_argument("--output", required=True, help="Output image path")
    parser.add_argument("--text", required=True, help="Exact replacement text")
    parser.add_argument("--box", required=True, type=parse_box, help="x1,y1,x2,y2 backing box in pixels")
    parser.add_argument("--font", default=None, help="Optional font path. Auto-detects Chinese fonts when omitted.")
    parser.add_argument("--font-size", type=int, required=True, help="Font size in pixels")
    parser.add_argument("--text-color", type=parse_rgba, default=(246, 250, 255, 255), help="r,g,b,a")
    parser.add_argument("--box-color", type=parse_rgba, default=(0, 0, 0, 255), help="r,g,b,a")
    parser.add_argument("--radius", type=int, default=16, help="Backing box corner radius")
    parser.add_argument("--padding-x", type=int, default=24)
    parser.add_argument("--padding-y", type=int, default=18)
    parser.add_argument("--align", choices=("left", "center", "right"), default="center")
    parser.add_argument("--valign", choices=("top", "middle", "bottom"), default="middle")
    parser.add_argument("--stroke-width", type=int, default=0)
    parser.add_argument("--stroke-color", type=parse_rgba, default=(0, 0, 0, 0), help="r,g,b,a")
    parser.add_argument("--quality", type=int, default=98)
    parser.add_argument("--print-font", action="store_true", help="Print selected font path")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        raise FileNotFoundError(f"Input image not found: {input_path}")

    font_path = find_font(args.font)
    if args.print_font:
        print(f"Using font: {font_path}")

    img = Image.open(input_path).convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_draw.rounded_rectangle(args.box, radius=args.radius, fill=args.box_color)
    img = Image.alpha_composite(img, overlay)

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, args.font_size)
    tw, th = text_size(draw, args.text, font)
    x1, y1, x2, y2 = args.box

    if args.align == "left":
        x = x1 + args.padding_x
    elif args.align == "right":
        x = x2 - tw - args.padding_x
    else:
        x = x1 + (x2 - x1 - tw) // 2

    if args.valign == "top":
        y = y1 + args.padding_y
    elif args.valign == "bottom":
        y = y2 - th - args.padding_y
    else:
        y = y1 + (y2 - y1 - th) // 2

    draw.text(
        (x, y),
        args.text,
        font=font,
        fill=args.text_color,
        stroke_width=args.stroke_width,
        stroke_fill=args.stroke_color,
    )

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    img.convert("RGB").save(output_path, quality=args.quality)
    print(output_path)


if __name__ == "__main__":
    main()
