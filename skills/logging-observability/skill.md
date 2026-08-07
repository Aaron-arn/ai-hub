# Logging and Observability

You add structured logging, traces and metrics so that production behavior is inspectable and debuggable.

## Log what matters

- Log every failure, every external call and every user-affecting action.
- Log at the right level: debug for detail, info for milestones, error for failures.
- Do not log the same event at multiple levels or multiple times.
- Log what you would want to see when debugging a problem.

## Structured logging

- Use a structured format (JSON), never free-form prose.
- Use stable field names across services: `request_id`, `user_id`, `operation`.
- Include context: service, version, environment, correlation IDs.
- Keep logs searchable: one event, one line, no multi-line errors.

## Context and correlation

- Generate a request ID at the entry point and propagate it downstream.
- Include the same request ID in logs, traces and error reports.
- Add scoped context per operation: resource, tenant, customer.

## Security and hygiene

- Never log secrets: passwords, tokens, keys, full credit cards, personal data.
- Redact sensitive fields before logging; sample or truncate large payloads.
- Know your retention policy and follow it.

## Traces

- Trace every request end to end, across services and queues.
- Add span attributes for meaningful business data and costs.
- Link traces and logs to each other by ID.

## Observability loop

- Verify logs and traces actually reach the sink in production, not only locally.
- Alert on anomalies, not on every event; dashboards are for inspection.
- Periodically search for errors you never noticed; fix those first.
