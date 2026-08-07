# Debugging

You debug systematically, in this order.

## 1. Reproduce

- Get a reliable reproduction before changing anything.
- Note the exact input, environment and version that trigger the bug.
- If you cannot reproduce it, say so instead of guessing.

## 2. Read the error

- Read the full error message and traceback before hypothesizing.
- The last line tells you what; the traceback tells you where.
- Check the line that raised the error, not the line you expected to be wrong.

## 3. Isolate

- Change one variable at a time.
- Reduce the failing case to its smallest form.
- Bisect: comment out or disable half the code, see if it still fails, repeat.

## 4. Find the root cause

- Distinguish cause from symptom. A crash is often the symptom.
- Check assumptions: data shape, types, encoding, timezones, off-by-one, resource state.
- If a fix does not explain the root cause, it is a patch, not a fix.

## 5. Fix and verify

- Apply the minimal correct fix.
- Verify the original reproduction passes.
- Run the surrounding tests and linting.
- Check for sibling bugs: similar patterns in nearby code.

## 6. Communicate

- Report: what was wrong, why it happened, what changed.
- If you could not solve it, report what you tried and where you stopped.

Never apply random fixes hoping one sticks. Never silence an error instead of fixing it.
