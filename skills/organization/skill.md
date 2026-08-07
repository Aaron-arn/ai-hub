# Organization

You follow these guidelines whenever you organize or structure a project.

## 1. Structure

- Keep the root minimal: one directory per concern.
- Put shared code in a shared module, not duplicated per feature.
- Tests live next to the code or in a `tests/` directory — pick one and stick to it.
- No nested directories beyond what is justified.

## 2. Naming

- Descriptive, consistent names: `src/`, `tests/`, `docs/`, `scripts/`.
- Files and folders: lowercase with dashes or underscores, consistent per project.
- Avoid `final`, `v2`, `new`, `copy` suffixes. If a file needs a new version, the version lives in the name of the artifact, not the file.

## 3. Documentation

- One README at the root that explains what, why, and how to run it.
- Keep a changelog if the project is released.
- Document commands in the README or in `AGENTS.md` so agents know how to lint, test and typecheck.

## 4. Workflow

- One source of truth for the project (repo, issue tracker, task list).
- Break work into small, visible steps; track them.
- Keep generated artifacts out of version control.
- Review the structure before adding anything new: does it already exist?

## 5. Priority

A project is organized when a newcomer (human or agent) can understand it in under a minute. If not, simplify.
