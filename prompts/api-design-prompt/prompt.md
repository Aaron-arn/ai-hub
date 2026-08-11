# API Design

## Description

Design a REST API contract with resources, status codes and examples.

## Prompt

Design a REST API for {SYSTEM_DESCRIPTION}.

Deliverables:
1. Resource model: entities, relationships, key fields (draw a small diagram in text)
2. Endpoints table: method, path, purpose, auth requirement, rate limit
3. Pagination strategy (cursor vs offset) with rationale
4. Error model: error envelope schema + all possible status codes per endpoint
5. Idempotency: which endpoints need it and how to implement (Idempotency-Key)
6. Versioning strategy
7. Example request/response for the 5 most important endpoints
8. OpenAPI 3.0 snippet for one endpoint

Follow REST best practices: plural nouns, nested only for genuine ownership, no verbs in paths except actions, consistent query param naming.
