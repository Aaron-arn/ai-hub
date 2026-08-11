from pathlib import Path
import csv

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("csv-server")

WORKSPACE = Path.cwd()


def _resolve(name: str) -> Path:
    path = (WORKSPACE / name).resolve()
    if not str(path).startswith(str(WORKSPACE.resolve())):
        raise ValueError("path escapes workspace")
    return path


def _load(name: str) -> list[dict]:
    with open(_resolve(name), newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


@mcp.tool()
def read_csv(name: str, limit: int = 50) -> str:
    """Read a CSV file and return its first rows with column names."""
    rows = _load(name)
    if not rows:
        return "empty file"
    cols = list(rows[0].keys())
    preview = rows[:limit]
    return f"columns: {cols}\nrows: {len(rows)}\n" + "\n".join(
        f"{i}: {row}" for i, row in enumerate(preview)
    )


@mcp.tool()
def filter_rows(name: str, column: str, value: str) -> str:
    """Return rows where the given column equals value."""
    rows = [r for r in _load(name) if r.get(column) == value]
    return f"matched {len(rows)} rows\n" + "\n".join(str(r) for r in rows[:50])


@mcp.tool()
def summarize(name: str) -> str:
    """Return row count and value counts for each column."""
    rows = _load(name)
    if not rows:
        return "empty file"
    lines = [f"rows: {len(rows)}"]
    for col in rows[0]:
        counts = {}
        for r in rows:
            v = r.get(col, "")
            counts[v] = counts.get(v, 0) + 1
        top = sorted(counts.items(), key=lambda kv: -kv[1])[:5]
        lines.append(f"{col}: unique={len(counts)}, top={top}")
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()
