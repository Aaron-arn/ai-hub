"""URL tool: parse, encode and decode URLs and query strings."""

import json
import sys
import urllib.parse


def clean_params(params: dict) -> dict:
    return {key: value[0] if len(value) == 1 else value for key, value in params.items()}


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if len(args) < 2:
        print(json.dumps({"error": "Usage: python main.py <parse|encode|decode|query> <value>"}))
        sys.exit(1)
    command, value = args[0], args[1]
    try:
        if command == "parse":
            parts = urllib.parse.urlparse(value)
            result = {
                "scheme": parts.scheme,
                "host": parts.netloc,
                "path": parts.path,
                "query": parts.query,
                "fragment": parts.fragment,
                "params": clean_params(urllib.parse.parse_qs(parts.query)),
            }
        elif command == "encode":
            result = {"encoded": urllib.parse.quote_plus(value)}
        elif command == "decode":
            result = {"decoded": urllib.parse.unquote_plus(value)}
        elif command == "query":
            result = {"params": clean_params(urllib.parse.parse_qs(value))}
        else:
            raise ValueError(f"Unknown command: {command}")
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))
        sys.exit(1)


if __name__ == "__main__":
    main()
