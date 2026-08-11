# Git Workflow

## When to use
Apply whenever working with git in a repository: fixing bugs, adding features, reviewing history, preparing releases.

## Branching
- `main` is always deployable; nothing lands directly on it.
- Feature branch naming: `feat/`, `fix/`, `refactor/`, `docs/`, `chore/` + short kebab-case description.
- Branch off `main` (or an issue branch), never off another feature branch.
- Keep branches short-lived (max a few days); merge or delete.

## Commits
- Conventional Commits format: `type(scope): subject` with type in feat|fix|refactor|docs|test|chore|perf|style|ci|build.
- Subject in imperative mood, under 72 chars, no trailing period.
- One logical change per commit. `git add -p` to stage hunks when a file mixes concerns.
- Never commit secrets, build artifacts, or generated files (use .gitignore).
- Reference issues in the footer: `Closes #123`.

## Before committing
1. `git status` to see what is staged/untracked
2. `git diff --check` for whitespace errors
3. Review `git diff` hunks for accidental changes
4. Run the relevant tests/lint for the changed scope

## Rebasing and merging
- Prefer `git pull --rebase` over merge commits when updating from main.
- Squash-merge feature branches so main history stays linear and readable.
- On conflict: resolve, `git add`, `git rebase --continue`; never force-push a shared branch.

## Release workflow
- Tag releases with `vX.Y.Z` (semver).
- Update CHANGELOG.md per Keep a Changelog.
- If a hotfix branches off the tag, cherry-pick the fix back to main.

## Troubleshooting
- `git reflog` to recover lost commits.
- `git bisect` to find the commit that introduced a regression.
- `git blame` before modifying unfamiliar code.
- Detached HEAD: create a branch immediately if you need to keep work.
