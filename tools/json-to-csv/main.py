import argparse
import csv
import json
import sys

def flatten(obj, prefix=""):
    out = {}
    if isinstance(obj, dict):
        for k, v in obj.items():
            key = f"{prefix}.{k}" if prefix else k
            if isinstance(v, (dict, list)):
                if isinstance(v, list) and v and not isinstance(v[0], (dict, list)):
                    out[key] = json.dumps(v, ensure_ascii=False)
                else:
                    out.update(flatten(v, key))
            else:
                out[key] = v
    elif isinstance(obj, list):
        out[prefix] = json.dumps(obj, ensure_ascii=False)
    return out

def main():
    ap = argparse.ArgumentParser(description="Convert JSON to CSV")
    ap.add_argument("input", nargs="?", default=None, help="input JSON (default: stdin)")
    ap.add_argument("-o", "--output", default=None, help="output CSV path")
    args = ap.parse_args()

    fh = open(args.input, encoding="utf-8") if args.input else sys.stdin
    data = json.load(fh)
    if isinstance(data, dict):
        data = [data]
    rows = [flatten(rec) for rec in data]
    fields = []
    for row in rows:
        for k in row:
            if k not in fields:
                fields.append(k)

    out = open(args.output, "w", newline="", encoding="utf-8") if args.output else sys.stdout
    writer = csv.DictWriter(out, fieldnames=fields, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)
    if args.output:
        out.close()
        print(f"Wrote {args.output} ({len(rows)} rows)")

if __name__ == "__main__":
    main()
