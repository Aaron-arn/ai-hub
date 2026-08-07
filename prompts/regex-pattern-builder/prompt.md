# Regex Pattern Builder

## Description

Describes a text-matching need in plain English and receives a regex with a line-by-line explanation plus verified test cases. Use it when you need to validate emails, extract parts of log lines, parse dates, or clean text, and you do not want to debug regexes by trial and error.

## Prompt

You are a regular expressions specialist. Build a regex that extracts ISO dates (YYYY-MM-DD) and log levels from log lines like this sample:

```
2025-07-01 09:12:33 INFO  User 42 logged in from 192.168.1.10
2025-07-01 09:14:02 ERROR Failed to connect to db: time out
2025-07-02 08:00:00 WARN  Disk usage above 80% on /dev/sda1
```

Requirements:
1. One regex with two named capture groups: `date` matching `YYYY-MM-DD` (years 1900-2099, real month/day ranges) and `level` matching `INFO|WARN|ERROR|DEBUG`.
2. The regex must use word boundaries to avoid matching dates embedded in longer tokens, and be case-sensitive.
3. Provide the regex for two engines: Python (with `re` flags, if any) and JavaScript (as a literal without flags).
4. Explain each token of the pattern in a numbered list aligned to its position in the pattern.
5. Show the exact matches extracted from the three sample lines, and the result for two negative examples: `2025-13-01` (invalid month) and `ERRORFatal` (embedded level), explaining why they fail.

Format: a code block with the Python regex and flags, a code block with the JS version, the token-by-token explanation, then the test results as a small table (input, matches, verdict).

## Notes

For single-letter tips: say which engine you target, since named-group syntax differs. Ask for a `verbose`-mode version if you want the pattern self-documenting.
