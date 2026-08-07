"""Markdown tools: convert Markdown text into HTML."""

import html
import os
import re
import sys


def render_inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"__([^_\n]+?)__", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+?)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"`([^`\n]+?)`", r"<code>\1</code>", text)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', text)
    return text


def convert(markdown):
    out = []
    code_lines = []
    in_code = False
    list_stack = []

    def flush_list():
        while list_stack:
            out.append(f"</{list_stack.pop()}>")

    def close_code():
        nonlocal in_code
        if in_code:
            out.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
            code_lines.clear()
            in_code = False

    for raw in markdown.splitlines():
        line = raw.rstrip()
        if line.startswith("```"):
            flush_list()
            close_code()
            in_code = True
            continue
        if in_code:
            code_lines.append(line)
            continue
        if not line.strip():
            flush_list()
            continue
        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading:
            flush_list()
            level = len(heading.group(1))
            out.append(f"<h{level}>{render_inline(heading.group(2))}</h{level}>")
            continue
        if re.match(r"^>\s*", line):
            flush_list()
            content = line[2:] if line[1:2] == " " else line[1:]
            out.append(f"<blockquote>{render_inline(content)}</blockquote>")
            continue
        if re.match(r"^([-=])\1{2,}$", line):
            flush_list()
            out.append("<hr>")
            continue
        if line.startswith(("* ", "- ")):
            if not list_stack or list_stack[-1] != "ul":
                flush_list()
                out.append("<ul>")
                list_stack.append("ul")
            out.append(f"<li>{render_inline(line[2:])}</li>")
            continue
        ordered = re.match(r"^\d+\.\s+(.*)$", line)
        if ordered:
            if not list_stack or list_stack[-1] != "ol":
                flush_list()
                out.append("<ol>")
                list_stack.append("ol")
            out.append(f"<li>{render_inline(ordered.group(1))}</li>")
            continue
        flush_list()
        out.append(f"<p>{render_inline(line)}</p>")
    flush_list()
    close_code()
    return "\n".join(out)


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"<markdown text>\"")
        print("  If the argument names an existing file, it is read from disk.")
        sys.exit(1)
    try:
        source = sys.argv[1]
        if os.path.exists(source):
            with open(source, "r", encoding="utf-8") as fh:
                source = fh.read()
        print(convert(source))
    except OSError as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
