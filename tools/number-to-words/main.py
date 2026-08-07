"""Number to words: converts numbers into English words."""

import re
import sys

ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
        "eighty", "ninety"]
SCALES = ["", "thousand", "million", "billion", "trillion", "quadrillion",
          "quintillion", "sextillion"]
NUMBER_RE = re.compile(r"^-?\d+(\.\d+)?$")


def below_1000(n):
  words = []
  if n >= 100:
    words.append(ONES[n // 100] + " hundred")
    n %= 100
  if n >= 20:
    tens = TENS[n // 10]
    n %= 10
    words.append(tens if not n else f"{tens}-{ONES[n]}")
  elif n > 0:
    words.append(ONES[n])
  return " ".join(words)


def integer_to_words(n):
  if n == 0:
    return "zero"
  chunks = []
  while n:
    chunks.append(n % 1000)
    n //= 1000
  if len(chunks) > len(SCALES):
    raise ValueError("number is too large")
  words = []
  for index in range(len(chunks) - 1, -1, -1):
    if chunks[index]:
      part = below_1000(chunks[index])
      if SCALES[index]:
        part += " " + SCALES[index]
      words.append(part)
  return " ".join(words)


def number_to_words(raw):
  if not NUMBER_RE.match(raw):
    raise ValueError(f"'{raw}' is not a valid number")
  negative = raw.startswith("-")
  digits = raw.lstrip("-")
  if "." in digits:
    whole, fraction = digits.split(".", 1)
    fraction = fraction.rstrip("0")
    words = integer_to_words(int(whole or "0"))
    if fraction:
      words += " point " + " ".join(ONES[int(digit)] for digit in fraction)
  else:
    words = integer_to_words(int(digits))
  return "negative " + words if negative else words


def main() -> None:
  if len(sys.argv) < 2:
    print("Usage: python main.py <number>")
    sys.exit(1)
  try:
    print(number_to_words(sys.argv[1]))
  except ValueError as exc:
    print(f"Error: {exc}")
    sys.exit(1)


if __name__ == "__main__":
  main()
