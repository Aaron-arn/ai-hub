# Incremental Refactoring Planner

Plan safe, step-by-step refactoring that preserves behavior and verifies every change.

## Usage

Open `prompt.md`, copy the text after `## Prompt`, and paste it into your favorite AI assistant (ChatGPT, Claude, Gemini...).

## What it does

- Breaks refactoring into small, independently mergeable steps with explicit "done" criteria.
- Specifies the tests needed before and during each phase to keep behavior preserved.
- Rates each step's risk and defines rollback conditions for safe reversibility.
