"""EAN-13 barcode generator producing SVG output (stdlib only)."""

import json
import sys

L = ["0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"]
G = ["0100111", "0110011", "0011011", "0100001", "0011101", "0111001", "0000101", "0010001", "0001001", "0010111"]
R = ["1110010", "1100110", "1101100", "1000010", "1011100", "1001110", "1010000", "1000100", "1001000", "1110100"]
STRUCTURES = {0: "LLLLLL", 1: "LLGLGG", 2: "LLGGLG", 3: "LLGGGL", 4: "LGLLGG",
              5: "LGGLLG", 6: "LGGGLL", 7: "LGLGLG", 8: "LGLGGL", 9: "LGGLGL"}


def checksum(digits: str) -> int:
    total = sum(int(d) * (3 if i % 2 == 0 else 1) for i, d in enumerate(digits))
    return (10 - total % 10) % 10


def encode(digits: str) -> str:
    if len(digits) != 12 or not digits.isdigit():
        raise ValueError("Need exactly 12 digits")
    check = checksum(digits)
    full = digits + str(check)
    structure = STRUCTURES[int(full[0])]
    out = "101"
    for i, ch in enumerate(structure):
        table = L if ch == "L" else G if ch == "G" else R
        out += table[int(full[i + 1])]
        if i == 5:
            out += "01010"
    return out + "101"


def svg(digits: str, width: int = 300, height: int = 120) -> str:
    bits = encode(digits)
    bar_width = width / len(bits)
    rects = []
    x = 0.0
    for bit in bits:
        if bit == "1":
            rects.append(f'<rect x="{x:.2f}" y="8" width="{bar_width + 0.05:.2f}" height="{height - 16}" fill="black"/>')
        x += bar_width
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" width="' + str(width) + '" height="' + str(height) + '">'
        + "".join(rects)
        + '<text x="' + str(width / 2) + '" y="' + str(height - 2) + '" text-anchor="middle" font-family="monospace" font-size="12">'
        + digits
        + "</text></svg>"
    )


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if not args or args[0] in ("-h", "--help", "help"):
        print(json.dumps({"error": "Usage: python main.py <12_digit_code> [svg_width] [svg_height]"}))
        sys.exit(1)
    try:
        width = int(args[1]) if len(args) > 1 else 300
        height = int(args[2]) if len(args) > 2 else 120
        print(json.dumps({"digits": args[0], "check_digit": checksum(args[0]), "svg": svg(args[0], width, height)}, ensure_ascii=False))
    except ValueError as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
