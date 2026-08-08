"""Unified diff between two texts or files (stdlib difflib)."""

import difflib
import json
import sys


def diff(a: str, b: str, label_a: str = "old", label_b: str = "new") -> str:
    lines = difflib.unified_diff(a.splitlines(), b.splitlines(), fromfile=label_a, tofile=label_b, lineterm="")
    return "\n".join(lines)


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if not args or args[0] in ("-h", "--help", "help"):
        print(json.dumps({"error": "Usage: python main.py <text_a|file_a> <text_b|file_b> [--files]"}))
        sys.exit(1)
    try:
        if len(args) >= 3 and args[2] == "--files":
            with open(args[0], encoding="utf-8") as fh:
                a = fh.read()
            with open(args[1], encoding="utf-8") as fh:
                b = fh.read()
            labels = (args[0], args[1])
        else:
            a, b, labels = args[0], args[1], ("old", "new")
        result = diff(a, b, labels[0], labels[1])
        print(json.dumps({"diff": result, "has_changes": bool(result)}, ensure_ascii=False))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
