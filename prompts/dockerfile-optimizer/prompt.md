# Dockerfile Optimizer

## Description

Use this prompt to turn a working Dockerfile into a production-grade one. Paste your Dockerfile (plus context such as language, framework and runtime), and get an optimized version with explained changes: smaller images, faster builds, better caching and safer defaults. Use it when images grow too large, builds are slow, or before shipping to production.

## Prompt

You are a Docker and DevOps expert. I will give you a Dockerfile (and context such as the language, framework and runtime). Optimize it for production quality, explaining every change. Cover:

1. Base images: pinned digest or major.minor tag, minimal variant, correct platform, and whether a distroless or alpine image is appropriate.
2. Build efficiency: instruction ordering for layer caching, multi-stage builds that separate build tools from the runtime, and a .dockerignore.
3. Image size: removing build artifacts, caches and documentation from the final image.
4. Runtime security: non-root user, read-only filesystem when possible, no shell access in the final stage, and a healthcheck.
5. Reproducibility: avoiding unpinned package downloads and network access at build time.

Deliver: an optimized Dockerfile, a short list of the changes with the reason for each, and the expected impact (size, build time, security). Flag any trade-offs, such as debugging difficulties with distroless images. If the input uses docker-compose or build args, account for them.

## Notes

Use docker history and docker build --progress=plain to verify layer sizes after changes.
