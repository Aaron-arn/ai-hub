"""Send messages to Discord via webhook."""

import json
import sys
import urllib.request


def send(webhook_url: str, content: str, username: str | None = None) -> int:
    payload = {"content": content}
    if username:
        payload["username"] = username
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        webhook_url, data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=15) as response:
        return response.status


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if len(args) < 2 or args[0] in ("-h", "--help", "help"):
        print(json.dumps({"error": "Usage: python main.py <webhook_url> <message> [username]"}))
        sys.exit(1)
    try:
        username = args[2] if len(args) > 2 else None
        status = send(args[0], args[1], username)
        print(json.dumps({"status": status, "sent": True}))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
