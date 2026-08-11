# Refactor Suggestions

## Description

Propose a step-by-step refactoring plan for messy code.

## Prompt

Analyze this code and propose a refactoring plan: {CODE}

Output:
1. SMELLS: list code smells with file/line references (duplication, god object, feature envy, long parameter list, etc.)
2. TARGET STATE: describe the ideal structure in 5 bullets (layering, modules, interfaces)
3. STEP-BY-STEP PLAN: numbered, each step = one safe behavior-preserving transformation with the specific technique (extract method, introduce parameter object, etc.)
4. RISKS per step: what tests could catch regressions, which steps change behavior
5. Suggested test additions

Rules: small steps only, prefer structural refactoring over rewrite, mark steps where behavior changes intentionally (bug fixes). Keep naming suggestions concrete, not generic.
