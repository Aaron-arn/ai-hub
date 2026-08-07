# Regex Tools

Test regular expressions and extract matching groups from text. Uses only the Python standard library `re` module.

## Usage

```bash
python main.py "\d+" "order 42 and 17"
python main.py "(\w+)@(\w+\.\w+)" "mail a@b.com, c@d.org"
python main.py "\d+" "app v1.2.3" --replace "X"
```

## Output

One matched substring per line (with capture groups, if any), or the substituted text when `--replace` is used.

## Security

- Pure computation, no I/O
- No network, no filesystem, no shell access
