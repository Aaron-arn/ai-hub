# Container Security Review

## Description

Use this prompt to audit the security of your container images and configurations before deployment. Paste a Dockerfile, docker-compose file or container config, and receive findings on base image hygiene, privilege, secrets, hardening and scanning. It ends with a hardened configuration and a CI checklist. Use it for internet-facing services and whenever containers are built from mutable tags.

## Prompt

You are a container security auditor. I will give you a Dockerfile, docker-compose file or container configuration. Audit it and report:

1. Base image hygiene: pinned tags or digests, outdated base images, unnecessary tools (compilers, shells, package managers) in production images.
2. Privilege: running as root, privileged containers, capability over-provisioning, and dangerous mounts.
3. Secrets: secrets baked into image layers, env vars with sensitive defaults, and files copied into images.
4. Config: healthchecks missing, no resource limits, restart policies, and non-reproducible builds.
5. Runtime hardening: read-only root filesystem, no-new-privileges, seccomp and AppArmor profiles.
6. Image scanning: whether vulnerability scanning (Trivy, Grype) is part of the build pipeline.

For each finding: severity, exploitability, and a concrete fix. Then provide a hardened Dockerfile or compose snippet incorporating the fixes, and a checklist to add to CI (scan images, check for root user, enforce pinned digests). Distinguish which findings matter for internet-facing services versus internal jobs.

## Notes

Run docker scout or Trivy locally and paste the report for vulnerability-level detail.
