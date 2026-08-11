import argparse
from PIL import Image

RAMP = " .:-=+*#%@"

def main():
    ap = argparse.ArgumentParser(description="Convert an image to ASCII art")
    ap.add_argument("input", help="input image")
    ap.add_argument("--width", type=int, default=80, help="output width in chars")
    ap.add_argument("--invert", action="store_true")
    args = ap.parse_args()

    img = Image.open(args.input).convert("L")
    w, h = img.size
    target_w = args.width
    target_h = max(1, round(h / w * target_w * 0.45))
    img = img.resize((target_w, target_h))

    ramp = RAMP[::-1] if args.invert else RAMP
    for y in range(target_h):
        row = []
        for x in range(target_w):
            v = img.getpixel((x, y))
            row.append(ramp[v * (len(ramp) - 1) // 255])
        print("".join(row))

if __name__ == "__main__":
    main()
