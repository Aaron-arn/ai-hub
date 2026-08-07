# TAR Tools

List, extract and create TAR archives. Uses the Python standard library `tarfile` module. gzip, bzip2 and xz compression is detected from the file extension.

## Usage

```bash
python main.py list archive.tar.gz
python main.py extract archive.tar out/
python main.py create bundle.tar file1.txt file2.txt
```

## Output

For `list`: one entry per line with type and size. For `extract`/`create`: a confirmation message.

## Security

- Extraction checks every entry path to prevent path traversal
- No network, no shell access
