import argparse
import csv
import json
import sys

def main():
    ap = argparse.ArgumentParser(description="Convert CSV to JSON")
    ap.add_argument("input", nargs="?", default=None, help="input CSV (default: stdin)")
    ap.add_argument("-o", "--output", default=None, help="output JSON path")
    ap.add_argument("--ndjson", action="store_true", help="one JSON object per line")
    ap.add_argument("--delimiter", default=",")
    args = ap.parse_args()

    fh = open(args.input, newline="", encoding="utf-8") if args.input else sys.stdin
    reader = csv.DictReader(fh, delimiter=args.delimiter)
    records = []
    for row in reader:
        records.append({k: (v if v != "" else None) for k, v in row.items()})

    text = ""
    if args.ndjson:
        text = "\n".join(json.dumps(r, ensure_ascii=False) for r in records) + "\n"
    else:
        text = json.dumps(records, indent=2, ensure_ascii=False) + "\n"

    if args.output:
        with open(args.output, "w", encoding="utf-8") as out:
            out.write(text)
        print(f"Wrote {args.output} ({len(records)} records)")
    else:
        sys.stdout.write(text)

if __name__ == "__main__":
    main()
