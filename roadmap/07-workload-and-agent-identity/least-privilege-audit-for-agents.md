# Least privilege & audit for agents

**TL;DR:** Least privilege for an agent means it holds only the permissions its current task
needs; audit means every action traces back to the agent, the user, and the grant. Scope
strings are too coarse for a request like transfer this amount to this merchant, so Rich
Authorization Requests let a client send `authorization_details`, typed JSON objects used at
consent and made available to the resource server. Dynamic client registration gives a
runtime-created agent a `client_id` from submitted metadata. Token revocation lets a client ask
the authorization server to invalidate a token, while CAEP can notify Receivers that a session
was revoked. Receivers choose enforcement, and short-lived self-contained tokens limit delays
when revocation state is not propagated.

Scoped, intent-carrying authorization (RAR), consent granularity, dynamic registration for
ephemeral agent clients, and the audit trail: who did what, for whom, under which
delegation. Kill switch = revocation + continuous evaluation.

## Resources

- [@official@RFC 9396 — Rich Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9396)
- [@official@RFC 7591 — Dynamic Client Registration](https://datatracker.ietf.org/doc/html/rfc7591)
- [@official@RFC 7009 — Token Revocation](https://datatracker.ietf.org/doc/html/rfc7009)
- [@official@OpenID CAEP](https://openid.net/specs/openid-caep-1_0-final.html)
- [@official@Agentic Trust Controls — control catalog for AI agents (not yet publicly published)](https://trustcontrols.ai/)

---

[← 07 · Workload & agent identity](README.md) · [Map](../../README.md)
