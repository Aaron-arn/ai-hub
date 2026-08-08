"""Web search tool using DuckDuckGo (no API key required)."""

import html
import json
import re
import sys
import urllib.parse
import urllib.request

URL = "https://html.duckduckgo.com/html/"


def search(query: str, max_results: int = 5) -> list[dict]:
    data = urllib.parse.urlencode({"q": query}).encode()
    request = urllib.request.Request(
        URL,
        data=data,
        headers={"User-Agent": "Mozilla/5.0 (compatible; AIHub web-search/1.0)"},
    )
    with urllib.request.urlopen(request, timeout=15) as response:
        page = response.read().decode("utf-8", errors="replace")

    results = []
    anchors = list(
        re.finditer(r'class="result__a" href="([^"]+)"[^>]*>(.*?)</a>', page, re.DOTALL)
    )
    for index, match in enumerate(anchors):
        end = match.end()
        next_start = anchors[index + 1].start() if index + 1 < len(anchors) else len(page)
        snippet_match = re.search(
            r'class="result__snippet"[^>]*>(.*?)</a>', page[end:next_start], re.DOTALL
        )
        results.append(
            {
                "title": html.unescape(re.sub(r"<[^>]+>", "", match.group(2))).strip(),
                "url": html.unescape(match.group(1)),
                "snippet": (
                    html.unescape(re.sub(r"<[^>]+>", "", snippet_match.group(1))).strip()
                    if snippet_match
                    else ""
                ),
            }
        )
        if len(results) >= max_results:
            break
    return results


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if not args:
        print(json.dumps({"error": "Usage: python main.py \"<query>\" [max_results]"}))
        sys.exit(1)
    query = args[0]
    max_results = int(args[1]) if len(args) > 1 else 5
    try:
        results = search(query, max_results)
        print(json.dumps({"query": query, "results": results}, ensure_ascii=False, indent=2))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))
        sys.exit(1)


if __name__ == "__main__":
    main()
