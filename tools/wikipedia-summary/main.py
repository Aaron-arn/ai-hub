"""Wikipedia article summaries from the free REST API."""

import json
import sys
import urllib.error
import urllib.parse
import urllib.request

API = "https://en.wikipedia.org/api/rest_v1/page/summary/"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; AIHub wikipedia/1.0)"}


def summary(title: str, lang: str = "en") -> dict:
    base = API if lang == "en" else f"https://{lang}.wikipedia.org/api/rest_v1/page/summary/"
    url = base + urllib.parse.quote(title.replace(" ", "_"))
    request = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(request, timeout=15) as response:
        data = json.loads(response.read().decode("utf-8"))
    return {
        "title": data.get("title"),
        "extract": data.get("extract"),
        "url": data.get("content_urls", {}).get("desktop", {}).get("page", ""),
        "thumbnail": (data.get("thumbnail") or {}).get("source", ""),
    }


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if not args or args[0] in ("-h", "--help", "help"):
        print(json.dumps({"error": "Usage: python main.py <article_title> [language]"}, ensure_ascii=False))
        sys.exit(1)
    lang = args[1] if len(args) > 1 else "en"
    try:
        data = summary(args[0], lang)
        if data.get("extract") is None:
            data["error"] = "Page not found"
        print(json.dumps(data, ensure_ascii=False, indent=2))
    except urllib.error.HTTPError as exc:
        print(json.dumps({"error": f"API error {exc.code}: page not found"}))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
