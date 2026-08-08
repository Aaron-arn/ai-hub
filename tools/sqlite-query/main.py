"""Read-only SQLite queries (SELECT only) using URI mode."""

import json
import sqlite3
import sys

SAFE_PREFIXES = ("select", "with", "pragma", "explain", "begin")
FORBIDDEN = ("insert", "update", "delete", "drop", "create", "alter", "attach", "detach", "vacuum", "reindex")


def is_read_only(query: str) -> bool:
    head = " ".join(query.strip().lower().split()[:2])
    if any(word in head.split() for word in FORBIDDEN):
        return False
    return head.startswith(SAFE_PREFIXES)


def run(db_path: str, query: str, params: list | None = None) -> dict:
    if not is_read_only(query):
        return {"error": "Only read-only queries are allowed"}
    conn = sqlite3.connect("file:" + db_path + "?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    try:
        cursor = conn.execute(query, params or [])
        rows = [dict(row) for row in cursor.fetchmany(1000)]
        return {
            "columns": [item[0] for item in cursor.description] if cursor.description else [],
            "rows": rows,
            "count": len(rows),
        }
    finally:
        conn.close()


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if len(args) < 2 or args[0] in ("-h", "--help", "help"):
        print(json.dumps({"error": "Usage: python main.py <database_path> <sql_query>"}))
        sys.exit(1)
    try:
        print(json.dumps(run(args[0], args[1]), ensure_ascii=False, indent=2))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
