# Git Workflow Helper

## Description

Describes a git problem and receives a safe, ordered list of commands with a plain-language explanation of each one. Use it when you have committed to the wrong branch, need to squash commits, want to undo a push, or have lost work — without guessing and making things worse.

## Prompt

You are a Git expert. I am in a repository with this situation:

- Branch `main` has commits `A -> B -> C`.
- I accidentally created branch `feature` from `main` at `B` and made 4 commits (`D, E, F, G`) on it, then realized my work belongs on a different branch that tracks `main` at `C`.
- I have NOT pushed `feature` yet. I have some uncommitted changes in the working tree that I want to keep.
- I want to end up with: my work squashed into a single commit `H`, placed on a fresh branch `clean-feature` created from `C` (the latest `main`), and nothing referencing `D..G` anymore.

Provide:
1. The exact commands in order, one per line, each preceded by a one-line comment explaining what it does and what state it leaves the repo in.
2. Prefer `git rebase --onto` for the move and `git reset --soft` + `git commit` for the squash; explain why this is safer than `git cherry-pick` here, or justify your alternative.
3. Include the commands to verify the result (`git log --oneline --graph`, `git status`, `git branch -v`).
4. For each destructive step, state the recovery command in case of a mistake (e.g., `git reflog` usage).
5. A one-line summary of the final graph: `main: A B C`, `clean-feature: A B C H`.

Output commands in a single code block with comments, then the final graph summary. Do not use interactive commands like `git rebase -i` in the plan.

## Notes

Replace the lettered graph with your own `git log --oneline` output for exact guidance. Always request a reflog-based undo line — it is the safety net.
