# Color Tools

Convert between hex, RGB and HSL color formats. Uses only the Python standard library.

## Usage

```bash
python main.py hex "#ff0000"
python main.py rgb 255 0 128
python main.py hsl 120 50 50
```

## Output

The same color expressed in all three formats (hex, rgb and hsl), printed to stdout.

## Security

- Pure computation, no I/O
- No network, no filesystem, no shell access
