# JavaScript Style

You write modern JavaScript that is explicit about its data flow and honest about its failure modes.

## Language level

- Use ES2020+ features consistently: optional chaining (`?.`), nullish coalescing (`??`), destructuring, spread.
- Use `const` by default and `let` only when rebinding; never use `var`.
- Prefer `===` over `==`; use `==` only for intentional null/undefined checks.
- Use template literals for string interpolation; avoid string concatenation with `+`.
- Use `Map` and `Set` for keyed collections when keys are not plain strings.
- Avoid `Date.parse` ambiguity; use ISO 8601 strings and `Intl.DateTimeFormat` for display.

## Functions and data

- Use arrow functions for callbacks and `function` declarations for named top-level functions.
- Destructure function parameters and objects at the boundary: `({ id, name } = user)`.
- Avoid mutation: prefer `map`/`filter`/`reduce` over loops that push into shared arrays.
- Return early and fail fast; avoid deep `if/else` nesting.
- Prefer default parameters over runtime fallback checks.
- Do not compare `NaN` with `===`; use `Number.isNaN`.

## Async and errors

- Use `async/await`; avoid `.then` chains and definitely avoid nested callbacks.
- Handle every `await` failure with `try/catch` or propagate it explicitly to a boundary.
- Use `Promise.all` for independent promises, `Promise.allSettled` when partial failure is acceptable.
- Never ignore promise rejections; attach a handler or `void` with intent.
- Never use floating-point equality; round money with cents as integers.
- Use `throw` with `Error` instances (or custom error classes), never strings.

## Modules and naming

- Use ESM (`import`/`export`) consistently; avoid mixing CJS and ESM in one file.
- Export named things; default export only for the main component/entry of a module.
- Name things by what they mean: `fetchOrders`, not `getData`.
- Keep modules small and cohesive; import only what you use.
- Avoid global state; pass dependencies explicitly or use a proper context/DI pattern.
- Prefix boolean variables with `is`, `has`, or `can`; keep predicates clear.

## Tooling and tests

- Run `eslint` and `prettier` in CI; fix warnings rather than disable rules globally.
- Test with a modern runner (vitest/jest); name tests for behavior, not implementation.
- Test async code with `await` and proper teardown; use `expect(...).rejects.toThrow()`.
- Use `console.error` for errors; keep `console.log` out of library code.
- Pin package versions and audit dependencies (`npm audit`).
- Avoid `any`-style escape hatches and `@ts-ignore`; if using TypeScript, let it work for you.
