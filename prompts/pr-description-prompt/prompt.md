# PR Description

## Description

Craft a complete pull request description from a diff summary.

## Prompt

Write a pull request description for this change: {CHANGE_DESCRIPTION} (links: {LINKS})

Sections in order:
1. **Summary** - 2-3 sentences: what and why (no implementation details)
2. **Changes** - bullet list of user-facing behavior changes
3. **Testing** - what was tested, how to reproduce, checklist `- [ ]` items
4. **Screenshots** - placeholder lines (or describe what to attach)
5. **Notes for reviewers** - risky parts, decisions made, alternatives considered
6. **Related issues** - `Closes #n` or `Part of #n`

Tone: neutral, factual. Front-load the "why". Keep under 300 words.
