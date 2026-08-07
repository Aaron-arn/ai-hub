# DevOps Pipeline Builder

## Description

Describes a project and receives a complete GitHub Actions workflow: lint, test, build, artifact upload, and a secure deploy job. Use it when adding CI to a repository, or when your existing pipeline is slow because dependencies are reinstalled on every run.

## Prompt

You are a CI/CD expert. Write a GitHub Actions workflow for this project:

- Stack: Python 3.12, FastAPI backend in `app/`, `pytest` tests in `tests/`, `ruff` for linting, `pip` with a `requirements.txt`, Docker image built with the tag `registry.example.com/app:${GITHUB_SHA::7}`.
- Branches: `main` is the deploy branch; all branches run the full pipeline except deployment.

Workflow requirements (name it `ci.yml` under `.github/workflows/`):
1. Trigger on `push` to `main` and on `pull_request` (all branches).
2. Job `test` on `ubuntu-latest`: checkout, set up Python 3.12, cache `pip` keyed on `requirements.txt` hash (use `actions/setup-python` cache), install, run `ruff check .`, then `pytest -q` with a step uploading the `pytest.xml` report via `actions/upload-artifact` even if tests fail (`if: failure()` or `always()` — justify the choice).
3. Job `build`, needs `test`: login to the registry using `docker/login-action` with secrets `REGISTRY_USER` and `REGISTRY_PASSWORD`, then `docker/build-push-action` with `push: true` on `main` only, and cache from `type=gha`.
4. Job `deploy`, needs `build`, `if: github.ref == 'refs/heads/main'`: one step running a deploy command over SSH via `appleboy/ssh-action` with secrets `DEPLOY_HOST`, `DEPLOY_USER`, `DEPLOY_KEY`; it pulls the built image and restarts the container (`docker compose up -d --pull always`).
5. Concurrency group keyed on the branch so fast PR pushes cancel stale runs, and `timeout-minutes: 15` on the test job.
6. Pin the third-party actions to their latest major tag.

Output the full YAML in one code block, then a 4-line summary of the secrets that must be set in the repo settings.

## Notes

Swap the stack lines for Node, Go, or Java — the job structure stays identical. Ask for a matrix build if you need multiple Python or Node versions.
