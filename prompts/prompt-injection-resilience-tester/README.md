# Prompt Injection Resilience Tester

Test system prompts against injection attacks and report robustness and defenses.

## Usage

Open `prompt.md`, copy the text after `## Prompt`, and paste it into your favorite AI assistant (ChatGPT, Claude, Gemini...).

## What it does

- Runs an authorized battery of direct, indirect, encoded and role-manipulation injection attacks against your system prompt.
- Scores resistance per attack class (strong, partial, weak) with predicted versus actual outcomes.
- Recommends concrete defenses: delimiting untrusted input, precedence rules, output filtering and least privilege.
