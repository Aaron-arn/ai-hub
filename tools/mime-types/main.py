"""MIME types tool: resolves MIME types from file extensions and vice versa."""

import mimetypes
import sys


def lookup(term):
  if term.startswith("."):
    mime, _ = mimetypes.guess_type("file" + term)
    if mime is None:
      raise ValueError(f"no MIME type known for extension '{term}'")
    return {term: mime}
  if "/" in term:
    extension = mimetypes.guess_extension(term)
    if extension is None:
      raise ValueError(f"no extension known for MIME type '{term}'")
    return {term: extension}
  for ext, mime in mimetypes.types_map.items():
    if ext.lstrip(".") == term:
      return {ext: mime}
  raise ValueError(f"unknown file extension or MIME type '{term}'")


def main() -> None:
  if len(sys.argv) < 2:
    print("Usage: python main.py <extension|mime-type>")
    sys.exit(1)
  try:
    result = lookup(sys.argv[1].lower())
  except ValueError as exc:
    print(f"Error: {exc}")
    sys.exit(1)
  for key, value in result.items():
    print(f"{key}: {value}")


if __name__ == "__main__":
  main()
