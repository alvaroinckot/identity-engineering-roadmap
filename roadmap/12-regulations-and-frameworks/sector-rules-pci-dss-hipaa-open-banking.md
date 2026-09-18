# Sector rules: PCI DSS, HIPAA & open banking

**TL;DR:** PCI DSS v4.0.1 is intended for entities that store, process, or transmit cardholder
data or sensitive authentication data, or that could affect the cardholder data environment:
Requirement 7 wants least-privilege access with accounts reviewed at least every six months,
Requirement 8 wants a unique ID per user, MFA for all non-console access into the CDE, and no
hard-coded passwords for application and system accounts usable for interactive login, and
Requirement 10 wants audit logs of individual access and administrative actions. HIPAA's
Security Rule, 45 CFR §164.312, makes covered entities and business associates implement access
control with unique user identification, audit controls, person or entity authentication, and
transmission security for ePHI. FAPI 2.0 was initially developed with a focus on financial
applications and suits high-security APIs; adoption requirements are ecosystem-specific.

PCI DSS is written by the PCI Security Standards Council as "a baseline of technical and
operational requirements designed to protect payment account data"; v4.0.1 is a limited
revision of v4.0 (March 2022) that added no requirements, and its identity clauses are 7.2.1
(access by job function with "the least privileges required"), 7.2.4 (account review "at least
once every six months"), 7.2.5 (application and system accounts on least privilege), 8.2.1
("All users are assigned a unique ID"), 8.3.1 (a knowledge, possession, or biometric factor),
8.4.2 (MFA for "all non-console access into the CDE", not applying to "application or system
accounts performing automated functions"), 8.6.1–8.6.2 (interactive use of system accounts
attributable to an individual, no passwords "hard coded in scripts, configuration/property
files, or bespoke and custom source code"), and 10.2.1.1–10.2.2 (logs of individual access to
cardholder data and of every administrative action, recording user, event, time, outcome,
origin, and target). HIPAA §164.312 is federal regulation, not an industry standard: it binds
covered entities and business associates and requires access only for "persons or software
programs that have been granted access rights", a unique name or number per user, mechanisms
that "record and examine activity", and procedures to verify a person or entity "is the one
claimed". An agent accessing ePHI falls within "software programs" for access-control purposes;
the section separately requires unique user identification and activity-recording mechanisms,
and does not expressly require a unique ID per software agent. Open banking: PSD2's
authentication rules have their own page ([PSD2 & strong customer
authentication](psd2-strong-customer-authentication.md)), and [FAPI
2.0](../05-identity-protocols/fapi-2-0.md) is the OAuth 2.0 security profile "initially
developed with a focus on financial applications" and suitable for high-security applications —
the spec names no open-banking ecosystem that mandates it.

_Not legal advice. Obligations and dates are quoted as published on 2026-09-17; check the
official text before relying on them._

## Resources

- [@official@PCI DSS v4.0.1 — Payment Card Industry Data Security Standard (PCI Security Standards Council)](https://www.pcisecuritystandards.org/standards/pci-dss/)
- [@official@HIPAA Security Rule — 45 CFR § 164.312 Technical safeguards (eCFR)](https://www.ecfr.gov/current/title-45/section-164.312)
- [@official@FAPI 2.0 Security Profile (OpenID Foundation, Final)](https://openid.net/specs/fapi-security-profile-2_0.html)

---

[← 12 · Regulations, frameworks & controls](README.md) · [Map](../../README.md)
