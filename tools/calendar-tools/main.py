"""Calendar tools: month calendars, ISO week numbers and day-of-week calculations."""

import calendar
import sys
from datetime import date


def main() -> None:
  args = sys.argv[1:]
  if not args:
    print("Usage: python main.py month [YYYY [MM]] | year YYYY | week YYYY-MM-DD | weekday YYYY-MM-DD")
    sys.exit(1)
  command = args[0]
  today = date.today()
  try:
    if command == "month":
      year = int(args[1]) if len(args) > 1 else today.year
      month = int(args[2]) if len(args) > 2 else today.month
      if not 1 <= month <= 12:
        raise ValueError("month must be between 1 and 12")
      print(calendar.month(year, month))
    elif command == "year":
      if len(args) < 2:
        raise ValueError("year requires a year argument")
      print(calendar.calendar(int(args[1])))
    elif command == "week":
      if len(args) < 2:
        raise ValueError("week requires a date argument (YYYY-MM-DD)")
      day = date.fromisoformat(args[1])
      iso_year, iso_week, iso_weekday = day.isocalendar()
      print(f"{day.isoformat()} is a {day.strftime('%A')}, ISO week {iso_week} of year {iso_year}")
    elif command == "weekday":
      if len(args) < 2:
        raise ValueError("weekday requires a date argument (YYYY-MM-DD)")
      day = date.fromisoformat(args[1])
      print(f"{day.isoformat()} is a {day.strftime('%A')}")
    else:
      print(f"Error: unknown command '{command}'")
      sys.exit(1)
  except (ValueError, IndexError) as exc:
    print(f"Error: {exc}")
    sys.exit(1)


if __name__ == "__main__":
  main()
