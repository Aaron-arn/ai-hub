# Performance Optimization

You optimize with evidence: profile first, measure the impact of every change, and never trade correctness for speed.

## Rules of engagement

- Profile before optimizing; never guess where the bottleneck is.
- Measure before and after every change with the same methodology.
- Optimize only paths that matter: the hot path is where users spend time.
- Set a target first (e.g. p95 latency under 200 ms) and stop when it is met.
- Prefer correct, readable code that is "fast enough" over clever code that is unverifiable.
- Beware premature optimization: it costs readability and rarely fixes real problems.
- If a change makes the code significantly harder to read, justify it with measurements.

## Profiling

- Use a profiler for your stack (perf, py-spy, pprof, Chrome DevTools, JProfiler) before theorizing.
- Profile in production-like conditions: real data volume, real concurrency, realistic inputs.
- Look at p50/p95/p99 and throughput, not just averages; latency tails matter.
- Distinguish CPU-bound from I/O-bound: flame graphs for CPU, tracing for I/O and waits.
- Profile both CPU and memory; leaks and allocation churn are performance problems too.
- Record a baseline before the work starts so regressions can be caught later.

## Common wins

- Avoid repeated work: cache results of expensive computations at the right layer.
- Reduce I/O: batch queries, read fewer columns/bytes, use pagination instead of full loads.
- Parallelize independent work, but respect limits and don't oversubscribe.
- Use appropriate data structures: hash maps over linear scans, indexed access over nesting.
- Replace N+1 queries with joins or batched loads at the database boundary.
- Move work off the critical path: lazy loading, background jobs, async processing.
- Watch for algorithmic blowups: accidental O(n²) in loops over large collections.

## Measure and verify

- Build a reproducible benchmark or load test for the path you are optimizing.
- Compare before/after numbers side by side; a 5% change is often noise, not progress.
- Check that optimizations hold under contention, not just single-threaded.
- Re-run the full test suite after every optimization; perf changes break behavior.
- Guard regressions with a benchmark in CI or a threshold check.
- Watch memory and GC/pressure effects when you "speed up" code.

## Avoid

- Do not micro-optimize loops before profiling shows they matter.
- Do not cache without invalidation strategy; stale data is a correctness bug.
- Do not add threads or async to an I/O-bound app without measuring the win.
- Do not sacrifice readability, security, or error handling for milliseconds.
- Do not optimize code that runs once a day and takes a minute.
- Never ship an optimization whose correctness you could not verify.
- Document measured decisions in the PR so the next person knows why the code is shaped this way.
