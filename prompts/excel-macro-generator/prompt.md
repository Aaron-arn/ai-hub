# Excel Macro Generator

## Description

Produces a complete, copy-paste-ready VBA macro that automates a repetitive Excel task on the active worksheet. Use it when you keep formatting, cleaning, or summarizing the same spreadsheet by hand. The macro is defensive: it checks selection, protects against empty sheets, and tells you what it did.

## Prompt

You are an Excel VBA expert. Write a macro named `CleanAndSummarize` that automates the following recurring task on the active worksheet (sheet name may vary):

1. Find the last used row and last used column using `UsedRange`.
2. Detect the header row: assume row 1 contains headers; if the active cell is in row 1, treat the current column's header as the "amount" column, otherwise ask for a message box fallback.
3. In the amount column: remove `$`, spaces, and non-numeric characters with `Val`; blank cells are skipped, non-numeric values are highlighted yellow.
4. Remove fully empty rows.
5. Auto-fit all columns, freeze the header row with `FreezePanes`.
6. Below the data (two blank rows), write `Total`, `Count`, and `Average` in bold with `SUM`, `COUNTA`, and `AVERAGE` formulas for the amount column.
7. Set the sheet to landscape orientation and fit to one page wide (`Zoom = False`, `FitToPagesWide = 1`).
8. Show a `MsgBox` reporting rows processed and total.

Requirements: use `Option Explicit`, declare every variable with explicit types, wrap the body in `On Error GoTo` with a friendly error message, add a comment header with purpose and date, and make the code work when the sheet has no data. Keep it under 100 lines. Output one code block, then 3 lines explaining how to install it (Alt+F11, Insert > Module, paste, run with F5 or assign to a button).

## Notes

State the exact columns and transformations of your own sheet and the macro adapts directly. Ask for a `Worksheet_Change` version if you want it to run automatically on edits.
