# Dependency Management

You add, update and audit dependencies with the care the supply chain deserves.

## Adding a dependency

- Add a dependency only when it earns its place: real functionality, not convenience.
- Evaluate the package: maintenance activity, security record, license, community.
- Prefer widely used, actively maintained libraries over abandoned ones.
- Document why the dependency exists; future maintainers will ask.

## Pinning and versions

- Pin exact versions in production artifacts; use ranges only in libraries.
- Commit lockfiles so builds are reproducible.
- Never leave dependencies unpinned or floating on "latest".
- Prefer a small set of well-chosen versions over many overlapping ones.

## Updating

- Update regularly on a schedule; pent-up dependency debt is risk.
- Upgrade in small steps: one major version at a time.
- Read changelogs and migration guides before upgrading.
- Run the full test suite on the upgrade, not just a smoke test.
- Keep a rollback path: know the previous version and how to return to it.

## Security

- Run vulnerability scanning on a schedule and in CI.
- Treat critical and high severity advisories as action items with deadlines.
- Investigate advisories before fixing: is the package reachable and exploitable?
- Replace unmaintained packages that accumulate unfixed advisories.
- Never trust dependencies blindly: review what you install, especially new ones.

## Hygiene

- Remove dependencies that are no longer used; prune dead trees.
- Watch for duplication: two libraries shipping the same code.
- Keep transitive dependencies as lean as the ecosystem allows.
- Record known caveats (licenses, native binaries, telemetry) in the repo.
