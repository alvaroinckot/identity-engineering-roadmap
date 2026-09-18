# Token exchange: RFC 8693

**TL;DR:** Token exchange is an OAuth grant for presenting one security token to an
authorization server and requesting another. A resource server can use it to obtain a token
suitable for a downstream API instead of forwarding the incoming token. The request contains a
required `subject_token` and `subject_token_type`, and it can contain an `actor_token`, target
resource or audience, scope, and requested token type. The authorization server validates the
request and decides what to issue. For JWTs, `act` can identify an actor, nested `act` claims
can record earlier actors, and `may_act` can state who is authorized to act. RFC 7523
separately defines a signed JWT used as an authorization grant.

The general protocol: `subject_token`, `actor_token`, requested token type, the `act` chain
and `may_act`. The JWT bearer grant (RFC 7523, 2015) is the older sibling; identity chaining
reuses it to carry a grant across trust domains (draft §2.4), and Entra's on-behalf-of flow
rides its grant-type URN.

## Resources

- [@official@RFC 8693 — OAuth 2.0 Token Exchange](https://datatracker.ietf.org/doc/html/rfc8693)
- [@official@RFC 7523 — JWT Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://datatracker.ietf.org/doc/html/rfc7523)

---

[← 08 · Delegation & impersonation](README.md) · [Map](../../README.md)
