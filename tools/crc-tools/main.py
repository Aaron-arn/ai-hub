"""CRC tools: computes CRC32 checksums and encodes/decodes base64 data."""

import base64
import binascii
import sys


def main() -> None:
  if len(sys.argv) < 3:
    print("Usage: python main.py crc32 <text> | base64 encode|decode <text>")
    sys.exit(1)
  command = sys.argv[1].lower()
  try:
    if command == "crc32":
      payload = " ".join(sys.argv[2:])
      print(f"{binascii.crc32(payload.encode('utf-8')) & 0xFFFFFFFF:08x}")
    elif command == "base64":
      if len(sys.argv) < 4:
        raise ValueError("base64 requires an action: encode or decode")
      action = sys.argv[2].lower()
      data = " ".join(sys.argv[3:])
      if action == "encode":
        print(base64.b64encode(data.encode("utf-8")).decode("ascii"))
      elif action == "decode":
        print(base64.b64decode(data, validate=True).decode("utf-8"))
      else:
        raise ValueError(f"unknown base64 action '{action}', expected 'encode' or 'decode'")
    else:
      raise ValueError(f"unknown command '{command}', expected 'crc32' or 'base64'")
  except ValueError as exc:
    print(f"Error: {exc}")
    sys.exit(1)


if __name__ == "__main__":
  main()
