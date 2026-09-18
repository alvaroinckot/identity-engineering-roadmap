# Agent protocols

**TL;DR:** Agent protocols define how an AI agent authenticates when it calls a tool server or
another agent, and each protocol picks a different identity model. MCP reuses OAuth 2.1: a
protected MCP server is the OAuth resource server, the MCP client is the OAuth client, and the
client presents an access token from an authorization server the server points it at. AAuth, an
individual Internet-Draft and not a standard, gives the agent its own identifier and signing
key, signs every HTTP request instead of sending a bearer token, and carries the user's
delegation inside the protocol. A2A covers one agent calling another: the called agent
publishes an Agent Card listing the standard HTTP authentication schemes it accepts and adds no
identity layer of its own.

MCP and the proposed AAuth illustrate contrasting authorization models for agent access.
*Retrofit OAuth:* MCP applies selected OAuth 2.1 mechanisms to protected MCP
client-to-server access, with the MCP client as the OAuth client. *Agent-native:* AAuth
makes the agent a first-class cryptographic identity, signs requests instead of bearing
tokens, and makes delegation explicit. A2A covers agent↔agent.

## Resources

- [@official@Model Context Protocol — Authorization specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [@official@Internet-Draft — AAuth Protocol](https://datatracker.ietf.org/doc/draft-hardt-oauth-aauth-protocol/) (draft-hardt-oauth-aauth-protocol)
- [@official@aauth.dev — AAuth explainer](https://www.aauth.dev/)
- [@article@Christian Posta — Deep Dive: AAuth](https://blog.christianposta.com/exploring-aauth-agent-auth-identity-and-access-management-for-ai-agents/)
- [@official@A2A — Agent2Agent Protocol](https://a2a-protocol.org/)

---

[← 07 · Workload & agent identity](README.md) · [Map](../../README.md)
