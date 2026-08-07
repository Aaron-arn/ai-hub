# XML Tools

Parse XML documents and convert them to JSON. Uses the Python standard library `xml.etree.ElementTree`.

## Usage

```bash
python main.py "<note><to>Tove</to><from>Jani</from></note>"
python main.py "<library><book><title>1984</title></book></library>"
python main.py document.xml
```

## Output

The document as indented JSON, printed to stdout.

## Security

- Parsing only, no I/O unless a file path is given
- No network, no shell access
