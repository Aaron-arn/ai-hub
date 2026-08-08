"""CSV tool: parse CSV data and convert it to JSON."""

import csv
import io
import json
import sys


def load_document(text: str | None) -> str:
    if text is None or not text.strip():
        return sys.stdin.read()
    return text


def parse_csv(text: str) -> list[dict]:
    return list(csv.DictReader(io.StringIO(text)))


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if not args:
        print(json.dumps({"error": "Usage: python main.py <to-json|rows|filter> <csv> [column] [value]"}))
        sys.exit(1)
    command = args[0]
    try:
        if command == "to-json":
            rows = parse_csv(load_document(args[1] if len(args) > 1 else None))
            print(json.dumps(rows, ensure_ascii=False, indent=2))
        elif command == "rows":
            rows = parse_csv(load_document(args[1] if len(args) > 1 else None))
            print(json.dumps({"rows": len(rows), "columns": list(rows[0].keys()) if rows else []}, ensure_ascii=False, indent=2))
        elif command == "filter" and len(args) >= 4:
            rows = parse_csv(load_document(args[1]))
            column, value = args[2], args[3]
            matched = [row for row in rows if row.get(column) == value]
            print(json.dumps({"column": column, "value": value, "matches": len(matched), "rows": matched}, ensure_ascii=False, indent=2))
        else:
            raise ValueError(f"Unknown command or missing arguments: {command}")
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))
        sys.exit(1)


if __name__ == "__main__":
    main()
