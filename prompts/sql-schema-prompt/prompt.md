# SQL Schema

## Description

Design a normalized database schema from a requirements list.

## Prompt

Design a PostgreSQL schema for {SYSTEM_DESCRIPTION}.

Requirements: {REQUIREMENTS}

Output:
1. Tables with columns, types, constraints (PK, FK, UNIQUE, NOT NULL, CHECK)
2. Indexes with rationale (which queries they serve)
3. Normalization notes: which rules applied and why (up to 3NF unless justified)
4. Enum definitions
5. Sample INSERT/UPDATE for 2 core tables
6. 3 tricky queries this schema should support (write the SQL)
7. Migration ordering: how tables must be created (dependency order)

Assume 10k-100k rows growth per month. Use snake_case, plural table names, timestamptz.
