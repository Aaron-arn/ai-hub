# Python CLI Scaffolder

## Description

This prompt turns a one-line idea into a complete, runnable Python CLI tool. Use it when starting any new command-line utility and you want a solid starting point: argument parsing, logging, error handling, and tests. Paste your tool description into the placeholder and get back a full project.

## Prompt

You are a senior Python developer. Create a complete CLI tool for the following description: "a command-line utility that reads a text file, counts word frequencies, and prints a ranked table with a configurable top-N limit".

Generate a project with these files:

1. `cli.py` — entry point using `argparse` with subcommand or single-command structure, `--top` option with default 10, `--verbose` flag, and a `--version` flag.
2. `core.py` — the logic separated from the CLI layer: a pure function `count_words(text) -> dict` and `top_words(counts, n) -> list`.
3. Error handling — missing file, empty file, and permission errors produce clear messages and a non-zero exit code.
4. `logging` — use the logging module, with level driven by `--verbose`.
5. Type hints and docstrings on every public function.
6. `tests/test_core.py` — 3 unit tests covering empty input, punctuation handling, and the top-N limit.

Constraints: standard library only, no third-party dependencies. Output each file in a code block with its filename as the header. Keep the total under 250 lines. End with a one-line usage example.

## Notes

Replace the example tool description with your own idea and keep the file structure. For tools with several subcommands, ask for `add_subparsers` structure instead.
