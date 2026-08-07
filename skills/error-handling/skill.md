# Error Handling

You write error handling that fails gracefully, reports clearly and recovers where possible.

## Design for failure

- Assume every call can fail: network, disk, auth, user input.
- Decide per operation: retry, fall back, degrade or fail loudly.
- Fail loud for bugs, fail graceful for expected conditions.
- Never swallow errors silently; if you ignore one, log why.

## Input validation

- Validate external input at the boundary, not deep inside the code.
- Validate type, range, format and size; reject what you do not expect.
- Return clear validation errors naming the offending field.

## Error types and propagation

- Use domain-specific error types for conditions callers must handle.
- Add context when propagating: what failed, with what input.
- Catch only what you can handle; do not catch and ignore.
- Do not use exceptions for expected control flow.

## Recovery

- Retry transient failures with backoff and a capped number of attempts.
- Use timeouts on all external calls so one slow service cannot hang you.
- Fall back to a degraded mode or cached data when the primary path fails.
- Clean up resources in all paths: files, sockets, transactions.

## Reporting

- Include actionable messages: what happened, why, and what to do.
- Include identifiers: request ID, record ID, operation name.
- Expose errors in a structured form that tools and UIs can consume.
- Never leak stack traces, secrets or internal paths to users.

## Testing

- Write tests for each error path, not only the happy path.
- Test failure injection: timeouts, disk full, malformed payloads.
- Verify the user sees a helpful message when the system fails.
