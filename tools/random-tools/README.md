# Random Tools

Generate secure random numbers, choices and sampling. Uses the `secrets` module for cryptographically secure randomness.

## Usage

```bash
python main.py number --min 1 --max 100
python main.py choice apple banana cherry
python main.py sample --n 2 a b c d e
python main.py password 16
```

## Output

The random value, printed to stdout.

## Security

- Uses `secrets` (cryptographically secure), never `random` for sensitive values
- No network, no filesystem, no shell access
