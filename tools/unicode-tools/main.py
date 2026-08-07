"""Unicode tools: shows character names, categories and normalization forms."""

import sys
import unicodedata

FORMS = ("NFC", "NFD", "NFKC", "NFKD")


def describe_char(char):
  name = unicodedata.name(char, "<unnamed>")
  category = unicodedata.category(char)
  combining = unicodedata.combining(char)
  return name, category, combining


def main() -> None:
  sys.stdout.reconfigure(encoding="utf-8")
  args = sys.argv[1:]
  if not args:
    print("Usage: python main.py <characters> | --normalize <form> \"<text>\" | --compare \"<a>\" \"<b>\"")
    sys.exit(1)
  if args[0] == "--normalize":
    if len(args) < 3:
      print("Error: --normalize requires a form and text")
      sys.exit(1)
    form = args[1].upper()
    text = " ".join(args[2:])
    if form not in FORMS:
      print(f"Error: unknown normalization form '{form}', expected one of {', '.join(FORMS)}")
      sys.exit(1)
    print(unicodedata.normalize(form, text))
    return
  if args[0] == "--compare":
    if len(args) < 3:
      print("Error: --compare requires two texts")
      sys.exit(1)
    normalized = [unicodedata.normalize("NFC", arg) for arg in args[1:3]]
    if len(args) > 3:
      print("Error: --compare accepts exactly two texts (quote each argument)")
      sys.exit(1)
    print("identical" if normalized[0] == normalized[1] else "different")
    return
  text = " ".join(args)
  if len(text) > 16:
    print(f"Error: '{text}' is too long ({len(text)} characters); inspect at most 16 characters")
    sys.exit(1)
  for char in text:
    name, category, combining = describe_char(char)
    print(f"U+{ord(char):04X} {char!r} category={category} combining={combining} {name}")
    print(f"  NFC: {unicodedata.normalize('NFC', char)!r}  NFD: {unicodedata.normalize('NFD', char)!r}")


if __name__ == "__main__":
  main()
