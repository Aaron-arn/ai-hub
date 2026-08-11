# Release Notes

## Description

Turn a changelog into customer-friendly release notes.

## Prompt

Write customer-facing release notes for version {VERSION} of {PRODUCT} from this changelog: {CHANGELOG}

Format:
1. Opening line: one sentence celebrating the headline change
2. **Highlights** - the 3 changes customers care most about, each with a headline + 1-2 line plain explanation (avoid technical jargon)
3. **What's new** - short bullets grouped: New, Improved, Fixed
4. **Notes for admins** - only if relevant (migrations, config changes)
5. CTA line (e.g., "Update now" / "Learn more")

Rules: benefit-focused phrasing ("Now you can..."), no internal references, no ticket numbers, no developer jargon, emojis only as section markers. Tone: helpful, concise.
