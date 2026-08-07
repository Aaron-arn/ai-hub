# Test Writing

You write tests that fail for the right reason and stay useful.

## 1. What to test

- The public behavior of each unit, not its internals.
- Normal cases, edge cases (empty, zero, null, max), and error cases.
- The bug you just fixed: add a regression test that fails on the old code.
- Config-driven or data-driven logic: table-driven tests over duplication.

## 2. Structure

One test per behavior, with a name that states the expectation:

- `test_adds_two_numbers` not `test_function_1`.
- Arrange, act, assert: set up, run the unit, check the outcome.
- Assert on outcomes, not on implementation details.

## 3. Determinism

- No dependence on wall-clock time, random values, network or locale.
- Use fixed inputs and explicit fixtures; freeze time or inject clocks when needed.
- Tests must pass in any order and in isolation.

## 4. Fakes and boundaries

- Mock the boundaries (network, filesystem, clock), not the unit under test.
- If mocking gets complicated, the design is the problem.

## 5. Maintenance

- Tests are code: keep them readable and review them.
- Delete tests that test the framework or assert trivia.
- A flaky test is a bug in the test - fix or remove it, never ignore it.

## 6. Coverage

- Use coverage to find gaps, not as a score to maximize.
- The valuable 100% is: every behavior is verified, not every line executed.
