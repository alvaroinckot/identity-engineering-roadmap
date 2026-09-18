# A2A

**TL;DR:** A2A, the Agent2Agent protocol, is for one agent handing a task to another agent over
HTTP, where MCP covers an agent calling a tool. It adds no identity mechanism of its own. The
serving agent publishes an Agent Card, a JSON document; when it requires authentication the
card's `securitySchemes` field lists the standard schemes it accepts: API key, HTTP
authentication, OAuth 2, OpenID Connect, or mutual TLS. The calling agent obtains a credential
through that scheme outside A2A and sends it in the usual HTTP headers on every request, and
the server must authenticate every request. A task can pause to ask for more authorization, but
A2A does not define what that credential is or how it is revoked.

Agent2Agent covers agent↔agent, where the peer is another agent rather than a tool: an agent
publishes what it can do in an Agent Card, which, when authentication is required,
advertises the standard web security schemes it accepts; callers authenticate with ordinary
HTTP credentials rather than a new identity layer, and identity stays outside A2A's task
semantics.

## Resources

- [@official@A2A — Agent2Agent Protocol](https://a2a-protocol.org/)

---

[← Agent protocols](agent-protocols-mcp-auth-aauth-a2a.md) · [07 · Workload & agent identity](README.md) · [Map](../../README.md)
