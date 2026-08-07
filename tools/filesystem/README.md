# Filesystem

List, read and write files inside a sandboxed directory. Agents can persist state here without touching the rest of the machine.

## Usage

```bash
python main.py list [path]
python main.py read <path>
python main.py write <path> <content>
```

## Sandbox

By default the sandbox is `~/.aihub/sandbox/`. Set `AIHUB_FS_ROOT` to use another directory.

Path traversal outside the sandbox is rejected.

## Permissions

- `filesystem` — restricted to the sandbox directory only
