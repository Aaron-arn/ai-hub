# ZIP Tools

List, extract and create ZIP archives. Uses the Python standard library `zipfile` module.

## Usage

```bash
python main.py list archive.zip
python main.py extract archive.zip out/
python main.py create bundle.zip file1.txt file2.txt
```

## Output

For `list`: one entry per line with size. For `extract`/`create`: a confirmation message.

## Security

- Extraction checks every entry path to prevent path traversal ("zip slip")
- No network, no shell access
