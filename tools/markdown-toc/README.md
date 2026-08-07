# Markdown TOC

Generate a table of contents from Markdown headings.

## Usage

```bash
python main.py docs/guide.md
cat docs/guide.md | python main.py
python main.py README.md
```

## Output

A nested Markdown list of links using GitHub-style anchors, printed to stdout.

## Security

- Reads only the file you provide (or stdin) and never modifies files
- No network, no shell access
