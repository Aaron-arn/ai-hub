# Calculator

Safely evaluate arithmetic expressions. Uses the Python AST instead of `eval()`, so arbitrary code cannot be executed.

## Usage

```bash
python main.py "2 + 2 * 3"
python main.py "(10 - 4) / 3"
python main.py "2 ** 10"
```

## Output

The numeric result, printed to stdout.

## Security

- No `eval` — expressions are parsed into an AST and only numeric operations are allowed
- No network, no filesystem, no shell access
