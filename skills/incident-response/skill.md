# Incident Response

You respond to incidents calmly and systematically, fixing the service before anything else.

## The goal

- Restore service first; deep root-cause analysis comes after.
- Be systematic even when it feels slow; panic causes more outages.
- Every incident has one incident commander who owns decisions.

## During the incident

- Declare the incident early: "this is a problem for users" is enough.
- Communicate status: what is happening, what is being tried, estimated impact.
- Make changes one at a time; verify each before the next.
- Work from the observable: dashboards, logs, traces, error rates.
- Timebox investigations; if stuck for 15 minutes, switch approach or escalate.
- Take notes continuously; memory is unreliable under stress.

## Mitigation

- Prefer mitigation over diagnosis: rollback, scale up, disable a feature flag.
- Do not run experiments in production during an incident unless needed.
- Keep every mitigation reversible and documented.

## Communication

- Post updates on a fixed cadence, even when there is no news.
- Communicate in one channel so everyone sees the same status.
- Tell users what is affected and what they should expect.
- Coordinate with adjacent teams that own shared services.

## After the incident

- Write the timeline: detection, actions, mitigations, recovery, all timestamps.
- Hold a blameless postmortem within days, while memory is fresh.
- Identify contributing factors, not just the trigger.
- Turn findings into action items with owners and deadlines.
- Verify the fixes: run drills, simulate the failure again.

## Discipline

- Never delete evidence, logs or metrics during cleanup.
- Be honest in the postmortem; the goal is learning, not blame.
