# SQL Query

Run read-only SQL queries against an in-memory SQLite database. Uses the Python standard library `sqlite3`.

## Usage

```bash
python main.py --table users --columns "id,name,age" --rows "1,Alice,30|2,Bob,25" "SELECT * FROM users"
python main.py --table users --columns "id,name,age" --rows "1,Alice,30|2,Bob,25" "SELECT name FROM users WHERE age > 25"
```

## Output

The query result as tab-separated rows (header first), printed to stdout.

## Security

- Only `SELECT` statements are accepted; the database lives entirely in memory
- No network, no filesystem, no shell access
