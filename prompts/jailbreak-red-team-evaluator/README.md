# Jailbreak Red Team Evaluator

Run an authorized red-team evaluation of a model's resistance to jailbreak attacks.

## Usage

Open `prompt.md`, copy the text after `## Prompt`, and paste it into your favorite AI assistant (ChatGPT, Claude, Gemini...).

## What it does

- Executes a jailbreak suite across six attack families with exact payloads and outcomes.
- Ranks attack families by success rate and identifies which guardrails failed.
- Produces a hardening report: prompt-level changes, training considerations and detection heuristics.
