# CRC Tools

Compute CRC32 checksums and base64 encode/decode data.

## Usage

```bash
python main.py crc32 "hello world"
python main.py base64 encode "hello world"
python main.py base64 decode "aGVsbG8gd29ybGQ="
```

## Output

The 8-hex-digit CRC32 checksum or the encoded/decoded string.

## Security

- Uses the standard `binascii` and `base64` modules only
- No network, no filesystem, no shell access
