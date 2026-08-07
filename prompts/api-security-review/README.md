# API Security Review

Audit APIs for authentication, authorization, injection and data exposure flaws.

## Usage

Open `prompt.md`, copy the text after `## Prompt`, and paste it into your favorite AI assistant (ChatGPT, Claude, Gemini...).

## What it does

- Audits authentication, authorization (including IDOR), input validation, rate limiting, data exposure and configuration.
- Produces findings with endpoint, severity, CWE reference, fix and verification step.
- Ranks the top five risks by exploitability, with special analysis for OAuth2, JWT or API key schemes.
