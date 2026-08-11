# Code Review

## Description

Systematic code review checklist prompt for any diff.

## Prompt

Review the following code as a senior engineer. Focus on:

1. CORRECTNESS: logic errors, off-by-one, race conditions, exception paths
2. SECURITY: injection, auth bypass, secrets, path traversal, SSRF
3. PERFORMANCE: unnecessary loops, N+1 queries, memory leaks, async blocking
4. MAINTAINABILITY: naming, duplication, dead code, complexity (note cyclomatic hotspots)
5. API DESIGN: breaking changes, error handling consistency, backward compat

Output format per issue: `[SEVERITY 1-3] file:line - one sentence problem` followed by a suggested fix snippet. Group by category, then a final verdict: approve / approve with nits / request changes. Only flag real issues, not style preferences. If code is missing context, state assumptions explicitly.
