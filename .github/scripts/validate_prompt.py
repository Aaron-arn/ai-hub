"""Validate a prompt pull request against the AIHub contract.

Run by the "Prompt PR auto-merge" workflow on pull_request_target. Reads
the PR's changed files through the GitHub API (never executes PR code),
validates them, and either passes so the workflow merges the PR, or
comments the errors and exits non-zero.

Usage:
    python validate_prompt.py

Requires env: GH_TOKEN, PR_NUMBER, PR_HEAD_SHA.
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REPO = "Aaron-arn/ai-hub"

LANGUAGES = {
    "english", "francais", "français", "espanol", "español", "deutsch",
    "italiano", "portugues", "português", "chinese", "中文", "japanese",
    "日本語", "korean", "한국어", "russian", "русский", "arabic", "العربية",
    "hindi", "हिन्दी", "other",
}

ALLOWED_TAGS = {
    "jailbreaking", "cybersecurity", "code-review", "agent-job", "coding",
    "building", "thinking", "image", "video", "audio", "writing", "marketing",
    "research", "data-analysis", "sql", "database", "web", "frontend",
    "backend", "devops", "docker", "cloud", "testing", "debugging",
    "refactoring", "security", "privacy", "prompt-engineering", "llm", "chat",
    "translation", "language-learning", "education", "math", "science",
    "finance", "legal", "health", "travel", "food", "music", "storytelling",
    "creative", "design", "ux", "product", "business", "sales",
    "customer-support", "automation", "productivity", "planning",
    "brainstorming", "decision", "api", "python", "javascript", "excel",
    "email", "meeting", "seo", "communication",
}

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def gh(*args: str) -> str:
    result = subprocess.run(["gh", *args], capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"gh {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


def fetch_file(pr_number: str, head_sha: str, path: str) -> str:
    return gh(
        "api",
        f"repos/{REPO}/contents/{path}",
        "-H", "Accept: application/vnd.github.raw+json",
        "-f", f"ref={head_sha}",
    )


def validate_manifest(manifest: dict, slug: str) -> list[str]:
    errors = []
    if manifest.get("name") != slug:
        errors.append(f"manifest name must be `{slug}`")
    if manifest.get("type") != "prompt":
        errors.append("manifest type must be `prompt`")
    if not manifest.get("version"):
        errors.append("manifest version is required")
    for field in ("display_name", "description", "author"):
        if not str(manifest.get(field, "")).strip():
            errors.append(f"manifest {field} is required")
    if manifest.get("license") != "MIT":
        errors.append("manifest license must be MIT")
    language = str(manifest.get("language", "")).strip()
    if language.lower() not in LANGUAGES:
        errors.append(f"unsupported language: {language or '(empty)'}")
    tags = manifest.get("tags")
    if not isinstance(tags, list) or not (2 <= len(tags) <= 4):
        errors.append("manifest tags must be a list of 2 to 4 entries")
    else:
        for tag in tags:
            if tag not in ALLOWED_TAGS:
                errors.append(f"unknown tag: {tag}")
    permissions = manifest.get("permissions") or {}
    granted = [key for key, value in permissions.items() if value]
    if granted:
        errors.append(f"prompts must not request permissions (granted: {', '.join(granted)})")
    if manifest.get("dependencies") not in (None, []):
        errors.append("prompts must not declare dependencies")
    published = str(manifest.get("published", ""))
    if not DATE_RE.match(published):
        errors.append(f"manifest published must be an ISO date, got: {published or '(empty)'}")
    return errors


def validate_prompt_md(text: str) -> list[str]:
    errors = []
    lines = text.splitlines()
    if not lines or not lines[0].startswith("# "):
        errors.append("prompt.md must start with `# <title>`")
    if "## Description" not in text:
        errors.append("prompt.md must contain a `## Description` section")
    marker = "## Prompt"
    index = text.find(marker)
    if index == -1:
        errors.append("prompt.md must contain a `## Prompt` section")
        return errors
    prompt_text = text[index + len(marker):].strip()
    for line in prompt_text.splitlines():
        if line.startswith("## "):
            prompt_text = prompt_text.split(line, 1)[0].strip()
            break
    if len(prompt_text) < 40:
        errors.append("prompt text must be at least 40 characters")
    return errors


def validate_registry_entry(registry: dict, manifest: dict) -> list[str]:
    errors = []
    entry = next((p for p in registry.get("packages", []) if p.get("name") == manifest.get("name")), None)
    if entry is None:
        return ["registry.json has no entry for the new prompt"]
    for key, expected in (
        ("name", manifest.get("name")),
        ("type", "prompt"),
        ("version", manifest.get("version")),
        ("path", f"prompts/{manifest.get('name')}"),
        ("display_name", manifest.get("display_name")),
        ("description", manifest.get("description")),
        ("tags", manifest.get("tags")),
        ("author", manifest.get("author")),
        ("published", manifest.get("published")),
        ("language", manifest.get("language")),
    ):
        if entry.get(key) != expected:
            errors.append(f"registry entry `{key}` mismatch (got {entry.get(key)!r}, expected {expected!r})")
    return errors


def main() -> int:
    pr_number = os.environ["PR_NUMBER"]
    head_sha = os.environ.get("PR_HEAD_SHA", "")

    files = gh("pr", "view", pr_number, "--json", "files", "--jq", ".files[].path").splitlines()
    prompt_files = [path for path in files if path.startswith("prompts/")]
    slugs = sorted({path.split("/")[1] for path in prompt_files if len(path.split("/")) >= 3})

    errors = []
    if len(slugs) > 1:
        errors.append(f"Only one prompt per pull request (found: {', '.join(slugs)})")
        slugs = slugs[:1]
    other = [path for path in files if not (path.startswith("prompts/") or path == "registry/registry.json")]
    if other:
        errors.append(f"Only `prompts/**` and `registry/registry.json` may change in an auto-merged PR (also changed: {', '.join(other[:5])})")

    registry_changed = "registry/registry.json" in files
    manifest = None
    if not slugs:
        errors.append("No prompt files found in this pull request.")
    else:
        slug = slugs[0]
        for required in ("manifest.json", "prompt.md", "README.md"):
            if f"prompts/{slug}/{required}" not in files:
                errors.append(f"Missing file: prompts/{slug}/{required}")
        if f"prompts/{slug}/manifest.json" in files:
            try:
                manifest = json.loads(fetch_file(pr_number, head_sha, f"prompts/{slug}/manifest.json"))
                errors.extend(validate_manifest(manifest, slug))
            except (json.JSONDecodeError, RuntimeError) as exc:
                errors.append(f"manifest.json is not valid: {exc}")
        if f"prompts/{slug}/prompt.md" in files:
            try:
                errors.extend(validate_prompt_md(fetch_file(pr_number, head_sha, f"prompts/{slug}/prompt.md")))
            except RuntimeError as exc:
                errors.append(f"Could not read prompt.md: {exc}")
        if manifest is not None:
            base_registry_path = ROOT / "registry" / "registry.json"
            try:
                base_registry = json.loads(base_registry_path.read_text(encoding="utf-8"))
                if any(p.get("name") == slug for p in base_registry.get("packages", [])):
                    errors.append(f"A prompt named `{slug}` already exists in the registry")
            except (OSError, json.JSONDecodeError) as exc:
                errors.append(f"Could not read the base registry: {exc}")
        if not registry_changed:
            errors.append("registry/registry.json must be updated in the pull request")
        elif manifest is not None:
            try:
                registry = json.loads(fetch_file(pr_number, head_sha, "registry/registry.json"))
                errors.extend(validate_registry_entry(registry, manifest))
            except (json.JSONDecodeError, RuntimeError) as exc:
                errors.append(f"registry.json is not valid: {exc}")

    if errors:
        body = "❌ **Validation failed.** Please fix the following:\n\n" + "\n".join(f"- {error}" for error in errors)
        gh("pr", "comment", pr_number, "--body", body)
        print("\n".join(errors), file=sys.stderr)
        return 1
    gh("pr", "comment", pr_number, "--body", "✅ **Validation passed.** This prompt will be merged automatically.")
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
