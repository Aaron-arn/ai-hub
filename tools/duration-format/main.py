"""Duration format: humanizes durations between two dates or from a number of seconds."""

import calendar
import sys
from datetime import date

UNITS = [("year", 365 * 24 * 3600), ("day", 24 * 3600), ("hour", 3600),
        ("minute", 60), ("second", 1)]


def humanize_seconds(total):
  total = int(total)
  if total < 0:
    raise ValueError("duration cannot be negative")
  parts = []
  for name, size in UNITS:
    count, total = divmod(total, size)
    if count:
      parts.append(f"{count} {name}" + ("s" if count != 1 else ""))
  return ", ".join(parts) if parts else "0 seconds"


def add_months(day, months):
  month_index = day.month + months
  year = day.year + (month_index - 1) // 12
  month = (month_index - 1) % 12 + 1
  last_day = calendar.monthrange(year, month)[1]
  return date(year, month, min(day.day, last_day))


def humanize_dates(start, end):
  if end < start:
    start, end = end, start
  total_months = (end.year - start.year) * 12 + (end.month - start.month)
  if end.day < start.day:
    total_months -= 1
  years, months = divmod(total_months, 12)
  days = (end - add_months(start, total_months)).days
  parts = []
  for name, count in (("year", years), ("month", months), ("day", days)):
    if count:
      parts.append(f"{count} {name}" + ("s" if count != 1 else ""))
  return ", ".join(parts) if parts else "same day"


def parse_date(raw):
  try:
    return date.fromisoformat(raw)
  except ValueError:
    print(f"Error: '{raw}' is not a valid date (expected YYYY-MM-DD)")
    sys.exit(1)


def main() -> None:
  args = sys.argv[1:]
  if len(args) == 1:
    try:
      print(humanize_seconds(float(args[0])))
    except ValueError:
      print(f"Error: '{args[0]}' is not a valid number of seconds")
      sys.exit(1)
    return
  if "--from" in args:
    if "--to" not in args:
      print("Error: --from requires --to")
      sys.exit(1)
    start = parse_date(args[args.index("--from") + 1])
    end = parse_date(args[args.index("--to") + 1])
    print(humanize_dates(start, end))
    return
  if len(args) == 2:
    print(humanize_dates(parse_date(args[0]), parse_date(args[1])))
    return
  print("Usage: python main.py <seconds> | --from <YYYY-MM-DD> --to <YYYY-MM-DD>")
  sys.exit(1)


if __name__ == "__main__":
  main()
