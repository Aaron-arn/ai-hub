# Docstring Generator

## Description

Write Google-style docstrings and type annotations for functions.

## Prompt

Write Google-style docstrings for this Python code: {CODE}

For each public function/method/class provide:
1. One-line summary (what it does, imperative)
2. Extended description only if behavior is non-obvious (state side effects, error cases)
3. Args: name - type - description (defaults documented)
4. Returns: type and description; Raises: exception - condition
5. Example usage snippet if non-trivial
6. Type hints on the signature itself (no stub-only hints, no `-> None` omissions)

Keep docstrings terse: no restating what the name implies. Also list any function missing a docstring that I should not write (private helpers that are self-explanatory).
