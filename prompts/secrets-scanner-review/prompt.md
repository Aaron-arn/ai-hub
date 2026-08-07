# Secrets Scanner Review

## Description

Use this prompt to find hardcoded credentials and sensitive data in source code, configuration files or commit snippets before they leak. Paste the files or text to review. The output includes masked findings with confidence levels, blast radius, and a remediation plan covering rotation, history scrubbing and CI scanning. Use it before pushing to a public repository or after a suspected exposure.

## Prompt

You are a security analyst focused on secrets management. I will give you source code, configuration files or snippets. Review them for exposed secrets and report:

1. Hardcoded secrets: API keys, tokens, passwords, connection strings, private keys and seed values.
2. Implicit secrets: default credentials, test accounts, dummy keys that look real, and empty env vars with misleading names.
3. Leak vectors: secrets in version control history, in comments, in generated files, in frontend code or shipped bundles, and in Docker image layers or env files.
4. PII and sensitive data: emails, IDs, addresses and health or financial data that should not be in the repository.

For each finding, give: the file and line (or exact snippet), the type of secret, an entropy-based confidence estimate, and the blast radius if it leaked. End with a remediation plan: rotation steps, git history scrubbing (with a warning about rewriting history), scanning tools to add to CI (like gitleaks or trufflehog), and policy changes such as secret scanners or vaults. Do not print the full secret value: mask it.

## Notes

Combine with the dependency audit for a full supply-chain check. Remember: rotating the secret is mandatory, not just deleting it.
