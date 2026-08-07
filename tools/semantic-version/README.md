# Semantic Version

Parse, validate and compare semantic version strings.

## Usage

```bash
python main.py parse 1.2.3-rc.1+build.5
python main.py compare 1.0.0 1.0.0-rc.1
python main.py compare 2.0.0 1.9.9
```

## Output

The parsed components, or the comparison result (`a < b`, `a == b`, `a > b`).

## Security

- Pure local parsing against the SemVer 2.0.0 grammar
- No network, no filesystem, no shell access
