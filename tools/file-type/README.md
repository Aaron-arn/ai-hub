# File Type

Detect file type from magic bytes. Reads only the first 512 bytes of the file, so it is fast and safe.

## Usage

```bash
python main.py document.pdf
python main.py archive.zip
python main.py photo.png
```

## Output

A human-readable type description, printed to stdout.

## Security

- Reads only a fixed 512-byte header, never the full file
- No network, no shell access
