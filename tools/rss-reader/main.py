"""RSS reader: fetches RSS or Atom feeds and prints their items."""

import sys
import urllib.request
import xml.etree.ElementTree as ET

ATOM = "{http://www.w3.org/2005/Atom}"


def fetch(url):
  request = urllib.request.Request(url, headers={"User-Agent": "aihub-rss-reader/1.0"})
  try:
    with urllib.request.urlopen(request, timeout=15) as response:
      return response.read()
  except Exception as exc:
    raise ValueError(f"failed to fetch feed: {exc}") from exc


def text(element, path, namespace=""):
  node = element.find(namespace + path)
  if node is None or node.text is None:
    return ""
  return node.text.strip()


def parse_feed(content):
  root = ET.fromstring(content)
  items = []
  if root.tag == "rss":
    channel = root.find("channel")
    if channel is None:
      raise ValueError("no <channel> element found")
    for item in channel.findall("item"):
      items.append({
          "title": text(item, "title"),
          "link": text(item, "link"),
          "description": text(item, "description"),
          "date": text(item, "pubDate"),
      })
  elif root.tag == ATOM + "feed":
    for entry in root.findall(ATOM + "entry"):
      link = entry.find(ATOM + "link")
      items.append({
          "title": text(entry, "title", ATOM),
          "link": link.get("href", "") if link is not None else "",
          "description": text(entry, "summary", ATOM),
          "date": text(entry, "updated", ATOM),
      })
  else:
    raise ValueError(f"'{root.tag}' is not an RSS or Atom feed")
  return [item for item in items if item["title"]]


def main() -> None:
  if len(sys.argv) < 2:
    print("Usage: python main.py <feed-url> [--limit N]")
    sys.exit(1)
  url = sys.argv[1]
  limit = None
  if "--limit" in sys.argv:
    index = sys.argv.index("--limit")
    if index + 1 >= len(sys.argv):
      print("Error: --limit requires a number")
      sys.exit(1)
    try:
      limit = int(sys.argv[index + 1])
    except ValueError:
      print(f"Error: invalid limit '{sys.argv[index + 1]}'")
      sys.exit(1)
  if limit is not None and limit < 1:
    print("Error: limit must be at least 1")
    sys.exit(1)
  try:
    items = parse_feed(fetch(url))
  except Exception as exc:
    print(f"Error: {exc}")
    sys.exit(1)
  if limit is not None:
    items = items[:limit]
  for index, item in enumerate(items, start=1):
    print(f"{index}. {item['title']}")
    if item["link"]:
      print(f"   Link: {item['link']}")
    if item["date"]:
      print(f"   Date: {item['date']}")


if __name__ == "__main__":
  main()
