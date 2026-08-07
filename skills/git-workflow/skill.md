# Git Workflow

You follow these guidelines when working with git, keeping history clean and reviewable.

## Branching

- Branch off `main` (or the project's default branch) for every change.
- Name branches with a short, descriptive slug: `fix/login-timeout`, `feat/user-export`.
- Prefix by intent when the project expects it: `feat/`, `fix/`, `chore/`, `docs/`, `refactor/`.
- Never commit directly to `main` unless the project explicitly says so.
- Delete your branch after it is merged.
- Keep one branch per logical change; do not pile unrelated work into a single branch.

## Commits

- Make small, focused commits that each represent one logical step.
- Commit working, tested code only; never commit broken intermediate states.
- Write a concise imperative summary under 50 characters: "Fix login timeout on slow networks".
- Leave the body (wrapped at 72 characters) for the why: context, trade-offs, links to issues.
- Do not include generated files, secrets, or local config in commits; use `.gitignore`.
- Never use `git commit -a` blindly; review staged changes with `git diff --cached` first.

## Staging

- Stage only the files related to the current change.
- Use `git add -p` to stage partial hunks when a file mixes concerns.
- Avoid `git add .` unless you have verified what it picks up.

## Rebasing and history

- Rebase feature branches onto the latest `main` before merging; prefer rebase over merge commits on shared branches.
- Prefer interactive rebase (`git rebase -i`) to squash fixups and reorder commits before pushing.
- Never rewrite history that has already been pushed unless you know everyone who has it.
- Use `git pull --rebase` instead of `git pull` to avoid pointless merge commits.
- Resolve conflicts carefully; when in doubt, preserve both sides and ask.

## Pull requests

- Open the PR early with a draft status if you want feedback before it is done.
- Write a clear title and a description covering: what changed, why, and how it was tested.
- Reference the issue it closes (e.g. "Closes #42") in the description.
- Keep the PR small enough to review; split large changes into stacked PRs when possible.
- Respond to review comments by pushing fixup commits, then clean them up with an interactive rebase.
- Request re-review after addressing feedback rather than relying on stale approvals.

## Reverting and recovering

- Prefer `git revert` over manually deleting changes when a merge must be undone.
- Use `git log -p -- <file>` to trace when a line was introduced.
- Use `git bisect` to find the commit that introduced a regression.
- `git reflog` is the recovery tool for lost commits; do not panic-reset.
- Do not use `git push --force` on shared branches; use `--force-with-lease` when forced pushes are unavoidable.
