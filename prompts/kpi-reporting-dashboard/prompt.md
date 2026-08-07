# KPI Reporting Dashboard Builder

## Description

Designs a KPI dashboard structure with the right metrics, targets, and reporting rhythm. Use it when starting to measure a business area or when your current dashboard shows vanity numbers. Output is a prioritized metric list you can build in any BI tool or spreadsheet.

## Prompt

You are a data analyst who designs reporting dashboards that executives and teams actually use. Design a KPI dashboard for my context.

What I want to track: [e.g. SaaS growth, e-commerce sales, marketing, customer support]
Business model: [one sentence describing how money is made]
Stage: [early / growing / mature]
Who reads this dashboard: [e.g. founder daily, team weekly, board monthly]
Current data available: [what tools or data you already have]

Deliver:
1. A North Star metric: the single metric that best reflects value delivered to customers, with a one-paragraph justification.
2. A metric hierarchy: 3 levels - top metrics (5 max), supporting metrics (5-8), and diagnostic metrics behind each top metric. Label each metric as leading or lagging.
3. For every metric: definition, formula or source, a suggested target or benchmark, and how often it should be reviewed (daily/weekly/monthly).
4. A one-page dashboard layout: where each metric goes (top row, middle, drill-down), including one ratio metric and one trend chart per top metric.
5. Which 3 metrics are most likely to be gamed or misinterpreted, with a guardrail for each.
6. The first 3 actions to take with the data: what pattern to look for each week and what decision it should drive.

Rules: exclude vanity metrics (page views, registered users) unless they feed a real decision. If my stage is early, bias toward metrics that predict retention over revenue.

## Notes

Paste a sample of your current data to get benchmark suggestions. Review the dashboard quarterly and retire metrics nobody acts on.
