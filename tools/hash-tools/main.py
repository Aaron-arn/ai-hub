"""Hash tool: compute digests and base64 encodings."""

import base64
import hashlib
import json
import sys


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if len(args) < 2:
        print(json.dumps({"error": "Usage: python main.py <md5|sha1|sha256|sha512|base64-encode|base64-decode> <text>"}))
        sys.exit(1)
    command, text = args[0], args[1]
    try:
        if command in ("md5", "sha1", "sha256", "sha512"):
            digest = hashlib.new(command, text.encode("utf-8")).hexdigest()
            result = {"algorithm": command, "hex": digest}
        elif command == "base64-encode":
            result = {"encoding": "base64", "value": base64.b64encode(text.encode("utf-8")).decode("ascii")}
        elif command == "base64-decode":
            result = {"encoding": "utf-8", "value": base64.b64decode(text).decode("utf-8")}
        else:
            raise ValueError(f"Unknown command: {command}")
        print(json.dumps(result, ensure_ascii=False))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))
        sys.exit(1)


if __name__ == "__main__":
    main()
