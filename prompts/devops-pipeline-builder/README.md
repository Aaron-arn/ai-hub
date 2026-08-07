# DevOps Pipeline Builder

Generate a GitHub Actions CI/CD pipeline with caching and security steps.

## Usage

Open `prompt.md`, copy the text after `## Prompt`, and paste it into your favorite AI assistant (ChatGPT, Claude, Gemini...).

## What it does

- Creates lint, test, and build jobs with dependency caching.
- Pushes Docker images and deploys via SSH on main.
- Cancels stale runs and pins action versions for safety.
