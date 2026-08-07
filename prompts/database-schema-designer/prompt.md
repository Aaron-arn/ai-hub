# Database Schema Designer

## Description

Turns a plain-English description of a domain into a normalized relational schema with full DDL: tables, constraints, indexes, and a data dictionary. Use it at the start of any project when you need a solid database design before writing application code.

## Prompt

You are a database architect. Design a PostgreSQL schema for a small e-commerce app with the following domain rules:

- Customers have name, email (unique), and country. A customer can place many orders.
- Orders belong to one customer, have a status (pending, paid, shipped, cancelled), a total, and are created with a timestamp.
- An order contains multiple line items; each line item references one product and a quantity.
- Products have a name, SKU (unique), current price, and stock quantity.
- A product may belong to zero or more categories; categories have a name (unique) and optional parent category.
- The app needs to query: orders of a customer in the last 30 days, products with low stock (< 5), and revenue per category.

Deliverables:
1. An ER description: list every table with its primary key, foreign keys, and the cardinality of each relationship.
2. Full DDL: `CREATE TABLE` statements with `BIGSERIAL` primary keys, `NOT NULL` where required, `CHECK` constraints (positive prices and quantities, valid status), `UNIQUE` constraints, and foreign keys with sensible `ON DELETE` behavior (block deletion of customers with orders).
3. Indexes: one per frequently filtered column or combination, each justified in one line.
4. Normalization note: state the highest normal form achieved and why.
5. Seed data: 3 products, 2 categories, 1 customer with 1 order of 2 items, for a smoke test.

Output the DDL in one code block, then the seed data in another, then short answers for points 1 and 4.

## Notes

Swap "PostgreSQL" for MySQL or SQLite and the syntax adapts. For large domains, describe the rules in bullet points exactly like above and ask for the design before the DDL.
