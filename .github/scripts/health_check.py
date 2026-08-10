"""Registry health check.

Verifies that every package referenced in registry/registry.json still
exists in the repository, that its manifest is valid and coherent with the
registry entry, and that required content files are present.

Run by the "Registry health" workflow on every push to main, nightly, and
manually. Exits non-zero when the registry is broken so the badge shows
"failing".

Usage:
    python health_check.py [--repo PATH]

    --repo   local clone root (defaults to the repository root)
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")

LANGUAGES = {
    "english", "francais", "français", "espanol", "español", "deutsch",
    "italiano", "portugues", "português", "chinese", "中文", "japanese",
    "日本語", "korean", "한국어", "russian", "русский", "arabic", "العربية",
    "hindi", "हिन्दी", "other",
}

CONTENT_FILES = {
    "prompt": ("prompt.md", "README.md"),
    "skill": ("skill.md",),
    "tool": ("entrypoint",),
    "mcp": ("entrypoint",),
    "agent": ("agent.md",),
}

ALLOWED_TYPES = {"prompt", "skill", "tool", "mcp", "agent"}


def read_json(path: Path) -> dict | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    return data if isinstance(data, dict) else None


def check_registry(repo: Path, errors: list[str], warnings: list[str]) -> None:
    registry_path = repo / "registry" / "registry.json"
    if not registry_path.is_file():
        errors.append("registry/registry.json is missing")
        return
    registry = read_json(registry_path)
    if registry is None:
        errors.append("registry/registry.json is not valid JSON (or not an object)")
        return
    if not isinstance(registry.get("version"), int):
        errors.append("registry version must be an integer")
    generated = str(registry.get("generated", ""))
    if not DATE_RE.match(generated):
        errors.append(f"registry generated must be an ISO date, got: {generated or '(empty)'}")
    if datetime.strptime(generated, "%Y-%m-%d").date() > datetime.now().date():
        warnings.append(f"registry generated date is in the future: {generated}")

    packages = registry.get("packages")
    if not isinstance(packages, list):
        errors.append("registry packages must be a list")
        return

    seen_names: dict[tuple[str, str], str] = {}
    seen_paths: set[str] = set()
    for entry in packages:
        if not isinstance(entry, dict):
            errors.append("registry contains a non-object package entry")
            continue
        name = str(entry.get("name", ""))
        type_ = str(entry.get("type", ""))
        path = str(entry.get("path", ""))
        if not name or not type_ or not path:
            errors.append(f"registry entry missing name/type/path: {entry!r}")
            continue
        if type_ not in ALLOWED_TYPES:
            errors.append(f"registry entry `{name}` has unknown type `{type_}`")
        key = (name, type_)
        if key in seen_names:
            errors.append(f"duplicate registry entry: {name} ({type_})")
        seen_names[key] = path
        if path in seen_paths:
            errors.append(f"two registry entries share the same path: {path}")
        seen_paths.add(path)
        check_package(repo, entry, name, type_, path, errors)


def check_package(
    repo: Path, entry: dict, name: str, type_: str, path: str, errors: list[str]
) -> None:
    package_dir = repo / path
    if not package_dir.is_dir():
        errors.append(f"{name} ({type_}): path does not exist: {path}")
        return
    manifest_path = package_dir / "manifest.json"
    if not manifest_path.is_file():
        errors.append(f"{name} ({type_}): manifest.json is missing")
        return
    manifest = read_json(manifest_path)
    if manifest is None:
        errors.append(f"{name} ({type_}): manifest.json is not valid JSON (or not an object)")
        return

    for key, expected in (
        ("name", name),
        ("type", type_),
        ("version", entry.get("version")),
    ):
        if manifest.get(key) != expected:
            errors.append(
                f"{name} ({type_}): manifest `{key}` is {manifest.get(key)!r}, expected {expected!r}"
            )

    version = str(manifest.get("version", ""))
    if not VERSION_RE.match(version):
        errors.append(f"{name} ({type_}): version must be semver, got: {version or '(empty)'}")
    for field in ("display_name", "description", "author"):
        if not str(manifest.get(field, "")).strip():
            errors.append(f"{name} ({type_}): manifest {field} is required")
    if manifest.get("license") != "MIT":
        errors.append(f"{name} ({type_}): manifest license must be MIT")
    tags = manifest.get("tags")
    if not isinstance(tags, list) or not tags:
        errors.append(f"{name} ({type_}): manifest tags must be a non-empty list")
    deps = manifest.get("dependencies")
    if deps is not None and not isinstance(deps, list):
        errors.append(f"{name} ({type_}): manifest dependencies must be a list")
    if type_ == "prompt":
        if deps not in (None, []):
            errors.append(f"{name}: prompts must not declare dependencies")
        permissions = manifest.get("permissions") or {}
        granted = [key for key, value in permissions.items() if value]
        if granted:
            errors.append(f"{name}: prompts must not request permissions (granted: {', '.join(granted)})")
        language = str(manifest.get("language", "")).strip()
        if language.lower() not in LANGUAGES:
            errors.append(f"{name}: unsupported language: {language or '(empty)'}")
        published = str(manifest.get("published", ""))
        if not DATE_RE.match(published):
            errors.append(f"{name}: manifest published must be an ISO date, got: {published or '(empty)'}")

    content = CONTENT_FILES.get(type_)
    if content:
        for file_field in content:
            if file_field == "entrypoint":
                entrypoint = manifest.get("entrypoint")
                if not entrypoint or not (package_dir / entrypoint).is_file():
                    errors.append(f"{name} ({type_}): entrypoint file is missing: {entrypoint or '(empty)'}")
            elif not (package_dir / file_field).is_file():
                errors.append(f"{name} ({type_}): required file is missing: {file_field}")

    if type_ == "mcp":
        mcp = manifest.get("mcp")
        if not isinstance(mcp, dict) or not mcp:
            errors.append(f"{name} (mcp): manifest must declare an `mcp` object")
        else:
            transport = mcp.get("transport")
            if transport not in ("stdio", "sse", "http"):
                errors.append(f"{name} (mcp): mcp.transport must be stdio, sse or http, got: {transport or '(empty)'}")
            tools = mcp.get("tools")
            if not isinstance(tools, list) or not tools:
                errors.append(f"{name} (mcp): mcp.tools must be a non-empty list")
    if type_ == "agent":
        tools = manifest.get("tools")
        if tools is not None and not isinstance(tools, list):
            errors.append(f"{name} (agent): manifest tools must be a list")
        elif tools:
            for tool in tools:
                if not isinstance(tool, str) or not tool.startswith("aihub:"):
                    errors.append(f"{name} (agent): tool references must use the aihub:<name> form, got: {tool!r}")


def check_history(repo: Path, errors: list[str]) -> None:
    history_path = repo / "registry" / "history.json"
    if not history_path.is_file():
        return
    history = read_json(history_path)
    if history is None:
        errors.append("registry/history.json is not valid JSON (or not an object)")
        return
    for entry in history.get("entries", []):
        if not isinstance(entry, dict) or not entry.get("version"):
            errors.append("registry/history.json contains an invalid entry")
            break


def main() -> int:
    parser = argparse.ArgumentParser(description="AIHub registry health check")
    parser.add_argument("--repo", default=str(ROOT), help="repository root")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()

    errors: list[str] = []
    warnings: list[str] = []
    check_registry(repo, errors, warnings)
    check_history(repo, errors)

    registry = read_json(repo / "registry" / "registry.json")
    total = len(registry.get("packages", [])) if registry else 0
    summary = f"Registry health: {total - len(errors)}/{total} packages OK"
    if warnings:
        summary += f" ({len(warnings)} warning{'s' if len(warnings) > 1 else ''})"
    print(summary)
    for warning in warnings:
        print(f"  WARN {warning}")
    for error in errors:
        print(f"  ERROR {error}", file=sys.stderr)

    summary_path = Path(__file__).parent / "health-summary.txt"
    summary_path.write_text(summary + "\n", encoding="utf-8")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
