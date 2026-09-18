# FAPI 2.0 security profile

**TL;DR:** FAPI 2.0 is the OpenID Foundation's high-security OAuth 2.0 profile for APIs that
move money or expose sensitive data, formally analyzed against a stated attacker model. It
removes many deployment choices: confidential clients only, code flow with PKCE S256, every
authorization request pushed through PAR, `iss` in the authorization response, and client
authentication by mutual TLS or `private_key_jwt`. Access tokens must be sender-constrained by
mutual TLS or DPoP. Resource servers must verify that binding and refuse tokens in query
parameters. Although written with financial APIs in mind, the profile applies to any API
handling high-value or sensitive data.

The OpenID Foundation's profile of OAuth 2.0 for high-value APIs, "proved by formal analysis to meet the stated attacker model" (§1) and built on RFC 9700, with public clients out of scope because the working group knows no way to secure them to the same degree (§5.1.1). For authorization-endpoint (code) flows it removes the choices that make OAuth deployments differ: `response_type` `code` only, PKCE with S256, every authorization request pushed via PAR with client authentication, `iss` in the authorization response against mix-up, client authentication by MTLS or `private_key_jwt`, authorization codes that live at most 60 seconds (§5.3.2.1–5.3.2.2). Unconstrained bearer access tokens are out: the server "shall only issue sender-constrained access tokens" bound by MTLS (RFC 8705) or DPoP (RFC 9449), and resource servers shall verify the binding and refuse tokens in query parameters (§5.3.4). The spec says it was developed with a focus on financial applications but is meant for any API exposing high-value or sensitive data; when an agent moves money or reads health records, this is the profile to evaluate rather than relying on baseline OAuth alone.

## Resources

- [@official@FAPI 2.0 Security Profile (OpenID Foundation, Final)](https://openid.net/specs/fapi-security-profile-2_0.html)
- [@official@FAPI 2.0 §5.3.2 — Requirements for authorization servers](https://openid.net/specs/fapi-security-profile-2_0.html#section-5.3.2)

---

[← OAuth Security BCP](oauth-security-bcp.md) · [OAuth 2.x](oauth-2x.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
