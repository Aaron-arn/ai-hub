# Security Audit

## Description

Audit code for security vulnerabilities using OWASP categories.

## Prompt

Perform a security audit of this code: {CODE}

Audit against OWASP Top 10 (2021):
A01 Broken Access Control, A02 Cryptographic Failures, A03 Injection, A04 Insecure Design, A05 Security Misconfiguration, A06 Vulnerable Components, A07 Auth Failures, A08 Integrity Failures, A09 Logging Failures, A10 SSRF.

For each finding: vulnerability name, location, severity (Critical/High/Medium/Low), CWE id, exploitation scenario in 2 sentences, and a concrete fix snippet.

Also check: input validation boundaries, secrets handling (hardcoded keys, log leakage), dependency risk (outdated packages), rate limiting, error messages leaking internals. Finish with a risk summary table and top 3 priorities.
