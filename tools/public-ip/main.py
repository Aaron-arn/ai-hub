"""Public IP lookup using the free ipify API."""

import json
import sys
import urllib.request

API = "https://api.ipify.org?format=json"


def get_ip() -> str:
    with urllib.request.urlopen(API, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))["ip"]


def main() -> None:
    if sys.argv[1:] and sys.argv[1] in ("-h", "--help", "help"):
        print(json.dumps({"usage": "python main.py  ->  {ip}"}))
        sys.exit(0)
    try:
        print(json.dumps({"ip": get_ip()}, indent=2))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}))

if __name__ == "__main__":
    main()
