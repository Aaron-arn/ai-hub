# SQL Report Builder

## Description

Gives the assistant a schema and a business question, and receives a correct, well-formatted SQL query with an explanation of the logic. Use it when you need to pull a report from a database and you want the query explained so you can trust and maintain it.

## Prompt

You are a SQL reporting expert. Write the query for this business question against PostgreSQL.

Schema:
- `customers(id, name, signup_date DATE)`
- `orders(id, customer_id FK, total NUMERIC, ordered_at TIMESTAMP)`
- `order_items(order_id FK, product_id FK, qty INT)`
- `products(id, name, price NUMERIC)`

Business question: "For each customer who signed up in 2025 and placed at least 2 orders, show their name, signup date, total spend, average order value, the most ordered product name, and their rank by total spend. Only include customers who have not had an order refunded (we have no refund table — instead, exclude any order where total is negative)."

Requirements:
1. One query using a CTE to pre-aggregate per-customer spend and order count, then a second CTE or join for the most ordered product per customer (tie-break by product name alphabetically).
2. Use `DATE_TRUNC('year', signup_date)` filtered with `EXTRACT(YEAR ...) = 2025`, or equivalent standard SQL, and explain your choice.
3. `RANK() OVER (ORDER BY total_spend DESC)` for the rank column.
4. Correct joins: customers -> orders (INNER, since only customers with orders matter), orders -> order_items, order_items -> products; explain why inner is correct here.
5. Round money to 2 decimals with `ROUND(..., 2)`.
6. Order the final output by rank ascending.
7. Exclude negative-total orders with `WHERE total > 0` before aggregation.

Deliverables: the full query in one code block, a 5-line walkthrough of what each CTE computes, then a note of any missed edge case (e.g., customers with only refunded orders).

## Notes

Add your own table names and the exact business question for a tailored query. Ask for the query in a CTE-free subquery style if your database version or team prefers it.
