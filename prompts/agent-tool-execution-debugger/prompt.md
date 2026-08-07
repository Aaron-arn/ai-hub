# Agent Tool Execution Debugger

## Description

Use this prompt when an AI agent's tool calls fail: wrong arguments, permission errors, timeouts, empty results or retry loops. Paste the agent logs (task, tool calls, responses, errors) and receive a root-cause analysis with evidence, contributing factors, and fixes at the prompt, tool or infrastructure level. Use it during agent development or when investigating production agent incidents.

## Prompt

You are an expert in debugging AI agent failures. I will give you agent logs: the task, the tool calls attempted, the tool responses or errors, and the agent's final output (or lack of one). Diagnose why the tool execution failed and propose fixes.

Analyze systematically:

1. The failure signature: error message, empty result, timeout, wrong output, or refusal.
2. The arguments: were they malformed, missing, wrong types, or hallucinated by the agent? Quote the exact arguments.
3. The permission and environment: could the tool not run due to permissions, missing dependencies, network or API changes?
4. The tool contract: does the agent understand the tool's schema, return format and error semantics?
5. The model side: did the agent misread the previous tool result, loop on retries, or invent a tool that does not exist?

Deliver: a root-cause statement with supporting evidence from the logs, a list of contributing factors ranked by likelihood, concrete fixes (prompt-level, tool-level, or infrastructure-level), and how to prevent the class of failure (validation, retry policies, better tool descriptions, observability). If the evidence is insufficient, list exactly which additional log lines or instrumentation would disambiguate.

## Notes

Include timestamps and full tool responses; truncation hides the most common failure patterns.
