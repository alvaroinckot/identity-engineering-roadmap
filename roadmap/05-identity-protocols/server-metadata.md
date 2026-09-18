# Server metadata: RFC 8414 & RFC 9728

**TL;DR:** Server metadata uses two JSON documents, one for an authorization server and one for
a protected resource. The authorization server publishes its `issuer` and supported endpoints
at `/.well-known/oauth-authorization-server` and can advertise a `jwks_uri`. The client must
reject metadata whose `issuer` does not match the expected URL. A protected resource publishes
its identifier at `/.well-known/oauth-protected-resource` and can list acceptable authorization
servers. It can advertise that document from a 401 response using `WWW-Authenticate`. When
those optional links are present, a client can discover the authorization server and begin a
flow without prior configuration, while requesting an audience-restricted token.

RFC 8414 has the authorization server publish a JSON document at `/.well-known/oauth-authorization-server`, inserted into its issuer identifier, which requires `issuer` and the supported response types, includes `authorization_endpoint` and `token_endpoint` when the server has them, and can advertise `jwks_uri`, supported scopes and client-authentication methods; the client MUST discard the document if its `issuer` does not match the URL it was fetched from (§3.3), which is the defence against mix-up. RFC 9728 does the same for a protected resource: a document at `/.well-known/oauth-protected-resource` whose `resource` member is the resource's own identifier and whose optional `authorization_servers` array lists the issuers that can mint tokens for it, and which the resource MAY advertise from a 401 as `WWW-Authenticate: Bearer resource_metadata="…"` (§5.1). Chained, the two documents automate discovery of a resource's authorization server, after which the client can begin an authorization flow and retry with the token (RFC 9728 §5, Figure 1), so a client can reach a resource server nobody configured it for. The price of that autonomy is RFC 9728 §7.4: such clients SHOULD request audience-restricted tokens (RFC 8707), because a hostile resource server can otherwise steer them into fetching a token it can replay somewhere legitimate.

## Resources

- [@official@RFC 8414 — Authorization Server Metadata](https://datatracker.ietf.org/doc/html/rfc8414#section-3)
- [@official@RFC 9728 — OAuth 2.0 Protected Resource Metadata](https://datatracker.ietf.org/doc/html/rfc9728)

---

[← Client registration & discovery](client-registration-discovery.md) · [OAuth 2.x](oauth-2x.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
