# Hex Dump

Print hexadecimal dumps of files or strings.

## Usage

```bash
python main.py image.png
python main.py --string "Hello"
python main.py --string "abc123"
```

## Output

Offset, hexadecimal bytes and a printable ASCII rendering per line, hexdump style.

## Security

- Reads only the file or string you provide and never modifies data
- No network, no shell access
