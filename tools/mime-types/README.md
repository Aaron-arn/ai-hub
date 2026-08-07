# MIME Types

Look up MIME types from file extensions and vice versa.

## Usage

```bash
python main.py .json
python main.py image/png
python main.py pdf
```

## Output

The matching MIME type or file extension, printed as `key: value`.

## Security

- Pure local lookup using the standard `mimetypes` module
- No network, no filesystem, no shell access
