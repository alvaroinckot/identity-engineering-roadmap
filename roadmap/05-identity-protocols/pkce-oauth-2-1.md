# PKCE & OAuth 2.1

**TL;DR:** PKCE extends the authorization code grant so a stolen code is unusable on its own. A
mobile application can lose a code when another application claims the same redirect URI. The
client creates a random verifier, sends its S256 hash as `code_challenge`, and sends the
verifier to the token endpoint. The authorization server hashes it and rejects a mismatch. Use
S256 because `plain` exposes the verifier to anyone able to read the authorization request.
OAuth 2.1 remains an Internet-Draft; it incorporates PKCE into the code grant and omits the
implicit and resource owner password credentials grants.

Proof Key for Code Exchange (RFC 7636) closed the authorization-code interception hole for
public clients. The OAuth 2.1 Internet-Draft consolidates RFC 6749, RFC 6750, PKCE and the
security BCP into one document and omits the implicit and resource owner password
credentials grants (§10).

## Resources

- [@official@RFC 7636 — PKCE](https://datatracker.ietf.org/doc/html/rfc7636)
- [@official@OAuth 2.1](https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/) (draft-ietf-oauth-v2-1)

---

[← OAuth 2.x](oauth-2x.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
