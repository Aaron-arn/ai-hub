# Port Check

Check whether a TCP port is reachable on a host.

## Usage

```bash
python main.py example.com 80
python main.py 127.0.0.1 5432 3
python main.py example.com 443 10
```

## Output

`host:port is open` or `host:port is closed or filtered`.

## Security

- Makes a single TCP connection attempt with a configurable timeout; no other network activity
- No filesystem, no shell access
