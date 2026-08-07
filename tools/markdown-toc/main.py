"""Markdown TOC: generates a nested table of contents from Markdown headings."""

import re
import sys
import unicodedata

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
FENCE_RE = re.compile(r"^\s*(```+|~~~+)")


def extract_headings(text):
  headings = []
  in_fence = False
  for line in text.splitlines():
    stripped = line.strip()
    if FENCE_RE.match(line):
      in_fence = not in_fence
      continue
    if in_fence:
      continue
    match = HEADING_RE.match(line)
    if match:
      headings.append((len(match.group(1)), match.group(2).strip()))
  return headings


def slugify(text):
  text = unicodedata.normalize("NFKD", text)
  text = "".join(char for char in text if not unicodedata.combining(char))
  text = re.sub(r"[^\w\s-]", "", text).strip().lower()
  return re.sub(r"[\s_]+", "-", text)


def build_toc(headings):
  seen = {}
  lines = []
  for level, text in headings:
    base = slugify(text)
    seen[base] = seen.get(base, 0) + 1
    anchor = base if seen[base] == 1 else f"{base}-{seen[base] - 1}"
    lines.append(f"{'  ' * (level - 1)}- [{text}](#{anchor})")
  return "\n".join(lines)


def main() -> None:
  if len(sys.argv) < 2:
    if sys.stdin.isatty():
      print("Usage: python main.py <markdown-file>")
      sys.exit(1)
    text = sys.stdin.read()
  else:
    path = sys.argv[1]
    try:
      with open(path, "r", encoding="utf-8") as handle:
        text = handle.read()
    except OSError as exc:
      print(f"Error: {exc}")
      sys.exit(1)
  headings = extract_headings(text)
  if not headings:
    print("Error: no headings found")
    sys.exit(1)
  print(build_toc(headings))


if __name__ == "__main__":
  main()
