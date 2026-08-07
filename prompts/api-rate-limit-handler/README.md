# API Rate Limit Handler

Generate robust Python code with retries and backoff for rate-limited APIs.

## Usage

Open `prompt.md`, copy the text after `## Prompt`, and paste it into your favorite AI assistant (ChatGPT, Claude, Gemini...).

## What it does

- Retries 429s and transient errors with exponential backoff and jitter.
- Honors Retry-After headers and per-request timeouts.
- Handles pagination with progress logging and loop protection.
