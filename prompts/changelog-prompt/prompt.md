# Changelog

## Description

Write a Keep a Changelog entry from a list of changes.

## Prompt

Write a changelog entry for version {VERSION} from these changes: {CHANGES}

Follow Keep a Changelog format:
1. `## [{VERSION}] - {DATE}`
2. Categories in order: `### Added` / `### Changed` / `### Deprecated` / `### Removed` / `### Fixed` / `### Security`
3. One bullet per change: past-tense-free, user-facing phrasing ("Added a keyboard shortcut for..." not "Updated handler.js")
4. Omit categories with no entries
5. Optional `### Migrations` section for breaking changes with a one-line migration note
6. Add a `## [Unreleased]` section above if missing

Keep each bullet under 100 chars. Write for users and maintainers, not for the git log.
