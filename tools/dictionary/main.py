"""Dictionary lookups from the free dictionaryapi.dev."""

import json
import sys
import urllib.error
import urllib.request

API = "https://api.dictionaryapi.dev/api/v2/entries/en/"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; AIHub dictionary/1.0)"}


def lookup(word: str) -> dict:
    request = urllib.request.Request(API + urllib.request.quote(word), headers=HEADERS)
    with urllib.request.urlopen(request, timeout=15) as response:
        data = json.loads(response.read().decode("utf-8"))
    entry = data[0]
    meanings = []
    for meaning in entry.get("meanings", []):
        definitions = [d.get("definition", "") for d in meaning.get("definitions", [])[:3]]
        meanings.append({"partOfSpeech": meaning.get("partOfSpeech"), "definitions": definitions})
    return {
        "word": entry.get("word"),
        "phonetic": entry.get("phonetic") or "",
        "meanings": meanings,
    }


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if not args or args[0] in ("-h", "--help", "help"):
        print(json.dumps({"error": "Usage: python main.py <word>"}))
        sys.exit(1)
    try:
        print(json.dumps(lookup(args[0]), ensure_ascii=False, indent=2))
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            print(json.dumps({"word": args[0], "error": "Word not found"}))
        else:
            print(json.dumps({"error": f"API error {exc.code}"}))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
