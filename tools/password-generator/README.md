# Password Generator

Generate strong random passwords with configurable length and character sets. Uses the `secrets` module, which is cryptographically secure.

## Usage

```bash
python main.py 16
python main.py 24 --no-symbols
python main.py 12 --count 5
```

## Output

One random password per line, printed to stdout.

## Security

- Uses `secrets.choice`, a cryptographically secure random source
- No network, no filesystem, no shell access
