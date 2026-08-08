"""Lorem ipsum placeholder text generator (stdlib only)."""

import json
import random
import sys

WORDS = (
    "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt "
    "ut labore et dolore magna aliqua enim ad minim veniam quis nostrud exercitation ullamco "
    "laboris nisi aliquip ex ea commodo consequat duis aute irure in reprehenderit voluptate "
    "velit esse cillum eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident "
    "sunt culpa qui officia deserunt mollit anim id est laborum"
).split()


def paragraph(sentences: int = 6) -> str:
    words = random.choices(WORDS, k=sentences * random.randint(8, 14))
    text = " ".join(words)
    text = text[:1].upper() + text[1:] + "."
    return text


def lorem(paragraphs: int = 1, sentences: int = 6, seed: int | None = None) -> str:
    if seed is not None:
        random.seed(seed)
    return "\n\n".join(paragraph(sentences) for _ in range(paragraphs))


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if not args or args[0] in ("-h", "--help", "help"):
        print(json.dumps({"error": "Usage: python main.py <paragraphs> [sentences_per_paragraph] [seed]"}))
        sys.exit(1)
    try:
        paragraphs = int(args[0])
        sentences = int(args[1]) if len(args) > 1 else 6
        seed = int(args[2]) if len(args) > 2 else None
        print(json.dumps({"paragraphs": paragraphs, "text": lorem(paragraphs, sentences, seed)}, ensure_ascii=False))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
