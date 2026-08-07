"""TAR tools: list, extract and create TAR archives."""

import os
import sys
import tarfile


def usage():
    print("Usage: python main.py list <archive>")
    print("       python main.py extract <archive> <destination>")
    print("       python main.py create <archive> <file1> [file2 ...]")
    print("  gzip/bzip2/xz compression is detected from the file extension.")


def mode_for(archive):
    if archive.endswith((".gz", ".tgz")):
        return "r:gz", "w:gz"
    if archive.endswith(".bz2"):
        return "r:bz2", "w:bz2"
    if archive.endswith(".xz"):
        return "r:xz", "w:xz"
    return "r:", "w:"


def safe_extract(tar, destination):
    destination = os.path.abspath(destination)
    for member in tar.getmembers():
        target = os.path.abspath(os.path.join(destination, member.name))
        if not target.startswith(destination + os.sep):
            raise ValueError(f"unsafe path in archive: {member.name}")
    tar.extractall(destination)


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        usage()
        sys.exit(1)
    command = args[0]
    try:
        if command == "list":
            read_mode, _ = mode_for(args[1])
            with tarfile.open(args[1], read_mode) as tar:
                for member in tar.getmembers():
                    kind = "dir" if member.isdir() else ("link" if member.issym() else "file")
                    print(f"{member.name} ({kind}, {member.size} bytes)")
        elif command == "extract":
            if len(args) < 3:
                raise ValueError("extract requires an archive and a destination")
            read_mode, _ = mode_for(args[1])
            with tarfile.open(args[1], read_mode) as tar:
                safe_extract(tar, args[2])
            print(f"Extracted {args[1]} to {args[2]}")
        elif command == "create":
            if len(args) < 3:
                raise ValueError("create requires an archive and at least one file")
            _, write_mode = mode_for(args[1])
            with tarfile.open(args[1], write_mode) as tar:
                for path in args[2:]:
                    tar.add(path, arcname=os.path.basename(path))
            print(f"Created {args[1]} with {len(args) - 2} file(s)")
        else:
            raise ValueError(f"unknown command: {command}")
    except (OSError, tarfile.TarError, ValueError) as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
