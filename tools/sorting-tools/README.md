# Sorting Tools

Sort lines of text in various ways: natural, numeric, reverse, unique.

## Usage

```bash
echo "img10.png" | python main.py
printf "img10.png\nimg2.png\nimg1.png" | python main.py --reverse
printf "10\n2\n1" | python main.py --numeric --unique
```

## Output

The sorted lines, one per line, printed to stdout.

## Security

- Pure local sorting, no external calls
- No network, no filesystem, no shell access
