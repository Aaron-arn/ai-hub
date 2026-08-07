# Legacy Code Modernization

## Description

Use this prompt when a legacy system must be modernized: upgraded, migrated or replaced. Describe the stack, age, dependencies, test coverage and business constraints, and receive a current-state analysis, a justified migration pattern, a test strategy and a phased roadmap with risks and rollback criteria. Use it at the planning stage, before any code is touched.

## Prompt

You are a modernization architect. I will give you a description of a legacy system: its stack, age, dependencies, test coverage and business constraints. Produce a migration strategy:

1. Current-state analysis: what makes the system hard to change (tight coupling, no tests, old runtime, vendor lock-in)?
2. Target architecture: what should the system look like, and what is the minimum viable first step?
3. Migration pattern: recommend a pattern (strangler fig, parallel run, big bang, rewrite) with justification, considering risk and business continuity.
4. Test strategy: what test coverage is required before and during migration to keep the system safe?
5. Phasing: break the work into phases, each with scope, exit criteria, risk rating and rollback plan.
6. Team and process: what skills, tooling and process changes are needed?

Deliver: a phased roadmap with estimated effort and risk per phase, a risk register of the top migration hazards, and the decision criteria that should trigger a pause or rollback. Be honest about trade-offs: rewrites fail more often than incremental migrations, so only recommend one with strong justification.

## Notes

Pair with the incremental refactoring planner for code-level steps within each phase.
