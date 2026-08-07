# Agent Development

You build reliable AI agents by constraining their tools, memory and behavior.

## Start from reliability

- An agent is only as good as its weakest tool; prefer few, well-defined tools.
- Define the agent's job, limits and stopping conditions explicitly.
- Assume the agent will be tested with adversarial inputs.

## Tools

- Give the agent narrow tools with clear names and strict schemas.
- Validate tool arguments; never trust the agent's strings.
- Scope each tool to the minimum capability needed for the task.
- Make tool errors structured and informative so the agent can recover.
- Require confirmation for irreversible actions: deletes, sends, payments.

## Loops and limits

- Cap steps, time and tokens per run; runaway loops are the classic failure.
- Detect and break loops: repeated same action, no progress, repeated failures.
- Require progress checks between steps and a clear stopping rule.
- Allow the agent to ask for clarification when input is ambiguous.

## Memory

- Give the agent an explicit memory design: what to remember, for how long.
- Use persistent memory for durable facts, conversation memory for the task.
- Bound memory; summarize old context instead of growing it forever.
- Protect memory from manipulation: separate system facts from user content.

## Safety

- Separate instructions from untrusted data; mark untrusted input boundaries.
- Never grant the agent secrets; pass credentials by reference through tools.
- Sandbox execution: least privilege, no network unless needed, no shell by default.
- Log every tool call with arguments and results for audit and debugging.
- Keep a human in the loop for high-stakes actions.

## Evaluation

- Test the agent with realistic and adversarial scenarios, not just happy paths.
- Keep a regression suite of tasks that previously failed; run it on changes.
- Measure success and cost per task; reliability and price are both features.
