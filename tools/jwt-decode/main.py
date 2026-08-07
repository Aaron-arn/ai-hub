"""JWT decoder: decodes and prints JWT headers and payloads without verification."""

import base64
import json
import sys


def b64url_decode(segment):
  padding = "=" * (-len(segment) % 4)
  return base64.urlsafe_b64decode(segment + padding)


def decode_token(token):
  parts = token.split(".")
  if len(parts) < 2 or len(parts) > 3:
    raise ValueError("token must have 2 or 3 dot-separated segments")
  header = json.loads(b64url_decode(parts[0]))
  payload = json.loads(b64url_decode(parts[1]))
  return header, payload


def main() -> None:
  if len(sys.argv) < 2:
    print("Usage: python main.py \"<jwt-token>\"")
    sys.exit(1)
  try:
    header, payload = decode_token(sys.argv[1])
  except Exception as exc:
    print(f"Error: invalid JWT: {exc}")
    sys.exit(1)
  print("Header:")
  print(json.dumps(header, indent=2, sort_keys=True))
  print("Payload:")
  print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
  main()
