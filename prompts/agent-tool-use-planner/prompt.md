# Agent Tool Use Planner

## Description

Use this prompt when designing or improving an AI agent that calls tools. Describe the task and paste the tool list (or tool schemas and descriptions), and receive a complete tool-use plan: which tool for which step, execution order, arguments, error handling, result verification and stopping criteria. Use it before implementing an agent, or to audit why an existing agent misbehaves.

## Prompt

You are an expert in building reliable AI agents. I will give you a task that an agent must complete, along with a list of available tools (functions the agent can call, with descriptions) or a description of the agent's capabilities. Design a tool-use plan:

1. Tool selection: for each step of the task, choose the right tool and explain why; identify tasks that need no tool.
2. Execution order: sequence the calls, note which depend on earlier outputs, and where parallel calls are possible.
3. Arguments: specify what inputs each call needs and how to derive them from the conversation context.
4. Error handling: define fallback behavior for each failure mode: tool errors, empty results, timeouts, and invalid inputs.
5. Verification: for each result, state how to check plausibility before trusting it (schema checks, sanity ranges, cross-checks).
6. Stopping criteria: define when the task is complete and when to stop and ask the user.

Deliver: a numbered plan, a decision table mapping situations to tool calls, and a list of conditions that should trigger escalation to a human. Ask clarifying questions only if the task or tool descriptions are ambiguous.

## Notes

Give the exact tool schemas for best results. Pair with the agent safety review to bound what the agent is allowed to do.
