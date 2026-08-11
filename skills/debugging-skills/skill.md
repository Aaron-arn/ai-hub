# Debugging Methodology

## When to use
Apply when a program behaves unexpectedly: crashes, wrong output, hangs, performance regressions.

## Method (in order)
1. **Reproduce**: get a minimal, deterministic reproduction. If flaky, capture logs with timestamps.
2. **Read the error carefully**: traceback, exit code, first failing assertion. Never skip the first line.
3. **Form a hypothesis**: state one concrete guess with a mechanism (not "something is broken").
4. **Instrument**: add targeted logging or assertions at the suspected boundary (input -> function -> output).
5. **Verify**: test the hypothesis. If wrong, refine. Never change code without a hypothesis.
6. **Fix minimally**: smallest change that addresses the root cause, not the symptom.
7. **Add a regression test**: prove the fix and prevent recurrence.

## Root-cause techniques
- **Bisect**: halve the search space (git bisect for commits, binary search over inputs).
- **Isolate layers**: input validation -> pure logic -> I/O -> framework. Test each boundary.
- **Rubber duck / explain out loud**: narrate what the code should do at each line.
- **Compare**: run the same input through a known-good reference implementation.
- **Simplify**: strip parts until the failure disappears; the removed part is implicated.

## Tools
- Python: pdb, breakpoint(), traceback module, -X dev mode.
- Logging: use structured levels (DEBUG detail, INFO lifecycle, WARNING anomalies).
- Time: `timeit` and cProfile for performance; measure before optimizing.

## Anti-patterns to avoid
- Shotgun debugging: changing random things hoping it works.
- Fixing the symptom: patching output without understanding input.
- Refactoring while debugging: one change at a time.
- Trusting memory: verify state at runtime, don't assume what variables contain.
