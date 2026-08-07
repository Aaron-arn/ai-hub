# DNS Lookup

Resolve hostnames to IP addresses (A and AAAA records). Uses the Python standard library `socket` module.

## Usage

```bash
python main.py example.com
python main.py example.com --type A
python main.py example.com --type AAAA
```

## Output

One record per line, prefixed with the record type (e.g. `A: 93.184.216.34`).

## Security

- Requires network access for DNS resolution only
- No filesystem, no shell access
