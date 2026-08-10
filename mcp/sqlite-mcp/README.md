# SQLite MCP Server

Exposes a SQLite database to any MCP-capable assistant (Claude, etc.) through
two read-only tools: `list_tables` and `query`.

## Install

```bash
aihub install sqlite-mcp
```

## Run

```bash
AIHUB_DB=/path/to/app.db python ~/.aihub/packages/sqlite-mcp/main.py
```

Add it to your MCP client as a stdio server with the command above and the
environment variable `AIHUB_DB` set to your database file.

## Tools

- `list_tables` — lists tables with row counts
- `query` — runs a read-only `SELECT` statement (single statement, up to 500 rows)
