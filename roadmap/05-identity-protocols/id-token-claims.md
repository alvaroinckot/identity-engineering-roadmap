# ID token & claims

**TL;DR:** The ID token is the JWT an OpenID provider signs to say it authenticated a user for
a specific relying party. Its required claims are `iss`, `sub`, `aud`, `iat` and `exp`. The
client checks the expected issuer, its own audience, the signature and expiration; if it sent a
`nonce`, it must also check the matching claim. An ID token is not an access token: it
identifies an authentication event and grants no API access. Only `iss` plus `sub` identify the
user stably, while email and other claims can change or be reused.

Core §2 defines the ID Token: a JWT the OpenID Provider signs to assert that it
authenticated an End-User, with `iss`, `sub`, `aud`, `exp` and `iat` required and `nonce`,
`auth_time`, `acr`, `amr` and `azp` where the flow needs them. §3.1.3.7 lists the validation
steps a Relying Party must run (issuer, audience, signature, expiry, nonce) before trusting
any of it. Its `aud` must contain the Relying Party's own `client_id` and may name other
audiences too (§2); it is issued for the RP and is not an access token: it tells the client
who logged in, authorization is the access token's job. An agent acting for a person learns
"which person" from `iss` + `sub` in this token (§5.7), the only claims the spec lets it
rely on as a stable identifier.

## Resources

- [@official@OpenID Connect Core 1.0 §2 — ID Token](https://openid.net/specs/openid-connect-core-1_0.html#IDToken)
- [@official@OpenID Connect Core 1.0 §3.1.3.7 — ID Token Validation](https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation)

---

[← OpenID Connect](openid-connect.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
