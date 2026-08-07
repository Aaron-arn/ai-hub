# HTML Entities

Encode and decode HTML entities in text.

## Usage

```bash
python main.py encode "<b>AT&T</b>"
python main.py decode "&lt;b&gt;AT&amp;T&lt;/b&gt;"
python main.py decode "Tom &amp; Jerry &copy; 2025"
```

## Output

The encoded or decoded text, printed to stdout.

## Security

- Uses the standard `html` module only
- No network, no filesystem, no shell access
