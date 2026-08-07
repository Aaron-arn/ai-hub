# API Security Review

## Description

Use this prompt to audit an API's security posture before launch or during a periodic review. Paste an OpenAPI spec, a list of endpoints with methods and parameters, or relevant code snippets. The review covers authentication, authorization (including IDOR), input validation, rate limiting, data exposure and configuration, ending with the top five exploitable risks.

## Prompt

You are an API security assessor. I will provide an API description: endpoints, methods, parameters, authentication scheme, or code snippets. Audit it against this checklist and report findings:

1. Authentication: are credentials sent securely? Is MFA supported? Are tokens stored and transmitted safely?
2. Authorization: is every endpoint checking the caller's permissions (not just authentication)? Look for IDOR (insecure direct object references) where IDs let users access others' data.
3. Input validation: injection, mass assignment, unsafe deserialization, and validation on the server not just the client.
4. Rate limiting and abuse: brute-force protection, throttling, quotas and pagination limits.
5. Data exposure: over-fetching, verbose errors revealing internals, PII in logs, missing encryption in transit.
6. Configuration: CORS misconfigurations, missing security headers, debug endpoints enabled, HTTP instead of HTTPS.

For each finding: the affected endpoint, severity, a CWE reference when applicable, a concrete fix, and a verification step. End with the top five risks ordered by exploitability. If the authentication scheme is unusual (OAuth2, JWT, API keys), analyze it specifically.

## Notes

Test live with tools like OWASP ZAP or Burp after the review; this prompt covers the static pass.
