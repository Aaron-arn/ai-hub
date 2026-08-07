"""Base converter: convert numbers between bases 2 through 36."""

import string
import sys

DIGITS = string.digits + string.ascii_lowercase


def to_int(text, base):
    text = text.strip().lower()
    if not text:
        raise ValueError("empty number")
    if base < 2 or base > 36:
        raise ValueError("base must be between 2 and 36")
    negative = text.startswith("-")
    if negative:
        text = text[1:]
    value = 0
    for char in text:
        if char not in DIGITS[:base]:
            raise ValueError(f"digit '{char}' not valid in base {base}")
        value = value * base + DIGITS.index(char)
    return -value if negative else value


def to_base(number, base):
    if base < 2 or base > 36:
        raise ValueError("base must be between 2 and 36")
    negative = number < 0
    number = abs(number)
    if number == 0:
        return "0"
    digits = []
    while number:
        digits.append(DIGITS[number % base])
        number //= base
    result = "".join(reversed(digits))
    return "-" + result if negative else result


def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <value> <from_base> <to_base>")
        print("Bases 2 through 36 are supported.")
        sys.exit(1)
    try:
        value = sys.argv[1]
        from_base = int(sys.argv[2])
        to_base_value = int(sys.argv[3])
        print(to_base(to_int(value, from_base), to_base_value))
    except ValueError as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
