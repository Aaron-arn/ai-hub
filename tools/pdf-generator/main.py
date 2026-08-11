import argparse
import sys
from fpdf import FPDF

def main():
    ap = argparse.ArgumentParser(description="Generate a PDF from text input")
    ap.add_argument("output", help="output PDF path")
    ap.add_argument("input", nargs="?", help="input text file (default: stdin)")
    ap.add_argument("--title", default=None, help="document title")
    ap.add_argument("--size", choices=["A4", "Letter"], default="A4")
    args = ap.parse_args()

    text = open(args.input, encoding="utf-8").read() if args.input else sys.stdin.read()

    pdf = FPDF(format=args.size)
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    if args.title:
        pdf.set_font("Helvetica", "B", 18)
        pdf.cell(0, 12, args.title, new_x="LMARGIN", new_y="NEXT")
        pdf.ln(4)
        pdf.set_draw_color(120)
        pdf.line(10, pdf.get_y(), pdf.w - 10, pdf.get_y())
        pdf.ln(6)
    pdf.set_font("Helvetica", size=11)
    for line in text.splitlines():
        if pdf.get_y() > pdf.h - 20:
            pdf.add_page()
            pdf.set_font("Helvetica", size=11)
        pdf.multi_cell(0, 6, line)
    pdf.output(args.output)
    print(f"Wrote {args.output}")

if __name__ == "__main__":
    main()
