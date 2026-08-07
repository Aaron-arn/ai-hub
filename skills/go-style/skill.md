# Go Style

You write Go the way its authors intended: simple, explicit, and composed from small packages.

## Formatting and naming

- Run `gofmt` (or `go fmt`) and `go vet` on everything; the formatter is non-negotiable.
- Use short, lowercase names scoped to their context: `i`, `n`, `err` in small scopes; descriptive names for exported things.
- Export only what consumers need; unexported identifiers stay lowercase.
- Use `MixedCaps` for exported names, never underscores in identifiers.
- Acronyms keep their case: `HTTP`, `URL`, `ID`, not `Http`, `Url`, `Id`.
- Follow Go conventions over Java conventions; the community style is the standard.

## Packages and structure

- Keep packages small and single-purpose; the package name is the start of every identifier.
- Avoid package-level mutable state; pass dependencies explicitly.
- Design interfaces on the consumer side: define what you need, accept concrete types, return interfaces rarely.
- Keep interfaces small (one or two methods) and favor composition.
- Use `internal/` for code not meant to be imported outside the module.
- Prefer flat `cmd/<name>/main.go` entry points that call into `internal` packages.

## Errors

- Check errors immediately and handle them; never ignore `err` with `_`.
- Use `fmt.Errorf("...: %w", err)` to wrap with context; unwrap with `errors.Is`/`errors.As`.
- Do not prefix error strings with "failed to"; wrap with context and let the call site read naturally.
- Use sentinel errors (`var ErrNotFound = errors.New(...)`) for values that callers must compare.
- Return the sentinel or a wrapped sentinel, not a new error of the same meaning.
- Do not `log.Fatal` in libraries; return the error to the caller.
- Use `errors.Join` (Go 1.20+) to combine independent errors.

## Concurrency

- Follow the rule: do not communicate by sharing memory; share memory by communicating.
- Use goroutines with `context.Context` and always pass `ctx` as the first argument.
- Ensure every goroutine has a way to stop: select on `ctx.Done()`.
- Wait for goroutines with `sync.WaitGroup` or `errgroup`; never leak them.
- Close channels from the producer, drain in the consumer; prefer range-over-channel.
- Protect shared state with `sync.Mutex`/`sync.RWMutex`; prefer `atomic` for counters.
- Never copy a `sync.Mutex` or `sync.WaitGroup` after use; pass pointers.
- Avoid `go func()` with no stop condition; test with `-race` always.

## Practical habits

- Write small, flat functions; handle errors at the top and return.
- Use table-driven tests with `t.Run` subtests and `t.Parallel()` where safe.
- Keep zero-value structs usable where it makes sense; document constructors when needed.
- Use `defer` for cleanup immediately after acquiring resources.
- Favor standard library and small dependencies; audit `go.mod` regularly.
- Run `go test ./...` and `golangci-lint` before considering work done.
