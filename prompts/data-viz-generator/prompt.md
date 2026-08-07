# Data Visualization Generator

## Description

Describes a dataset and the story you want to tell, and receives a complete Python chart script (matplotlib or plotly) with clean styling and sensible defaults. Use it when you need publication-ready charts from CSV or JSON data without wrestling with matplotlib boilerplate.

## Prompt

You are a data visualization specialist. Write a Python script `charts.py` that reads `sales.csv` (columns: `date` in `YYYY-MM-DD`, `region` in `North|South|East|West`, `product`, `units`, `revenue`) and produces three charts using `pandas` and `matplotlib` (no seaborn).

Chart requirements:
1. Monthly revenue trend: one line per region, x = month (label `%b %y`), y = sum of revenue, distinct colors, legend outside top-right, grid on y only.
2. Revenue share by product: a horizontal bar chart sorted descending, with percentage labels at the end of each bar and a title stating the total revenue.
3. Units by region: a box plot of `units` per region showing spread and outliers, with a note in the caption on which region has the most outliers.
4. A fourth quick view: a 2x2 subplot layout combining the three charts and a small table of top 5 product revenues in a text box.

Styling requirements for all charts:
- Consistent figure size 10x6, dpi 150, tight layout, `plt.rcParams` with font family `DejaVu Sans`, font size 10.
- Colorblind-safe palette (`#1f77b4`, `#ff7f0e`, `#2ca02c`, `#d62728`).
- Every axis labeled, every chart titled, dates parsed with `pd.to_datetime` and invalid dates dropped.
- No `show()` calls; save each figure with `savefig` to `out_<name>.png`, and print the paths at the end.

Also: if the CSV has fewer than 2 regions or 0 rows, print a friendly error and exit code 1. Output the full script in one code block (under 160 lines), then a line listing the four output filenames.

## Notes

Say whether you want interactive charts and the assistant switches to plotly with hover tooltips. Add a `--style dark` option if your charts must match a dark dashboard theme.
