"""Hex dump: prints hexadecimal dumps of files or strings in classic hexdump style."""

import sys

WIDTH = 16


def hex_dump(data):
  lines = []
  for offset in range(0, len(data), WIDTH):
    chunk = data[offset:offset + WIDTH]
    hex_part = " ".join(f"{byte:02x}" for byte in chunk)
    hex_part = hex_part.ljust(WIDTH * 3 - 1)
    ascii_part = "".join(chr(byte) if 32 <= byte < 127 else "." for byte in chunk)
    lines.append(f"{offset:08x}  {hex_part}  |{ascii_part}|")
  return lines


def main() -> None:
  if len(sys.argv) < 2:
    print("Usage: python main.py <file> | --string \"<text>\"")
    sys.exit(1)
  if sys.argv[1] == "--string":
    data = " ".join(sys.argv[2:]).encode("utf-8")
  else:
    path = sys.argv[1]
    try:
      with open(path, "rb") as handle:
        data = handle.read()
    except OSError as exc:
      print(f"Error: {exc}")
      sys.exit(1)
  for line in hex_dump(data):
    print(line)


if __name__ == "__main__":
  main()
