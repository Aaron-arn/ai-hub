"""Morse code encoder/decoder (stdlib only)."""

import json
import sys

MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--",
    "/": "-..-.", "(": "-.--.", ")": "-.--.-", "&": ".-...", ":": "---...",
    ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "-": "-....-", "_": "..--.-",
    '"': ".-..-.", "$": "...-..-", "@": ".--.-.",
}
REVERSE = {code: char for char, code in MORSE.items()}


def encode(text: str) -> str:
    words = text.strip().upper().split()
    return " / ".join(" ".join(MORSE.get(char, char) for char in word) for word in words)


def decode(code: str) -> str:
    words = code.strip().split(" / ")
    return " ".join("".join(REVERSE.get(symbol, symbol) for symbol in word.split()) for word in words)


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if len(args) < 2 or args[0] in ("-h", "--help", "help"):
        print(json.dumps({"error": "Usage: python main.py <encode|decode> <message>"}))
        sys.exit(1)
    try:
        if args[0] == "encode":
            print(json.dumps({"morse": encode(args[1])}, ensure_ascii=False))
        elif args[0] == "decode":
            print(json.dumps({"text": decode(args[1])}, ensure_ascii=False))
        else:
            print(json.dumps({"error": "Unknown command"}))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
