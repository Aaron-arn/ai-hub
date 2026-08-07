"""Password generator: creates strong random passwords with configurable length and character sets."""

import argparse
import secrets
import string
import sys

DEFAULT_LENGTH = 16


class CliParser(argparse.ArgumentParser):
  def error(self, message):
    print(f"Error: {message}")
    sys.exit(1)


def build_pool(use_lower, use_upper, use_digits, use_symbols):
  pool = ""
  if use_lower:
    pool += string.ascii_lowercase
  if use_upper:
    pool += string.ascii_uppercase
  if use_digits:
    pool += string.digits
  if use_symbols:
    pool += "!@#$%^&*()_+-=[]{}|;:,.<>?"
  if not pool:
    raise ValueError("at least one character set must be enabled")
  return pool


def generate(length, pool, count):
  return ["".join(secrets.choice(pool) for _ in range(length)) for _ in range(count)]


def main() -> None:
  parser = CliParser(description="Generate strong random passwords.")
  parser.add_argument("length", nargs="?", type=int, default=DEFAULT_LENGTH, help="password length")
  parser.add_argument("--no-lower", action="store_true", help="exclude lowercase letters")
  parser.add_argument("--no-upper", action="store_true", help="exclude uppercase letters")
  parser.add_argument("--no-digits", action="store_true", help="exclude digits")
  parser.add_argument("--no-symbols", action="store_true", help="exclude symbols")
  parser.add_argument("--count", type=int, default=1, help="number of passwords to generate")
  args = parser.parse_args()

  if args.length < 1:
    print("Error: length must be at least 1")
    sys.exit(1)
  if args.count < 1:
    print("Error: count must be at least 1")
    sys.exit(1)
  try:
    pool = build_pool(not args.no_lower, not args.no_upper, not args.no_digits, not args.no_symbols)
  except ValueError as exc:
    print(f"Error: {exc}")
    sys.exit(1)
  for password in generate(args.length, pool, args.count):
    print(password)


if __name__ == "__main__":
  main()
