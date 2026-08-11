# Code Review

## When to use
Apply when reviewing any code change: PRs, peer reviews, or reviewing your own diff before commit.

## Review order
1. **Understand intent first**: read the PR description, linked issue, and tests before the implementation.
2. **Read tests first**: they reveal the contract. Missing tests for core logic is itself a finding.
3. **Read the diff chronologically**: entry points -> data flow -> edge cases.

## What to look for (in priority order)
1. Correctness: logic errors, race conditions, error paths, off-by-one.
2. Security: injection, hardcoded secrets, auth/authorization gaps, path traversal.
3. Maintainability: dead code, duplication, confusing naming, god functions.
4. Performance: N+1 queries, quadratic loops, blocking calls in async code.
5. Style: only where inconsistent with the codebase; don't bikeshed.

## Comment style
- Each comment: location, the problem in one sentence, why it matters, a concrete suggestion.
- Separate: blocking issues, non-blocking suggestions, questions (tag: `[nit]`, `[question]`, `[blocking]`).
- Phrase as observations, not orders: "This branch can raise X" not "You must fix this".
- Praise good parts: note what is done well, especially clever-but-clear code.

## Reviewing your own diff
- Let it sit (or re-read after fresh eyes); `git diff` with word-diff to catch typos.
- Check for: debug prints left in, TODO markers, changes unrelated to the task, test coverage of the new behavior.

## Verdicts
- Approve: no blocking issues. Request changes: list blockers distinctly from nits.
- Never approve what you cannot run/verify mentally; say what you tested.
