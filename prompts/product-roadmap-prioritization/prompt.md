# Product Roadmap Prioritization

## Description

Turns a messy feature list into a scored, sequenced quarterly roadmap. Use it during planning season or whenever stakeholders all want their feature first. Produces a defensible priority order grounded in user value, business impact, and build effort.

## Prompt

You are an experienced product manager who prioritizes features using the RICE and value-versus-effort methods. Turn my feature list into a quarterly roadmap.

Features (one per line, include any known details): [list features]
Product context: [what the product does and its stage]
Business goals for the quarter: [e.g. retention, revenue, activation]

For each feature, estimate on a 1-5 scale:
- User value: how much it improves life for target users.
- Business value: revenue, retention, or strategic importance.
- Effort: engineering time and complexity (1 = trivial, 5 = very expensive).
- Confidence: how sure we are of the first three estimates.

Output:
1. A table with all features, the four scores, and a priority score computed as (User value x 2 + Business value x 1.5) / Effort, multiplied by Confidence.
2. A recommendation of the top 5 features to build this quarter, in order.
3. A proposed roadmap with a rough sequencing rationale: dependencies first, quick wins early for momentum, big bets spread out.
4. A list of features to reject or park, with a one-line reason for each.
5. Highlight where low confidence scores mean we should do research or a prototype before committing.

Challenge my inputs: if a feature looks over-scored or under-scored compared to others, say so and ask me to confirm.

## Notes

Re-run after each sprint with updated effort estimates. Pair with customer interviews to validate the user value scores.
