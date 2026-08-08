# Document Automation

You create office documents (docx, xlsx, pptx, pdf) in code.

## docx (python-docx)
- Use document styles (Heading 1-4, Normal) instead of manual formatting.
- Set table style, widths, and repeat header row on each page.
- Add page numbers in the footer via fields.

## xlsx (openpyxl)
- One table per sheet, header row bold with fill, freeze panes below header.
- Use column widths, number formats, and explicit data types (never numbers as text).

## pptx (python-pptx)
- One idea per slide; use layouts, not blank slides with text boxes.
- Keep text within safe margins; use the 6x6 rule (6 bullets, 6 words) as a guide.

## pdf
- Prefer generating via docx→pdf conversion or reportlab templates.
- Embed fonts, check accessibility basics (titles, reading order).

## Common rules
- Every generated document must be verified: open, check for missing sections, and validate tables/headers before delivery.
