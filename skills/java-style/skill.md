# Java Style

You write Java that is explicit, null-safe, and boring in the good way: predictable and easy to maintain.

## Language level

- Use a modern LTS Java and its features: records for data, sealed interfaces, pattern matching for switch.
- Prefer records over classes with getters and equals/hashCode; use them as DTOs and domain values.
- Use `var` only where the type is obvious from the initializer; avoid it for public APIs.
- Use text blocks for multiline strings; use `Optional` for possibly-absent returns.
- Prefer immutable fields (`final`) and immutable collections; use `List.of`, `Map.of` for small constants.
- Do not use deprecated APIs; remove warnings instead of suppressing them.

## Structure and naming

- One class per file; package by feature (`com.example.orders`), not by type layer.
- Keep classes small and cohesive; favor composition over deep inheritance.
- Name by intent: `OrderService`, `computeTotal()`, `isActive()`; avoid `Manager`/`Util` as catch-alls.
- Fields: `private` by default; expose behavior through methods, not getter/setter pairs on collections.
- Keep method signatures small; pass domain objects instead of long parameter lists.
- Use `final` classes or explicit extension points; prefer interfaces for seams.

## Errors and null safety

- Fail fast with `Objects.requireNonNull` or `java.util.Objects.checkIndex` for invariants.
- Validate inputs at boundaries (DTOs, controllers) and throw `IllegalArgumentException`/`IllegalStateException`.
- Prefer `Optional` returns over null; never return `Optional` from collections fields.
- Catch specific exceptions; do not catch `Exception` or `Throwable` broadly.
- Use try-with-resources for every closable resource; never close manually in finally.
- Do not log and rethrow in the same place; log at the boundary, wrap with context when crossing it.
- Wrap checked exceptions at module boundaries with a custom `RuntimeException` when appropriate.

## API design

- Expose the smallest public surface: package-private by default, `public` only for consumers.
- Return immutable views (`Collections.unmodifiableList`, `List.copyOf`) from getters.
- Use enums for fixed domains; avoid stringly-typed parameters.
- Prefer dependency injection of interfaces; avoid static mutable singletons and `new` everywhere.
- Design with `equals`/`hashCode` consistent for value types; records handle this for you.

## Testing and build

- Use JUnit 5 with assertion libraries; name tests as behavior statements (`shouldRejectNegativeAmount`).
- Prefer small unit tests with mocks at the boundary; keep tests fast and deterministic.
- Run the full build with `mvn test` or `gradle test` and fix failing tests before adding features.
- Enforce style with a formatter (Spotless or Eclipse formatter) and static analysis in CI.
- Pin dependency versions and keep the dependency tree minimal; audit licenses.
- Keep the build reproducible: locked dependency versions, no timestamps in artifacts.
