# Test Generator

## Description

Generate unit tests covering normal, edge and failure cases.

## Prompt

Write pytest tests for this code: {CODE}

Coverage plan:
1. NORMAL: happy-path inputs (at least 3 meaningful cases)
2. EDGE: empty input, single element, max values, unicode, whitespace handling
3. FAILURE: expected exceptions (assert with pytest.raises and match), error messages
4. BOUNDARIES: off-by-one ranges, type mismatches if runtime-validated

Test style: Arrange-Act-Assert, one assertion concept per test, parametrize with @pytest.mark.parametrize where the cases share a shape, readable test names `test_<fn>_<scenario>`. Include a conftest fixture note if needed. Mark any test requiring external resources (network/DB) with @pytest.mark.integration so they can be skipped.
