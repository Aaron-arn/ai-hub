# Code Reviewer

## Description

Pastes a code snippet (or a whole file) and receives a structured review: issues ranked by severity, each with a concrete fix and a short rationale. Use it before opening a PR or merging a refactor, to catch bugs, security problems, and maintainability traps that a quick glance misses.

## Prompt

You are a senior software engineer doing a code review. Review this Python function and rank your findings.

```python
def process_payments(rows, config):
    results = []
    for row in rows:
        amount = row.get("amount", 0)
        fee = config.fee_rate * amount
        if row.get("currency") == "USD":
            fee = fee + 1
        result = {"id": row["id"], "net": amount - fee}
        if row.get("retry_count", 0) > 3:
            continue
        results.append(result)
    results.sort(key=lambda r: r["net"], reverse=True)
    return results
```

The caller does: `net = process_payments(data, cfg)[0]["net"]` and `config.fee_rate` is read from an unvalidated settings file.

Deliverables:
1. A findings table with columns: severity (Critical/High/Medium/Low), line or code fragment, issue, and suggested fix. Identify at least 6 findings. Candidates to check: unhandled `KeyError` on `row["id"]` when id is missing, negative `net` for very high fees, `float` rounding on money, mutation of the input list ordering expectation, `row.get("amount")` with a None value, lack of input validation, the `continue`-then-sort interaction, and the caller's assumption that the list is non-empty (IndexError).
2. Rank each finding and justify the ranking in one line: which ones can lose money, crash the app, or are style-only.
3. Provide the corrected function (full block) that fixes the Critical and High findings without changing behavior.
4. Write a one-paragraph review summary in the tone of a PR comment: 3 sentences, professional, no sarcasm, ending with a "LGTM after changes" statement.
5. List 2 tests that would have caught the Critical finding.

Output the table, the corrected code block, the summary paragraph, and the test names.

## Notes

Paste diffs for review-in-place. For a stricter pass, ask to also flag performance issues and security (SQL injection, secrets) explicitly.
