# Performance Tuning

## Description

Profile-driven optimization advice for slow code paths.

## Prompt

Optimize this slow code: {CODE} (context: {CONSTRAINTS} - e.g., processes 10k items, 2s budget)

Process:
1. HYPOTHESIZE: identify likely bottlenecks with complexity analysis (state Big-O per block)
2. MEASURE FIRST: what profiling data do I need? Suggest the exact commands (cProfile, py-spy, perf)
3. THEN OPTIMIZE, ordered by impact: algorithmic change > caching > data structure > micro-optimizations. Give each as a before/after snippet.
4. TRADEOFFS: memory vs speed, complexity vs readability for each suggestion
5. VALIDATION: how to benchmark correctly (warm-up, median over N runs, avoid noise)

Rule: never micro-optimize before profiling. Flag if the real fix is likely outside the shown code (I/O, DB, network).
