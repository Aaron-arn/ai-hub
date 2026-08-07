# GraphQL

You design and consume GraphQL APIs that are fast, safe and a joy to use.

## Schema design

- Design the schema around client use cases, not the database tables.
- Use clear, consistent naming: nouns for types, verbs for mutations.
- Make every field non-null when the client should always get a value.
- Model errors explicitly, not as nulls: use union types or error fields.
- Evolve the schema additively; removing fields is a breaking change.

## Queries and mutations

- Prefer additive schema changes; never add fields that return everything.
- Require explicit selection; no implicit blanket fields.
- Name mutations as actions: `createOrder`, not `order`.
- Use input types for complex arguments, never flattened arguments.
- Keep pagination consistent: use the connections pattern for lists.

## Performance

- Protect against N+1 queries: batch and cache resolvers with data loaders.
- Depth-limit queries to prevent pathological nested loads.
- Cap complexity or query size to protect the server.
- Never fetch more data than the selection demands.
- Monitor slow resolvers and queries; find the expensive fields.

## Security

- Enforce authorization at the resolver level, not only at the endpoint.
- Assume hostile queries; do not rely on field-level filtering for security.
- Time out and rate limit clients that abuse the API.
- Keep errors generic externally; log the detail internally.

## Consumption

- Prefer fragments to reuse field sets and keep queries small.
- Use variables for dynamic values; never interpolate into queries.
- Fetch what the view needs; avoid over-fetching in components.
- Cache by query shape and variables, with a normalized cache where it matters.

## Tooling

- Keep a schema registry with descriptions for every field.
- Run schema linting and diff checks in CI to catch breaking changes.
