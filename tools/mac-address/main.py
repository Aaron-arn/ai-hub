"""MAC address tool: validates, formats, parses and generates MAC addresses."""

import random
import re
import sys


def parse(mac):
  cleaned = re.sub(r"[:\-.]", "", mac).lower()
  if not re.fullmatch(r"[0-9a-f]{12}", cleaned):
    raise ValueError(f"'{mac}' is not a valid MAC address")
  return cleaned


def format_address(mac, separator=":"):
  cleaned = parse(mac)
  return separator.join(cleaned[i:i + 2] for i in range(0, 12, 2))


def generate():
  return ":".join(f"{random.randrange(256):02x}" for _ in range(6))


def main() -> None:
  if len(sys.argv) < 2:
    print("Usage: python main.py validate <mac> | format <mac> [separator] | parse <mac> | generate")
    sys.exit(1)
  command = sys.argv[1].lower()
  if command == "generate":
    print(generate())
    return
  if len(sys.argv) < 3:
    print(f"Error: '{command}' requires a MAC address argument")
    sys.exit(1)
  mac = sys.argv[2]
  if command == "validate":
    try:
      parse(mac)
    except ValueError:
      print(f"invalid: {mac}")
      sys.exit(1)
    print(f"valid: {mac}")
  elif command == "format":
    separator = sys.argv[3] if len(sys.argv) > 3 else ":"
    try:
      print(format_address(mac, separator))
    except ValueError as exc:
      print(f"Error: {exc}")
      sys.exit(1)
  elif command == "parse":
    try:
      print(parse(mac))
    except ValueError as exc:
      print(f"Error: {exc}")
      sys.exit(1)
  else:
    print(f"Error: unknown command '{command}'")
    sys.exit(1)


if __name__ == "__main__":
  main()
