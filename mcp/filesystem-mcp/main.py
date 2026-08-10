"""Filesystem MCP server: sandboxed access to a single allowed directory.

Usage:
    AIHUB_ROOT=/path/to/workspace python main.py

Speaks MCP over stdio. All paths are resolved against AIHUB_ROOT and
cannot escape it. Exposes three tools: list_files, read_file, search_files.
"""

import os
from pathlib import Path

from mcp.server.fastmcp import FastMCP

ROOT = Path(os.environ.get("AIHUB_ROOT", ".")).resolve()
MAX_READ_BYTES = 256 * 1024

mcp = FastMCP("filesystem-mcp")


def _safe_path(relative: str) -> Path:
    target = (ROOT / relative).resolve()
    if not target.is_relative_to(ROOT):
        raise ValueError("Path escapes the allowed directory")
    return target


@mcp.tool()
def list_files(relative: str = "") -> list[dict]:
    """List the files and directories inside a directory."""
    path = _safe_path(relative)
    if not path.is_dir():
        raise ValueError("Not a directory")
    return [
        {"name": child.name, "type": "dir" if child.is_dir() else "file"}
        for child in sorted(path.iterdir())
    ]


@mcp.tool()
def read_file(relative: str) -> str:
    """Read a text file (up to 256 KB)."""
    path = _safe_path(relative)
    if not path.is_file():
        raise ValueError("Not a file")
    data = path.read_bytes()
    if len(data) > MAX_READ_BYTES:
        raise ValueError("File is too large to read")
    return data.decode("utf-8", errors="replace")


@mcp.tool()
def search_files(pattern: str, relative: str = "") -> list[str]:
    """Find files whose name matches a glob pattern (e.g. '*.py')."""
    path = _safe_path(relative)
    return [
        str(match.relative_to(ROOT))
        for match in path.rglob(pattern)
        if match.is_file()
    ][:200]


if __name__ == "__main__":
    mcp.run(transport="stdio")
