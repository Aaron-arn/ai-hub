# CSV Tools

Parse CSV data, convert it to JSON, count rows and filter by column value. CSV can be passed as an argument or piped on stdin.

## Usage

```bash
python main.py to-json "name,age\nAaron,30\nBob,25"
python main.py rows "name,age\nAaron,30\nBob,25"
python main.py filter "name,age\nAaron,30\nBob,25" name Bob
Get-Content data.csv | python main.py to-json
```

## Permissions

- No permissions required
