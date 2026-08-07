"""Cron parser: parses 5-field cron expressions and describes their schedules."""

import sys

FIELDS = ["minute", "hour", "day of month", "month", "day of week"]
BOUNDS = [(0, 59), (0, 23), (1, 31), (1, 12), (0, 6)]
WEEKDAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


def parse_field(part, low, high):
  if part == "*":
    return set(range(low, high + 1))
  if "/" in part:
    base, step = part.split("/", 1)
    if not step.isdigit() or int(step) < 1:
      raise ValueError(f"invalid step '{step}'")
    start = low if base in ("", "*") else min(parse_field(base, low, high))
    return set(range(start, high + 1, int(step)))
  values = set()
  for token in part.split(","):
    if "-" in token:
      pieces = token.split("-", 1)
      if len(pieces) != 2 or not pieces[0].isdigit() or not pieces[1].isdigit():
        raise ValueError(f"invalid range '{token}'")
      start, end = int(pieces[0]), int(pieces[1])
      if not low <= start <= end <= high:
        raise ValueError(f"range '{token}' out of bounds ({low}-{high})")
      values.update(range(start, end + 1))
    elif token.isdigit():
      value = int(token)
      if not low <= value <= high:
        raise ValueError(f"value {value} out of bounds ({low}-{high})")
      values.add(value)
    else:
      raise ValueError(f"invalid token '{token}'")
  return values


def summarize(values, formatter):
  ordered = sorted(values)
  if len(ordered) == 1:
    return formatter(ordered[0])
  return ", ".join(formatter(v) for v in ordered)


def describe_time(hours, minutes):
  if hours == set(range(24)) and minutes == set(range(60)):
    return "every minute"
  if hours == set(range(24)):
    plural = "s" if len(minutes) > 1 else ""
    return f"every hour at minute{plural} {summarize(minutes, str)}"
  if minutes == set(range(60)):
    plural = "s" if len(hours) > 1 else ""
    return f"at every minute of hour{plural} {summarize(hours, str)}"
  if len(hours) == 1 and len(minutes) == 1:
    return f"at {sorted(hours)[0]:02d}:{sorted(minutes)[0]:02d}"
  return f"at minute {summarize(minutes, str)} of hour {summarize(hours, str)}"


def describe(values):
  minutes, hours, dom, month, dow = values
  clauses = []
  if month != set(range(1, 13)):
    clauses.append("in " + summarize(month, lambda m: MONTHS[m - 1]))
  if dom != set(range(1, 32)):
    plural = "s" if len(dom) > 1 else ""
    clauses.append(f"on day{plural} {summarize(dom, str)} of month")
  if dow != set(range(7)):
    clauses.append("on " + summarize(dow, lambda d: WEEKDAYS[d]))
  schedule = describe_time(hours, minutes)
  if clauses:
    schedule += " " + " ".join(clauses)
  return schedule


def main() -> None:
  if len(sys.argv) < 2:
    print("Usage: python main.py \"<minute> <hour> <dom> <month> <dow>\"")
    sys.exit(1)
  parts = sys.argv[1].split()
  if len(parts) != 5:
    print("Error: cron expression must have exactly 5 fields")
    sys.exit(1)
  try:
    values = [parse_field(part, low, high) for part, (low, high) in zip(parts, BOUNDS)]
  except ValueError as exc:
    print(f"Error: invalid field: {exc}")
    sys.exit(1)
  print(describe(values))


if __name__ == "__main__":
  main()
