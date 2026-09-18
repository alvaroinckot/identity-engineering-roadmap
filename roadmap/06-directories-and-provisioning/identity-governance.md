# Identity governance: lifecycle & access reviews

**TL;DR:** Identity governance is the process that keeps accounts and permissions matched to
what a person currently does. Without it access accretes: an employee who changes teams keeps
old groups, and a contractor who left keeps a live login. A joiner, mover, leaver lifecycle
creates an account on entry, changes it on a move, and disables and removes it on exit, often
as workflows triggered by an HR attribute such as `employeeHireDate`. Recurring access reviews
ask a manager, a group owner, or the users themselves to approve or deny each group membership,
application assignment, and role, and inactive or orphaned accounts get disabled. SCIM only
carries the resulting create, update, and delete calls; the decisions are policy. Agents'
service accounts fall under the same disable, review, and audit controls.

Identity governance is the set of controls that keep accounts and entitlements matched to
what people actually do: a joiner/mover/leaver lifecycle — Microsoft Entra's lifecycle
workflows define the phases as "Joiner: When an individual enters the scope of needing
access", "Mover: When an individual moves between boundaries within an organization" and
"Leaver: When an individual leaves the scope of needing access" — that creates, changes,
disables and removes accounts; periodic recertification, where, depending on the resource
type, reviewers can include specified reviewers, group owners, managers or the users
themselves, approving or denying continued access to groups, applications and roles on a
weekly-to-annual cadence (Entra access reviews); and separation of duties (NIST SP 800-53
Rev. 5 AC-5). It exists because access accretes: AC-2 requires an organization to "Create,
enable, modify, disable, and remove accounts" under policy, review them for compliance and
align them with personnel termination and transfer, AC-2(3) requires disabling accounts that
have expired, are no longer associated with a person or have been inactive, and AC-6(7)
requires a periodic review of assigned privileges "to validate the need for such privileges"
— [SCIM](scim.md) supplies create, modify and delete operations, with deactivation as an
update that sets `active` to false (RFC 7643 §4.1.1, RFC 7644), not this process. What AI
agents change: AC-2's own list of account types already includes "system" and "service"
accounts, so where an agent uses a system or service account, those disable, review and
audit controls apply to it as to an employee's account, and the OWASP Non-Human Identities
Top 10 ranks "Improper Offboarding" — "the inadequate deactivation or removal of non-human
identities (NHIs) such as service accounts and access keys when they are no longer needed" —
first, as NHI1:2025.

## Resources

- [@official@NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
- [@official@Microsoft Entra ID Governance — What are lifecycle workflows?](https://learn.microsoft.com/en-us/entra/id-governance/what-are-lifecycle-workflows)
- [@official@Microsoft Entra ID Governance — What are access reviews?](https://learn.microsoft.com/en-us/entra/id-governance/access-reviews-overview)
- [@official@RFC 7643 — SCIM: Core Schema](https://datatracker.ietf.org/doc/html/rfc7643)
- [@official@RFC 7644 — SCIM: Protocol](https://datatracker.ietf.org/doc/html/rfc7644)
- [@official@OWASP Non-Human Identities Top 10](https://owasp.org/www-project-non-human-identities-top-10/)

---

[← 06 · Directories & provisioning](README.md) · [Map](../../README.md)
