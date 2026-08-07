# HTML Tools

Extract text content and links from HTML pages. Uses the Python standard library `html.parser`.

## Usage

```bash
python main.py text "<p>Hello <b>world</b>!</p>"
python main.py links "<a href='https://a.com'>A</a> <a href='https://b.org'>B</a>"
```

## Output

For `text`: the readable text content, one line per block. For `links`: one href per line.

## Security

- Parsing only, no I/O
- No network, no filesystem, no shell access
