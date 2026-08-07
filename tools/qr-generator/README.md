# QR Generator

Generate QR codes as PNG or SVG images. Requires the `qrcode[pil]` package.

## Usage

```bash
python main.py --data "https://example.com" --out qr.png
python main.py --data "Hello world" --out qr.svg --svg
python main.py --data "https://example.com" --out qr.png --size 6 --border 2
```

## Output

A confirmation message; the QR code image is written to the file given with `--out`.

## Security

- Data is encoded into the QR code only, no execution of content
- No network, no shell access
