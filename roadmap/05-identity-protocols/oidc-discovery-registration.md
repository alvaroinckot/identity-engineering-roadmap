# OIDC Discovery & registration

**TL;DR:** Discovery and dynamic registration let a relying party connect to an OpenID provider
that was not manually configured. With Discovery, the client fetches a JSON document by HTTP
GET from the issuer plus `/.well-known/openid-configuration`. The document advertises the
provider's available endpoints, signing-key URI, supported response types, subject types and
algorithms; optional capabilities can be absent. With Dynamic Client Registration, the client
POSTs metadata including `redirect_uris` to the registration endpoint and receives a
`client_id`, sometimes with a secret. The provider may require an initial access token. An
agent connecting to a new provider can use these two mechanisms when the provider supports
them.

OpenID Connect Discovery 1.0 lets a Relying Party learn a provider's endpoints, supported
scopes, response types, signing algorithms and JWKS URI from one JSON document at
`/.well-known/openid-configuration` (§4) and, given only a user identifier such as an e-mail
address, find the provider itself through WebFinger (§2). OpenID Connect Dynamic Client
Registration 1.0 defines the Client Registration Endpoint (§3) through which a client obtains
a `client_id` at runtime. They are the OpenID Connect counterparts of RFC 8414 and RFC 7591
(→ [Client registration & discovery](client-registration-discovery.md)), and they are what
lets an agent meet an identity provider it has never seen before.

## Resources

- [@official@OpenID Connect Discovery 1.0 §4 — Provider Configuration](https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderConfig)
- [@official@OpenID Connect Discovery 1.0 §2 — Issuer Discovery (WebFinger)](https://openid.net/specs/openid-connect-discovery-1_0.html#IssuerDiscovery)
- [@official@OpenID Connect Dynamic Client Registration 1.0 §3 — Client Registration Endpoint](https://openid.net/specs/openid-connect-registration-1_0.html#ClientRegistration)

---

[← OpenID Connect](openid-connect.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
