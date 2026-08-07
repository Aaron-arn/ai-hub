# JavaScript Data Transformer

## Description

Hands an LLM a messy API payload and asks for a set of pure, tested transformation functions that reshape it into a clean structure. Use it when an external API returns inconsistent, nested, or awkwardly named JSON and you need predictable data for your UI or backend logic.

## Prompt

You are a JavaScript data engineering specialist. I receive the following messy payload from a third-party API:

```json
{
  "order_details": [
    {
      "OrderID": "A-1023",
      "customer": { "CustomerName": "JANE DOE", "EmailAddress": "jane@example.com" },
      "items": [
        { "sku": "SKU-1", "qty": "2", "unit_price": "12.50" },
        { "sku": "SKU-7", "qty": "1", "unit_price": "4.99", "discount_pct": 10 }
      ],
      "OrderDate": "2025-03-14T09:30:00Z",
      "status": "SHIPPED"
    }
  ]
}
```

Write a pure module `transform.js` (no side effects, no external libraries) that exports:
1. `normalizeOrders(raw) -> array` returning `{ id, customer: {name, email}, items: [{sku, qty, unitPrice, lineTotal}], date, status }`, with `lineTotal = qty * unitPrice * (1 - discount/100)`, customer name converted to title case, and id without the `A-` prefix.
2. `summarizeOrders(orders) -> {totalItems, revenue, uniqueCustomers}` computed from the normalized array.
3. `groupByStatus(orders) -> object` mapping status to normalized orders.
4. Handle missing fields gracefully: default `qty` to 0, `unit_price` to 0, `discount_pct` to 0, and unknown status to `"UNKNOWN"`.

Use optional chaining, `map`/`reduce`/`filter`, and no `for` loops. Add JSDoc comments. Then give 3 example assertions (input -> output) proving the discount math and the title-case conversion.

## Notes

Paste real samples of your own payload to get exact field mapping. If amounts come as integers in cents, say so in the prompt and the transformer will convert them.
