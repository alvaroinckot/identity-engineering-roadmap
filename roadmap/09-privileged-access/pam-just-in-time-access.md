# PAM & just-in-time access

**TL;DR:** Privileged account management (PAM) covers accounts with elevated or sensitive
capabilities, such as a cloud tenant administrator or root on a server. Standing privilege is
usable by anyone who steals its credential, without an activation or approval step. A PAM
system can store managed privileged passwords in a vault and use them to open brokered,
recorded sessions to target systems. Just-in-time access removes continuously active privilege:
a role is assigned as eligible, and its holder activates it for a bounded duration with a
reason, often behind MFA and approval. The activation expires automatically and is retained in
audit history. A developer may encounter this as an activation step before using a production
console.

Privileged account management: vaulting admin credentials, brokering sessions, and
replacing standing privilege with time-bound, approved elevation.

## Resources

- [@official@NIST SP 1800-18 — Privileged Account Management](https://csrc.nist.gov/pubs/sp/1800/18/ipd) (initial public draft, 2018; development ceased 2022)
- [@official@Microsoft Entra PIM — What is Privileged Identity Management? (JIT elevation)](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure)

---

[← 09 · Privileged access](README.md) · [Map](../../README.md)
