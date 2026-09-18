# DPoP: RFC 9449

**TL;DR:** DPoP binds an access token to a key pair the client holds, so a copied token is
unusable without the private key. It operates at the HTTP layer and suits browser or installed
clients that cannot present a client certificate. The client signs a per-request proof JWT
containing the HTTP method, request URI, timestamp and unique identifier. The authorization
server binds the token to that public key. A JWT access token carries the binding as `cnf` and
`jkt`; an opaque token exposes it through introspection. The resource server verifies the proof
and binding, and the token travels as `Authorization: DPoP`. DPoP still requires HTTPS.

Demonstrating Proof of Possession at the application layer: the client holds a key pair and
sends a DPoP proof JWT, signed with the private key and carrying the HTTP method (`htm`),
URI (`htu`), a timestamp and a unique `jti`, on the token request and on every resource
request; the authorization server binds the token to the public key's thumbprint in its
`cnf` claim (`jkt`). The resource server checks that the proof's key matches the token's
binding, so a token lifted from a log or a proxy cannot be replayed without the key. It
needs no TLS client certificates: RFC 9449 §1 offers it for cases where transport-layer
binding such as RFC 8705 is "not available or desirable", naming single-page applications in
a browser and applications installed on a user's device.

## Resources

- [@official@RFC 9449 — Demonstrating Proof of Possession (DPoP)](https://datatracker.ietf.org/doc/html/rfc9449)

---

[← Sender-constrained tokens](sender-constrained-tokens.md) · [OAuth 2.x](oauth-2x.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
