# NIS2 & DORA: access control and MFA as legal duties

**TL;DR:** Two EU acts turn common identity controls into legal obligations. NIS2 (Directive
(EU) 2022/2555) requires "essential" and "important" entities in the sectors listed in its
annexes to take cybersecurity risk-management measures that must include access control
policies and, where appropriate, multi-factor or continuous authentication, and to report
significant incidents with an early warning within 24 hours and a notification within 72 hours;
as a directive it applies through the national laws that transpose it. DORA (Regulation (EU)
2022/2554) applies directly to financial entities and requires logical access limited to
legitimate and approved functions, strong authentication, protection of cryptographic keys,
continuous monitoring of ICT systems, and monitoring of user activity to detect anomalies.

NIS2 Art. 21(1) obliges member states to ensure that essential and important entities (defined
by size and sector in Art. 3) take "appropriate and proportionate technical, operational and
organisational measures", and Art. 21(2) lists what those measures "shall include at least":
point (i) "access control policies" and point (j) "the use of multi-factor authentication or
continuous authentication solutions", the latter qualified by "where appropriate"; Art. 23(4)
sets the clock: an early warning "within 24 hours", an incident notification "within 72 hours"
and a final report within one month. DORA Art. 9(4)(c) requires policies that limit "physical
or logical access to information assets and ICT assets to what is required for legitimate and
approved functions and activities only", Art. 9(4)(d) requires "strong authentication
mechanisms" and "protection measures of cryptographic keys", and Art. 9(1) and Art. 10 require
financial entities to "continuously monitor" ICT systems and to "monitor user activity" — the
duties behind [multi-factor authentication](../02-authentication/multi-factor.md) and [audit
trails & attribution](../09-privileged-access/audit-trails-attribution.md). The cited
provisions require in-scope entities to administer access rights, operate authentication
controls, monitor activity, and make timed notifications.

_Not legal advice. Obligations and dates are quoted as published on 2026-09-17; check the
official text before relying on them._

## Resources

- [@official@Directive (EU) 2022/2555 (NIS 2) — Art. 21 risk-management measures, Art. 23 incident reporting, Art. 41 transposition](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)
- [@official@Regulation (EU) 2022/2554 (DORA) — Art. 9 access control and strong authentication, Art. 10 detection, Art. 64 application](https://eur-lex.europa.eu/eli/reg/2022/2554/oj)

---

[← European Union: identity regulation](eu-identity-regulation.md) · [12 · Regulations, frameworks & controls](README.md) · [Map](../../README.md)
