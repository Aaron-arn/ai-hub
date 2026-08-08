"""Crypto prices from the free CoinGecko simple price API."""

import json
import sys
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.coingecko.com/api/v3/simple/price"


def price(coins: list[str], currency: str = "usd") -> dict:
    params = urllib.parse.urlencode({"ids": ",".join(coins), "vs_currencies": currency})
    with urllib.request.urlopen(API + "?" + params, timeout=15) as response:
        data = json.loads(response.read().decode("utf-8"))
    out = {}
    for coin, values in data.items():
        out[coin] = {currency: values.get(currency)}
    return out


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if not args or args[0] in ("-h", "--help", "help"):
        print(json.dumps({"error": "Usage: python main.py <coin_id> [coin_id...] [currency]  e.g. bitcoin,ethereum usd"}))
        sys.exit(1)
    currency = "usd"
    coins = args[:]
    if args[-1].isalpha() and len(args[-1]) == 3 and len(args) > 1:
        currency = args[-1]
        coins = args[:-1]
    try:
        data = price(coins, currency)
        print(json.dumps(data, ensure_ascii=False, indent=2))
    except urllib.error.HTTPError as exc:
        print(json.dumps({"error": f"API error {exc.code}"}))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
