# Impersonation vs. delegation

**TL;DR:** Impersonation and delegation are two semantics RFC 8693 defines for one party acting
for another. The subject is the party represented by the token, and the actor is the party
currently acting. In impersonation, the actor receives the subject's rights within a defined
context and is indistinguishable from the subject there. In delegation, actions remain
attributable to the actor representing the subject. For JWTs, an `act` claim can name the
current actor while top-level claims describe the subject. A token-exchange request uses
`subject_token` for the represented party and can use `actor_token` for the acting party.

Impersonation: the actor becomes indistinguishable from the subject. Delegation: the actor
acts for the subject and the token says so. RFC 8693 §1.1 defines both; subject vs. actor
(→ [01](../01-primitives/subject-vs-actor.md)) is the primitive underneath.

## Resources

- [@official@RFC 8693 — OAuth 2.0 Token Exchange](https://datatracker.ietf.org/doc/html/rfc8693), §1.1

---

[← 08 · Delegation & impersonation](README.md) · [Map](../../README.md)
