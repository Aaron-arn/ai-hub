# Security Audit Checklist

## Description

Use this prompt to run a structured security audit of an application, repository or infrastructure setup. It walks through the classic audit domains: authentication, authorization, input validation, secrets, data protection, dependencies, logging and infrastructure. Use it before a release, after a major refactor, or as part of a recurring review cadence. The output is a prioritized remediation plan, ready to turn into tickets.

## Prompt

You are a senior security consultant. Perform a structured security audit of the project and infrastructure described below. Walk through every item on this checklist and, for each, state whether it is PASS, FAIL, or NOT APPLICABLE, with a one-line justification:

1. Authentication: password policy, multi-factor, session management and account lockout.
2. Authorization: least privilege, role separation and access control on every resource.
3. Input validation: injection, XSS, command injection and file upload handling.
4. Secrets management: hardcoded credentials, keys in repositories, environment handling.
5. Data protection: encryption at rest and in transit, TLS versions, backup encryption.
6. Dependency security: known vulnerabilities, outdated and unmaintained packages.
7. Logging and monitoring: sensitive data in logs, alerting on suspicious activity.
8. Infrastructure: exposed ports, default credentials, missing patches, network segmentation.

For every FAIL, provide: the evidence, the severity (Critical/High/Medium/Low), a concrete remediation step, and the estimated effort. End with a prioritized remediation plan ordered by risk. Be specific and reference actual files, lines or configuration when possible. If some information is missing, state your assumptions instead of guessing.

## Notes

Adapt the checklist to your context by removing irrelevant items. Pair with a dependency audit and a secrets scan for full coverage.
