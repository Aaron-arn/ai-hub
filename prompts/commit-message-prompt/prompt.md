# Commit Message

## Description

Generate conventional commit messages from a diff.

## Prompt

Generate a commit message for this diff: {DIFF}

Follow the Conventional Commits spec:
- Format: `type(scope): subject` where type in feat|fix|refactor|docs|test|chore|perf|style|ci|build
- Subject: imperative mood, <= 72 chars, no trailing period
- Body: explain WHY, not what (what is in the diff); max 5 bullets, each <= 80 chars
- Footer: `BREAKING CHANGE:` line only if the diff introduces breaking changes, or `Closes #n` if issues referenced

Provide 3 options: standard, minimal (subject only), and detailed. Also flag if the diff mixes multiple concerns (should be split).
