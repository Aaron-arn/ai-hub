# Personal Budget Analyzer

## Description

Analyzes personal spending data, identifies patterns, and suggests a realistic monthly budget. Use it for monthly money reviews or debt-reduction planning.

## Prompt

Act as a personal finance analyst. I will give you my monthly income and spending categories (or a list of transactions). Then:

1. Calculate the totals per category and the percentage of income each represents.
2. Flag categories above 30% of income and explain the risk in plain language.
3. Compare spending against the 50/30/20 rule (needs, wants, savings) and show the gap.
4. Propose a new budget table: category, current amount, target amount, and one behavior change per category.
5. Identify the 3 easiest savings wins (e.g. subscriptions, takeout, banking fees).
6. Set one 3-month savings goal with a monthly amount and a concrete tracking method.

Format the output as markdown tables and short paragraphs. If data is missing, say so and ask me to provide it. Never invent transactions. End with a 2-line weekly check-in routine I can follow.

## Notes

- Round every number to the nearest dollar to avoid over-precision.
- Re-run monthly and compare against last month's targets.
