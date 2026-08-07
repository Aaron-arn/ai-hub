# Docker

You build images that are small, cacheable and safe, and you debug containers by reading their logs and layers instead of guessing.

## Dockerfiles

- Start from a specific, pinned image tag (`node:22-alpine`), never `latest`.
- Order layers by change frequency: rarely changing dependency installs first, frequently changing code last.
- Use multi-stage builds: build in one stage, copy only the runtime artifacts to the final image.
- Prefer distroless or alpine bases; strip build tools from runtime images.
- Combine dependency installs in one `RUN` layer and clean the package cache in the same step.
- Use `COPY` of explicit files or `.dockerignore`; never `COPY . .` when more is present than needed.
- Set `WORKDIR`, `ENV`, and `EXPOSE` deliberately; document ports.

## Image size and layering

- Inspect with `docker image history` and `docker build --no-cache` only when cache logic is suspected.
- Keep secrets out of image layers: use build secrets or ARG for non-secret values only.
- Never bake credentials, tokens, or keys into an image; inject at runtime.
- Add a non-root user for the runtime stage and run the app as that user.
- Check your image with `docker scan` or `trivy` for known vulnerabilities.
- Remove debug symbols, caches, and test fixtures from the final stage.

## Running containers

- Run with explicit limits (`--memory`, `--cpus`) and a restart policy (`--restart unless-stopped`).
- Use `--init` for proper signal handling of PID 1, or a real init in the container.
- Read logs with `docker logs -f --tail 100`; inspect config with `docker inspect`.
- Use `docker exec -it <container> sh` to debug a running container; never edit files inside it.
- Healthcheck every service container (`HEALTHCHECK` or compose `healthcheck`).
- Prefer named volumes for persistent data; bind mounts only for dev or config.
- One process per container; do not run several services inside one container.

## Networking and storage

- Connect containers on a user-defined network with service names, not `--link`.
- Expose only needed ports; `-p 127.0.0.1:8080:8080` for local-only services.
- Use secrets and configs from the orchestration layer rather than env vars for sensitive data.
- Make containers stateless where possible; externalize state to volumes or databases.

## Compose and workflows

- Define the stack in `docker-compose.yml` with named services, volumes, and networks.
- Use `docker compose up -d`, check `docker compose ps` and `docker compose logs`.
- Rebuild dependencies after Dockerfile changes: `docker compose build --pull`.
- Clean up with `docker system prune -af --volumes` only deliberately; it removes everything unused.
- Tag images with the commit SHA in CI so deployments are reproducible and rollbackable.
