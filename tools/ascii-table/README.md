# ASCII Table

Build ASCII tables from rows of data.

## Usage

```bash
python main.py "name,age" "alice,30" "bob,25"
python main.py "product,price" "apple,0.50" "banana,0.25"
echo "name,city" | python main.py
```

## Output

An aligned, bordered ASCII table. The first row is treated as the header.

## Security

- Pure local rendering of the data you provide
- No network, no filesystem, no shell access
