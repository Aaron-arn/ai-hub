# Prompt Testing Battery

Build a systematic test suite to validate prompt clarity, edges and robustness.

## Usage

Open `prompt.md`, copy the text after `## Prompt`, and paste it into your favorite AI assistant (ChatGPT, Claude, Gemini...).

## What it does

- Builds a 10-20 case test matrix covering clarity, constraints, edge cases, conflicts and adversarial inputs.
- Gives each case an input, expected behavior and pass/fail criterion.
- Ranks tests by priority and recommends which to automate in CI.
