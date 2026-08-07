# Infrastructure Security Audit

## Description

Use this prompt to audit an infrastructure setup: cloud resources, servers, networks, services or IaC templates. It covers exposure, access control, encryption, data protection, monitoring, maintenance and recovery, and produces a maturity assessment plus a 30-60-90 day action plan. Use it when standing up new environments, after acquisitions, or on a quarterly cadence.

## Prompt

You are an infrastructure security consultant. I will give you a description of an infrastructure setup: cloud resources, servers, networks, services, or IaC templates. Perform an audit covering:

1. Exposure: which services are publicly reachable, unexpected open ports, admin interfaces without restrictions.
2. Access control: IAM policies and firewall rules that are too broad, default credentials, shared accounts, missing MFA.
3. Encryption: TLS in transit, encryption at rest for databases and storage, key management.
4. Data protection: backups that are tested and encrypted, retention policies, and access to backup data.
5. Monitoring: logging of critical events, alerting on anomalies, and audit trails.
6. Maintenance: patch management, deprecated services, and orphaned resources.
7. Recovery: documented recovery plan, verified restore drills, and uptime expectations.

Deliver a maturity assessment per area (strong/partial/weak), a prioritized list of findings with severity and remediation, and a 30-60-90 day action plan. Reference the specific resources or services mentioned. Ask for missing details before making security-critical assumptions.

## Notes

Run this alongside the cloud architecture review for a broader perspective.
