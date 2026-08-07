# Cron Parser

Parse cron expressions and describe their schedule.

## Usage

```bash
python main.py "*/5 * * * *"
python main.py "30 15 * * 1-5"
python main.py "0 0 1 1 *"
```

## Output

A human-readable description of the schedule, such as `every hour at minute 0, 30`.

## Security

- Pure local parsing using the standard library
- No network, no filesystem, no shell access
