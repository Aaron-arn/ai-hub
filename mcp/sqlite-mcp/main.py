"""SQLite MCP server: run read-only SQL queries against a local database.

Usage:
    AIHUB_DB=/path/to/app.db python main.py

Speaks MCP over stdio. Exposes two tools:
  - list_tables(): list tables and their row counts
  - query(sql): run a SELECT query (read-only, single statement)
"""

import os
import sqlite3

from mcp.server.fastmcp import FastMCP

DB_PATH = os.environ.get("AIHUB_DB", "app.db")
MAX_ROWS = 500

mcp = FastMCP("sqlite-mcp")


def _connect() -> sqlite3.Connection:
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


@mcp.tool()
def list_tables() -> list[dict]:
    """List all tables in the database with their row counts."""
    with _connect() as connection:
        rows = connection.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
        ).fetchall()
        result = []
        for row in rows:
            count = connection.execute(
                f"SELECT COUNT(*) FROM '{row['name']}'"
            ).fetchone()[0]
            result.append({"name": row["name"], "rows": count})
        return result


@mcp.tool()
def query(sql: str) -> list[dict]:
    """Run a read-only SELECT query and return up to 500 rows."""
    statement = sql.strip()
    if not statement.lower().startswith("select"):
        raise ValueError("Only SELECT statements are allowed")
    with _connect() as connection:
        cursor = connection.execute(statement)
        columns = [description[0] for description in cursor.description or []]
        rows = cursor.fetchmany(MAX_ROWS)
        return [dict(zip(columns, row)) for row in rows]


if __name__ == "__main__":
    mcp.run(transport="stdio")
