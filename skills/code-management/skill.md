# Code Management

You follow these guidelines whenever you manage code for the user.

## 1. Version control

- Never commit unless the user explicitly asks.
- Before committing: run `git status`, `git diff`, and `git log --oneline -10`.
- Stage only intended files. Never commit secrets, keys, `.env` files or build artifacts.
- Write concise commit messages that match the repo style.
- Do not amend, force-push, skip hooks, or update git config unless explicitly requested.

## 2. Commits

Each commit should be:

- Small: one logical change per commit.
- Atomic: the code compiles and tests pass at each commit.
- Clear: the message explains *why*, not just *what*.

## 3. Branches

- Default branch: `main`.
- Short-lived feature branches: `feature/<name>`.
- Fix branches: `fix/<name>`.
- Delete branches after merge.

## 4. Dependencies

- Prefer the project's existing libraries and conventions over new ones.
- Before adding a library, check if the project already uses it.
- Keep the dependency list minimal and documented.

## 5. Project hygiene

- Keep the structure obvious: source, tests, docs in clearly named directories.
- No dead code, no commented-out code blocks, no debug prints.
- Follow the existing code style of the project.
- Keep generated files out of the repository (add them to `.gitignore`).
