# Password Checker

Estimate password strength and entropy.

## Usage

```bash
python main.py "hunter2"
python main.py "Tr0ub4dor&3"
python main.py "correct horse battery staple"
```

## Output

A report with the password length, character sets used, estimated entropy in bits and a strength rating.

## Security

- Passwords are processed only in memory and never stored or sent anywhere
- No network, no filesystem, no shell access
