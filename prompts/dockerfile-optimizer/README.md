# Dockerfile Optimizer

Optimize Dockerfiles for size, caching, multi-stage builds and production safety.

## Usage

Open `prompt.md`, copy the text after `## Prompt`, and paste it into your favorite AI assistant (ChatGPT, Claude, Gemini...).

## What it does

- Rewrites your Dockerfile with pinned base images, multi-stage builds and correct instruction ordering.
- Hardens the runtime: non-root user, read-only filesystem, healthcheck and no build tools in the final image.
- Explains each change with the expected impact on size, build time and security.
