"""Password checker: estimates password strength and entropy."""

import math
import re
import sys

COMMON_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123", "monkey",
    "1234567", "letmein", "trustno1", "dragon", "111111", "iloveyou",
    "admin", "welcome", "123123", "sunshine", "master", "654321",
    "password1", "football", "123456789", "1234567890", "qwertyuiop",
    "letmein123", "dragon123", "password123",
}


def used_sets(password):
  sets = []
  if re.search(r"[a-z]", password):
    sets.append("lowercase")
  if re.search(r"[A-Z]", password):
    sets.append("uppercase")
  if re.search(r"\d", password):
    sets.append("digits")
  if re.search(r"[^a-zA-Z0-9]", password):
    sets.append("symbols")
  return sets


def estimate_pool_size(password):
  size = 0
  if re.search(r"[a-z]", password):
    size += 26
  if re.search(r"[A-Z]", password):
    size += 26
  if re.search(r"\d", password):
    size += 10
  if re.search(r"[^a-zA-Z0-9]", password):
    size += 33
  return size


def entropy_bits(password):
  pool = estimate_pool_size(password)
  if not password:
    return 0.0
  return len(password) * math.log2(pool)


def strength_label(bits):
  if bits < 28:
    return "very weak"
  if bits < 36:
    return "weak"
  if bits < 60:
    return "fair"
  if bits < 128:
    return "strong"
  return "very strong"


def main() -> None:
  if len(sys.argv) < 2:
    print("Usage: python main.py \"<password>\"")
    sys.exit(1)
  password = " ".join(sys.argv[1:])
  bits = entropy_bits(password)
  label = strength_label(bits)
  sets = used_sets(password)
  print(f"Length: {len(password)}")
  print(f"Character sets: {', '.join(sets) if sets else 'none'}")
  print(f"Entropy: {bits:.1f} bits")
  print(f"Strength: {label}")
  if password.lower() in COMMON_PASSWORDS:
    print("Warning: matches a commonly used password; treat as very weak")


if __name__ == "__main__":
  main()
