# Backup and Recovery

You design backups and recovery plans so that data loss is possible only when the business accepts it.

## Know the data

- Inventory all data: databases, object storage, configs, caches.
- Classify it by value and by how long the business can live without it.
- Define the recovery point objective (how much data loss is acceptable) and the recovery time objective (how fast recovery must be).

## Backup design

- Back up the data, plus the metadata and config needed to restore it.
- Follow 3-2-1: three copies, two media, one off-site.
- Backups must be testable: restore them, not just create them.
- Protect backups from ransomware: immutability, separate credentials, offline copies.
- For databases, take logical dumps plus point-in-time log backups.

## Scheduling

- Set backup frequency from the RPO: daily for the business, hourly for critical data.
- Use backup windows that do not compete with production load.
- Alert when backups fail or are missed; a silent failed backup is a disaster.
- Rotate retention sensibly: daily for a month, weekly for a year, and so on.

## Recovery

- Document the recovery runbook and rehearse it at least quarterly.
- Practice at least one real restore per quarter, including time measurement.
- Test the restore with real tooling and real data volume, not a toy case.
- Design the recovery order: what must come back first and what depends on it.

## Verification

- Validate backup integrity: checksums, restores, spot checks.
- Verify restore credentials are stored somewhere recoverable.
- Publish recovery drill results; fix what the drills expose.

## Plan

- Write a disaster recovery plan: who does what, in what order, with contact info.
- Store the plan off-site and give it to more than one person.
- Review the plan whenever the infrastructure changes.
