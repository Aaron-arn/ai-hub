"""Convert text into URL-friendly slugs (stdlib only)."""

import json
import re
import sys
import unicodedata

REPLACEMENTS = {"&": "and", "@": "at", "%": "percent", "#": "hash", "+": "plus"}


def slugify(text: str, sep: str = "-") -> str:
    text = text.strip().lower()
    for char, word in REPLACEMENTS.items():
        text = text.replace(char, f" {word} ")
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = re.sub(r"[^a-z0-9]+", sep, text)
    return text.strip(sep) or "empty"


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if not args or args[0] in ("-h", "--help", "help"):
        print(json.dumps({"error": "Usage: python main.py <text> [separator]"}))
        sys.exit(1)
    try:
        sep = args[1] if len(args) > 1 else "-"
        print(json.dumps({"input": args[0], "slug": slugify(args[0], sep)}))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
