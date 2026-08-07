# Duration Format

Humanize durations between two dates or from seconds.

## Usage

```bash
python main.py 90061
python main.py --from 2024-01-01 --to 2024-03-15
python main.py 2023-06-01 2024-01-01
```

## Output

A human-readable duration such as `1 day, 1 hour, 1 minute, 1 second`.

## Security

- Pure local calculation using the standard `datetime` and `calendar` modules
- No network, no filesystem, no shell access
