"""YAML tools: convert between YAML and JSON documents."""

import json
import sys

import yaml


def usage():
    print("Usage: python main.py yaml2json \"<yaml text>\"")
    print("       python main.py json2yaml \"<json text>\"")


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        usage()
        sys.exit(1)
    command = args[0]
    source = " ".join(args[1:])
    try:
        if command == "yaml2json":
            data = yaml.safe_load(source)
            print(json.dumps(data, indent=2))
        elif command == "json2yaml":
            data = json.loads(source)
            print(yaml.safe_dump(data, default_flow_style=False, sort_keys=False).rstrip())
        else:
            raise ValueError(f"unknown command: {command}")
    except (yaml.YAMLError, json.JSONDecodeError, ValueError) as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
