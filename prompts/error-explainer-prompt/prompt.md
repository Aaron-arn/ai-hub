# Error Explainer

## Description

Explain stack traces and runtime errors in plain language with fixes.

## Prompt

Explain this error: {ERROR} (context: {CODE_OR_STACK})

Format:
1. WHAT HAPPENED: one plain-language sentence (no jargon)
2. ROOT CAUSE: the actual mechanism - point to the exact line and value involved
3. WHY IT'S CONFUSING: common misconception this error triggers
4. FIXES: 2-3 ranked options with short code snippets, note the tradeoff of each
5. PREVENTION: how to avoid this class of error (guard clause, type check, validation)

If the trace is incomplete, list what information would help me diagnose precisely. Do not guess: mark any part of the explanation that is a hypothesis rather than certain.
