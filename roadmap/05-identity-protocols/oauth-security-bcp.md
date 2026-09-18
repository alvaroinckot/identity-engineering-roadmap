# OAuth Security BCP

**TL;DR:** The OAuth Security BCP is the current catalog of attacks on OAuth 2.0 deployments
and the countermeasures clients, authorization servers and resource servers are expected to
apply. It exists because the base framework left choices open that proved exploitable, such as
loose redirect URI matching and clients that talk to several authorization servers and can be
steered to the wrong one. It requires PKCE for public clients and on every authorization
server, and exact redirect URI matching; clients must defend against mix-up by tracking which
issuer each request went to. Clients should not use the implicit grant and must not use the
resource owner password credentials grant. Access tokens should be sender-constrained and
audience-restricted to one resource server, which must refuse tokens not meant for it.

The consolidated threat and mitigation catalog: redirect URI matching, mix-up attacks,
token leakage, sender-constraining.

## Resources

- [@official@RFC 9700 — OAuth 2.0 Security Best Current Practice](https://datatracker.ietf.org/doc/html/rfc9700)

---

[← OAuth 2.x](oauth-2x.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
