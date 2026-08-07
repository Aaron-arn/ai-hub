"""UUID generator: produces v1, v4 and v5 UUIDs."""

import sys
import uuid


def generate(version, name, namespace):
    if version == "5":
        if not name:
            raise ValueError("v5 UUIDs require --name <name>")
        ns = uuid.UUID(namespace) if namespace else uuid.NAMESPACE_URL
        return uuid.uuid5(ns, name)
    if version == "1":
        return uuid.uuid1()
    if version == "4":
        return uuid.uuid4()
    raise ValueError(f"Unsupported version: {version}")


def usage():
    print("Usage: python main.py <1|4|5> [--name <name>] [--namespace <uuid>] [--count <n>]")
    print("  Default version is 4. Version 5 requires --name.")


def main() -> None:
    args = sys.argv[1:]
    version = "4"
    name = None
    namespace = None
    count = 1
    i = 0
    while i < len(args):
        arg = args[i]
        if arg in ("--name", "--namespace", "--count", "-n", "-ns", "-c"):
            if i + 1 >= len(args):
                print(f"Error: {arg} requires a value")
                sys.exit(1)
            value = args[i + 1]
            if arg in ("--name", "-n"):
                name = value
            elif arg in ("--namespace", "-ns"):
                namespace = value
            else:
                count = int(value)
            i += 2
        elif arg in ("--help", "-h"):
            usage()
            sys.exit(0)
        elif arg in ("1", "2", "3", "4", "5"):
            version = arg
            i += 1
        else:
            print(f"Error: unknown argument: {arg}")
            sys.exit(1)
    try:
        for _ in range(count):
            print(generate(version, name, namespace))
    except ValueError as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
