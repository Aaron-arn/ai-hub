"""HTML tools: extract text content and links from HTML pages."""

import sys
from html.parser import HTMLParser


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        if tag in ("p", "br", "div", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self.skip:
            self.skip -= 1
        if tag in ("p", "li", "h1", "h2", "h3", "h4", "h5", "h6"):
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href")
            if href:
                self.links.append(href)


def usage():
    print("Usage: python main.py text|links \"<html>\"")


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        usage()
        sys.exit(1)
    command = args[0]
    html_text = " ".join(args[1:])
    try:
        if command == "text":
            parser = TextExtractor()
            parser.feed(html_text)
            text = "".join(parser.parts)
            lines = [line.strip() for line in text.splitlines() if line.strip()]
            print("\n".join(lines))
        elif command == "links":
            parser = LinkExtractor()
            parser.feed(html_text)
            for link in parser.links:
                print(link)
        else:
            raise ValueError(f"unknown command: {command}")
    except ValueError as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
