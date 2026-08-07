# JWT Decode

Decode and inspect JWT headers and payloads without verification.

## Usage

```bash
python main.py "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFsaWNlIn0.signature"
python main.py "eyJhbGciOiJub25lIn0.eyJpc3MiOiJleGFtcGxlLmNvbSJ9."
```

## Output

The decoded header and payload as pretty-printed JSON.

## Security

- Decoding only: signatures are never verified and no external calls are made
- No network, no filesystem, no shell access
