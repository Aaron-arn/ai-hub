import argparse
import re
import sys

WPM = 200

def main():
    ap = argparse.ArgumentParser(description="Count words in text files")
    ap.add_argument("inputs", nargs="*", help="input files (default: stdin)")
    ap.add_argument("--chars", action="store_true", help="count characters too")
    ap.add_argument("--unique", action="store_true", help="count unique words")
    args = ap.parse_args()

    def analyze(name, text):
        words = re.findall(r"[\w'-]+", text.lower())
        sentences = re.split(r"[.!?]+\s+", text.strip())
        minutes = len(words) / WPM
        line = f"{name}: {len(words)} words, {len(text)} chars, {len(text.splitlines())} lines, ~{minutes:.1f} min read"
        if args.chars:
            line += f", {len(text)} total chars"
        if args.unique:
            line += f", {len(set(words))} unique"
        print(line)

    if args.inputs:
        for path in args.inputs:
            with open(path, encoding="utf-8", errors="replace") as fh:
                analyze(path, fh.read())
    else:
        analyze("stdin", sys.stdin.read())

if __name__ == "__main__":
    main()
