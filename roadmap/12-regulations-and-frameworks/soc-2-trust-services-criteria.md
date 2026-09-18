# SOC 2 & the Trust Services Criteria

**TL;DR:** A SOC 2 report is an attestation, not a certification: a CPA examines a service
organization's description of its system and its controls relevant to security, availability,
processing integrity, confidentiality, or privacy under AICPA attestation standards; customers
and business partners request the report to assess outsourcing risk. In the March 2020 text of
the 2017 Trust Services Criteria, a type 2 report includes an opinion on operating
effectiveness plus the auditor's tests and results; a type 1 does not. Common criteria CC6
cover logical access (authorizing users before issuing credentials, removing credentials when
access ends, least privilege, authenticating persons, infrastructure, and software) and CC7
covers monitoring and logging of anomalies. A type 2 examination tests the relevant controls;
the evidence depends on the controls and scope.

Customers and business partners often request SOC 2 reports to assess outsourcing risk; AICPA
attestation standards govern the examination, and the Assurance Services Executive Committee
publishes the criteria used to evaluate the scoped controls. The criteria apply to whoever
chooses to be examined, and in the March 2020 edition the identity-relevant ones are CC6.1
(logical access software and architecture; persons, infrastructure, and software identified and
authenticated before access), CC6.2 (users registered and authorized before credentials are
issued, credentials removed when no longer authorized), CC6.3 (access by role with least
privilege and segregation of duties, reviewed periodically), CC6.6–CC6.8 (external threats,
transmission, malicious software), and CC7.2 (monitoring and logging of anomalies); the 2022
revision changed the points of focus, and that edition's text is not quoted here. Because CC6.1
covers persons, infrastructure, and software, agent services can fall within its access-control
scope; the auditor's tests and evidence depend on the controls and the engagement scope.
Compare the log requirements in [Sector rules: PCI DSS, HIPAA & open
banking](sector-rules-pci-dss-hipaa-open-banking.md).

_Not legal advice. Obligations and dates are quoted as published on 2026-09-17; check the
official text before relying on them._

## Resources

- [@official@AICPA — SOC 2 and the System and Organization Controls (SOC) suite](https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2)
- [@official@AICPA — 2017 Trust Services Criteria (with revised points of focus, 2022)](https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022)

---

[← 12 · Regulations, frameworks & controls](README.md) · [Map](../../README.md)
