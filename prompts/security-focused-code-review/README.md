# Security Focused Code Review

Review code for OWASP-class vulnerabilities with severity-ranked findings and fixes.

## Usage

Open `prompt.md`, copy the text after `## Prompt`, and paste it into your favorite AI assistant (ChatGPT, Claude, Gemini...).

## What it does

- Reviews injection, XSS, access control, secrets, cryptography, deserialization and logic flaws.
- Reports each finding with file and line, CWE, severity and attacker exploitability.
- Ranks risks and lists the top three issues to fix before release, with verification tests for suspicions.
