"""Sorting tools: sorts lines from stdin with natural, numeric, reverse and unique options."""

import re
import sys

NATURAL_RE = re.compile(r"(\d+)")


def natural_key(line):
  return [int(part) if part.isdigit() else part.lower() for part in NATURAL_RE.split(line)]


def main() -> None:
  mode = "natural"
  reverse = False
  unique = False
  for arg in sys.argv[1:]:
    if not arg.startswith("--"):
      print(f"Error: unexpected argument '{arg}'")
      sys.exit(1)
    option = arg[2:]
    if option == "reverse":
      reverse = True
    elif option == "unique":
      unique = True
    elif option in ("natural", "numeric", "alphabetical"):
      mode = option
    else:
      print(f"Error: unknown option '--{option}'")
      sys.exit(1)

  if sys.stdin.isatty():
    print("Usage: python main.py [--natural|--numeric|--alphabetical] [--reverse] [--unique]")
    print("       (reads lines from stdin)")
    sys.exit(1)
  lines = [line.rstrip("\n") for line in sys.stdin]
  if unique:
    lines = list(dict.fromkeys(lines))
  try:
    if mode == "numeric":
      lines.sort(key=float, reverse=reverse)
    elif mode == "alphabetical":
      lines.sort(key=str.lower, reverse=reverse)
    else:
      lines.sort(key=natural_key, reverse=reverse)
  except ValueError as exc:
    print(f"Error: {exc}")
    sys.exit(1)
  for line in lines:
    print(line)


if __name__ == "__main__":
  main()
