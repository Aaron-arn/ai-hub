"""DNS lookup: resolve hostnames to A and AAAA records."""

import socket
import sys


def usage():
    print("Usage: python main.py <hostname> [--type A|AAAA|ANY]")


def main():
    args = sys.argv[1:]
    if not args:
        usage()
        sys.exit(1)
    hostname = args[0]
    record_type = "ANY"
    if "--type" in args:
        i = args.index("--type")
        if i + 1 >= len(args):
            print("Error: --type requires a value")
            sys.exit(1)
        record_type = args[i + 1].upper()
        if record_type not in ("A", "AAAA", "ANY"):
            print("Error: --type must be A, AAAA or ANY")
            sys.exit(1)
    try:
        infos = socket.getaddrinfo(hostname, None, 0, socket.SOCK_STREAM)
        seen = set()
        for info in infos:
            family = info[0]
            address = info[4][0]
            kind = "A" if family == socket.AF_INET else "AAAA"
            if record_type not in ("ANY", kind):
                continue
            key = (kind, address)
            if key in seen:
                continue
            seen.add(key)
            print(f"{kind}: {address}")
        if not seen:
            print(f"No {record_type} records found for {hostname}")
    except socket.gaierror as exc:
        print(f"Error: could not resolve {hostname}: {exc}")
        sys.exit(1)
    except OSError as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
