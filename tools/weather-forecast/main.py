"""Weather forecast using the free Open-Meteo API (no key required)."""

import json
import sys
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.open-meteo.com/v1/forecast"

WMO = {
    0: "clear", 1: "mainly clear", 2: "partly cloudy", 3: "overcast", 45: "fog",
    48: "depositing rime fog", 51: "light drizzle", 53: "moderate drizzle", 55: "dense drizzle",
    61: "light rain", 63: "moderate rain", 65: "heavy rain", 71: "light snow", 73: "moderate snow",
    75: "heavy snow", 80: "light rain showers", 81: "moderate rain showers", 82: "violent rain showers",
    95: "thunderstorm", 96: "thunderstorm with light hail", 99: "thunderstorm with heavy hail",
}


def forecast(lat: float, lon: float, days: int = 3) -> dict:
    params = urllib.parse.urlencode({
        "latitude": lat, "longitude": lon,
        "current": "temperature_2m,weather_code,wind_speed_10m,relative_humidity_2m",
        "daily": "temperature_2m_max,temperature_2m_min,weather_code,precipitation_probability_max",
        "forecast_days": days, "timezone": "auto",
    })
    with urllib.request.urlopen(API + "?" + params, timeout=15) as response:
        data = json.loads(response.read().decode("utf-8"))
    current = data.get("current", {})
    daily = data.get("daily", {})
    days_out = []
    for i, day in enumerate(daily.get("time", [])):
        code = daily.get("weather_code", [None])[i]
        days_out.append({
            "date": day,
            "max": daily.get("temperature_2m_max", [])[i],
            "min": daily.get("temperature_2m_min", [])[i],
            "rain_probability": daily.get("precipitation_probability_max", [])[i],
            "condition": WMO.get(code, f"code {code}"),
        })
    return {
        "location": data.get("timezone", "unknown"),
        "current": {
            "temperature_c": current.get("temperature_2m"),
            "humidity": current.get("relative_humidity_2m"),
            "wind_kmh": current.get("wind_speed_10m"),
            "condition": WMO.get(current.get("weather_code"), "unknown"),
        },
        "forecast": days_out,
    }


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if len(args) < 2 or args[0] in ("-h", "--help", "help"):
        print(json.dumps({"error": "Usage: python main.py <latitude> <longitude> [days]"}, ensure_ascii=False))
        sys.exit(1)
    try:
        lat = float(args[0])
        lon = float(args[1])
        days = int(args[2]) if len(args) > 2 else 3
        print(json.dumps(forecast(lat, lon, days), ensure_ascii=False, indent=2))
    except urllib.error.HTTPError as exc:
        print(json.dumps({"error": f"API error {exc.code}"}))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
