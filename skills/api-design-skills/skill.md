# API Design

## When to use
Apply when designing a new API, endpoint, library interface, or schema.

## Principles
- **Consistency beats cleverness**: same naming, error shape, pagination style everywhere.
- **Convention over exception**: follow the codebase/framework conventions unless there is a real reason not to.
- **Design for the consumer**: name things from the caller's perspective, not the implementer's.

## REST design rules
- Resources in plural nouns: `/users`, `/orders`; nested only for genuine ownership: `/users/{id}/orders`.
- Actions as POST to a sub-resource (`/orders/{id}/cancel`), not verbs on the main resource.
- HTTP semantics: GET read-only, POST create, PUT replace, PATCH partial update, DELETE remove.
- Status codes: 200/201/202/204, 400 for bad input, 401/403 distinct, 404, 409 conflict, 429 rate limit, 5xx only for server faults.
- Errors: consistent envelope `{"error": {"code", "message", "details"}}` with stable machine-readable codes.
- Pagination: cursor-based for large collections, offset for small/simple; return `next` token.
- Idempotency: POST with `Idempotency-Key` header for payment-like operations.
- Versioning: URL prefix `/v1` or header negotiation; document deprecation policy.

## Library API design
- One clear primary entry point; expose minimal surface (fewer exports = less to maintain).
- Return rich objects, not tuples; raise typed exceptions with actionable messages.
- Validate input early, fail fast, document invariants.
- Defaults that are safe: fail closed, log loudly.

## Evolution
- Additive changes are safe: new optional fields, new endpoints.
- Breaking changes need deprecation notices, then a major version.
- Document every breaking change with a migration path.
