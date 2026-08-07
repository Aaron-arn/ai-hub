# Subnet Calculator

Calculate network, broadcast, mask and host ranges from a CIDR. Uses the Python standard library `ipaddress` module.

## Usage

```bash
python main.py 192.168.1.0/24
python main.py 10.0.0.0/8
python main.py 2001:db8::/64
```

## Output

CIDR, network address, broadcast address, netmask, wildcard mask, prefix length, total and usable host counts, plus the first and last host addresses.

## Security

- Pure computation, no I/O
- No network, no filesystem, no shell access
