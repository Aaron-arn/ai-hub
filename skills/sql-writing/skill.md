# SQL Writing

You write SQL that is readable at a glance and performs well under real data volumes.

## Formatting

- Capitalize keywords (SELECT, FROM, WHERE) and write table and column names in lowercase.
- Put each major clause on its own line; indent conditions in the WHERE clause.
- Use meaningful aliases (`o` for `orders`, `u` for `users`) and always qualify columns with the table alias.
- Write explicit joins with `JOIN ... ON ...`; never use comma-joined tables.
- List the columns you need explicitly; avoid `SELECT *` outside interactive exploration.
- Add comments for non-obvious business logic, not for transliterating the SQL.

## Filtering and joins

- Apply all filters in the WHERE clause; do not rely on HAVING for row filtering.
- Filter joined tables in the WHERE clause only if it cannot change the join semantics; otherwise filter in the ON clause.
- Remember `COUNT(*)` counts rows and `COUNT(col)` counts non-null values; pick deliberately.
- Use `LEFT JOIN` only when you truly need unmatched rows; otherwise `INNER JOIN`.
- Use `EXISTS` instead of `IN` with subqueries when the subquery is large or the outer table is big.
- Avoid `SELECT DISTINCT` as a fix for bad joins; deduplicate the join, not the result.

## Aggregations

- Group by the minimal set of columns that defines your grain; every non-aggregated column must be in GROUP BY.
- Use `FILTER (WHERE ...)` (PostgreSQL) or `CASE WHEN` for conditional aggregation instead of multiple scans.
- Use window functions (`ROW_NUMBER()`, `LAG()`, `SUM() OVER`) for rankings, deltas, and running totals.
- Mind NULLs: use `COALESCE` deliberately, and know that NULL never equals anything, including NULL.

## Performance

- Run `EXPLAIN ANALYZE` on important queries and look for sequential scans on big tables and excessive row counts.
- Push filters and limits as early as possible; the database can often do it for you if you write it directly.
- Avoid functions on indexed columns in the WHERE clause (`WHERE date(created_at) = ...`); use a range instead.
- Be wary of `OR` across different columns; `UNION ALL` of two sargable conditions is often faster.
- Parameterize values; never concatenate user input into a query string.
- Use `LIMIT` with an `ORDER BY` deliberately; without the order it is arbitrary.

## Safety and review

- Use parameter placeholders (`$1`, `?`) for all user-supplied values; guard against SQL injection.
- Escape or avoid dynamic identifiers; never build table or column names from user input.
- Write read-only queries for analysis (use transactions with `READ ONLY` where the driver supports it).
- Test the query against realistic data volumes, not just the sample rows you have locally.
- Prefer one clear query with window functions over many small queries in a loop.
