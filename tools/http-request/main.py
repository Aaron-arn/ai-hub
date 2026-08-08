"""HTTP request tool: send GET and POST requests and return the response."""

import json
import sys
import urllib.error
import urllib.request

USER_AGENT = "aihub-http-request/1.0"


def request(method: str, url: str, data: str | None = None, timeout: int = 15, max_bytes: int = 100_000) -> dict:
    payload = data.encode("utf-8") if data is not None else None
    req = urllib.request.Request(
        url,
        data=payload,
        method=method.upper(),
        headers={"User-Agent": USER_AGENT},
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        body = response.read(max_bytes + 1)
        return {
            "method": method.upper(),
            "url": url,
            "status": response.status,
            "headers": dict(response.headers.items()),
            "body": body[:max_bytes].decode("utf-8", errors="replace"),
            "truncated": len(body) > max_bytes,
        }


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if len(args) < 2 or args[0].lower() not in ("get", "post"):
        print(json.dumps({"error": "Usage: python main.py <get|post> <url> [data] [--timeout 15] [--max-bytes 100000]"}))
        sys.exit(1)
    method = args[0].lower()
    url = args[1]
    data = None
    timeout = 15
    max_bytes = 100_000
    i = 2
    if len(args) > 2 and not args[2].startswith("--"):
        data = args[2]
        i = 3
    while i < len(args):
        if args[i] == "--timeout" and i + 1 < len(args):
            timeout = int(args[i + 1])
            i += 2
        elif args[i] == "--max-bytes" and i + 1 < len(args):
            max_bytes = int(args[i + 1])
            i += 2
        else:
            i += 1
    try:
        result = request(method, url, data, timeout, max_bytes)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (urllib.error.HTTPError, urllib.error.URLError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))
        sys.exit(1)


if __name__ == "__main__":
    main()
