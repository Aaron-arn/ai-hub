"""XML tools: parse XML documents and convert them to JSON."""

import json
import os
import sys
import xml.etree.ElementTree as ET


def element_to_dict(element):
    children = list(element)
    if children:
        result = {}
        for child in children:
            data = element_to_dict(child)
            if child.tag in result:
                if isinstance(result[child.tag], list):
                    result[child.tag].append(data)
                else:
                    result[child.tag] = [result[child.tag], data]
            else:
                result[child.tag] = data
    else:
        result = element.text.strip() if element.text and element.text.strip() else None
    if element.attrib:
        result = {"#attributes": dict(element.attrib), "#content": result}
    return result


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"<xml document>\"")
        print("  If the argument names an existing file, it is read from disk.")
        sys.exit(1)
    source = sys.argv[1]
    data = source
    try:
        if os.path.exists(source):
            with open(source, "r", encoding="utf-8") as fh:
                data = fh.read()
        root = ET.fromstring(data)
        print(json.dumps({root.tag: element_to_dict(root)}, indent=2))
    except ET.ParseError as exc:
        print(f"Error: invalid XML: {exc}")
        sys.exit(1)
    except OSError as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
