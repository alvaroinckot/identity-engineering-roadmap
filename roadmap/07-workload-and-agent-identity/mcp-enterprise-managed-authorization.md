# MCP Enterprise-Managed Authorization

**TL;DR:** Enterprise-Managed Authorization (EMA) is the Model Context Protocol extension that
puts Cross App Access inside MCP. Without it, every employee connects every MCP server by
hand, clicking through an OAuth consent screen for each one, and the company cannot see or
revoke those connections in one place. With EMA, the user signs in to the MCP client once
through enterprise SSO. When an MCP server needs a token, the client asks the company's
identity provider for an ID-JAG and trades it at the server's authorization server for an
access token. The user is never redirected. The identity provider decides which MCP servers
each user may reach. The extension was declared stable in June 2026.

The extension identifier is `io.modelcontextprotocol/enterprise-managed-authorization`. The
client keeps the identity assertion (ID token or SAML assertion) from SSO and requests an
ID-JAG from the enterprise identity provider. It then presents the ID-JAG at the MCP
authorization server and must not redirect the user to that server's authorization
endpoint. The server validates the ID-JAG's issuer, audience, expiry and signature against
the identity provider's keys. At launch the MCP blog named Okta as the first supported
identity provider, Claude, Claude Code and Cowork as clients, VS Code in preview, and Asana,
Atlassian, Canva, Figma, Granola, Linear and Supabase as servers. The extension page lists
more identity providers and says implementations track different draft revisions of ID-JAG,
so check which revision a vendor targets. EMA decides which MCP servers a user's client may
connect to. Whether a specific tool call with specific arguments is allowed is still the
server's job (→ [Least privilege & audit for agents](least-privilege-audit-for-agents.md)).
It sits on top of the base [MCP authorization](mcp-authorization.md) profile.

## Resources

- [@official@Model Context Protocol — Enterprise-Managed Authorization extension](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization)
- [@official@MCP Blog — Enterprise-Managed Authorization: Zero-touch OAuth for MCP (18 June 2026)](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/)
- [@article@Atlassian — How We Brought Enterprise-Managed Authorization to Rovo MCP with XAA and ID-JAG](https://www.atlassian.com/blog/development/enterprise-managed-authorization-rovo-mcp-xaa-id-jag)

---

[← Cross-app access: XAA](cross-app-access-xaa.md) · [07 · Workload & agent identity](README.md) · [Map](../../README.md)
