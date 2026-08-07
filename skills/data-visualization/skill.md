# Data Visualization

You build charts that communicate truthfully and instantly, choosing the form that matches the question.

## Choose the right chart

- Time trends: line chart (many points) or bar chart (few time buckets).
- Comparison across categories: bar chart, sorted when order is not meaningful.
- Distribution: histogram for continuous, bar for categorical; box plot for spread.
- Part to whole: stacked bar or treemap; use pie charts only for a few segments and never for precision.
- Relationship between two variables: scatter plot; avoid scatter when either axis is time.
- Ranking: horizontal bars; composition over time: stacked or area chart.
- When in doubt, a simple well-labeled bar or line chart beats a clever one.

## Axes and scales

- Always start the numeric axis at zero for bar charts; truncating the axis exaggerates differences.
- For line charts comparing trends, zero baseline is not mandatory, but label the axis clearly.
- Use consistent scales when comparing multiple panels side by side.
- Never use dual axes unless the two series are provably comparable; prefer small multiples.
- Show the unit on every axis (`revenue ($)`, `latency (ms)`) and format large numbers (`1.2M`, not `1200000`).

## Encoding

- Use position and length for the primary comparison; they are the most accurately read channels.
- Use color for grouping or highlighting, not as a third numeric scale unless essential.
- Reserve red for the key takeaway or the negative finding; do not color for decoration.
- Limit categorical palettes to about 8 distinguishable colors; use labels as backup.
- Sort categorical bars by value by default; alphabetical order hides the story.

## Labels and annotation

- Title the chart as a sentence that states the takeaway: "Sales doubled after the summer launch".
- Label data points directly when there are few; use a legend only when direct labels crowd the chart.
- Annotate anomalies, reference lines (targets, averages), and regime changes.
- Provide tooltips or tables with exact values; never make the viewer estimate.
- Label your data source and time period in a caption.

## Honesty

- Do not truncate bars, reorder time, or change scales to exaggerate differences.
- Show uncertainty (error bars, confidence bands) when the estimate is noisy.
- Aggregate with care: different summary statistics can paint very different pictures.
- Do not use 3D effects, chartjunk, or gratuitous gradients; they obscure data.
- If a chart lies, even by accident, use a different chart; honesty over decoration.
- Include the null case: show zero and the full range so small effects are not inflated.
