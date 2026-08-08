"""Generate bar/line chart SVGs from JSON data (stdlib only)."""

import json
import sys


def bar_chart(values: list[float], labels: list[str], title: str = "", width: int = 600, height: int = 320) -> str:
    padding = 40
    chart_w = width - padding * 2
    chart_h = height - padding * 2
    if not values:
        raise ValueError("No values provided")
    vmax = max(max(values), 0) or 1
    vmin = min(min(values), 0)
    span = (vmax - vmin) or 1
    step = chart_w / len(values)
    bars = []
    for i, value in enumerate(values):
        h = abs(value) * chart_h / span
        y = padding + chart_h - (value - vmin) * chart_h / span
        color = "#2f81f7" if value >= 0 else "#f85149"
        bars.append(f'<rect x="{padding + i * step + 6:.1f}" y="{y:.1f}" width="{step - 12:.1f}" height="{max(h - 2, 1):.1f}" fill="{color}"/>')
        if labels and i < len(labels):
            bars.append(f'<text x="{padding + i * step + step / 2:.1f}" y="{height - 8}" text-anchor="middle" font-size="11">{labels[i]}</text>')
        bars.append(f'<text x="{padding + i * step + step / 2:.1f}" y="{y - 5:.1f}" text-anchor="middle" font-size="10">{value}</text>')
    head = f'<text x="{width / 2}" y="16" text-anchor="middle" font-size="14" font-weight="bold">{title}</text>' if title else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">' + head
            + f'<line x1="{padding}" y1="{padding}" x2="{padding}" y2="{height - padding}" stroke="#888"/>'
            + f'<line x1="{padding}" y1="{height - padding}" x2="{width - padding}" y2="{height - padding}" stroke="#888"/>'
            + "".join(bars) + "</svg>")


def line_chart(values: list[float], labels: list[str], title: str = "", width: int = 600, height: int = 320) -> str:
    padding = 40
    chart_w = width - padding * 2
    chart_h = height - padding * 2
    if len(values) < 2:
        raise ValueError("Need at least 2 values")
    vmax = max(max(values), 0) or 1
    vmin = min(min(values), 0)
    span = (vmax - vmin) or 1
    step = chart_w / (len(values) - 1)
    points = [(padding + i * step, padding + chart_h - (v - vmin) * chart_h / span) for i, v in enumerate(values)]
    poly = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    circles = "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="#2f81f7"/>' for x, y in points)
    texts = ""
    for i, (x, y) in enumerate(points):
        if labels and i < len(labels):
            texts += f'<text x="{x:.1f}" y="{height - 8}" text-anchor="middle" font-size="11">{labels[i]}</text>'
        texts += f'<text x="{x:.1f}" y="{y - 8:.1f}" text-anchor="middle" font-size="10">{values[i]}</text>'
    head = f'<text x="{width / 2}" y="16" text-anchor="middle" font-size="14" font-weight="bold">{title}</text>' if title else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">' + head
            + f'<polyline points="{poly}" fill="none" stroke="#2f81f7" stroke-width="2"/>'
            + circles + texts + "</svg>")


def main() -> None:
    args = sys.argv[1:]
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if len(args) < 2 or args[0] in ("-h", "--help", "help"):
        print(json.dumps({"error": "Usage: python main.py <bar|line> <json_data>  where json_data = {\"values\": [..], \"labels\": [..], \"title\": \"..\"}"}, ensure_ascii=False))
        sys.exit(1)
    try:
        data = json.loads(args[1])
        if args[0] == "bar":
            svg = bar_chart(data.get("values", []), data.get("labels", []), data.get("title", ""))
        else:
            svg = line_chart(data.get("values", []), data.get("labels", []), data.get("title", ""))
        print(json.dumps({"kind": args[0], "svg": svg}, ensure_ascii=False))
    except Exception as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
