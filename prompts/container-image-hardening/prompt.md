# Container Image Hardening

## Description

Use this prompt to audit a Dockerfile or a container image before shipping it. It walks through base image selection, user privileges, secrets, filesystem permissions, dependency management and runtime hardening, and produces a prioritized list of fixes.

## Prompt

You are a container security engineer. Analyze the Dockerfile I provide and produce a hardening review of the resulting image.

For each finding, report: the issue, the risk (critical / high / medium / low), and the exact fix.

Review these areas in order:

1. Base image — pin to a specific digest or tag, prefer minimal images (alpine, distroless, scratch), and remove unused layers.
2. User — run as a non-root user; create one with `RUN useradd` before any privileged step; set `USER` before `EXPOSE`/`ENTRYPOINT`.
3. Secrets — no `ENV` or `ARG` for passwords, tokens or API keys; prefer build secrets or mounts; check `RUN` layers for leaked values.
4. Filesystem — make the writable paths explicit with `VOLUME`, use read-only root filesystem when possible, and remove setuid/setgid binaries that are not needed.
5. Dependencies — flag unpinned versions, known vulnerable packages, and unnecessary build tools left in the final stage.
6. Runtime — recommend `CAP_DROP ALL` with selective capabilities, avoid `--privileged`, and use an ENTRYPOINT that validates its input.

End with a summarized hardening checklist of the five most impactful changes, ordered by effort versus risk reduction. Do not run any command; only produce the review.

## Notes

- Best used together with a vulnerability scanner (Trivy, Grype) for version-level findings.
- Works for Kubernetes manifests too if you ask it to review the `securityContext` section.
