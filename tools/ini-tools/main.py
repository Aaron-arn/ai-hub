"""INI configuration parsing and conversion (stdlib configparser)."""

import configparser
import json
import sys


def parse(text: str) -> dict:
    parser = configparser.ConfigParser()
    parser.read_string(text)
    out = {}
    for section in parser.sections():
        out[section] = dict(parser.items(section))
    if parser.defaults():
        out["DEFAULT"] = dict(parser.defaults())
    return out


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if not args or args[0] in ("-h", "--help", "help"):
        print(json.dumps({"error": "Usage: python main.py <ini_text>  or: python main.py --file <path>"}))
        sys.exit(1)
    try:
        if args[0] == "--file" and len(args) > 1:
            with open(args[1], encoding="utf-8") as fh:
                text = fh.read()
        else:
            text = args[0]
        print(json.dumps(parse(text), ensure_ascii=False, indent=2))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
