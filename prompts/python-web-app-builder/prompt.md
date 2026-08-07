# Python Web App Builder

## Description

Scaffolds a small but production-minded FastAPI application: routers, Pydantic models, structured error handling, and dependency injection. Use it when starting a new backend service and you want clean architecture from the first commit instead of a single monolithic `main.py`.

## Prompt

You are a senior backend engineer. Build a complete FastAPI application for a simple notes API. Python 3.11+, FastAPI, Pydantic v2. In-memory storage (a module-level dict) is fine — no database.

Structure (one file per concern):
1. `main.py` — creates the app, includes the router, adds a middleware logging each request method and path, and defines a root `GET /` returning `{ "service": "notes-api" }`.
2. `models.py` — Pydantic schemas: `NoteCreate` (`title` 1-100 chars, `body` optional, `tags` list of strings max 5), `NoteUpdate` (all optional, at least one field required at validation time), `NoteOut` (adds `id` and `created_at` ISO string).
3. `routes.py` — an `APIRouter` with: `GET /notes` (list, optional `tag` query filter), `GET /notes/{id}` (404 with a clear message if missing), `POST /notes` (201 with the created note, 422 handled by FastAPI), `PUT /notes/{id}` (404 or 200), `DELETE /notes/{id}` (204, idempotent — a second delete also returns 204).
4. `errors.py` — a custom `HTTPException` handler returning `{ "error": { "code", "message" } }` for 404s, and a generic 500 handler that logs and returns a safe message (no stack traces leaked).
5. `deps.py` — a dependency `get_store()` returning the in-memory store, so routes never import it directly.
6. Auto-generated docs must work via `/docs`.

Include type hints everywhere, docstrings on route functions, and `status` module constants instead of raw numbers. Output each file in its own code block with the filename header, then a 5-line usage summary (uvicorn command, example curl for create + get).

## Notes

Say whether you want async routes (`async def`) for I/O-bound work. For a database-backed version, ask to swap `deps.py` with SQLAlchemy session injection.
