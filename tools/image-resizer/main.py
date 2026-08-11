import argparse
from pathlib import Path
from PIL import Image

def main():
    ap = argparse.ArgumentParser(description="Resize and convert images")
    ap.add_argument("inputs", nargs="+", help="input image paths or globs")
    ap.add_argument("-w", "--width", type=int, help="target width (keeps aspect if no height)")
    ap.add_argument("-h", "--height", type=int, help="target height")
    ap.add_argument("-f", "--format", choices=["JPEG", "PNG", "WEBP"], default=None)
    ap.add_argument("-q", "--quality", type=int, default=85)
    ap.add_argument("-o", "--output-dir", default="resized", help="output directory")
    args = ap.parse_args()

    out = Path(args.output_dir)
    out.mkdir(exist_ok=True)
    for pattern in args.inputs:
        for path in Path(".").glob(pattern) if any(c in pattern for c in "*?[") else [Path(pattern)]:
            img = Image.open(path)
            w, h = img.size
            tw, th = args.width or w, args.height or h
            if args.width and not args.height:
                th = round(h * tw / w)
            elif args.height and not args.width:
                tw = round(w * th / h)
            img = img.resize((tw, th), Image.LANCZOS)
            fmt = (args.format or path.suffix[1:].upper()).replace("JPG", "JPEG")
            dest = out / f"{path.stem}.{fmt.lower()}"
            img.save(dest, fmt, quality=args.quality)
            print(f"{path} -> {dest} ({tw}x{th})")

if __name__ == "__main__":
    main()
