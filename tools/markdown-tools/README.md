# Markdown Tools

Convert Markdown text into HTML. Implements headings, lists, code blocks, quotes, emphasis, links and more using only the Python standard library.

## Usage

```bash
python main.py "# Hello\n\nSome **bold** and `code`."
python main.py "## List\n- one\n- two"
python main.py notes.md
```

## Output

The generated HTML, printed to stdout.

## Security

- All text is HTML-escaped before rendering
- No network, no shell access
