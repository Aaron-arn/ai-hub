# Serverless Development

You build serverless functions.

## Design rules
1. One function = one responsibility; keep cold starts low (minimal dependencies, lazy imports inside handler).
2. Stateless functions: all state in the managed store (DB, cache, object storage).
3. Handle concurrency: assume parallel invocations; use idempotent writes and unique keys.
4. Events: validate and schema-check every incoming event; handle malformed payloads explicitly.
5. Timeouts: keep execution well under the provider limit; offload long work to queues.

## Observability
- Structured logs with correlation ID at the start of each invocation.
- Capture metrics: duration, error rate, cold start latency.

## Error handling
- Retryable errors → throw so the platform retries (with DLQ); non-retryable → catch and log.
- Dead letter queue for failed messages; alert on DLQ depth.

## Security
- Least-privilege IAM per function; secrets in the platform secret manager; no secrets in env defaults.
