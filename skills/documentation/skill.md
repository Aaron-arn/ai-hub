# Documentation

You write documentation that answers questions before they are asked.

## 1. README

A good README answers, in order:

1. What is this? (one clear sentence)
2. Why does it exist / when to use it?
3. How to install and run it (exact commands)
4. How to use it (the main commands or examples)
5. How to contribute and test
6. License

Write for the person who has never seen the project.

## 2. Language and style

- Short sentences, active voice, concrete examples.
- Show, don't only tell: every option worth mentioning gets an example.
- Consistent terminology throughout.
- Keep commands copy-pasteable (no placeholders unless explained).

## 3. Code comments and docstrings

- Comment the *why* (intent, constraints), not the *what* (the code already says that).
- Docstrings explain: what the function does, its parameters, its return, and anything surprising.
- No comments that restate the code.

## 4. Changelog

- One section per release: added, changed, fixed, removed.
- Written for users, not for the commit history.
- Breaking changes are highlighted first.

## 5. Maintenance

- Documentation that is wrong is worse than no documentation: verify every command.
- When code changes, update the related docs in the same change.
- Keep one canonical place per piece of information; link instead of copying.
