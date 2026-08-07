# Product Requirements Document Builder

## Description

Writes a structured Product Requirements Document (PRD) from a feature idea. Use it before handing a feature to design and engineering. Produces a PRD that answers the why, the what, and the how-to-verify, in a format teams can review in one sitting.

## Prompt

You are a senior product manager writing PRDs that engineers call "the best they have ever seen". Write a PRD for the feature described below.

Feature idea: [what you want to build]
Problem it solves: [for whom and why now]
Business goal: [revenue, retention, activation, cost saving]
Users: [who uses it and their context]
Constraints: [tech stack, platform, deadlines, dependencies, or non-negotiables]

Structure the PRD:
1. Summary: 3 sentences - the problem, the solution, the expected outcome.
2. Goals and non-goals: 3 goals stated as outcomes with measurable targets, and a clear non-goals list (what this feature explicitly will not do).
3. User personas: 2 short personas for the primary users.
4. User stories and acceptance criteria: 5-10 stories in the format "As a [persona], I want [action], so that [outcome]", each with 3-5 concrete acceptance criteria phrased as testable conditions.
5. Functional requirements: a numbered list covering the main flows (happy path, edge cases, error states, empty states).
6. UI and copy notes: key layout decisions and any copy requirements, only where they matter.
7. Metrics: success metrics with targets (e.g. activation rate, task completion) and 2 guardrail metrics to watch.
8. Out of scope and future iterations.
9. Risks and open questions: 3 risks with mitigations, and a list of open questions that block development.

Rules: no invented features beyond my input. Requirements must be testable, not vague ("fast" must become "under 2 seconds"). Flag anything in my input that is ambiguous and offer a default assumption.

## Notes

Bring real user research quotes into the summary for a stronger PRD. Share the PRD with an engineer before design starts to catch scope creep.
