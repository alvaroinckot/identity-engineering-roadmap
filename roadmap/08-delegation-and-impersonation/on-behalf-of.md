# On-behalf-of

**TL;DR:** On-behalf-of is Microsoft Entra's flow for a middle-tier API that must call a
downstream API as the user who called it. Without it the middle tier forwards a token meant for
itself or calls as itself and loses who the user was. The middle tier posts the access token it
received to the token endpoint as the `assertion` of a JWT bearer grant with
`requested_token_use=on_behalf_of`, and receives a token for the downstream API that still
identifies the user as subject. The incoming token's audience must be the middle-tier
application, and the flow works only for user principals; a service calling as itself uses
client credentials instead. The issued token holds the user's delegated scopes and never the
application's roles.

A middle-tier service exchanging the user's incoming token for a token to call a downstream
API on behalf of that user, with delegated scopes. Entra's flow is its own, not RFC 8693
token exchange: the request uses RFC 7523's jwt-bearer grant-type URN with
`requested_token_use=on_behalf_of` and the incoming token as the `assertion`.

## Resources

- [@official@Microsoft identity platform — On-Behalf-Of flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow)
- [@official@RFC 7523 — JWT Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://datatracker.ietf.org/doc/html/rfc7523)

---

[← 08 · Delegation & impersonation](README.md) · [Map](../../README.md)
