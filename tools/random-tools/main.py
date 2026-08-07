"""Random tools: secure random numbers, choices, sampling and passwords."""

import secrets
import string
import sys


def usage():
    print("Usage: python main.py <command> [args]")
    print("Commands:")
    print("  number [--min N] [--max N]   random integer in [min, max] (default 0-100)")
    print("  choice <item> ...            random item from a list")
    print("  sample --n N <item> ...      N random items, no repeats")
    print("  password [length]            random alphanumeric password (default 16)")
    print("  bytes [count]                random bytes as hex (default 16)")


def cmd_number(args):
    lo = int(args[args.index("--min") + 1]) if "--min" in args else 0
    hi = int(args[args.index("--max") + 1]) if "--max" in args else 100
    if hi < lo:
        raise ValueError("--max must be >= --min")
    print(secrets.randbelow(hi - lo + 1) + lo)


def cmd_choice(args):
    if not args:
        raise ValueError("need at least one item to choose from")
    print(secrets.choice(args))


def cmd_sample(args):
    if "--n" not in args:
        raise ValueError("sample requires --n <count>")
    i = args.index("--n")
    if i + 1 >= len(args):
        raise ValueError("sample requires --n <count>")
    n = int(args[i + 1])
    items = args[:i] + args[i + 2:]
    if not items:
        raise ValueError("need at least one item to sample from")
    if n > len(items):
        raise ValueError(f"cannot sample {n} of {len(items)} items")
    print(" ".join(secrets.SystemRandom().sample(items, n)))


def cmd_password(args):
    length = int(args[0]) if args else 16
    if length < 1:
        raise ValueError("length must be >= 1")
    alphabet = string.ascii_letters + string.digits
    print("".join(secrets.choice(alphabet) for _ in range(length)))


def cmd_bytes(args):
    count = int(args[0]) if args else 16
    if count < 1:
        raise ValueError("count must be >= 1")
    print(secrets.token_hex(count))


def main():
    args = sys.argv[1:]
    if not args:
        usage()
        sys.exit(1)
    command = args.pop(0)
    try:
        if command == "number":
            cmd_number(args)
        elif command == "choice":
            cmd_choice(args)
        elif command == "sample":
            cmd_sample(args)
        elif command == "password":
            cmd_password(args)
        elif command == "bytes":
            cmd_bytes(args)
        else:
            raise ValueError(f"unknown command: {command}")
    except (ValueError, IndexError) as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
