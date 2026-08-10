# Code Review Agent

Reviews pull requests and code changes with a structured verdict,
prioritized findings and a test-coverage check.

## Install

```bash
aihub install code-review-agent
```

The agent loads `agent.md` into the assistant's context. The optional
`aihub:web-search` tool dependency is installed automatically when you
install with dependencies enabled.
