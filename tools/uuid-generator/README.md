# UUID Generator

Generate UUIDs (v1, v4, v5) for unique identifiers. Uses the Python standard library `uuid` module.

## Usage

```bash
python main.py 4
python main.py 1
python main.py 5 --name "user@example.com" --count 3
```

## Output

One UUID per line, printed to stdout.

## Security

- Pure computation, no I/O
- No network, no filesystem, no shell access
