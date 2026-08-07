# Web Search

Search the web using DuckDuckGo and retrieve results. No API key required.

## Usage

```bash
python main.py "your query"
python main.py "your query" 10   # limit to 10 results
```

## Output

JSON object with `query` and `results` (title, url, snippet).

## Permissions

- `network` — required to reach DuckDuckGo
