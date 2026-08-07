# Agent Tool Use Planner

Plan how an AI agent should choose, call and verify tools for a task.

## Usage

Open `prompt.md`, copy the text after `## Prompt`, and paste it into your favorite AI assistant (ChatGPT, Claude, Gemini...).

## What it does

- Selects the right tool per task step with justification and a full execution order.
- Defines argument derivation, fallback behavior for every failure mode, and result verification rules.
- Produces a decision table, stopping criteria and escalation conditions for human handoff.
