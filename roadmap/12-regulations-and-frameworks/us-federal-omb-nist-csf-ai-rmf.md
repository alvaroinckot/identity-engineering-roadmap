# US federal: OMB zero trust, NIST CSF 2.0 & the AI RMF

**TL;DR:** NIST CSF 2.0 "does not prescribe how outcomes should be achieved", and the NIST AI
RMF 1.0 is "intended to be voluntary". OMB M-22-09 (January 26, 2022) imposed specific
zero-trust requirements on federal agencies and cited NIST SP 800-63B and SP 800-207: it set an
end-of-FY2024 goal and required agencies to run centralized identity management, enforce MFA at
the application layer, require phishing-resistant MFA, drop SMS/voice/OTP/push MFA, remove
password complexity and rotation rules per SP 800-63B, and weigh at least one device signal
when authorizing access; some actions were due within one year. CSF 2.0 (February 26, 2024) has
six Functions; its PR.AA category covers identities, credentials, authentication, assertions,
and least-privilege permissions for users, services, and hardware. AI RMF 1.0 (January 2023)
adds GOVERN, MAP, MEASURE, and MANAGE.

NIST writes the technical guidance — SP 800-63B, which M-22-09 cites for its password rules
(see [Assurance levels](../02-authentication/assurance-levels.md)), and SP 800-207, which it
cites for attribute-based access control (see [Zero trust
architecture](../10-zero-trust-and-continuous-access/zero-trust-architecture.md)) — and OMB
M-22-09 section A "Identity" set the agency obligations: "centralized identity management
systems", MFA "enforced at the application layer, instead of the network layer",
phishing-resistant MFA (defined in footnote 6 as resisting disclosure of secrets to a
masquerading site), removal of special-character and rotation rules "within one year", and "at
least one device-level signal alongside identity information" in authorization decisions; those
deadlines have passed. CSF 2.0 does not prescribe implementation; it gives every organization
the outcome vocabulary an assessor maps controls to, and PR.AA-01 to PR.AA-05 name users,
services and hardware, so applying the category to workload and agent identities is an
implementation inference, not a stated requirement. AI RMF 1.0 is voluntary: GOVERN 1.6 calls
for an inventory of AI systems, GOVERN 3.2 and MAP 3.5 address roles and human oversight, and
MANAGE 4.1 addresses post-deployment monitoring, including "appeal and override,
decommissioning, incident response".

_Not legal advice. Obligations and dates are quoted as published on 2026-09-17; check the
official text before relying on them._

## Resources

- [@official@OMB M-22-09 — Moving the U.S. Government Toward Zero Trust Cybersecurity Principles](https://www.whitehouse.gov/wp-content/uploads/2022/01/M-22-09.pdf)
- [@official@NIST Cybersecurity Framework (CSF) 2.0 — NIST CSWP 29](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf)
- [@official@NIST AI Risk Management Framework (AI RMF 1.0) — NIST AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)
- [@official@NIST SP 800-63B-4 — Authentication & Authenticator Management](https://pages.nist.gov/800-63-4/sp800-63b.html)
- [@official@NIST SP 800-207 — Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)

---

[← 12 · Regulations, frameworks & controls](README.md) · [Map](../../README.md)
