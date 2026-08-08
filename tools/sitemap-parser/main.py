"""Parse XML sitemaps into URL lists (stdlib urllib + xml)."""

import json
import sys
import urllib.request
import xml.etree.ElementTree as ET


def parse_sitemap(url: str, max_urls: int = 500) -> dict:
    with urllib.request.urlopen(url, timeout=20) as response:
        content = response.read()
    root = ET.fromstring(content)
    urls = []
    namespaces = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    for url_elem in root.findall(".//s:url", namespaces):
        loc = url_elem.find("s:loc", namespaces)
        lastmod = url_elem.find("s:lastmod", namespaces)
        if loc is not None and loc.text:
            urls.append({"url": loc.text.strip(), "lastmod": lastmod.text.strip() if lastmod is not None else ""})
        if len(urls) >= max_urls:
            break
    return {"source": url, "urls": urls, "count": len(urls)}


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if not args or args[0] in ("-h", "--help", "help"):
        print(json.dumps({"error": "Usage: python main.py <sitemap_url> [max_urls]"}))
        sys.exit(1)
    try:
        max_urls = int(args[1]) if len(args) > 1 else 500
        print(json.dumps(parse_sitemap(args[0], max_urls), ensure_ascii=False, indent=2))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
