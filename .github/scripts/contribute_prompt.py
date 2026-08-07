"""Turn a GitHub issue into an AIHub prompt package + PR.

Triggered by the "Prompt contributions" workflow. The issue body must
follow the structured format produced by the AIHub website form:

    ## AIHub Prompt Contribution

    ### Title
    <title>

    ### Description
    <one sentence>

    ### Author
    <name>

    ### Language
    English

    ### Tags
    tag1, tag2, tag3

    ### Prompt
    <the prompt text, everything until the end of the issue body>

The script validates the fields, creates prompts/<slug>/ (manifest.json,
prompt.md, README.md), regenerates registry/registry.json from all
manifests, then opens a pull request.
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

MARKER = "## AIHub Prompt Contribution"

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


def gh(*args: str, input_text: str | None = None) -> str:
    cmd = ["gh"]
    cmd.extend(args)
    result = subprocess.run(cmd, input=input_text, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"gh {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


def run(*args: str) -> None:
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"{' '.join(args)} failed: {result.stderr.strip()}")


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:64] or "prompt"


def parse_body(body: str) -> dict:
    data: dict[str, str] = {}
    body = body.replace("\r\n", "\n")
    if MARKER not in body:
        raise ValueError("Missing contribution marker")
    _, rest = body.split(MARKER, 1)
    for section in re.split(r"\n### ", rest):
        if not section.strip():
            continue
        header, _, value = section.partition("\n")
        data[header.strip().lower()] = value.strip()
    return data


def validate(data: dict) -> dict:
    errors = []
    for field in ("title", "description", "author", "language", "tags", "prompt"):
        if not data.get(field):
            errors.append(f"- `{field.capitalize()}` is required")
    if errors:
        raise ValueError("Missing fields:\n" + "\n".join(errors))
    language = data["language"].strip()
    if language.lower() not in LANGUAGES:
        raise ValueError(f"Unsupported language: {language}")
    tags = [t.strip().lower() for t in data["tags"].split(",") if t.strip()]
    invalid = [t for t in tags if t not in ALLOWED_TAGS]
    if invalid:
        raise ValueError(f"Unknown tag(s): {', '.join(invalid)}")
    if not (2 <= len(tags) <= 4):
        raise ValueError("Provide 2 to 4 tags")
    data["tags"] = tags
    return data


def manifest_for(data: dict, slug: str) -> dict:
    return {
        "name": slug,
        "display_name": data["title"],
        "version": "1.0.0",
        "type": "prompt",
        "description": data["description"],
        "author": data["author"],
        "license": "MIT",
        "language": data["language"],
        "published": date.today().isoformat(),
        "tags": data["tags"],
        "permissions": {
            "network": False,
            "filesystem": False,
            "shell": False,
            "environment": False,
        },
        "dependencies": [],
    }


def build_prompt_md(data: dict) -> str:
    return (
        f"# {data['title']}\n\n"
        f"## Description\n\n{data['description']}\n\n"
        f"## Prompt\n\n{data['prompt']}\n"
    )


def build_readme(data: dict) -> str:
    return (
        f"# {data['title']}\n\n{data['description']}\n\n"
        "## Usage\n\nOpen `prompt.md`, copy the text after `## Prompt`, "
        "and paste it into your favorite AI assistant (ChatGPT, Claude, Gemini...).\n"
    )


def regenerate_registry() -> None:
    packages = []
    for kind, type_name in (("tools", "tool"), ("skills", "skill"), ("prompts", "prompt")):
        for folder in sorted((ROOT / kind).iterdir()):
            if not folder.is_dir():
                continue
            manifest = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
            packages.append({
                "name": manifest.get("name"),
                "type": manifest.get("type"),
                "version": manifest.get("version"),
                "path": f"{kind}/{manifest.get('name')}",
                "display_name": manifest.get("display_name"),
                "description": manifest.get("description"),
                "tags": manifest.get("tags", []),
                "author": manifest.get("author", ""),
                "published": manifest.get("published", ""),
                "language": manifest.get("language", ""),
            })
    packages.sort(key=lambda p: (p["type"], p["name"]))
    registry = {"version": 1, "generated": date.today().isoformat(), "packages": packages}
    (ROOT / "registry" / "registry.json").write_text(
        json.dumps(registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--issue-number", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--body", required=True)
    parser.add_argument("--author", required=True)
    args = parser.parse_args()

    def comment(message: str) -> None:
        try:
            gh("issue", "comment", args.issue_number, input_text=message)
        except RuntimeError:
            pass

    try:
        data = parse_body(args.body)
        if not data.get("title"):
            data["title"] = args.title
        validate(data)
    except ValueError as exc:
        comment(f"⚠️ {exc}\n\nYour prompt was not added. Please fix it and open a new issue.")
        return 1

    slug = slugify(data["title"])
    folder = ROOT / "prompts" / slug
    if folder.exists():
        comment(f"⚠️ A prompt named `{slug}` already exists. Choose a different title.")
        return 1

    try:
        folder.mkdir(parents=True)
        manifest = manifest_for(data, slug)
        (folder / "manifest.json").write_text(
            json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        (folder / "prompt.md").write_text(build_prompt_md(data), encoding="utf-8")
        (folder / "README.md").write_text(build_readme(data), encoding="utf-8")
        regenerate_registry()

        run("git", "config", "user.name", "github-actions[bot]")
        run("git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
        run("git", "checkout", "-b", f"prompt/{slug}")
        run("git", "add", f"prompts/{slug}", "registry/registry.json")
        run("git", "commit", "-m", f"Add prompt: {data['title']} (#{args.issue_number})")
        run("git", "push", "--set-upstream", "origin", f"prompt/{slug}")
        url = gh(
            "pr", "create",
            "--title", f"Add prompt: {data['title']}",
            "--body", f"Automatically created from issue #{args.issue_number}.\n\nCloses #{args.issue_number}.",
            "--label", "prompt",
        )
        gh("issue", "edit", args.issue_number, "--add-label", "prompt")
        comment(f"✅ Prompt `{slug}` created. Review it in {url}")
        return 0
    except Exception as exc:
        comment(f"⚠️ Failed to create the prompt: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
