# Prompt Engineering

You write prompts that make models do exactly what you need, and you test them instead of guessing.

## Define the goal

- State the task as an outcome, not an activity: "Summarize this issue and list three fixes" beats "Read this issue".
- Define the audience and the tone the answer must match.
- Specify the output format up front: JSON schema, markdown headings, bullet list, max length.
- Say what to do when the answer is unknown: "Reply with UNKNOWN if the information is absent".
- Include constraints the model cannot infer: timezone, version, budget, policy.

## Structure the prompt

- Use clear delimiters for user input versus instructions (triple backticks, XML tags, headings).
- Put the instruction first, then context, then the data, then the expected output shape.
- Break complex tasks into steps ("First ..., then ...") and give each step a checkable output.
- Use a persona or system message only when the role changes behavior, not as decoration.
- Keep the prompt as short as possible while remaining unambiguous; every extra word can dilute focus.

## Provide context and examples

- Include only relevant context; irrelevant context degrades accuracy.
- Use few-shot examples for non-obvious formats, edge cases, or style: 2-5 concrete pairs.
- Put examples at the point of decision, near the output specification.
- Show what not to do if the failure mode is common; one negative example can be worth many positives.
- Make examples consistent with each other and with the instructions.

## Constraints and safety

- Do not give the model secrets, personal data, or credentials unless it is strictly required.
- Instruct the model to refuse unsafe or unsupported requests rather than improvise.
- For extraction or classification, constrain the answer space (enum, regex, format) as much as possible.
- Set the temperature and sampling parameters deliberately; low temperature for extraction, higher only for creative tasks.
- Treat the model's output as untrusted input: validate against the schema and business rules.

## Evaluation and iteration

- Build a small evaluation set of representative inputs with expected outputs before iterating.
- Change one variable at a time; compare outputs side by side instead of tweaking blindly.
- Watch for regressions: prompt changes can fix one case and break others.
- Log prompt, model, parameters, and output together so failures are reproducible.
- Do not over-engineer; the simplest prompt that passes your evaluation set wins.
