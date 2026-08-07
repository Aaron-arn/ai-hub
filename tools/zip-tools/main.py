"""ZIP tools: list, extract and create ZIP archives."""

import os
import sys
import zipfile


def usage():
    print("Usage: python main.py list <archive>")
    print("       python main.py extract <archive> <destination>")
    print("       python main.py create <archive> <file1> [file2 ...]")


def cmd_list(archive):
    with zipfile.ZipFile(archive) as zf:
        for info in zf.infolist():
            name = info.filename if info.is_dir() else info.filename
            size = "" if info.is_dir() else f" ({info.file_size} bytes)"
            print(f"{name}{size}")


def cmd_extract(archive, destination):
    destination = os.path.abspath(destination)
    with zipfile.ZipFile(archive) as zf:
        for info in zf.infolist():
            target = os.path.abspath(os.path.join(destination, info.filename))
            if target != destination and not target.startswith(destination + os.sep):
                raise ValueError(f"unsafe path in archive: {info.filename}")
        zf.extractall(destination)
    print(f"Extracted {archive} to {destination}")


def cmd_create(archive, files):
    if not files:
        raise ValueError("create requires at least one input file")
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in files:
            zf.write(path, os.path.basename(path))
    print(f"Created {archive} with {len(files)} file(s)")


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        usage()
        sys.exit(1)
    command = args[0]
    try:
        if command == "list":
            cmd_list(args[1])
        elif command == "extract":
            if len(args) < 3:
                raise ValueError("extract requires an archive and a destination")
            cmd_extract(args[1], args[2])
        elif command == "create":
            cmd_create(args[1], args[2:])
        else:
            raise ValueError(f"unknown command: {command}")
    except (OSError, zipfile.BadZipFile, ValueError) as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
