# Cross-app access: XAA

**TL;DR:** Cross App Access (XAA) is the informal name for ID-JAG, the Identity Assertion JWT
Authorization Grant, an OAuth working-group draft. It lets one enterprise application, or an
AI agent inside it, call another application's API on a signed-in user's behalf, with the
company's identity provider in the middle. In the direct OAuth pattern it replaces, each user
connects the two apps themselves, and the identity provider neither sees nor controls that
connection. With XAA, the requesting app hands the user's ID token or SAML assertion to the
identity provider. If administrator policy allows, the identity provider returns an ID-JAG,
and the app trades that at the other app's authorization server for a scoped access token
without another consent screen. As of November 2026 it is still a draft, but it ships: Okta
made it generally available, and MCP adopted it as a stable extension.

The draft (draft-ietf-oauth-identity-assertion-authz-grant, revision -06, 31 October 2026, a
WG Document in the OAuth working group with no last call yet) is two existing grants in a
row. The first is RFC 8693 token exchange at the identity provider, with requested token
type `urn:ietf:params:oauth:token-type:id-jag` (Section 4.3). The second is an RFC 7523 JWT
bearer grant at the resource authorization server (Section 4.4). The ID-JAG is a JWT with
`typ` `oauth-id-jag+jwt`. Its `aud` is the resource authorization server and its
`client_id` is the client registered there. It can carry `resource`, `scope`,
`authorization_details`, `act` and `tenant` (Section 3.1). A SAML 2.0 assertion works as the
subject token. The resource side should not issue refresh tokens: the client resubmits the
ID-JAG, or gets a fresh one, instead (Section 4.4.4). Revision -05 added mTLS alongside DPoP
for sender-constraining the ID-JAG, and specified how the resource server finds the signing
keys. Appendix A.4 walks through an AI agent calling an external tool. The MCP profile of
this flow is [MCP Enterprise-Managed
Authorization](mcp-enterprise-managed-authorization.md). Okta shipped it as Agent SSO,
generally available on 24 August 2026 and included in core Okta SSO. Okta maintains xaa.dev,
a sandbox that now also runs the SAML flow. The same grant shape, for agents acting on their
own behalf with no user, is the [Workload Authorization
Grant](workload-authorization-grant-wag.md).

## Resources

- [@official@IETF draft — Identity Assertion JWT Authorization Grant (draft-ietf-oauth-identity-assertion-authz-grant-06)](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-identity-assertion-authz-grant-06)
- [@official@IETF datatracker — ID-JAG status and revision history](https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/)
- [@official@Cross App Access (XAA) — sandbox and docs](https://xaa.dev/)
- [@official@Okta Developer — Cross App Access (XAA)](https://developer.okta.com/docs/concepts/xaa/)
- [@official@Okta — Okta brings first-class identity to AI agents with Agent SSO (GA, 24 August 2026)](https://www.okta.com/newsroom/press-releases/okta-brings-first-class-identity-to-ai-agents-with-agent-sso/)
- [@official@RFC 8693 — OAuth 2.0 Token Exchange](https://datatracker.ietf.org/doc/html/rfc8693)
- [@official@RFC 7523 — JWT Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://datatracker.ietf.org/doc/html/rfc7523)

---

[← 07 · Workload & agent identity](README.md) · [Map](../../README.md)
