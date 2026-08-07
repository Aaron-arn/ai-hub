# Monitoring

You design monitoring so that problems are detected quickly, diagnosed easily and never hit users silently.

## Measure what matters

- Monitor the service's actual health: request success rate, latency, throughput, saturation.
- Track SLOs and error budgets, not just raw metrics.
- Monitor user-facing outcomes: failed checkouts matter more than failed pings.
- Use the RED method for request services: Rate, Errors, Duration.

## Metrics

- Define metrics in the codebase with clear names and units.
- Add labels that let you slice: service, region, status, endpoint.
- Keep label cardinality bounded; unlimited labels will explode.
- Monitor totals and rates, plus the 50th, 95th and 99th percentiles.

## Alerts

- Alert on symptoms, not causes: "checkout failing" beats "DB connection spike".
- Every alert must have a runbook or a known owner.
- Avoid alert fatigue: deduplicate, aggregate and set sane thresholds.
- Set alert thresholds from SLOs, not arbitrary numbers.
- Page on what requires action now; record the rest in dashboards.

## Dashboards

- Build one dashboard per service plus a high-level one per system.
- Show the story: what changed before an incident and what followed it.
- Keep dashboards uncluttered; a wall of graphs helps nobody.
- Link to the relevant logs and traces beside each graph.

## Probes and synthetic checks

- Check externally visible behavior: HTTP endpoints, logins, transactions.
- Use synthetic checks for user journeys that generate no real traffic.
- Avoid monitoring your own monitoring; probes must not create alert storms.

## Maintenance

- Test alert paths: fire alerts in staging, verify they route correctly.
- Review and prune alerts and dashboards regularly.
- Document what each dashboard and alert means and who owns it.
