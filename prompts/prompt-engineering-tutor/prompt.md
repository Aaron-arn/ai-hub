# Prompt Engineering Tutor

## Description

You describe a task you want to delegate to an LLM, and the assistant rewrites it as a structured, high-quality prompt with role, context, constraints, and output format — then explains the improvements. Use it before generating prompts for code, writing, analysis, or data work so the results are consistent and useful.

## Prompt

You are a prompt engineering expert. I need a better prompt for this task:

"My job: I get raw CSV exports of customer feedback with columns `date, rating (1-5), comment, product`. I want an LLM to turn each row into a short summary of the main complaint or praise, and tag it with a category. I want the results in a table I can paste back into a spreadsheet."

Produce:
1. A final prompt (English, ready to paste into ChatGPT or Claude) with these sections in order: role, task, input format, processing rules, output format, and quality bar. Make the output a strict markdown table with columns `date`, `product`, `category`, `summary`, and require categories drawn only from `pricing, quality, shipping, support, other`.
2. The prompt must include: a worked example row and its expected output, an instruction to output only the table (no commentary), a rule to keep summaries under 15 words, and an instruction to return "unparseable" in the category column when the comment is empty or gibberish.
3. After the prompt, add a section "Why this prompt works" with exactly 4 numbered bullets explaining which prompt element addresses which failure mode (vague output, wrong categories, table breakage, summary length).
4. Give one variation: a condensed one-paragraph version of the same prompt for chat-based quick use.

Keep the final prompt under 250 words.

## Notes

Swap the example for your own real task; the section structure transfers to any domain. Ask for a JSON output variant when you need machine-readable results instead of a table.
