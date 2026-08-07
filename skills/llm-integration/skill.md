# LLM Integration

You integrate LLMs into applications, handling calls, errors and costs responsibly.

## Design the integration

- Define the task precisely; many LLM features are simpler than they look.
- Pick the smallest and cheapest model that reliably does the task.
- Treat the model as a component with a contract: input format, output format, failure modes.
- Keep prompts versioned with their code, so behavior changes are trackable.

## Prompts

- Write prompts with explicit instructions: role, task, constraints, output format.
- Ask for structured output (JSON schema) and validate it strictly.
- Include examples of good and bad output where mistakes are costly.
- Keep prompts deterministic where possible: low temperature for extraction, tools and math.

## Handling output

- Never trust model output as-is for data that matters; validate and parse it.
- Use the model as a hypothesis generator where output is non-deterministic.
- Add constraints for dangerous content: reject, escalate, or stay silent.
- Base decisions on structured fields, not free text, where possible.

## Errors and retries

- Treat API calls like any network call: timeouts, retries, backoff.
- Handle rate limits and quota errors with exponential backoff.
- Handle malformed output by retrying or re-prompting with guidance.
- Degrade gracefully when the provider is down: fallback path or clear message.

## Costs and latency

- Track tokens per request and set budgets per user and per day.
- Cache and reuse results for identical or similar requests.
- Stream responses when latency matters for the user experience.
- Trim context: send only the necessary history, not the whole transcript.
- Batch independent calls where it improves cost.

## Safety and privacy

- Never send secrets, personal data or regulated data without approval.
- Disclose when content is AI-generated where the context requires it.
- Guard against prompt injection: separate instructions from untrusted input.
- Log model usage minimally and protect those logs as data.
