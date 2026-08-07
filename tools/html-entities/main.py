"""HTML entities tool: encodes and decodes HTML entities in text."""

import html
import sys


def main() -> None:
  if len(sys.argv) < 3:
    print("Usage: python main.py encode|decode \"<text>\"")
    sys.exit(1)
  action = sys.argv[1].lower()
  text = " ".join(sys.argv[2:])
  if action == "encode":
    print(html.escape(text, quote=True))
  elif action == "decode":
    print(html.unescape(text))
  else:
    print(f"Error: unknown action '{action}', expected 'encode' or 'decode'")
    sys.exit(1)


if __name__ == "__main__":
  main()
