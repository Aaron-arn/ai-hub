"""Roman numerals: converts integers to Roman numerals and back."""

import sys

NUMERALS = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
]
VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def to_roman(n):
  if not 1 <= n <= 3999:
    raise ValueError("number must be between 1 and 3999")
  result = []
  for value, symbol in NUMERALS:
    while n >= value:
      result.append(symbol)
      n -= value
  return "".join(result)


def from_roman(text):
  if not text:
    raise ValueError("input is empty")
  total = 0
  previous = 0
  for char in text.upper():
    if char not in VALUES:
      raise ValueError(f"invalid Roman numeral character '{char}'")
    value = VALUES[char]
    if value > previous:
      total += value - 2 * previous
    else:
      total += value
    previous = value
  if not 1 <= total <= 3999 or to_roman(total) != text.upper():
    raise ValueError(f"'{text}' is not a valid Roman numeral")
  return total


def main() -> None:
  if len(sys.argv) < 3:
    print("Usage: python main.py to <integer> | from <roman-numeral>")
    sys.exit(1)
  action = sys.argv[1].lower()
  arg = sys.argv[2]
  try:
    if action == "to":
      print(to_roman(int(arg)))
    elif action == "from":
      print(from_roman(arg))
    else:
      print(f"Error: unknown action '{action}', expected 'to' or 'from'")
      sys.exit(1)
  except ValueError as exc:
    print(f"Error: {exc}")
    sys.exit(1)


if __name__ == "__main__":
  main()
