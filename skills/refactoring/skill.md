# Refactoring

You refactor code so that behavior never changes and confidence stays high.

## 1. The golden rule

Refactoring is restructuring without changing observable behavior. If behavior changes, it is a feature - say so.

## 2. Before you start

- Understand the current behavior: what are the inputs, outputs, edge cases?
- Check that tests exist or can be added cheaply.
- Refactor with a safety net, or build one first.

## 3. Small steps

- One transformation per step: rename, extract, inline, move.
- After each step, run the tests. If they fail, the step was not safe.
- Keep each step small enough to review in minutes.

## 4. Common moves

- Extract: pull repeated logic into a named function.
- Rename: names that reflect intent; do not be afraid of longer names.
- Reduce nesting: early returns, guard clauses.
- Remove duplication, but never at the cost of clarity.
- Split functions that do more than one thing.

## 5. After the change

- Run the full test suite and linting.
- Review the diff for accidental changes (whitespace-only diffs included).
- Update documentation if interfaces or behavior are described there.
- Do not mix refactoring and new features in the same change.

## 6. Stop conditions

- Stop when the diff grows beyond what can be verified.
- Stop if you cannot explain why a step is safe.
- If a step fails twice, revert it and try a smaller one.
