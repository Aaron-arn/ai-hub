# Rust Style

You write Rust that leans on the compiler: safe by default, explicit about errors, and expressive through types.

## Ownership and borrowing

- Prefer ownership with `&` references for read access; clone only when the cost is justified.
- Use `&mut` where mutation is needed; keep borrow scopes short.
- Avoid fighting the borrow checker: restructure data (Rc/RefCell, split fields) before using `unsafe`.
- Let the compiler infer lifetimes in most code; add explicit lifetimes only where they document relationships.
- Prefer iterators over indexed loops: `.iter()`, `.map()`, `.filter()`, `.collect()`.
- Use `&str` for borrowed text and `String` only when you need owned data.

## Errors

- Return `Result<T, E>` from fallible functions; `Option<T>` only where absence is not an error.
- Define a crate-level error type (thiserror, anyhow for apps) and convert errors with `?`.
- Use `thiserror` for libraries (typed errors) and `anyhow` for binaries (context).
- Prefer `?` over `unwrap()`/`expect()` in library code; reserve `expect` for invariants with a message.
- Do not swallow errors; `ok()` and `.map_err` deliberately.
- Handle `None` with `ok_or`, `unwrap_or`, or early `return`.

## Traits and generics

- Implement common traits for public types: `Debug`, `Clone`, `PartialEq`, and `Default` when sensible.
- Use trait objects (`dyn Trait`) only where dynamic dispatch is needed; prefer generics otherwise.
- Keep bounds minimal: generic functions should not over-constrain their inputs.
- Implement `From`/`TryFrom` for conversions instead of hand-rolled conversion functions.
- Use builder patterns or `Default`-based constructors over many-argument `new`.
- Prefer `impl Trait` for return types of private helpers.

## Concurrency

- Use `Arc<Mutex<T>>` or `Arc<RwLock<T>>` for shared mutable state; prefer `RwLock` for read-heavy data.
- Use `tokio`/`async-std` consistently for async; keep the executor choice at the binary.
- Send owned data into spawned tasks; never share references across threads casually.
- Prefer channels (`std::sync::mpsc`, `tokio::sync::mpsc`) over polling shared state.
- Keep locks held for the shortest possible scope; never await while holding a std lock.

## Unsafe discipline

- Avoid `unsafe` by default; reach for it only when FFI or performance truly demands it.
- When used, isolate `unsafe` in a small module with `# Safety` invariants documented on the function.
- Prefer safe wrappers from the ecosystem (safe FFI crates) over hand-written bindings.
- Run `cargo clippy`, `cargo test`, and `cargo miri` (when relevant) in CI.

## Practical habits

- Run `cargo fmt` and `cargo clippy -D warnings`; treat warnings as errors in CI.
- Use `Option`/`Result` combinators over nested `match` where a chain is clearer.
- Keep modules small; use `pub(crate)` to hide internals.
- Write doctests for public API examples; they keep documentation honest.
- Prefer `std::time::Duration` and `Instant` for time; avoid platform-specific time calls.
- Pin and audit dependencies (`cargo audit`); keep the dependency tree small.
