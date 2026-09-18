# Subject vs. actor

**TL;DR:** The subject is the party an action is about; the actor is the party performing it. A
system that stores one field for both cannot later tell a user's own request from a service's
request on that user's behalf. RFC 8693 describes impersonation as making the acting party
indistinguishable from the subject in a context, and defines act as a way for a JWT to identify
a delegated actor. The token request carries a subject_token for the party on whose behalf it
is made and an optional actor_token for the party that will act. An AI agent reading a
customer's calendar is the actor and the customer is the subject; a log that records only one
of them cannot say who did what.

The party an action is *about* versus the party *performing* it. Keep them apart from day
one; delegation and agent identity depend on it.

## Resources

- [@official@RFC 8693 — OAuth 2.0 Token Exchange](https://datatracker.ietf.org/doc/html/rfc8693), §1.1 (delegation vs. impersonation) and the `act` claim

---

[← 01 · Primitives](README.md) · [Map](../../README.md)
