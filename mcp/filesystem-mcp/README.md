# Filesystem MCP Server

Exposes sandboxed file access to any MCP-capable assistant through three
tools: `list_files`, `read_file` and `search_files`.

## Install

```bash
aihub install filesystem-mcp
```

## Run

```bash
AIHUB_ROOT=/path/to/workspace python ~/.aihub/packages/filesystem-mcp/main.py
```

All paths are resolved against `AIHUB_ROOT` and can never escape it.

## Tools

- `list_files` — list a directory
- `read_file` — read a text file (256 KB limit)
- `search_files` — glob search by filename pattern
