# MAC Address

Validate, format, parse and generate MAC addresses.

## Usage

```bash
python main.py validate 00:1A:2B:3C:4D:5E
python main.py format 001a.2b3c.4d5e -
python main.py generate
```

## Output

A validation result, a reformatted address or a generated random address.

## Security

- Pure local operations; generated addresses use `random` and are not sent anywhere
- No network, no filesystem, no shell access
