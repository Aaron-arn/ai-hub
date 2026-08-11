# Markdown Doc

## Description

Turn rough notes into a well-structured Markdown document.

## Prompt

Convert these raw notes into a polished Markdown document: {NOTES}

Structure:
1. H1 title (derived from content), optional 2-line intro
2. H2 sections with H3 subsections, ordered by logical flow (not note order)
3. Tables for anything list-like with 3+ columns
4. Code blocks (fenced with language) for commands and examples
5. A "Quick reference" table at the end for key terms

Rules: remove repetition and filler, keep all factual content, add transitions between sections, use bold for key terms (max 2 per section), use checklist `- [ ]` where appropriate. Output only the document, no commentary.
