"""Caesar cipher (ROT-N) encoder/decoder (stdlib only)."""

import json
import string
import sys


def shift(text: str, amount: int, decode: bool = False) -> str:
    if decode:
        amount = -amount
    out = []
    for char in text:
        if char in string.ascii_uppercase:
            out.append(chr((ord(char) - 65 + amount) % 26 + 65))
        elif char in string.ascii_lowercase:
            out.append(chr((ord(char) - 97 + amount) % 26 + 97))
        else:
            out.append(char)
    return "".join(out)


def brute_force(text: str) -> list[str]:
    return [shift(text, n, decode=True) for n in range(26)]


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if len(args) < 3 or args[0] in ("-h", "--help", "help"):
        print(json.dumps({"error": "Usage: python main.py <encode|decode|brute> <shift> <text>  e.g. python main.py encode 13 hello"}))
        sys.exit(1)
    try:
        command = args[0]
        if command == "brute":
            print(json.dumps({"attempts": brute_force(args[2])}, ensure_ascii=False))
        else:
            amount = int(args[1]) % 26
            result = shift(args[2], amount, decode=(command == "decode"))
            print(json.dumps({"result": result}, ensure_ascii=False))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
