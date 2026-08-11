import argparse
import sys
from pypdf import PdfReader, PdfWriter

def parse_ranges(spec):
    if not spec:
        return None
    pages = set()
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            a, _, b = part.partition("-")
            pages.update(range(int(a), int(b) + 1))
        else:
            pages.add(int(part))
    return pages

def main():
    ap = argparse.ArgumentParser(description="Merge PDF files")
    ap.add_argument("inputs", nargs="+", help="input PDFs")
    ap.add_argument("-o", "--output", default="merged.pdf", help="output path")
    ap.add_argument("--pages", help="keep only pages, e.g. '1-3,5' (per input file)")
    args = ap.parse_args()

    writer = PdfWriter()
    keep = parse_ranges(args.pages)
    for path in args.inputs:
        reader = PdfReader(path)
        for i, page in enumerate(reader.pages, start=1):
            if keep is None or i in keep:
                writer.add_page(page)
    writer.add_metadata({"/Title": args.output})
    with open(args.output, "wb") as fh:
        writer.write(fh)
    print(f"Wrote {args.output} with {len(writer.pages)} pages")

if __name__ == "__main__":
    main()
