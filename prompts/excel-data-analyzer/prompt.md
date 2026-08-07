# Excel Data Analyzer

## Description

Describes the structure of a spreadsheet and a business question, and receives the exact formulas, PivotTable setup, or Power Query steps needed to answer it. Use it when you analyze exports in Excel and want repeatable, correct calculations without trial-and-error with formulas.

## Prompt

You are an Excel analyst expert. My sheet `Sheet1` has a header row in row 1, data from row 2. Columns: `A: OrderDate` (real Excel dates), `B: Region` (North, South, East, West), `C: Product`, `D: Units`, `E: UnitPrice` (currency), `F: Rep` (may be blank).

I need to answer these questions. For each, give a working solution:

1. Total revenue per region. Provide (a) a SUMIFS formula in a summary block starting at `H2` with region labels in column G, and (b) the steps to build an equivalent PivotTable (rows = Region, values = Sum of Revenue) after adding a helper column `G2 = D2*E2`.
2. Best month (by revenue) for the current year: a `SUMPRODUCT` formula with `MONTH`/`YEAR` conditions on the helper column, plus the month name via `TEXT`.
3. Top 3 products by units in the West region: an array formula using `LARGE` + `IF` (Ctrl+Shift+Enter in older Excel, dynamic arrays in Microsoft 365), and a simpler filter + `SORT` alternative.
4. The `Rep` column has blanks: give an INDEX/MATCH-based formula that fills blank F cells from a lookup table `Reps` (columns `J: Region`, `K: Rep`) when a region has exactly one rep, else leaves blank.
5. Power Query: 3 numbered steps to load this table, rename columns, and change `OrderDate` to date type, so the result refreshes automatically.

Format the answer as one numbered section per question, formulas in code blocks labeled with the target cell, and PivotTable steps at most 6 bullets.

## Notes

Adapt the column letters to your own sheet and the answers keep working. Ask for a `LET`-based version for Microsoft 365 or a VBA macro if you want the analysis fully automated.
