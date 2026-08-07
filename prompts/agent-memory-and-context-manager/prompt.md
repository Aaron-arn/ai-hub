# Agent Memory and Context Manager

## Description

Use this prompt when an AI agent forgets important context, runs out of window, or remembers stale information. Describe the agent's domain, tools and interaction length, and receive a memory architecture: what to remember, where to store it, how to compress, retrieve and invalidate, all within a context budget. Use it when designing a new agent or fixing context-handling problems in an existing one.

## Prompt

You are an engineer specializing in AI agent architectures. I will give you a description of an agent: its task domain, the tools it uses, the length of its interactions and any context-window constraints. Design a memory strategy:

1. What to remember: distinguish ephemeral state (current task progress) from durable knowledge (user preferences, facts, learned procedures) and from tool-derived data (results worth caching).
2. Where to store it: short-term conversation context, structured long-term memory (a database or vector store), or files. Justify each choice.
3. Compression: when and how to summarize: threshold-based triggers, what older content to compress, and what must never be lost (constraints, pending confirmations).
4. Retrieval: how to decide which memories to load into context, with recency, relevance and trustworthiness signals.
5. Staleness: how to invalidate or refresh outdated memories, and how to detect contradictory information.
6. Budget: how to stay within context limits while keeping the important facts available.

Deliver: a memory architecture diagram (text-based), a table mapping memory types to storage and lifecycle, and a set of rules an agent should follow when deciding to write, update or forget a memory. Flag privacy considerations for sensitive data.

## Notes

Pair with the agent tool-use planner to align memory design with tool-call patterns.
