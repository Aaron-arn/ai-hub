# Database Migration Writer

## Description

Describes a schema change and receives a complete, reversible migration: the `up` script with data backfill, a matching `down` script, and a safety checklist. Use it when renaming columns, changing types, adding NOT NULL constraints, or backfilling data — the changes that break production if done carelessly.

## Prompt

You are a database migration specialist. Write a PostgreSQL migration for this change:

Current `users` table:
- `id BIGINT PK`, `email TEXT NOT NULL UNIQUE`, `full_name TEXT`, `is_admin BOOLEAN NOT NULL DEFAULT false`, `created_at TIMESTAMP NOT NULL DEFAULT now()`.

Required change:
1. Split `full_name` into `first_name` and `last_name` (both `TEXT`, nullable).
2. Backfill the two new columns from `full_name`: last space-separated token goes to `last_name`, the rest to `first_name`; empty or NULL `full_name` leaves both NULL.
3. Add column `role TEXT` with a CHECK constraint (`admin`, `user`, `viewer`) and default `user`.
4. Migrate data: where `is_admin = true`, set `role = 'admin'`.
5. Remove `is_admin` and `full_name` ONLY after the backfill is verified, in the same script but at the end.
6. Add index on `role`.

Deliverables:
1. `up.sql`: a single transaction (`BEGIN`/`COMMIT`): `ALTER TABLE` ADD COLUMN first, `UPDATE` backfill, dropping old columns last. Add `COMMENT ON` for the two new columns.
2. `down.sql`: reverses everything safely — rebuild `full_name` as `first_name || ' ' || last_name` (trimmed), restore `is_admin` from `role = 'admin'`, drop the new columns and the index.
3. A "rollback trigger" rule: the down script is only safe before data loss; explain in 3 lines why order matters.
4. A 5-item pre-deploy checklist: staging test copy, row count, 10-row backfill preview, `NOT NULL` impact check, backup.

Output `up.sql` and `down.sql` in separate code blocks, then the checklist.

## Notes

Add the production table size (row count) to the prompt for guidance on batch updates vs single UPDATE. For zero-downtime, ask for the expand-contract version with an application-level switch.
