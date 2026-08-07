# Python Style

You write Python that reads like the standard library: explicit, typed, and simple.

## Style basics

- Follow PEP 8: 4-space indentation, snake_case functions and variables, `UPPER_CASE` constants.
- Use `black` for formatting and `ruff` for linting; fix what they flag instead of suppressing it.
- Write docstrings in Google or NumPy style for public functions; document the why, not the what.
- Keep functions small and single-purpose; prefer returning early over deep nesting.
- Use descriptive names; `data` and `temp` are code smells.

## Typing

- Annotate all public function signatures with type hints; run `mypy` or `pyright` in CI.
- Prefer `collections.abc` generics (`list[str]`, `dict[str, int]`) over `List[str]` on Python 3.9+.
- Use `Optional[T]` or `T | None` consistently; document what `None` means in the docstring.
- Model domain data with `@dataclass`, `NamedTuple`, or `Enum` instead of raw dicts and strings.
- Use `TypeVar`, `Protocol` and generics only when they remove duplication; not for decoration.

## Idioms

- Use list/set/dict comprehensions for transforming collections, but not when they hurt readability.
- Use `enumerate` over range(len()); use `zip(strict=True)` where lengths must match.
- Prefer `pathlib.Path` over `os.path`; it is composable and cross-platform.
- Use `f-strings` for formatting; never `%`-formatting or string concatenation for interpolation.
- Use `any()`/`all()` for existence checks instead of hand-written loops.
- Prefer `str.startswith`/`endswith`/`split` over regex for simple patterns.

## Errors and resources

- Raise specific exceptions (`ValueError`, `KeyError`, custom types); never bare `raise Exception`.
- Catch only what you can handle; re-raise with `raise ... from e` to preserve the chain.
- Use `try/except/else/finally` correctly: put the happy path in `else`, cleanup in `finally`.
- Use context managers (`with open(...)`, `with closing(...)`) for every resource you open.
- Never swallow exceptions silently; log or re-raise at the boundary.
- Prefer raising early: validate inputs at the top of the function with clear messages.

## Structure and packaging

- Separate code from config and data; keep secrets out of modules.
- Use absolute imports within the package; avoid `sys.path` hacks.
- Add `__main__` guards for scripts; keep entry points thin.
- Declare dependencies explicitly in `pyproject.toml`; pin versions for reproducibility.
- Keep modules cohesive: one module per concern, importable without side effects.
- Write tests with pytest; name test functions for the behavior (`test_returns_404_for_unknown_id`).
