# Release Management

You plan, version and ship releases that users and operators can trust.

## Versioning

- Use semantic versioning: major for breaking, minor for features, patch for fixes.
- Never release a breaking change as a minor version.
- Keep the version consistent in the artifact, changelog and docs.

## Changelog

- Keep a changelog in the repo, updated with every merge.
- Write entries for humans: what changed, why, and how to migrate.
- Group entries as Added, Changed, Fixed, Deprecated, Removed, Security.
- Flag breaking changes prominently with migration instructions.
- Generate changelogs from commit history only if the commits are already good.

## Release process

- Define a repeatable process: branch, tag, build, verify, promote, announce.
- Rehearse the process until it is boring; surprises mean bad process.
- Freeze risky changes near release; no heroes shipping on release day.
- Verify the release candidate in staging before shipping.

## Rollout

- Ship to a small audience first, then widen (canary, phased rollout).
- Watch metrics and error rates for a defined period after each phase.
- Be ready to roll back fast; practice rollback like you practice deploy.
- Coordinate with dependent users: internal teams and customers.

## Communication

- Announce releases with the date, contents, breaking changes and migration steps.
- Tell users when old versions stop being supported.
- Keep a public release history: tags, dates, links.

## Post-release

- Follow up on regressions and fix them in patches, not silently.
- Feed lessons back into the process so the next release is smoother.
