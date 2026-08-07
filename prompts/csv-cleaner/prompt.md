# CSV Cleaner

## Description

Builds a Python script that cleans a messy CSV file end to end: deduplication, type coercion, date normalization, and a summary report. Use it when you receive exported spreadsheets with inconsistent values and you want a repeatable, documented cleaning pipeline instead of manual Excel edits.

## Prompt

You are a data-cleaning specialist. Write a Python 3 script `clean_csv.py` that cleans a messy CSV and produces a report. Use only the standard library (`csv`, `datetime`, `statistics`, `collections`).

Input file `sales.csv` looks like this:

```csv
order_id,date,customer,amount,country,sku
ORD-1,2025/03/14,jane@example.com,"1,250.50",FR,SKU-1
ORD-2,03-15-2025,JOHN@EXAMPLE.COM,25,US,sku-1
ORD-1,2025/03/14,jane@example.com,"1,250.50",FR,SKU-1
ORD-3,2025/3/15,jane@example.com,,FR,SKU-9
ORD-4,16/03/2025,bob@example.com,"12,5",FR,SKU-2
```

Cleaning rules:
1. Deduplicate by `order_id`, keeping the first occurrence; count removed rows.
2. Normalize `date` to `YYYY-MM-DD`. Accept these formats: `YYYY/MM/DD`, `MM-DD-YYYY`, `D/MM/YYYY`, `YYYY/M/D`. Invalid dates are left blank and counted.
3. Normalize `amount`: strip quotes, remove thousand separators, convert comma to decimal point, parse as float; invalid amounts become blank and are counted.
4. Lowercase `customer` email, trim whitespace on all fields, and uppercase `country` (2-letter codes only; anything else becomes blank).
5. Uppercase `sku`.
6. Drop rows where both `amount` and `date` are blank.
7. Write `sales_clean.csv` with the same columns and header.

Report printed at the end (plain text): total input rows, rows kept, duplicate rows removed, blank dates, blank amounts, invalid countries, and the mean and median of `amount` on the cleaned data.

Output: the full script in one code block, then the expected report output for the sample above.

## Notes

Paste a real sample of your own CSV (first 10 lines) to have the rules adapted to its quirks. Add `--dry-run` if you want a preview mode before writing the output file.
