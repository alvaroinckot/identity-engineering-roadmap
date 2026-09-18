# Audit trails & attribution

**TL;DR:** An audit trail is the stored record of who did what, when, where, from which source,
and with what outcome, one entry per event. It exists so an action can be attributed to a
person, or to a process acting for one, and the record can serve as evidence. Protect logs from
the parties whose actions they record; separate storage and append-only access are controls to
consider, not universal requirements. Passwords, session identifiers, and access tokens should
not be logged in clear text; mask or hash them instead. After token exchange, a token's
top-level claims can name the subject while its `act` claim names the current actor, allowing
one log entry to record both.

An audit trail is the record of who did what, when, where, and with what outcome — the six
fields NIST SP 800-53 control AU-3 requires of an audit record, built on SP 800-92's
definition of a log as "a record of the events occurring within an organization's systems
and networks" that is generated, transmitted, stored, analyzed and finally disposed of. It
exists for accountability and reconstruction: AU-10 asks for "irrefutable evidence that an
individual (or process acting on behalf of an individual) has performed" an action, and a
trail the recorded party can edit proves nothing, so AU-9 protects audit information and
tools from unauthorized access, modification and deletion, SP 800-92 §5.1.3 recommends
append-only, no-read access for users "if possible", and OWASP's logging guidance says
passwords, session identifiers and tokens "should usually not be recorded directly" but
removed, masked, hashed or encrypted. Agents change what "who" means: a token obtained
through RFC 8693 token exchange carries an `act` claim that "identif[ies] the acting party
to whom authority has been delegated" (§4.1) while its top-level claims identify the
subject, so a record can name both the human principal and the agent acting for them (the
RFC itself requires no logging); that every tool call an agent makes is logged as its own
event, not just the session that contained it, is a design position this map takes without a
standard behind it (for the permission side, see [Least privilege & audit for
agents](../07-workload-and-agent-identity/least-privilege-audit-for-agents.md)).

## Resources

- [@official@NIST SP 800-92 — Guide to Computer Security Log Management](https://csrc.nist.gov/pubs/sp/800/92/final)
- [@official@NIST SP 800-53 Rev. 5 — Security and Privacy Controls (AU-2, AU-3, AU-9, AU-10)](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)
- [@official@OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
- [@official@RFC 8693 — OAuth 2.0 Token Exchange, §4.1 "act" (Actor) Claim](https://datatracker.ietf.org/doc/html/rfc8693#section-4.1)

---

[← 09 · Privileged access](README.md) · [Map](../../README.md)
