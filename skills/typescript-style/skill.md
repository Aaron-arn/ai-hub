# TypeScript Style

You use TypeScript as a modeling tool: the compiler catches mistakes, and the types document the intent.

## Strictness

- Enable `strict: true` (and `noImplicitAny`, `strictNullChecks`, `noUncheckedIndexedAccess` where applicable).
- Treat the compiler as the source of truth: fix type errors, do not suppress them.
- Never use `any`; reach for `unknown` and narrow, or a proper union type.
- Avoid `@ts-ignore` and `as any`; if a cast is needed, prefer `as const` or a narrow cast with a comment.
- Use `satisfies` (TS 4.9+) to keep literal types while validating structure.
- Run `tsc --noEmit` in CI; type errors are build failures.

## Modeling types

- Model domain data with interfaces and type aliases; prefer interfaces for object shapes that may extend.
- Use discriminated unions (`type = 'a' | 'b'`) for state machines and variant data.
- Represent optionality explicitly: `value?: T` for absent, `value: T | null` for present-but-null.
- Prefer string literal unions over string types for known domains: `'pending' | 'paid'`.
- Derive types from data (`typeof`, `ReturnType`, `Awaited`) instead of duplicating shapes by hand.
- Avoid classes for pure data; use plain interfaces and factory functions or a serialization layer.

## Functions and narrowing

- Annotate function signatures; let the compiler infer local variables.
- Narrow with `typeof`, `in`, and discriminant checks; avoid unsafe `as` casts after checks.
- Use `unknown` in catch blocks and narrow before using error properties.
- Type generic functions where the constraint helps: `T extends Record<string, unknown>`.
- Do not over-genericize; a plain interface beats a clever generic that no one reads.

## Structure

- Colocate types with the code that uses them; export only what consumers need.
- Use one module per cohesive unit; import types with `import type` when they are types only.
- Prefer folders by feature over folders by type (`features/orders/` not `types/`, `utils/`).
- Keep configuration in typed config files; validate environment variables with a small schema (e.g. zod) at the boundary.
- Exhaustively handle unions with a `never` check in default branches: `const _exhaustive: never = x`.

## Practical discipline

- Keep `tsconfig` strictness consistent across the project; do not loosen flags per file.
- Use path aliases (`@/lib/...`) with a baseUrl only if the tooling handles them fully.
- Write tests that exercise the types where behavior is subtle (`@ts-expect-error` in negative tests).
- Prefer library types over hand-written declarations; audit `@types/*` packages.
- Incremental migration is fine, but each migrated file should reach full strictness.
