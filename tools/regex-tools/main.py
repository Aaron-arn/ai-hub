"""Regex tools: test regular expressions and extract matching groups."""

import re
import sys


def usage():
    print("Usage: python main.py <pattern> \"<text>\" [--replace <replacement>]")


def main():
    args = sys.argv[1:]
    replacement = None
    if "--replace" in args:
        i = args.index("--replace")
        if i + 1 >= len(args):
            print("Error: --replace requires a value")
            sys.exit(1)
        replacement = args[i + 1]
        del args[i:i + 2]
    if len(args) < 2:
        usage()
        sys.exit(1)
    pattern = args[0]
    text = " ".join(args[1:])
    try:
        regex = re.compile(pattern)
    except re.error as exc:
        print(f"Error: invalid pattern: {exc}")
        sys.exit(1)
    if replacement is not None:
        try:
            print(regex.sub(replacement, text))
        except re.error as exc:
            print(f"Error: invalid replacement: {exc}")
            sys.exit(1)
        return
    matches = list(regex.finditer(text))
    if not matches:
        print("No match")
        return
    for match in matches:
        if match.groups():
            print(f"{match.group(0)} -> groups: {match.groups()}")
        else:
            print(match.group(0))


if __name__ == "__main__":
    main()
