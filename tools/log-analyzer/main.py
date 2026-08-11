import argparse
import re
import sys
from collections import Counter

LEVEL_RE = re.compile(r"\b(ERROR|WARN(?:ING)?|INFO|DEBUG|FATAL|CRITICAL)\b", re.IGNORECASE)

def main():
    ap = argparse.ArgumentParser(description="Summarize a log file")
    ap.add_argument("input", nargs="?", default=None, help="log file (default: stdin)")
    ap.add_argument("--top", type=int, default=15, help="top patterns per level")
    args = ap.parse_args()

    fh = open(args.input, encoding="utf-8", errors="replace") if args.input else sys.stdin
    levels = Counter()
    messages = Counter()
    lines = 0
    for line in fh:
        lines += 1
        m = LEVEL_RE.search(line)
        if not m:
            continue
        level = m.group(1).upper()
        levels[level] += 1
        key = re.sub(r"\b[\w.+-]+@[\w.-]+\b", "<email>", line)
        key = re.sub(r"(\d{1,3}\.){3}\d{1,3}", "<ip>", key)
        key = re.sub(r"0x[0-9a-fA-F]+", "<hex>", key)
        key = re.sub(r"\b\d+\b", "<n>", key)
        key = re.sub(r"[\s\S]{0,60}$", "", key).rstrip()
        messages[(level, key)] += 1

    print(f"lines: {lines}")
    print(f"levels: {dict(levels)}")
    for level in ["FATAL", "ERROR", "CRITICAL", "WARN", "WARNING", "INFO", "DEBUG"]:
        subset = {(k, n) for (lvl, k), n in messages.items() if lvl == level}
        if not subset:
            continue
        print(f"\n== {level} == (top {args.top})")
        for (k, n) in sorted(subset, key=lambda x: -x[1])[: args.top]:
            print(f"  {n:6d}  {k}")

if __name__ == "__main__":
    main()
