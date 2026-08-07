# API Rate Limit Handler

## Description

Builds a reusable Python HTTP client that survives 429s, timeouts, and transient 5xx errors with exponential backoff and jitter. Use it for any external API integration where naive `requests.get` calls keep failing, or when a batch job dies in the middle of a long run because of throttling.

## Prompt

You are an API integration expert. Write a resilient API client in Python 3.11 using the `requests` library (single dependency).

Context: I call a REST API with a token, 1000 requests per day, rate limits signalled by HTTP 429 with a `Retry-After` header in seconds. Endpoints: `GET /orders?page=N` (paginated, `next` cursor in JSON) and `POST /orders/{id}/refund`.

Requirements:
1. A class `RateLimitedClient` with constructor `(base_url, token, max_retries=5, backoff_base=1.0)`.
2. Private method `_request(method, path, **kwargs)` used by all public methods, implementing:
   - `Authorization: Bearer <token>` header on every call.
   - Retry on 429, 500, 502, 503, 504, and on `requests.exceptions.Timeout`/`ConnectionError`.
   - Exponential backoff `backoff_base * 2 ** attempt` plus random jitter in [0, 0.5) seconds; on 429, honor `Retry-After` header when present (use `max(retry_after, computed_backoff)`).
   - A `RetryBudgetExceeded` custom exception raised after `max_retries`, carrying the last status code and response snippet.
   - A per-request timeout of 10 seconds.
3. Public methods: `get_orders(cursor=None) -> dict` and `refund_order(order_id, amount) -> dict`, both delegating to `_request`.
4. A module-level function `fetch_all_orders(client) -> list` that follows the `next` cursor and stops when it is None, logging progress every 50 pages via `logging`.
5. Protect against infinite loops: a `max_pages` parameter default 1000 raising `ValueError` if exceeded.
6. A short `if __name__ == "__main__":` demo with fake credentials and 3 lines of comments describing how to swap in real ones.

Output the full module in one code block (under 180 lines), then a 5-line usage summary. Do not call the real API during code generation.

## Notes

Add a token-refresh callback parameter if your API uses short-lived tokens. For bulk jobs, ask for a `tenacity`-based variant or a throttling `sleep` between calls.
