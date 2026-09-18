# Before OAuth

**TL;DR:** Before OAuth, a printing service that wanted a user's photos from a photo-sharing
site asked for the user's password there, a credential that opened the whole account and could
only be revoked by changing it. OpenID Authentication 2.0 let a person prove control of a URL
identifier to a relying party without handing over a password. The relying party discovered the
OpenID provider from the identifier, redirected the user there, and verified the signature and
nonce on the returned assertion. OAuth 1.0 added a third role, the resource owner, and had the
client sign each API request with a token and shared secret instead of a password. Delegated
authorization and federated authentication, the problems these designs named, are what OAuth
2.x and OpenID Connect solve today.

The password anti-pattern (giving app B your app A password, RFC 6749 §1), OpenID
Authentication 2.0 for federated login, and OAuth 1.0's signed requests (RFC 5849 §3.1,
§3.4). Why delegated authorization and federated authentication happened at all.

## Resources

- [@official@OpenID Authentication 2.0](https://openid.net/specs/openid-authentication-2_0.html)
- [@official@RFC 5849 — The OAuth 1.0 Protocol](https://datatracker.ietf.org/doc/html/rfc5849)

---

[← 05 · Identity protocols](README.md) · [Map](../../README.md)
