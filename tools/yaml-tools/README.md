# YAML Tools

Convert between YAML and JSON documents. Requires the `PyYAML` package.

## Usage

```bash
python main.py yaml2json "name: Alice
age: 30"
python main.py json2yaml '{"name": "Bob", "tags": ["a", "b"]}'
```

## Output

The converted document, printed to stdout.

## Security

- Uses `yaml.safe_load` only (no arbitrary object construction)
- No network, no filesystem, no shell access
