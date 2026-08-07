# Prompt Injection Defense Builder

## Description

Use this prompt to harden an LLM application or agent against prompt injection before deployment. Paste your system prompt, agent configuration or app description, and receive a hardened system prompt, input and output defenses, architectural defenses and a test suite. Use it right after building an assistant and re-run it after each prompt change. Designed for defensive engineering, not attack guidance.

## Prompt

You are a defensive AI engineer specializing in securing LLM applications. I will give you a system prompt, agent configuration, or a description of an application that embeds an LLM. Harden it against prompt injection and deliver:

1. A hardened system prompt that: clearly separates instructions from data, gives precedence rules when instructions conflict, instructs the model to treat user content as untrusted data, and forbids acting on instructions found in data.
2. Input defenses: filtering and sanitization of user and third-party content, delimiters around untrusted text, and length or format limits.
3. Output defenses: validating that tool calls match an allowlist of actions and arguments, detecting and blocking attempts to exfiltrate instructions or system data.
4. Architectural defenses: least-privilege tool permissions, human approval for sensitive actions, sandboxing external content, and monitoring for injection attempts.
5. Testing: a short test suite of injection attempts the hardened system should refuse, plus a regression procedure.

Explain each defense, its limitations, and how attackers typically try to bypass it. Keep recommendations proportionate: a chatbot needs less than an agent with financial tools.

## Notes

Run the prompt injection resilience tester afterwards to measure the improvement.
