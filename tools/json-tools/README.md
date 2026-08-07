# JSON Tools

Validate, format and extract values from JSON documents. JSON can be passed as an argument or piped on stdin.

## Usage

```bash
python main.py validate '{"a": 1}'
python main.py format '{"a":1,"b":[1,2,3]}'
python main.py get '{"user":{"name":"Aaron"}}' user.name
echo '{"a": 1}' | python main.py validate
```

Paths use dot notation; list indexes are supported (`items.0.name`).

## Permissions

- No permissions required
