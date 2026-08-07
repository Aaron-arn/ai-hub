# IP Tools

Validate and parse IPv4 and IPv6 addresses and CIDR ranges. Uses the Python standard library `ipaddress` module.

## Usage

```bash
python main.py validate 192.168.1.1
python main.py describe "2001:db8::1"
python main.py cidr 10.0.0.0/8
```

## Output

Validation status, address details (version and flags), or CIDR network summary.

## Security

- Pure computation, no I/O
- No network, no filesystem, no shell access
