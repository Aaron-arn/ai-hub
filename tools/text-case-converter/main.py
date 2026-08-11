import argparse
import re
import sys

def split_words(text):
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", text)
    text = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", text)
    return [w for w in re.split(r"[^\w]+|_", text) if w]

def to_snake(text):
    return "_".join(w.lower() for w in split_words(text))

def to_camel(text):
    words = split_words(text)
    return words[0].lower() + "".join(w.capitalize() for w in words[1:])

def to_pascal(text):
    return "".join(w.capitalize() for w in split_words(text))

def to_kebab(text):
    return "-".join(w.lower() for w in split_words(text))

def to_title(text):
    return " ".join(w.capitalize() for w in split_words(text))

CONVERTERS = {
    "snake": to_snake, "camel": to_camel, "pascal": to_pascal,
    "kebab": to_kebab, "title": to_title,
}

def main():
    ap = argparse.ArgumentParser(description="Convert text between case styles")
    ap.add_argument("text", nargs="?", help="text to convert (default: stdin)")
    ap.add_argument("--all", action="store_true", help="output all styles")
    for name in CONVERTERS:
        ap.add_argument(f"--{name}", action="store_true", help=f"convert to {name}")
    args = ap.parse_args()

    text = args.text if args.text is not None else sys.stdin.read().strip()
    if args.all:
        for name, fn in CONVERTERS.items():
            print(f"{name:6s}: {fn(text)}")
        return
    requested = [name for name in CONVERTERS if getattr(args, name)]
    if not requested:
        ap.error("choose a style (--all or one of " + ", ".join(CONVERTERS) + ")")
    for name in requested:
        print(CONVERTERS[name](text))

if __name__ == "__main__":
    main()
