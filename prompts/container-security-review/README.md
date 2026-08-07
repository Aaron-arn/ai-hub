# Container Security Review

Audit container images and configs for vulnerabilities, privileges and misconfigurations.

## Usage

Open `prompt.md`, copy the text after `## Prompt`, and paste it into your favorite AI assistant (ChatGPT, Claude, Gemini...).

## What it does

- Audits base image hygiene, privilege, secrets, config, runtime hardening and image scanning.
- Provides a hardened Dockerfile or compose snippet with all fixes applied.
- Builds a CI checklist: scan images, forbid root user, enforce pinned digests.
