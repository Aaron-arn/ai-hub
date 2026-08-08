"""TOML parsing and validation (stdlib tomllib, Python 3.11+)."""

import json
import sys

try:
    import tomllib
except ImportError:
    tomllib = None


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if not args or args[0] in ("-h", "--help", "help"):
        print(json.dumps({"error": "Usage: python main.py <toml_text>  or: python main.py --file <path>  (requires Python 3.11+)"}))
        sys.exit(1)
    if tomllib is None:
        print(json.dumps({"error": "tomllib requires Python 3.11+"}))
        sys.exit(1)
    try:
        if args[0] == "--file" and len(args) > 1:
            with open(args[1], "rb") as fh:
                data = tomllib.load(fh)
        else:
            data = tomllib.loads(args[0])
        print(json.dumps(data, ensure_ascii=False, indent=2))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
