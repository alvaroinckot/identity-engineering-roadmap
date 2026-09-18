# Dynamic client registration: RFC 7591

**TL;DR:** Dynamic client registration lets a client register itself with an authorization
server over HTTPS instead of waiting for a person to complete a form. It is one runtime route
to a `client_id`; Client ID Metadata Documents and OpenID Federation provide other models. The
client POSTs JSON metadata such as redirect URIs, grant types and its token-endpoint
authentication method. The server may reject or replace values and returns a `client_id`,
sometimes with a secret. Registration can be open or require an initial access token. The MCP
authorization specification deprecates this mode for new deployments in favor of Client ID
Metadata Documents.

RFC 7591 defines a Client Registration Endpoint: the client POSTs its metadata (redirect
URIs, grant types, token endpoint authentication method, name, …) and receives a `client_id`
and, where the server issues one, a secret (§3). The endpoint may be an OAuth-protected
resource gated by an initial access token, or the server may allow open registration (§3).
The server assigns the client identifier and MAY issue the same `client_id` to multiple
instances of one client (§3.2.1), and it has to decide whether it accepts registrations from
anyone at all; the MCP authorization spec now marks Dynamic Client Registration deprecated
in favor of Client ID Metadata Documents (→ [MCP
authorization](../07-workload-and-agent-identity/mcp-authorization.md)).

## Resources

- [@official@RFC 7591 §3 — Client Registration Endpoint](https://datatracker.ietf.org/doc/html/rfc7591#section-3)

---

[← Client registration & discovery](client-registration-discovery.md) · [OAuth 2.x](oauth-2x.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
