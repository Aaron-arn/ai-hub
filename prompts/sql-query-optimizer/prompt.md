# SQL Query Optimizer

## Description

Paste a slow SQL query and its table schema, and get a rewritten, faster version with index recommendations and an explanation of why it is faster. Use it when a query times out, scans too many rows, or drags down an application. Works for PostgreSQL, MySQL, and SQLite.

## Prompt

You are a database performance expert. I have a slow query and I need it optimized. Here is the context:

Schema:
- `orders(id BIGINT PK, customer_id BIGINT, status VARCHAR(20), total NUMERIC(10,2), created_at TIMESTAMP)`
- `customers(id BIGINT PK, name VARCHAR(100), country VARCHAR(2))`

Query:
```sql
SELECT c.name, COUNT(o.id) AS order_count, SUM(o.total) AS revenue
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE c.country = 'FR' AND o.status = 'paid' AND o.created_at >= '2024-01-01'
GROUP BY c.name
ORDER BY revenue DESC
LIMIT 20;
```

Tasks:
1. Identify the problems: missing predicates, join order, implicit casts, functions on indexed columns, or unnecessary work.
2. Rewrite the query to be logically equivalent and faster. If the LEFT JOIN can become INNER JOIN without changing results, do it and say why.
3. Recommend indexes: exact `CREATE INDEX` statements, one per needed index, and explain which part of the plan each helps.
4. Explain the change in 3-5 short bullets using terms like seq scan, index scan, and filter pushdown.

Output format: a code block with the optimized query, then a code block with the indexes, then the bullets. Do not invent columns that are not in the schema.

## Notes

Include an `EXPLAIN ANALYZE` output in your prompt if you have one, and the optimizer will interpret it directly. State your database engine, since index syntax and planner behavior differ.
