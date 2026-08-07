# Image Info

Read image dimensions and format from PNG, JPEG, GIF, BMP and WebP headers. Header-only parsing, no image decoding library required.

## Usage

```bash
python main.py photo.png
python main.py image.jpg
```

## Output

The detected format and dimensions (width x height), printed to stdout.

## Security

- Reads only the first 512 bytes of the file, never decodes content
- No network, no shell access
