"""Currency converter using the free Frankfurter API (no key required)."""

import json
import sys
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.frankfurter.app/latest"


def convert(amount: float, source: str, target: str) -> dict:
    query = urllib.parse.urlencode({"amount": amount, "from": source, "to": target})
    request = urllib.request.Request(
        API + "?" + query,
        headers={"User-Agent": "Mozilla/5.0 (compatible; AIHub currency-converter/1.0)"},
    )
    with urllib.request.urlopen(request, timeout=15) as response:
        return json.loads(response.read().decode("utf-8"))


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if len(args) < 3 or args[0] in ("-h", "--help", "help"):
        print(json.dumps({"error": "Usage: python main.py <amount> <from_currency> <to_currency>"}))
        sys.exit(1)
    try:
        amount = float(args[0])
        result = convert(amount, args[1].upper(), args[2].upper())
        rates = result.get("rates", {})
        rate = list(rates.values())[0]
        print(json.dumps({
            "amount": amount,
            "from": args[1].upper(),
            "to": args[2].upper(),
            "rate": rate,
            "converted": round(amount * rate, 4),
            "date": result.get("date", ""),
        }, ensure_ascii=False, indent=2))
    except urllib.error.HTTPError as exc:
        print(json.dumps({"error": f"API error {exc.code}: {exc.reason}"}))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
