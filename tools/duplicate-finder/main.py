import argparse
import hashlib
from pathlib import Path

def hash_file(path, chunk=1 << 20):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        while True:
            block = fh.read(chunk)
            if not block:
                break
            h.update(block)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser(description="Find duplicate files")
    ap.add_argument("target", default=".", help="directory to scan")
    ap.add_argument("--min-size", type=int, default=1, help="ignore files smaller than N bytes")
    ap.add_argument("--delete", action="store_true", help="delete duplicates (keeps first)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    by_size = {}
    for path in Path(args.target).rglob("*"):
        if path.is_file():
            size = path.stat().st_size
            if size >= args.min_size:
                by_size.setdefault(size, []).append(path)

    by_hash = {}
    for size, paths in by_size.items():
        if len(paths) < 2:
            continue
        for path in paths:
            by_hash.setdefault(hash_file(path), []).append(path)

    groups = [g for g in by_hash.values() if len(g) > 1]
    total_wasted = 0
    for group in groups:
        keep, *dupes = sorted(group)
        saved = sum(p.stat().st_size for p in dupes)
        total_wasted += saved
        print(f"group of {len(group)}: {keep.name} (kept)")
        for dup in dupes:
            if args.delete and not args.dry_run:
                dup.unlink()
                print(f"  DELETED {dup}")
            else:
                print(f"  duplicate: {dup} ({saved} bytes)")

    print(f"--- {len(groups)} duplicate groups, {total_wasted} bytes recoverable ---")

if __name__ == "__main__":
    main()
