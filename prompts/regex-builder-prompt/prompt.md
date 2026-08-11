# Regex Builder

## Description

Build and explain regex patterns with test cases.

## Prompt

Write a regex to match {PATTERN_DESCRIPTION}.

Example inputs: {EXAMPLE_INPUTS}

Provide:
1. The regex pattern (PCRE flavor)
2. A line-by-line breakdown of each part of the pattern
3. Test cases: 5 that should match, 5 that should NOT match (with reasons)
4. Edge cases: empty string, very long input, unicode, case sensitivity
5. The equivalent pattern for: Python, JavaScript, grep (if different)
6. Performance note: any backtracking risk and how to mitigate

Pattern must be as simple as possible while passing all tests. If my examples are contradictory, ask me to confirm before writing.
