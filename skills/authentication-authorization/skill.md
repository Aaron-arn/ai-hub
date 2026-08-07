# Authentication and Authorization

You implement authentication and authorization using proven patterns, never your own crypto.

## Use proven foundations

- Never roll your own cryptography, hash or token scheme.
- Use well-maintained libraries and frameworks for auth.
- Keep auth libraries updated; auth is where old vulnerabilities live.

## Authentication

- Store passwords with a modern slow hash (argon2id, bcrypt) and per-user salts.
- Enforce password policy: length over complexity, and check against breach lists.
- Use multi-factor authentication for anything privileged.
- Protect against enumeration: do not reveal whether a user exists.
- Rate limit login attempts; throttle or lock out repeated failures.
- Use short-lived sessions and rotate tokens; revoke on logout.

## Tokens and sessions

- Prefer standard tokens (JWT, OAuth2, OIDC) configured correctly.
- Verify signature, issuer, audience, expiry and revocation on every use.
- Store session identifiers and refresh tokens server-side where possible.
- Never put sensitive data in tokens that clients can read.

## Authorization

- Apply authorization on every request at the resource level; surface checks are not enough.
- Follow least privilege: grant the minimum scope for the job.
- Use a consistent model (RBAC, ABAC) and document the matrix.
- Deny by default; allowlists beat blocklists.
- Check authorization server-side; client-side hiding is not security.

## Secrets and flows

- Keep secrets in a vault or environment, never in code or logs.
- Use standard flows (OAuth2 authorization code with PKCE) for browser clients.
- Scope tokens narrowly: least privilege per use case, short lifetimes.

## Hardening

- Log and alert on auth events: failures, lockouts, unusual activity.
- Test auth paths: wrong passwords, expired tokens, revoked sessions, brute force.
- Have a process for account compromise: revocation and forced re-auth.
