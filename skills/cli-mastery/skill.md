# CLI Mastery

You use the command line as a composable toolbox: small tools, combined safely, reading their output before acting.

## Discover before you guess

- Check `--help` or `man <tool>` before inventing flags; most tools document themselves.
- Use `type <cmd>` or `which <cmd>` to verify what a command resolves to before relying on it.
- Prefer the tool's built-in dry-run (`-n`, `--dry-run`) and verbose flags for destructive operations.
- For unknown output, pipe through `head` or inspect a sample before parsing the whole stream.

## Pipes and composition

- Compose single-purpose tools: `grep`, `sort`, `uniq`, `wc`, `head`, `cut`, `awk`, `xargs`.
- Use `sort | uniq -c | sort -rn` for top-N counts; remember `uniq` needs sorted input.
- Use `grep -r` with `--include` and `--exclude` patterns to narrow searches to relevant files.
- Prefer `xargs -I{}` or `find -exec` over shell loops for iterating over files.
- Quote arguments that may contain spaces or glob characters; know when you want the shell to expand.
- Write the pipeline so failures are visible: end it with a tool that fails loudly on no input.

## Inspection and navigation

- Use `git grep` inside repositories; it respects the index and is faster than `grep -r` on `.git`.
- Use `rg` (ripgrep) when available; it respects `.gitignore` and skips binaries by default.
- Inspect file types with `file`, sizes with `du -sh` and `ls -lh` before processing.
- Use `watch` for repeating commands and `tail -f` (or `-F`) for following logs.
- Learn one pager (less) well: `/` to search, `g`/`G` for jump, `q` to quit.

## Output and errors

- Separate stdout from stderr (`2>/dev/null` vs `2>&1`); they carry different information.
- Check exit codes (`echo $?`) in scripts instead of guessing success.
- Use `set -euo pipefail` at the top of every non-trivial bash script.
- Redirect with `>` carefully: it truncates; `>>` appends. `2>` redirects errors.
- Avoid destructive pipelines that write in place (`foo file | bar > file` corrupts the file).
- When output is huge, summarize it instead of dumping it: `grep -c`, `cut -f2 | sort -u`.

## Scripting habits

- Wrap repeated command sequences in functions or scripts with clear names.
- Quote every variable (`"$var"`) and use `--` to separate options from operands where tools allow.
- Use `mktemp` for scratch files instead of fixed paths like `/tmp/x`.
- Never embed secrets in scripts; read them from environment or secret stores.
- Make scripts idempotent when they touch the filesystem, and print what they are about to change.
- Prefer `find ... -name '*.log' -exec rm` over hand-written path globs; they break on spaces.
