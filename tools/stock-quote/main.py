"""Stock quote fetcher using the public Yahoo Finance chart API."""

import json
import sys
import urllib.error
import urllib.request

API = "https://query1.finance.yahoo.com/v8/finance/chart/"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AIHub/1.0"}


def quote(symbol: str, range_days: str = "5d") -> dict:
    url = API + urllib.request.quote(symbol) + "?interval=1d&range=" + range_days
    request = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(request, timeout=15) as response:
        data = json.loads(response.read().decode("utf-8"))
    result = data.get("chart", {}).get("result")
    if not result:
        raise ValueError("No data for symbol: " + symbol)
    meta = result[0].get("meta", {})
    timestamps = result[0].get("timestamp", [])
    quote_data = result[0].get("indicators", {}).get("quote", [{}])[0]
    closes = quote_data.get("close", [])
    history = []
    for i, ts in enumerate(timestamps):
        if i < len(closes) and closes[i] is not None:
            history.append({"date": ts, "close": closes[i]})
    return {
        "symbol": meta.get("symbol", symbol),
        "currency": meta.get("currency", ""),
        "price": meta.get("regularMarketPrice"),
        "previous_close": meta.get("chartPreviousClose"),
        "market_state": meta.get("marketState", ""),
        "history": history,
    }


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if not args or args[0] in ("-h", "--help", "help"):
        print(json.dumps({"error": "Usage: python main.py <symbol> [range]  e.g. AAPL / MSFT  (range: 1d, 5d, 1mo)"}, ensure_ascii=False))
        sys.exit(1)
    try:
        symbol = args[0].upper()
        range_days = args[1] if len(args) > 1 else "5d"
        print(json.dumps(quote(symbol, range_days), ensure_ascii=False, indent=2))
    except urllib.error.HTTPError as exc:
        print(json.dumps({"error": f"API error {exc.code}"}))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
