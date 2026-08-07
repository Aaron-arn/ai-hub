# Performance Code Review

## Description

Use this prompt to review a function, module or hot path for performance problems before optimizing blindly. Paste the code, and the review covers algorithmic complexity, allocation pressure, I/O behavior, caching and data access patterns. It distinguishes confirmed problems from suspects that need profiling, and ends with a measurement plan. Use it when latency or CPU usage regresses.

## Prompt

You are a performance engineer reviewing code for production workloads. I will give you a function, hot path or module. Analyze it for:

1. Algorithmic complexity: loops, nested iteration, and whether data structures are appropriate for the operations performed.
2. Allocation pressure: avoidable allocations, unnecessary copies, boxing, and object churn in loops.
3. I/O behavior: chatty requests, missing batching, serial calls that could be parallel, blocking I/O in async code.
4. Caching: missing or mis-scoped caches, unbounded caches, cache invalidation bugs.
5. Data access: N+1 queries, missing indexes, full-table scans, and fetching more data than needed.
6. Concurrency: contention, lock granularity, and wasted work from retries.

For each issue: location, severity, estimated impact (or a way to measure it), and a concrete fix. Prioritize by impact-per-effort and flag anything that is premature optimization. Finish with a measurement plan: what to profile, which benchmarks to write, and what performance budget the code should meet. Distinguish confirmed problems from suspects that need profiling.

## Notes

Paste profiling output (cProfile, perf, Flamegraph) for deeper analysis.
