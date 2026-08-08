"""System information report (stdlib platform module)."""

import json
import os
import platform
import sys


def info() -> dict:
    return {
        "os": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor() or "unknown",
        "hostname": platform.node(),
        "python": platform.python_version(),
        "cpu_count": os.cpu_count() or 0,
        "cwd": os.getcwd(),
        "user": getattr(os, "getlogin", lambda: "unknown")(),
    }


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if sys.argv[1:] and sys.argv[1] in ("-h", "--help", "help"):
        print(json.dumps({"usage": "python main.py  ->  system info JSON"}))
        sys.exit(0)
    print(json.dumps(info(), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
