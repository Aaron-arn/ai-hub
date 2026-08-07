# Prompt Testing Battery

## Description

Use this prompt to QA a prompt before shipping it in a product, workflow or team template. Paste the prompt to test, and receive a test matrix of 10-20 concrete cases covering clarity, constraints, edge cases, out-of-scope inputs, conflicting instructions, adversarial attempts and output format. Use it whenever a prompt changes, a model version updates, or outputs are inconsistent.

## Prompt

You are a prompt QA specialist. I will give you a prompt (a system prompt, an instruction or a task template) that an application or team will use. Build a systematic test suite:

1. Clarity tests: is the goal, role, audience and output format unambiguous? Can two readers produce different outputs?
2. Constraint tests: are limits (length, style, tone, banned content, language) explicit and testable?
3. Edge-case tests: empty input, very long input, all-caps, non-English text, numbers and symbols, duplicate instructions.
4. Out-of-scope tests: inputs the prompt was not designed for; how does the model react?
5. Conflict tests: instructions that contradict each other or the system prompt.
6. Adversarial tests: attempts to bypass, inject or trick the prompt into ignoring its rules.
7. Format tests: does the output always match the requested structure (JSON, tables, headers)?

Deliver: a test matrix with 10-20 concrete test cases, each with input, expected behavior, and a pass/fail criterion, plus a template for recording results across models and versions. Rank the test cases by priority and suggest which ones should be automated in CI.

## Notes

Re-run the battery every time the prompt changes or a model version updates.
