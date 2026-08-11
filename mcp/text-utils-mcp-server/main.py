import re
import string
from collections import Counter

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("text-utils-server")


@mcp.tool()
def count_stats(text: str) -> str:
    """Count words, characters, lines and reading time of a text."""
    words = re.findall(r"[\w'-]+", text)
    return (
        f"words: {len(words)}\n"
        f"characters: {len(text)}\n"
        f"lines: {text.count(chr(10)) + 1}\n"
        f"reading time: ~{len(words) / 200:.1f} min"
    )


@mcp.tool()
def extract_keywords(text: str, top: int = 10) -> str:
    """Return the most frequent significant words in a text."""
    stop = set(string.punctuation) | {
        "the", "a", "an", "and", "or", "but", "of", "to", "in", "on",
        "for", "with", "at", "by", "is", "are", "was", "were", "be", "this",
        "that", "it", "as", "from", "not", "we", "you", "i", "they", "he", "she",
    }
    words = [w.lower() for w in re.findall(r"[\w'-]+", text) if w.lower() not in stop]
    return "\n".join(f"{w}: {n}" for w, n in Counter(words).most_common(top))


@mcp.tool()
def convert_case(text: str, style: str) -> str:
    """Convert text case. style in: upper, lower, title, snake, kebab, camel, pascal."""
    words = [w for w in re.split(r"[^\w]+", text) if w]
    if style == "upper":
        return text.upper()
    if style == "lower":
        return text.lower()
    if style == "title":
        return text.title()
    if style == "snake":
        return "_".join(w.lower() for w in words)
    if style == "kebab":
        return "-".join(w.lower() for w in words)
    if style == "camel":
        return words[0].lower() + "".join(w.capitalize() for w in words[1:])
    if style == "pascal":
        return "".join(w.capitalize() for w in words)
    raise ValueError(f"unknown style: {style}")


if __name__ == "__main__":
    mcp.run()
