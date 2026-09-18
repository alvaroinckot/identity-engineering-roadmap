# MCP authorization

**TL;DR:** MCP authorization is the OAuth 2.1 profile that protects the connection between an
MCP client, the program hosting the agent, and a remote MCP tool server. The MCP server is the
OAuth resource server, the MCP client is the OAuth client, and no new token format is defined.
An unauthenticated call gets a 401 whose WWW-Authenticate header points at the server's
protected resource metadata, a JSON document under /.well-known/oauth-protected-resource that
lists the authorization servers issuing tokens for it, as RFC 9728 defines. The client obtains
an access token there and retries. Clients must send the `resource` parameter naming the MCP
server; the server must reject tokens issued for another audience and must not pass them
upstream. The current spec prefers Client ID Metadata Documents over dynamic client
registration.

The Model Context Protocol's authorization spec applies OAuth 2.1 to agent↔tool: a protected
MCP server acts as an OAuth resource server, the MCP client acts as the OAuth client, and
the access token comes from an authorization server the MCP server points the client at (via
RFC 9728 protected resource metadata, → [Server
metadata](../05-identity-protocols/server-metadata.md)). The retrofit model: MCP defines no
new token format; it profiles selected existing OAuth/OIDC mechanisms and maps MCP roles
onto OAuth roles.

## Resources

- [@official@Model Context Protocol — Authorization specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [@official@RFC 9728 — OAuth 2.0 Protected Resource Metadata](https://datatracker.ietf.org/doc/html/rfc9728)

---

[← Agent protocols](agent-protocols-mcp-auth-aauth-a2a.md) · [07 · Workload & agent identity](README.md) · [Map](../../README.md)
