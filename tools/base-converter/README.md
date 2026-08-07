# Base Converter

Convert numbers between bases 2, 8, 10, 16 and 36. Uses only the Python standard library.

## Usage

```bash
python main.py ff 16 10
python main.py 255 10 2
python main.py abc 16 36
```

## Output

The number expressed in the target base, printed to stdout.

## Security

- Pure computation, no I/O
- No network, no filesystem, no shell access
