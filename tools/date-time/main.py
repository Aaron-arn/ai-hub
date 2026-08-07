"""Date-time tool: current time, formatting and timezone conversions."""

import json
import sys
from datetime import datetime
from zoneinfo import ZoneInfo


def iso_with_tz(value: datetime) -> str:
    return value.isoformat(timespec="seconds")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print(json.dumps({"error": "Usage: python main.py <now|unix|convert> [timezone] [timestamp]"}))
        sys.exit(1)
    command = args[0]
    tz_name = args[1] if len(args) > 1 else "UTC"
    try:
        tz = ZoneInfo(tz_name)
    except Exception:
        print(json.dumps({"error": f"Unknown timezone: {tz_name}"}, ensure_ascii=False))
        sys.exit(1)
    try:
        if command == "now":
            now = datetime.now(tz)
            result = {
                "timezone": tz_name,
                "iso": iso_with_tz(now),
                "unix": int(now.timestamp()),
                "date": now.strftime("%Y-%m-%d"),
                "time": now.strftime("%H:%M:%S"),
            }
        elif command == "unix":
            result = {"unix": int(datetime.now(tz).timestamp())}
        elif command == "convert":
            value = int(args[2]) if len(args) > 2 else None
            if value is None:
                raise ValueError("convert requires a unix timestamp")
            result = {
                "unix": value,
                "timezone": tz_name,
                "iso": iso_with_tz(datetime.fromtimestamp(value, tz)),
            }
        else:
            raise ValueError(f"Unknown command: {command}")
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))
        sys.exit(1)


if __name__ == "__main__":
    main()
