# REST API Client Generator

## Description

Feed an OpenAPI spec (or a plain list of endpoints) and get a typed, dependency-free JavaScript fetch client with error handling. Use it when you need to talk to an API from the browser or Node.js without pulling in axios or a codegen tool. The output works in both environments.

## Prompt

You are an API integration specialist. Generate a JavaScript client for the following REST API. The client must use the native `fetch` and run in both browser and Node.js 18+.

API endpoints:
- `GET /api/users?page=1&limit=20` -> `{ users: [{id, name, email}], total }`
- `GET /api/users/:id` -> `{ user: {id, name, email} }` or 404
- `POST /api/users` body `{name, email}` -> 201 `{ user }` or 422 with `{ errors: [{field, message}] }`
- `PUT /api/users/:id` -> 200 `{ user }`
- `DELETE /api/users/:id` -> 204

Requirements:
1. Export a class `ApiClient` taking `baseUrl` and optional `token` in the constructor.
2. One method per endpoint with JSDoc types for parameters and return values.
3. All methods return parsed JSON for success, and throw a typed `ApiError` with `status`, `statusText`, and `body` for non-2xx responses.
4. Attach `Authorization: Bearer <token>` automatically when a token is set.
5. Accept and forward a per-call `signal` (AbortSignal) for cancellation.
6. Use `encodeURIComponent` for path parameters.

Output one code block with the full client (under 120 lines), then a short usage example showing error handling with try/catch. Use only native browser/Node features.

## Notes

For large specs, paste the OpenAPI JSON and ask for the client to be generated from the paths section. Add a second optional constructor argument for custom headers if the API needs them.
