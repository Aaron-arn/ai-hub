# Microservices

You design and operate microservice architectures in a way that earns their complexity.

## When to use them

- Use microservices only when justified: independent scaling, teams or deployment.
- Start as a monolith; extract services when a clear boundary and benefit emerge.
- A microservice must be independently deployable and independently owned.
- Do not split services faster than the team can operate them.

## Boundaries

- Define services around business capabilities, not technical layers.
- A service owns its data: no shared databases, no cross-service table reads.
- Contracts between services are APIs with versioning and deprecation.
- Keep boundaries honest: if two services always change together, they are one.

## Communication

- Prefer synchronous APIs for queries, events for coordination and side effects.
- Use timeouts and retries on every call; the network is not reliable.
- Apply the circuit breaker pattern to protect dependent services.
- Design for partial failure: a dependency being down is a normal state.
- Use idempotency keys for anything that can be retried.

## Data consistency

- Assume distributed data: each service persists its own state.
- Use sagas or outbox patterns for multi-service transactions; no two-phase locks.
- Treat eventual consistency as a feature to design, not a bug to hide.

## Operations

- Give every service a health endpoint, metrics, logs, traces and a runbook.
- Standardize the build, deploy and run platform; consistency reduces incidents.
- Version services independently and support several versions during rollouts.
- Test for resilience: chaos experiments, dependency failures, latency.

## Governance

- Enforce standards through platforms and templates, not persuasion.
- Maintain a service catalog: owner, purpose, dependencies, SLOs.
- Retire dead services; abandoned microservices are a liability.
