import argparse
import json
import sys


def main():
    ap = argparse.ArgumentParser(description="Pretty-print or filter JSON")
    ap.add_argument("input", nargs="?", help="input file (default: stdin)")
    ap.add_argument("-o", "--output", help="output file (default: stdout)")
    ap.add_argument("--indent", type=int, default=2)
    ap.add_argument("--compact", action="store_true", help="minified output")
    ap.add_argument("--validate", action="store_true", help="only validate, no output")
    ap.add_argument("--jq", help="select a path with dot notation, e.g. results.0.name")
    args = ap.parse_args()

    fh = open(args.input, encoding="utf-8") if args.input else sys.stdin
    try:
        data = json.load(fh)
    except json.JSONDecodeError as e:
        print(f"INVALID JSON at line {e.lineno} col {e.colno}: {e.msg}", file=sys.stderr)
        sys.exit(1)

    if args.validate:
        print("valid JSON")
        return

    if args.jq:
        for part in args.jq.split("."):
            if part.isdigit():
                data = data[int(part)]
            else:
                data = data[part]

    text = json.dumps(data, indent=None if args.compact else args.indent, ensure_ascii=False)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as out:
            out.write(text + "\n")
        print(f"Wrote {args.output}")
    else:
        sys.stdout.write(text + "\n")


if __name__ == "__main__":
    main()
