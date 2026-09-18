# Sender-constrained tokens

**TL;DR:** A sender-constrained token is bound to a secret or private key held by its
legitimate client, so the token alone is insufficient. A bearer token instead works for any
party that possesses it. Mutual TLS binds a token to the certificate presented on the TLS
connection, while DPoP binds it to a key proven through a signed request header. The resource
server checks the binding on every call and rejects a request without the matching certificate
or proof. RFC 9700 recommends these mechanisms. They prevent use of a copied token when the
attacker cannot also use the bound private key.

RFC 6750's bearer token is usable by whoever holds it. A sender-constrained token is bound to
something only the legitimate client has, so a stolen token is useless on its own; RFC 9700
§2.2 tells authorization and resource servers to use one of the two standard bindings, taken
apart in the sub-topics: mutual TLS, which binds the token to the client certificate of the
TLS connection (RFC 8705), and DPoP, which binds it to a key the client proves possession of
on every request (RFC 9449). For agents that hold tokens across long sessions and hand them
between processes, binding turns a leaked token from a breach into a nuisance.

## Resources

- [@official@RFC 6750 — Bearer Token Usage](https://datatracker.ietf.org/doc/html/rfc6750) (the flaw being fixed)
- [@official@RFC 9700 §2.2 — Token Replay Prevention](https://datatracker.ietf.org/doc/html/rfc9700#section-2.2)

---

[← OAuth 2.x](oauth-2x.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
