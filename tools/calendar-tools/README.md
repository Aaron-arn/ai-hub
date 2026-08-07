# Calendar Tools

Show month calendars, week numbers and day-of-week calculations.

## Usage

```bash
python main.py month 2025 4
python main.py year 2025
python main.py week 2025-04-15
```

## Output

A text calendar, or the ISO week number and weekday name for a given date.

## Security

- Pure local calculations using the standard `calendar` module
- No network, no filesystem, no shell access
