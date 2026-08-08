"""Minimal Markdown to HTML converter (stdlib only)."""

import html
import json
import re
import sys


def convert(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    list_stack: list[str] = []
    in_code = False
    code_buffer: list[str] = []

    def close_list() -> None:
        while list_stack:
            out.append("</" + list_stack.pop() + ">")

    for raw in lines:
        if raw.strip().startswith("```"):
            if in_code:
                out.append("<pre><code>" + html.escape("\n".join(code_buffer)) + "</code></pre>")
                code_buffer = []
                in_code = False
            else:
                close_list()
                in_code = True
            continue
        if in_code:
            code_buffer.append(raw)
            continue
        stripped = raw.strip()
        if not stripped:
            close_list()
            continue
        m = re.match(r"^(#{1,6})\s+(.*)", stripped)
        if m:
            close_list()
            level = len(m.group(1))
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            continue
        m = re.match(r"^[-*]\s+(.*)", stripped)
        if m:
            if not list_stack or list_stack[-1] != "ul":
                close_list()
                out.append("<ul>")
                list_stack.append("ul")
            out.append("<li>" + inline(m.group(1)) + "</li>")
            continue
        m = re.match(r"^\d+[.)]\s+(.*)", stripped)
        if m:
            if not list_stack or list_stack[-1] != "ol":
                close_list()
                out.append("<ol>")
                list_stack.append("ol")
            out.append("<li>" + inline(m.group(1)) + "</li>")
            continue
        close_list()
        out.append("<p>" + inline(stripped) + "</p>")
    close_list()
    if in_code:
        out.append("<pre><code>" + html.escape("\n".join(code_buffer)) + "</code></pre>")
    return "\n".join(out)


def inline(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', text)
    return text


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if not args or args[0] in ("-h", "--help", "help"):
        print(json.dumps({"error": "Usage: python main.py <markdown_text>  (or read from stdin)"}, ensure_ascii=False))
        sys.exit(1)
    try:
        source = args[0] if args else sys.stdin.read()
        print(json.dumps({"html": convert(source)}, ensure_ascii=False))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
