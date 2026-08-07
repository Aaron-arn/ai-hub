"""SQL query tool: run read-only SELECT queries against an in-memory SQLite database."""

import sqlite3
import sys


def usage():
    print("Usage: python main.py --table <name> --columns <a,b,c> --rows \"<r1|r2|r3>\" \"<SELECT query>\"")
    print("  Rows are separated by '|', fields by ','. Only SELECT is allowed.")


def main():
    args = sys.argv[1:]
    table = None
    columns = None
    rows = None
    query = None
    i = 0
    while i < len(args):
        arg = args[i]
        if arg in ("--table", "--columns", "--rows"):
            if i + 1 >= len(args):
                print(f"Error: {arg} requires a value")
                sys.exit(1)
            value = args[i + 1]
            if arg == "--table":
                table = value
            elif arg == "--columns":
                columns = value
            else:
                rows = value
            i += 2
        else:
            query = arg
            i += 1
    if not query:
        usage()
        sys.exit(1)
    if query.lstrip().split()[0].upper() != "SELECT":
        print("Error: only read-only SELECT queries are allowed")
        sys.exit(1)
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()
    try:
        if table:
            if not columns or rows is None:
                raise ValueError("--table requires --columns and --rows")
            col_list = [c.strip() for c in columns.split(",")]
            placeholders = ",".join("?" for _ in col_list)
            cursor.execute(f"CREATE TABLE {table} ({','.join(col_list)})")
            for row in rows.split("|"):
                fields = [f.strip() for f in row.split(",")]
                if len(fields) != len(col_list):
                    raise ValueError(f"row '{row}' has {len(fields)} fields, expected {len(col_list)}")
                cursor.execute(f"INSERT INTO {table} VALUES ({placeholders})", fields)
        cursor.execute(query)
        header = [d[0] for d in cursor.description]
        print("\t".join(header))
        for row in cursor.fetchall():
            print("\t".join("" if v is None else str(v) for v in row))
    except sqlite3.Error as exc:
        print(f"Error: {exc}")
        sys.exit(1)
    finally:
        connection.close()


if __name__ == "__main__":
    main()
