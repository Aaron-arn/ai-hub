# Resume Optimizer

## Description

Rewrite resume bullets for impact using the STAR method.

## Prompt

Optimize this resume for a {ROLE} application: {RESUME}

1. BULLETS: rewrite each to follow: action verb + what you did + measurable outcome (metric or scale). Convert passive statements to active. Max 2 lines each.
2. GAPS: flag missing keywords for {ROLE} that I should add (from real experience only).
3. STRUCTURE: order sections for this role: summary, skills, experience, education, extras.
4. SUMMARY: 2 lines - who you are, what you deliver, target role.
5. ATS CHECK: note any formatting that will break ATS parsing (tables, columns, graphics).

Rules: never invent facts or metrics - where a number is missing write [INSERT METRIC]. Output a markdown table: original bullet | rewritten bullet | why better.
