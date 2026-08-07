# RSS Reader

Parse RSS and Atom feeds into structured items.

## Usage

```bash
python main.py https://example.com/feed.xml
python main.py https://example.com/feed.xml --limit 5
python main.py https://example.com/atom.xml --limit 3
```

## Output

Numbered items with title, link and date, printed to stdout.

## Security

- Fetches only the URL you provide and parses it with the standard `xml.etree` module
- No filesystem, no shell access
