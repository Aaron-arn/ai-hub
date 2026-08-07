"""Image info: read image dimensions and format from binary headers (no PIL)."""

import struct
import sys


def info_png(data):
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    width, height = struct.unpack(">II", data[16:24])
    return "PNG", width, height


def info_jpeg(data):
    if data[:2] != b"\xff\xd8":
        return None
    offset = 2
    while offset + 9 < len(data):
        if data[offset] != 0xFF:
            offset += 1
            continue
        marker = data[offset + 1]
        if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
                      0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
            height, width = struct.unpack(">HH", data[offset + 5:offset + 9])
            return "JPEG", width, height
        length = struct.unpack(">H", data[offset + 2:offset + 4])[0]
        offset += 2 + length
    return None


def info_gif(data):
    if data[:6] not in (b"GIF87a", b"GIF89a"):
        return None
    width, height = struct.unpack("<HH", data[6:10])
    return "GIF", width, height


def info_bmp(data):
    if data[:2] != b"BM":
        return None
    width, height = struct.unpack("<ii", data[18:26])
    return "BMP", abs(width), abs(height)


def info_webp(data):
    if data[:4] != b"RIFF" or data[8:12] != b"WEBP":
        return None
    if data[12:16] == b"VP8 ":
        width, height = struct.unpack("<HH", data[26:30])
        return "WebP", width & 0x3FFF, height & 0x3FFF
    if data[12:16] == b"VP8L":
        bits = int.from_bytes(data[21:25], "little")
        return "WebP", (bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1
    if data[12:16] == b"VP8X":
        width = data[24] | data[25] << 8 | data[26] << 16
        height = data[27] | data[28] << 8 | data[29] << 16
        return "WebP", width + 1, height + 1
    return None


DETECTORS = [info_png, info_jpeg, info_gif, info_bmp, info_webp]


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <image_path>")
        sys.exit(1)
    path = sys.argv[1]
    try:
        with open(path, "rb") as fh:
            data = fh.read(512)
    except OSError as exc:
        print(f"Error: {exc}")
        sys.exit(1)
    for detector in DETECTORS:
        result = detector(data)
        if result:
            fmt, width, height = result
            print(f"Format: {fmt}")
            print(f"Dimensions: {width}x{height}")
            return
    print("Error: unsupported or unrecognized image format")
    sys.exit(1)


if __name__ == "__main__":
    main()
