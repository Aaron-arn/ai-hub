import argparse
from PIL import Image
from PIL.ExifTags import TAGS


def main():
    ap = argparse.ArgumentParser(description="Read image metadata")
    ap.add_argument("inputs", nargs="+", help="image files")
    ap.add_argument("--all", action="store_true", help="show all EXIF fields")
    args = ap.parse_args()

    for path in args.inputs:
        print(f"== {path} ==")
        with Image.open(path) as img:
            print(f"format: {img.format}  size: {img.size}  mode: {img.mode}")
            info = img.info
            for key in ("dpi", "gamma", "progressive", "quality"):
                if key in info:
                    print(f"{key}: {info[key]}")
            exif = img.getexif()
            if exif:
                for tag_id, value in exif.items():
                    name = TAGS.get(tag_id, tag_id)
                    if args.all or name in ("DateTime", "Make", "Model", "Software", "Artist", "Copyright", "Orientation", "ExposureTime", "FNumber", "ISOSpeedRatings", "FocalLength"):
                        print(f"  {name}: {value}")
            else:
                print("  (no EXIF data)")

if __name__ == "__main__":
    main()
