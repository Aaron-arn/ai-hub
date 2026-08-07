# Unicode Tools

Inspect Unicode characters: names, categories and normalization.

## Usage

```bash
python main.py é
python main.py --normalize NFC "e\u0301"
python main.py --compare "cafe\u0301" "café"
```

## Output

The code point, category, name and normalization forms for each character, or the normalized/compared text.

## Security

- Pure local inspection using the standard `unicodedata` module
- No network, no filesystem, no shell access
