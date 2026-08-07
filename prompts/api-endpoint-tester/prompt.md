# API Endpoint Tester

## Description

Turns an endpoint description into an executable test plan: happy path, error cases, edge cases, and ready-to-run curl commands with expected status codes. Use it before shipping an API change or when you inherit an API with no tests and want a quick manual smoke suite.

## Prompt

You are an API quality engineer. Build a manual test plan for the following endpoint, including executable curl commands.

Endpoint: `POST /api/v1/users`
Request body: `{ "email": "string", "password": "string", "plan": "free|pro" }`
Auth: `Authorization: Bearer <admin token>` required.
Behavior:
- 201 with `{ "id", "email", "plan", "created_at" }` when valid; password never echoed.
- 400 when the body is not valid JSON or unknown fields are present.
- 422 with `{ "errors": [{ "field", "message" }] }` when: email missing/invalid, password under 8 chars, plan not in the allowed set.
- 401 without or with an invalid token.
- 409 when the email is already registered.

Deliverables:
1. A numbered test-case table: id, scenario, request summary, expected status, expected key fields.
2. For each case, a curl command using `-sS`, `-w` to print the HTTP status code, `-H` headers, and `-d` JSON body. Include one with an unknown extra field, one with a short password, one duplicate email, and the missing-token case.
3. A shell one-liner that runs the happy-path test and asserts the status is 201 (using a variable and grep, or `--fail`), so it can be pasted into a CI step.
4. List the 3 riskiest cases and what a regression would indicate.

Base URL is `https://api.example.com`. Output the table in markdown, then the curls in one code block, then the CI one-liner, then the risk list.

## Notes

Replace the endpoint details with yours; the plan structure stays valid. Ask for a Python `pytest` version if you want an automated suite instead of curl commands.
