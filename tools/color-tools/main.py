"""Color tools: convert between hex, RGB and HSL color formats."""

import colorsys
import sys


def usage():
    print("Usage: python main.py hex \"#ff0000\"")
    print("       python main.py rgb 255 0 0")
    print("       python main.py hsl 0 100 50")


def parse_hex(text):
    text = text.strip().lstrip("#")
    if len(text) == 3:
        text = "".join(ch * 2 for ch in text)
    if len(text) != 6:
        raise ValueError("hex color must be 3 or 6 hex digits")
    try:
        return tuple(int(text[i:i + 2], 16) for i in (0, 2, 4))
    except ValueError as exc:
        raise ValueError("hex color must contain only hex digits") from exc


def print_color(r, g, b):
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    print(f"hex: #{r:02x}{g:02x}{b:02x}")
    print(f"rgb: rgb({r}, {g}, {b})")
    print(f"hsl: hsl({h * 360:.1f}, {s * 100:.1f}%, {l * 100:.1f}%)")


def main():
    args = sys.argv[1:]
    if not args:
        usage()
        sys.exit(1)
    try:
        command = args[0].lower()
        if command == "hex" and len(args) >= 2:
            r, g, b = parse_hex(args[1])
        elif command == "rgb" and len(args) >= 4:
            r, g, b = (int(float(v)) for v in args[1:4])
            if not all(0 <= v <= 255 for v in (r, g, b)):
                raise ValueError("RGB values must be between 0 and 255")
        elif command == "hsl" and len(args) >= 4:
            h, s, l = (float(v) for v in args[1:4])
            if not (0 <= h <= 360 and 0 <= s <= 100 and 0 <= l <= 100):
                raise ValueError("HSL values out of range")
            r, g, b = (round(v * 255) for v in colorsys.hls_to_rgb(h / 360, l / 100, s / 100))
        else:
            raise ValueError("invalid command or arguments")
        print_color(r, g, b)
    except (ValueError, IndexError) as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
