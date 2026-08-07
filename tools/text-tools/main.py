"""Text tool: count, transform and manipulate text."""

import json
import re
import sys


def count(text: str) -> dict:
    return {
        "words": len(re.findall(r"\S+", text)),
        "characters": len(text),
        "lines": len(text.splitlines()),
    }


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or ""


def main() -> None:
    args = sys.argv[1:]
    if len(args) < 2:
        print(json.dumps({"error": "Usage: python main.py <count|slug|upper|lower|title|replace> <text> [old] [new]"}))
        sys.exit(1)
    command, text = args[0], args[1]
    try:
        if command == "count":
            result = count(text)
        elif command == "slug":
            result = {"slug": slug(text)}
        elif command == "upper":
            result = {"text": text.upper()}
        elif command == "lower":
            result = {"text": text.lower()}
        elif command == "title":
            result = {"text": text.title()}
        elif command == "replace" and len(args) >= 4:
            result = {"text": text.replace(args[2], args[3])}
        else:
            raise ValueError(f"Unknown command or missing arguments: {command}")
        print(json.dumps(result, ensure_ascii=False))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))
        sys.exit(1)


if __name__ == "__main__":
    main()
