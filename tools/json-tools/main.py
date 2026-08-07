"""JSON tool: validate, format and extract values from JSON documents."""

import json
import sys


def load_document(text: str | None) -> str:
    if text is None or not text.strip():
        return sys.stdin.read()
    return text


def get_path(data, path: str):
    if not path:
        return data
    current = data
    for part in path.split("."):
        if isinstance(current, dict) and part in current:
            current = current[part]
        elif isinstance(current, list) and part.isdigit() and int(part) < len(current):
            current = current[int(part)]
        else:
            raise KeyError(f"Path not found: {path}")
    return current


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print(json.dumps({"error": "Usage: python main.py <validate|format|get> <json> [path]"}))
        sys.exit(1)
    command = args[0]
    try:
        if command == "validate":
            json.loads(load_document(args[1] if len(args) > 1 else None))
            print(json.dumps({"valid": True}))
        elif command == "format":
            data = json.loads(load_document(args[1] if len(args) > 1 else None))
            print(json.dumps(data, ensure_ascii=False, indent=2))
        elif command == "get":
            data = json.loads(load_document(args[1] if len(args) > 1 else None))
            path = args[2] if len(args) > 2 else ""
            print(json.dumps(get_path(data, path), ensure_ascii=False, indent=2))
        else:
            raise ValueError(f"Unknown command: {command}")
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))
        sys.exit(1)


if __name__ == "__main__":
    main()
