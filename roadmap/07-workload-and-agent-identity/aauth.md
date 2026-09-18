# AAuth

**TL;DR:** AAuth is a proposed protocol, an individual Internet-Draft with no working-group
adoption, in which an AI agent signs every HTTP request with its own key instead of presenting
a bearer token. It argues that an OAuth client has no identity of its own, only a `client_id`
that is meaningless at another authorization server. The agent has an identifier of the form
aauth:local@domain bound to a published signing key, and each request carries an RFC 9421 HTTP
Message Signature, so a copied token is useless without the private key. When a user is
involved, a person server confirms the user's identity and consent in an auth token, and an
`act` claim records the chain of delegation.

The agent-native model: the agent is a first-class cryptographic identity that signs each
request (RFC 9421 HTTP Message Signatures, the same primitive as [Web Bot
Auth](bots-on-the-web.md)) instead of bearing a token; in the draft's PS-asserted mode the
person server confirms the user's consent and the `act` claim records upstream delegation,
so delegation is explicit in the protocol. Status matters here: an individual Internet-Draft
(draft-hardt-oauth-aauth-protocol), not adopted by the OAuth working group, so read it as a
proposal being argued, not a standard.

## Resources

- [@official@Internet-Draft — AAuth Protocol](https://datatracker.ietf.org/doc/draft-hardt-oauth-aauth-protocol/) (draft-hardt-oauth-aauth-protocol)
- [@official@RFC 9421 — HTTP Message Signatures](https://datatracker.ietf.org/doc/html/rfc9421)
- [@official@aauth.dev — AAuth explainer](https://www.aauth.dev/)
- [@article@Christian Posta — Deep Dive: AAuth](https://blog.christianposta.com/exploring-aauth-agent-auth-identity-and-access-management-for-ai-agents/)

---

[← Agent protocols](agent-protocols-mcp-auth-aauth-a2a.md) · [07 · Workload & agent identity](README.md) · [Map](../../README.md)
