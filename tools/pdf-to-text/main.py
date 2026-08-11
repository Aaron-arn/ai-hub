import argparse
from pypdf import PdfReader

def main():
    ap = argparse.ArgumentParser(description="Extract text from a PDF")
    ap.add_argument("input", help="input PDF")
    ap.add_argument("output", nargs="?", help="output .txt (default: stdout)")
    ap.add_argument("--pages", help="page ranges, e.g. '1-3,5'")
    args = ap.parse_args()

    reader = PdfReader(args.input)
    selected = set()
    if args.pages:
        for part in args.pages.split(","):
            part = part.strip()
            if "-" in part:
                a, _, b = part.partition("-")
                selected.update(range(int(a), int(b) + 1))
            else:
                selected.add(int(part))

    chunks = []
    for i, page in enumerate(reader.pages, start=1):
        if selected and i not in selected:
            continue
        text = page.extract_text() or ""
        chunks.append(f"--- page {i} ---\n{text}")
    result = "\n".join(chunks)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(result)
        print(f"Wrote {args.output}")
    else:
        print(result)

if __name__ == "__main__":
    main()
