"""File type: detect file type from magic bytes."""

import sys


def detect(data):
    if data.startswith(b"%PDF-"):
        return "PDF document"
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return "PNG image"
    if data.startswith(b"\xff\xd8\xff"):
        return "JPEG image"
    if data[:6] in (b"GIF87a", b"GIF89a"):
        return "GIF image"
    if data.startswith(b"BM"):
        return "BMP image"
    if data.startswith(b"PK\x03\x04"):
        return "ZIP archive (or Office/Java package)"
    if data.startswith(b"\x1f\x8b"):
        return "GZIP archive"
    if data.startswith(b"Rar!\x1a\x07"):
        return "RAR archive"
    if data.startswith(b"7z\xbc\xaf\x27\x1c"):
        return "7-Zip archive"
    if data.startswith(b"SQLite format 3\x00"):
        return "SQLite database"
    if data.startswith(b"\x7fELF"):
        return "ELF executable"
    if data.startswith(b"MZ"):
        return "Windows executable (PE)"
    if data.startswith(b"OggS"):
        return "OGG media"
    if data.startswith(b"ID3"):
        return "MP3 audio"
    if data[:4] == b"RIFF":
        if data[8:12] == b"WEBP":
            return "WebP image"
        if data[8:12] == b"WAVE":
            return "WAV audio"
        return "RIFF container"
    if data[257:262] == b"ustar":
        return "TAR archive"
    if data[:5].lower() == b"<?xml":
        return "XML document"
    if data.startswith(b"\xef\xbb\xbf"):
        return "UTF-8 text (BOM)"
    return "Plain text or unknown binary"


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_path>")
        sys.exit(1)
    path = sys.argv[1]
    try:
        with open(path, "rb") as fh:
            data = fh.read(512)
    except OSError as exc:
        print(f"Error: {exc}")
        sys.exit(1)
    print(detect(data))


if __name__ == "__main__":
    main()
