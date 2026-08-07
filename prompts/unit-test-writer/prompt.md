# Unit Test Writer

## Description

Pastes a function and its specification, and receives a complete, runnable unit test suite covering happy paths, edge cases, and error handling. Use it when you need tests fast, or when you want independent verification that your function behaves as documented.

## Prompt

You are a test engineer. Write a comprehensive pytest suite for the following Python function:

```python
def calculate_discount(price, coupon):
    """Apply a coupon to a price.

    Args:
        price: float or int, must be >= 0.
        coupon: optional dict with 'percent' (0-100) or 'flat' (>= 0)
                or None. A coupon with both fields raises ValueError.
    Returns:
        float rounded to 2 decimals.
    Raises:
        ValueError for negative price, invalid coupon, or percent > 100.
    """
```

Requirements:
1. File `test_discount.py` using plain `pytest` (no fixtures beyond `@pytest.mark.parametrize`).
2. Groups of tests, each group in its own test function:
   - Normal cases: no coupon, percent 10, percent 100, flat 5, flat exactly equal to price, percent with a float price (rounding check, e.g. 19.99 at 10% -> 17.99).
   - Edge cases: price 0 with coupon, very large price, price as numeric string (assume the function raises TypeError; test that it propagates).
   - Error cases: negative price, percent > 100, percent < 0, both percent and flat present, empty dict coupon.
3. Use `pytest.raises(ValueError)` for error cases with a `match` regex on the message where the message is deterministic.
4. A `parametrize` block with at least 6 rows combining input and expected output.
5. Add a docstring to each test function stating the scenario.

Then provide the run command with output expectation: `python -m pytest test_discount.py -v` should pass, and estimate the total test count. Output the test file in one code block, then the run command and expected pass count.

## Notes

The same prompt works for JavaScript by asking for Jest/Vitest with `describe/it/expect`. If your function has side effects, add the input/output pairs and ask for mock-based tests instead.
