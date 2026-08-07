# Prompt Injection Defense Builder

Harden system prompts and agent designs against prompt injection attacks.

## Usage

Open `prompt.md`, copy the text after `## Prompt`, and paste it into your favorite AI assistant (ChatGPT, Claude, Gemini...).

## What it does

- Rewrites your system prompt with instruction/data separation and precedence rules.
- Adds input, output and architectural defenses: filtering, tool-call allowlists, least privilege.
- Provides a test suite of injection attempts the hardened system should refuse.
