import json
from pathlib import Path

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("todo-server")

STORE = Path.home() / ".aihub" / "todo-server.json"
STORE.parent.mkdir(parents=True, exist_ok=True)


def _load() -> list[dict]:
    if not STORE.exists():
        return []
    return json.loads(STORE.read_text(encoding="utf-8"))


def _save(todos: list[dict]) -> None:
    STORE.write_text(json.dumps(todos, indent=2, ensure_ascii=False), encoding="utf-8")


@mcp.tool()
def add_todo(task: str, priority: str = "medium", tags: list[str] = None) -> str:
    """Add a new todo item."""
    todos = _load()
    new_id = max((t["id"] for t in todos), default=0) + 1
    todos.append({
        "id": new_id, "task": task, "priority": priority,
        "tags": tags or [], "done": False,
    })
    _save(todos)
    return f"added todo #{new_id}"


@mcp.tool()
def list_todos(done: bool | None = None) -> str:
    """List todos, optionally filtered by completion state."""
    todos = _load()
    if done is not None:
        todos = [t for t in todos if t["done"] == done]
    if not todos:
        return "no todos"
    return "\n".join(
        f"[{'x' if t['done'] else ' '}] #{t['id']} {t['task']} ({t['priority']})"
        for t in todos
    )


@mcp.tool()
def complete_todo(todo_id: int) -> str:
    """Mark a todo as done."""
    todos = _load()
    for t in todos:
        if t["id"] == todo_id:
            t["done"] = True
            _save(todos)
            return f"completed #{todo_id}"
    return f"todo #{todo_id} not found"


@mcp.tool()
def delete_todo(todo_id: int) -> str:
    """Delete a todo."""
    todos = [t for t in _load() if t["id"] != todo_id]
    _save(todos)
    return f"deleted #{todo_id}"


if __name__ == "__main__":
    mcp.run()
