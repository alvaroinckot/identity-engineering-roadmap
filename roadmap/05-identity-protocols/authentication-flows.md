# Authentication flows: code, implicit, hybrid

**TL;DR:** OpenID Connect has three ways for a relying party to obtain the ID token, chosen by
`response_type`. In the authorization code flow the browser redirect carries a one-time code,
which the client exchanges at the token endpoint. In the implicit flow the tokens return in the
redirect fragment, where the browser can leak them. The hybrid flow splits tokens across both
endpoints. Every request carries the `openid` scope and can carry a `nonce`, which the client
compares with the ID token to detect replay. Current security guidance favors the code flow
with PKCE.

Core §3 defines three ways to obtain the ID Token, selected by `response_type`: the
Authorization Code Flow (§3.1) returns tokens from the token endpoint, the Implicit Flow
(§3.2) returns them in the redirect itself, and the Hybrid Flow (§3.3) mixes the two. The
authentication request adds `nonce`, which binds the ID Token to the client session, and
`prompt`, `max_age`, `login_hint`, `acr_values` and `id_token_hint` to steer how the
provider authenticates (§3.1.2.1). RFC 9700 §2.1.1–2.1.2 says clients SHOULD NOT use
response types that put an access token in the authorization response unless the leakage is
mitigated, that public clients MUST use PKCE and confidential clients are RECOMMENDED to,
which in practice retires the implicit flow as OAuth used it; the code flow with PKCE (→
[PKCE & OAuth 2.1](pkce-oauth-2-1.md)) is the safe default.

## Resources

- [@official@OpenID Connect Core 1.0 §3 — Authentication](https://openid.net/specs/openid-connect-core-1_0.html#Authentication)
- [@official@RFC 9700 §2.1.2 — Implicit Grant](https://datatracker.ietf.org/doc/html/rfc9700#section-2.1.2)

---

[← OpenID Connect](openid-connect.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
