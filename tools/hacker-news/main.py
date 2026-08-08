"""Hacker News search using the free Algolia HN API."""

import json
import sys
import urllib.error
import urllib.parse
import urllib.request

API = "https://hn.algolia.com/api/v1/search"


def search(query: str, hits: int = 5) -> list[dict]:
    params = urllib.parse.urlencode({"query": query, "tags": "story", "hitsPerPage": hits})
    with urllib.request.urlopen(API + "?" + params, timeout=15) as response:
        data = json.loads(response.read().decode("utf-8"))
    results = []
    for hit in data.get("hits", []):
        results.append({
            "title": hit.get("title"),
            "url": hit.get("url") or "https://news.ycombinator.com/item?id=" + str(hit.get("objectID")),
            "points": hit.get("points"),
            "comments": hit.get("num_comments"),
            "author": hit.get("author"),
            "created": hit.get("created_at"),
        })
    return results


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if not args or args[0] in ("-h", "--help", "help"):
        print(json.dumps({"error": "Usage: python main.py <query> [max_results]"}))
        sys.exit(1)
    try:
        hits = int(args[1]) if len(args) > 1 else 5
        results = search(args[0], hits)
        print(json.dumps({"query": args[0], "results": results}, ensure_ascii=False, indent=2))
    except urllib.error.HTTPError as exc:
        print(json.dumps({"error": f"API error {exc.code}"}))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
