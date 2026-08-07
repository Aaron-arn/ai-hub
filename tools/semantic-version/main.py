"""Semantic version tool: parses, validates and compares SemVer 2.0.0 strings."""

import re
import sys

SEMVER_RE = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?"
    r"(?:\+([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?$"
)


def parse(version):
  match = SEMVER_RE.match(version)
  if not match:
    raise ValueError(f"'{version}' is not a valid semantic version")
  return {
      "major": int(match.group(1)),
      "minor": int(match.group(2)),
      "patch": int(match.group(3)),
      "prerelease": match.group(4) or "",
      "build": match.group(5) or "",
  }


def compare_prerelease(left, right):
  left_ids, right_ids = left.split("."), right.split(".")
  for a, b in zip(left_ids, right_ids):
    if a == b:
      continue
    a_is_num, b_is_num = a.isdigit(), b.isdigit()
    if a_is_num and b_is_num:
      return 1 if int(a) > int(b) else -1
    if a_is_num:
      return -1
    if b_is_num:
      return 1
    return 1 if a > b else -1
  return 1 if len(left_ids) > len(right_ids) else -1


def compare(left, right):
  a, b = parse(left), parse(right)
  for key in ("major", "minor", "patch"):
    if a[key] != b[key]:
      return 1 if a[key] > b[key] else -1
  if a["prerelease"] == b["prerelease"]:
    return 0
  if not a["prerelease"]:
    return 1
  if not b["prerelease"]:
    return -1
  return compare_prerelease(a["prerelease"], b["prerelease"])


def main() -> None:
  if len(sys.argv) < 3:
    print("Usage: python main.py parse <version> | compare <version> <version>")
    sys.exit(1)
  command = sys.argv[1].lower()
  try:
    if command == "parse":
      parsed = parse(sys.argv[2])
      for key in ("major", "minor", "patch", "prerelease", "build"):
        value = parsed[key]
        print(f"{key}: {value if value else '(none)'}")
    elif command == "compare":
      if len(sys.argv) < 4:
        print("Error: compare requires two versions")
        sys.exit(1)
      left, right = sys.argv[2], sys.argv[3]
      result = compare(left, right)
      if result == 0:
        print(f"{left} == {right}")
      elif result > 0:
        print(f"{left} > {right}")
      else:
        print(f"{left} < {right}")
    else:
      print(f"Error: unknown command '{command}', expected 'parse' or 'compare'")
      sys.exit(1)
  except ValueError as exc:
    print(f"Error: {exc}")
    sys.exit(1)


if __name__ == "__main__":
  main()
