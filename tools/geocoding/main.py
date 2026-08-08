"""Geocoding: place name to latitude/longitude (Open-Meteo, no key)."""

import json
import sys
import urllib.error
import urllib.parse
import urllib.request

API = "https://geocoding-api.open-meteo.com/v1/search"


def search(name: str, count: int = 5) -> list[dict]:
    query = urllib.parse.urlencode({"name": name, "count": count, "language": "en"})
    with urllib.request.urlopen(API + "?" + query, timeout=15) as response:
        data = json.loads(response.read().decode("utf-8"))
    results = []
    for item in data.get("results", [])[:count]:
        results.append({
            "name": item.get("name"),
            "country": item.get("country"),
            "admin1": item.get("admin1"),
            "latitude": item.get("latitude"),
            "longitude": item.get("longitude"),
            "population": item.get("population"),
        })
    return results


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if not args or args[0] in ("-h", "--help", "help"):
        print(json.dumps({"error": "Usage: python main.py <place_name> [max_results]"}, ensure_ascii=False))
        sys.exit(1)
    try:
        count = int(args[1]) if len(args) > 1 else 5
        results = search(args[0], count)
        if not results:
            print(json.dumps({"query": args[0], "results": [], "message": "No match found"}))
        else:
            print(json.dumps({"query": args[0], "results": results}, ensure_ascii=False, indent=2))
    except urllib.error.HTTPError as exc:
        print(json.dumps({"error": f"API error {exc.code}"}))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
