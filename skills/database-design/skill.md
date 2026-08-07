# Database Design

You design relational schemas that are normalized where it matters, indexed where it is hot, and safe to evolve.

## Normalization

- Normalize to third normal form by default: no repeating groups, no partial or transitive dependencies.
- Store a fact once; derive or join instead of duplicating data.
- Use surrogate primary keys (`id BIGSERIAL` or UUID) and add a unique constraint for natural keys.
- Denormalize only with a reason: a measured hot read path, and document the trade-off.
- Prefer junction tables for many-to-many relationships; keep relationship metadata there.

## Data types and constraints

- Choose the smallest correct type: `INTEGER` over `VARCHAR` for ids, `NUMERIC` for money, `TIMESTAMPTZ` for instants.
- Use `VARCHAR(n)` only when the limit is a real business rule; otherwise use `TEXT`.
- Store money as `NUMERIC` or an integer of minor units, never floating point.
- Add every constraint that is true: NOT NULL, CHECK, UNIQUE, FOREIGN KEY.
- Name constraints and indexes explicitly so errors are understandable.
- Use soft deletes sparingly; when used, filter on the flag in every query and index it.

## Naming

- Use singular nouns for tables (`order`, not `orders`) or plural consistently across the schema; pick one.
- Use snake_case everywhere; use consistent suffixes for columns (`_id`, `_at`, `_by`).
- Name foreign key columns after the referenced table: `user_id` in `order`.
- Use a clear pattern for timestamps: `created_at`, `updated_at`, `deleted_at`.

## Indexes

- Index foreign keys used in joins and every column used in WHERE, ORDER BY or GROUP BY hot paths.
- Use composite indexes for queries filtering on multiple columns; order columns by selectivity and query usage.
- Never index a column you do not query on; every index slows writes.
- Be careful with indexes on low-cardinality columns (booleans, small enums); they rarely help.
- Watch for leading-wildcard `LIKE '%x'` queries; they cannot use a B-tree index.
- Monitor with `EXPLAIN ANALYZE`; remove unused indexes, do not add them speculatively.

## Migrations

- Every schema change is a versioned, ordered migration; never edit an applied migration.
- Make migrations forward-only in production; add a separate rollback script where the team keeps them.
- Use additive changes (new columns, new tables) that are safe to deploy before the code that uses them.
- Expand and contract: add the column, backfill, deploy code, then drop the old column.
- Wrap data backfills in the same migration only when the table is small; otherwise do it in batches.
- Test migrations against a copy of production data, not just a fresh database.
- Never change a column type in place on large tables; create a new column and swap it.
