# Downloads API (counts)

Shared contract between the AIHub CLI (reports installs) and the AIHub website (displays and sorts by popularity).

## Endpoints

### POST /api/counts

Called by the CLI after a successful install. Fire and forget: the CLI ignores failures, so the endpoint should never block an install.

Request body:

```json
{
  "type": "tool",
  "name": "web-search"
}
```

### GET /api/counts

Returns total downloads per package, keyed by `"<type>:<name>"`.

```json
{
  "tool:web-search": 42,
  "skill:code-review": 7
}
```

The `type:name` key format guarantees that a skill and a tool sharing the same name never mix their counts.

## Validation

- `name` must be a valid package name (`^[a-z0-9][a-z0-9-]*$`).
- `type` must be one of: `skill`, `tool`, `agent`, `mcp`, `package`, `prompt`.
- Invalid requests should be rejected with `400`.
- Unknown `type:name` pairs may be rejected with `404` if the endpoint knows the registry.

## Likes API

### POST /api/likes

Called by the website when a visitor likes or unlikes a package. Likes are per anonymous user (a UUID stored in `localStorage`).

Request body:

```json
{
  "type": "tool",
  "name": "web-search",
  "user": "0f3c1a2b-...",
  "action": "like"
}
```

`action` is `"like"` or `"unlike"`. The endpoint is idempotent: liking twice keeps the count at 1, unliking a non-liked package never goes below 0.

### GET /api/likes?user=...

Returns total likes per package plus the packages the given user has liked.

```json
{
  "counts": { "tool:web-search": 42 },
  "user": ["tool:web-search"]
}
```

Validation: `user` must match `^[a-zA-Z0-9-]{8,64}$`.

## Hosting note

GitHub Pages serves static files only. The counts API must be deployed on a serverless host (Cloudflare Pages Functions, Vercel, Netlify - all have free tiers) or any small backend with a database / KV store. The contract above is independent of the host.
