# Manual registration

**TL;DR:** Manual registration is a person creating the client's record at the authorization
server, typically through an HTML form in a developer portal. The record includes allowed
redirect URIs, client type and authentication method. The developer receives a `client_id` and,
when the server uses shared-secret authentication, a `client_secret` to protect in
configuration. Other confidential clients use certificates or asymmetric keys instead. The
`client_id` is public and must never stand alone as client authentication. Manual registration
does not scale to a client that first encounters an authorization server at runtime, which
motivates dynamic registration and Client ID Metadata Documents.

RFC 6749 §2 puts registration out of scope: before it can take part, a client registers with
the authorization server, "typically" through a person filling in an HTML form, and comes
away with a `client_id` (§2.2), credentials if it is a confidential client (§2.3), its
redirect URIs and its client type (§2.1). Every other registration mode is an alternative to
this form. It does not scale to a client, agent or otherwise, that first encounters an
authorization server at runtime; such a client may use one of the two modes beside it (RFC
7591 §1; CIMD §1).

## Resources

- [@official@RFC 6749 §2 — Client Registration](https://datatracker.ietf.org/doc/html/rfc6749#section-2)

---

[← Client registration & discovery](client-registration-discovery.md) · [OAuth 2.x](oauth-2x.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
