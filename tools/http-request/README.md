# HTTP Request

Send GET and POST requests. Returns status code, headers and body as JSON.

## Usage

```bash
python main.py get "https://api.example.com/data"
python main.py get "https://api.example.com/data" --timeout 30
python main.py post "https://api.example.com/data" '{"name": "test"}'
```

The body is truncated to 100 KB by default (`--max-bytes`).

## Permissions

- `network` — required to reach remote servers
