import argparse
import re
import shutil
from collections import Counter
from pathlib import Path

EXT_MAP = {
    "images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp"},
    "documents": {".pdf", ".docx", ".doc", ".txt", ".md", ".odt", ".rtf"},
    "spreadsheets": {".xlsx", ".xls", ".csv", ".ods"},
    "presentations": {".pptx", ".ppt", ".odp"},
    "archives": {".zip", ".tar", ".gz", ".rar", ".7z"},
    "audio": {".mp3", ".wav", ".flac", ".m4a", ".ogg"},
    "video": {".mp4", ".mkv", ".mov", ".avi", ".webm"},
    "code": {".py", ".js", ".ts", ".tsx", ".html", ".css", ".json", ".yml", ".yaml", ".go", ".rs", ".java", ".c", ".h", ".cpp"},
    "scripts": {".sh", ".bat", ".ps1", ".cmd"},
}

def category_for(path):
    ext = path.suffix.lower()
    for cat, exts in EXT_MAP.items():
        if ext in exts:
            return cat
    return ext[1:].upper() or "misc"

def main():
    ap = argparse.ArgumentParser(description="Organize files into category folders")
    ap.add_argument("target", nargs="?", default=".", help="directory to organize")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    root = Path(args.target)
    counts = Counter()
    for path in sorted(root.iterdir()):
        if not path.is_file():
            continue
        cat = category_for(path)
        dest = root / cat
        if args.dry_run:
            print(f"[dry] {path.name} -> {cat}/")
        else:
            dest.mkdir(exist_ok=True)
            shutil.move(str(path), dest / path.name)
            print(f"{path.name} -> {cat}/")
        counts[cat] += 1

    total = sum(counts.values())
    print(f"--- {total} files, {len(counts)} categories ---")
    for cat, n in counts.most_common():
        print(f"  {cat}: {n}")

if __name__ == "__main__":
    main()
