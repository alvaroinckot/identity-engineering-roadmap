# JWT validation pitfalls & BCP

**TL;DR:** Validating a JWT means checking more than the signature. If the verifier trusts the
token's own alg header, an attacker sets it to none and skips the signature, or switches an RSA
token to HMAC so the public key becomes the HMAC secret. If the verifier skips aud, a token
minted for one service replays against another. So the application pins the algorithms it
accepts, confirms the signing key belongs to the expected issuer, and checks that aud names
itself; RFC 9068 adds a typ of at+jwt and an exact iss match for OAuth access tokens. In OpenID
Connect, an unfamiliar kid prompts a JWK Set refresh, and recently retired signing keys should
remain published during rollover. Header values such as kid and jku are attacker input.

`alg` confusion (`none`, asymmetric/symmetric swap; RFC 8725 §2.1), missing audience checks,
and key rollover handled wrong: on an unfamiliar `kid` a verifier re-fetches the JWK Set,
and the publisher keeps recently decommissioned keys available for a while (OpenID Connect
Core §10.1.1). The BCP and the OAuth access-token profile (→
[05](../05-identity-protocols/oauth-2x.md)) say what a validator must do.

## Resources

- [@official@RFC 8725 — JSON Web Token Best Current Practices](https://datatracker.ietf.org/doc/html/rfc8725)
- [@official@RFC 9068 — JWT Profile for OAuth 2.0 Access Tokens](https://datatracker.ietf.org/doc/html/rfc9068)
- [@official@OpenID Connect Core 1.0 §10.1.1 — Rotation of Asymmetric Signing Keys](https://openid.net/specs/openid-connect-core-1_0.html#RotateSigKeys)

---

[← 04 · Tokens & cryptography](README.md) · [Map](../../README.md)
