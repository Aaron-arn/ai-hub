"""ASCII table: renders rows of data as a bordered ASCII table."""

import csv
import sys


def cell_text(row, index, widths):
  value = str(row[index]) if index < len(row) else ""
  return f" {value.ljust(widths[index])} "


def render(rows):
  headers = rows[0]
  body = rows[1:]
  widths = [len(str(cell)) for cell in headers]
  for row in body:
    for index in range(len(widths)):
      value = str(row[index]) if index < len(row) else ""
      widths[index] = max(widths[index], len(value))
  border = "+" + "+".join("-" * (width + 2) for width in widths) + "+"
  lines = [border]
  lines.append("|" + "|".join(cell_text(headers, index, widths) for index in range(len(widths))) + "|")
  lines.append(border)
  for row in body:
    lines.append("|" + "|".join(cell_text(row, index, widths) for index in range(len(widths))) + "|")
  lines.append(border)
  return "\n".join(lines)


def parse_rows(lines):
  rows = []
  for line in lines:
    rows.append(next(csv.reader([line])))
  return rows


def main() -> None:
  if len(sys.argv) > 1:
    lines = sys.argv[1:]
  else:
    if sys.stdin.isatty():
      print("Usage: python main.py \"<header1>,<header2>\" \"<value1>,<value2>\" ...")
      sys.exit(1)
    lines = [line.strip() for line in sys.stdin if line.strip()]
  rows = parse_rows(lines)
  if not rows:
    print("Error: no data provided")
    sys.exit(1)
  print(render(rows))


if __name__ == "__main__":
  main()
