# Data Cleaning

## Description

Plan and implement a data cleaning pipeline for messy datasets.

## Prompt

Design a data cleaning pipeline for this dataset description: {DATA_DESCRIPTION}

Steps:
1. AUDIT: list expected issues by category - missing values (counts), duplicates (exact vs fuzzy), types (wrong dtype, mixed), outliers (method: IQR or z-score), inconsistencies (casing, spacing, formats)
2. PIPELINE: numbered cleaning steps with pandas code snippets, each idempotent and logged
3. RULES: explicit decisions - drop vs impute vs flag (with justification), dedup key choice
4. QA: validation checks after cleaning (row counts, nulls, duplicates, range checks) as assert statements
5. REPRODUCIBILITY: how to version the output (hash of input + pipeline version)

Output as a Python module skeleton with a `clean(df) -> (df, report)` signature and a printed summary report of every transformation.
