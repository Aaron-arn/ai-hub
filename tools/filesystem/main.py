"""Filesystem tool: list, read and write files inside a sandboxed directory."""

import json
import os
import sys

SAFE_COMMANDS = ("list", "read", "write")


def base_dir() -> str:
    return os.environ.get("AIHUB_FS_ROOT") or os.path.join(os.path.expanduser("~"), ".aihub", "sandbox")


def resolve(relative_path: str) -> str:
    root = os.path.realpath(base_dir())
    target = os.path.realpath(os.path.join(root, relative_path))
    if target != root and not target.startswith(root + os.sep):
        raise ValueError(f"Path escapes sandbox: {relative_path}")
    return target


def cmd_list(path: str) -> dict:
    target = resolve(path)
    if not os.path.exists(target):
        if target == os.path.realpath(base_dir()):
            return {"path": path, "entries": []}
        return {"error": f"Not found: {path}"}
    if os.path.isdir(target):
        entries = [
            {
                "name": name,
                "type": "dir" if os.path.isdir(os.path.join(target, name)) else "file",
            }
            for name in sorted(os.listdir(target))
        ]
        return {"path": path, "entries": entries}
    return {"path": path, "type": "file"}


def cmd_read(path: str) -> dict:
    target = resolve(path)
    if not os.path.isfile(target):
        return {"error": f"Not a file: {path}"}
    with open(target, "r", encoding="utf-8", errors="replace") as fh:
        return {"path": path, "content": fh.read()}


def cmd_write(path: str, content: str) -> dict:
    target = resolve(path)
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(content)
    return {"path": path, "written": True}


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if len(args) < 1 or args[0] not in SAFE_COMMANDS:
        print(f"Usage: python main.py <{'|'.join(SAFE_COMMANDS)}> <path> [content]")
        sys.exit(1)
    command = args[0]
    try:
        if command == "list":
            result = cmd_list(args[1] if len(args) > 1 else ".")
        elif command == "read":
            result = cmd_read(args[1])
        else:
            result = cmd_write(args[1], args[2] if len(args) > 2 else "")
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))
        sys.exit(1)


if __name__ == "__main__":
    main()
