# API Design

You design APIs that are consistent, predictable and safe to evolve.

## Resource modeling

- Model the domain as resources (nouns), not actions: `/orders`, `/orders/{id}`.
- Use actions (verbs) only for non-CRUD operations: `POST /orders/{id}/cancel`.
- One resource per URL path; nest only for clear ownership (`/users/{id}/orders`).
- Do not over-nest beyond two levels; use query parameters or sub-resources instead.
- Give every resource a stable unique identifier, ideally opaque and server-generated.

## HTTP conventions

- Use the right methods: GET for reads, POST for creation, PUT for full replacement, PATCH for partial updates, DELETE for removal.
- Make GET and DELETE idempotent; PUT must be idempotent; POST is not.
- Return meaningful status codes: 200, 201 with Location, 204, 400, 401, 403, 404, 409, 422, 429, 500.
- Return the created or updated resource in the response body where it saves a round trip.
- Set standard headers: `Content-Type`, `Cache-Control`, `ETag`, `RateLimit-*` where relevant.

## Naming and data

- Use kebab-case for URL segments and snake_case or camelCase consistently for JSON fields (pick one, document it).
- Use plural nouns for collection resources: `/users`, not `/user`.
- Use ISO 8601 (`2026-08-07T14:30:00Z`) for timestamps; document the timezone.
- Use stable, typed enums in responses; add new values instead of reusing existing ones.
- Never return `null` and omit fields interchangeably; be consistent per field.

## Pagination, filtering and sorting

- Paginate every collection endpoint; use cursor-based pagination for large, changing datasets.
- Return a consistent page envelope: items, next cursor or page token, and total when cheap.
- Support filtering with query parameters (`?status=active`), sorting (`?sort=-created_at`), and field selection (`?fields=id,name`) when useful.
- Set sane default page sizes and enforce a maximum.

## Errors

- Use a consistent error shape: error code, human-readable message, and details for validation.
- Never leak stack traces, SQL, or internal paths in error bodies.
- Include a request or correlation ID in every error response and log it server-side.
- 400 for malformed input, 404 for unknown resources, 409 for conflicts, 422 for semantically invalid bodies.

## Versioning and evolution

- Version the API explicitly, in the URL (`/v1/orders`) or via a header; pick one and keep it.
- Never break backward compatibility within a major version.
- Additive changes (new fields, new endpoints) are safe; removal, renaming, and type changes require a new major version.
- Keep old versions alive for a documented deprecation window; log usage and communicate the schedule.
- Add new fields to responses before you need them, so old clients are not surprised later.

## Documentation

- Document every endpoint: purpose, request/response examples, error cases, and rate limits.
- Keep an OpenAPI (or equivalent) spec as the source of truth and validate it in CI.
- Provide a public changelog that notes breaking changes in advance.
