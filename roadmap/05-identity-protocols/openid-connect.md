# OpenID Connect

**TL;DR:** OpenID Connect is an identity layer on OAuth 2.0. A relying party sends the user to
an OpenID provider for authentication and receives an ID token, usually alongside an access
token. The access token authorizes requests to a resource server; the ID token tells the
relying party which End-User authenticated. It is a signed JWT whose `iss`, `sub`, `aud`, `iat`
and `exp` claims identify the provider, user, client and validity period. The relying party
checks the signature, issuer, audience and expiration. An agent acting for a person obtains the
person's stable identifier from `iss` plus `sub`.

An identity layer on top of OAuth 2.0 (Core §1): the Relying Party sends the user to an
OpenID Provider and gets back, next to the access token, an ID Token that says who
authenticated, when and how. Around that core sit discovery and dynamic registration, the
UserInfo endpoint and a family of session and logout specifications. The sub-topics take it
apart. For an agent acting for a person, OIDC is how it learns which person; OAuth decides
what it may touch.

## Resources

- [@official@OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)

---

[← [05 · Identity protocols](README.md) · [Map](../../README.md)
