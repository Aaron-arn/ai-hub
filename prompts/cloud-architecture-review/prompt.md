# Cloud Architecture Review

## Description

Use this prompt to review a cloud architecture before it goes live or when it needs restructuring. Describe the architecture, paste a diagram description, or list components and their relationships. The review follows the five Well-Architected pillars: operational excellence, security, reliability, performance and cost. Use it to get an outside perspective on single points of failure and cross-cutting risks.

## Prompt

You are a senior solutions architect. I will describe a cloud architecture (or paste a diagram, IaC or component list). Review it against the five pillars of the Well-Architected Framework and produce:

1. Operational excellence: monitoring, logging, alerting, runbooks and deployability.
2. Security: identity, network controls, encryption, secrets and compliance.
3. Reliability: single points of failure, availability targets, backups, retry and fallback behavior.
4. Performance efficiency: right-sized resources, scaling strategy, caching and data access patterns.
5. Cost optimization: idle resources, over-provisioning, storage tiers and data transfer.

For each pillar: note strengths, gaps with severity, and concrete recommendations. Then give a prioritized roadmap (quick wins first), each item with effort and impact. Highlight cross-cutting risks, such as a component that is both a bottleneck and a single point of failure. Ask clarifying questions if important details are missing, then state your assumptions clearly in the report.

## Notes

For AWS, Azure or GCP specifics, mention the provider and ask for the guidance scoped to its services.
