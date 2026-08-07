"""QR generator: create QR codes as PNG or SVG images."""

import sys


def usage():
    print("Usage: python main.py --data \"<text>\" --out <file> [--size N] [--border N] [--svg]")


def main():
    args = sys.argv[1:]
    data = None
    out = None
    size = 10
    border = 4
    svg = False
    i = 0
    while i < len(args):
        arg = args[i]
        if arg in ("--data", "--out", "--size", "--border"):
            if i + 1 >= len(args):
                print(f"Error: {arg} requires a value")
                sys.exit(1)
            value = args[i + 1]
            if arg == "--data":
                data = value
            elif arg == "--out":
                out = value
            elif arg == "--size":
                size = int(value)
            else:
                border = int(value)
            i += 2
        elif arg == "--svg":
            svg = True
            i += 1
        elif arg in ("--help", "-h"):
            usage()
            sys.exit(0)
        else:
            print(f"Error: unknown argument: {arg}")
            sys.exit(1)
    if not data or not out:
        usage()
        sys.exit(1)
    try:
        import qrcode
        factory = None
        if svg:
            from qrcode.image.svg import SvgPathImage
            factory = SvgPathImage
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=size,
            border=border,
        )
        qr.add_data(data)
        qr.make(fit=True)
        image = qr.make_image(fill_color="black", back_color="white", image_factory=factory)
        image.save(out)
        print(f"QR code saved to {out}")
    except Exception as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
