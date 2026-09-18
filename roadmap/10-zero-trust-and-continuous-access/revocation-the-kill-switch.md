# Revocation & the kill switch

**TL;DR:** Revocation asks an authorization server to invalidate a token before its scheduled
expiry. In OAuth the client posts the token to the revocation endpoint; revoking a refresh
token should also invalidate access tokens from the same grant when access-token revocation is
supported. A resource server validating a self-contained JWT locally may continue accepting it
unless revocation state reaches that server. RFC 7009 does not standardize the required
authorization-server-to-resource-server interaction, so short access-token lifetimes bound the
delay. CAEP provides another propagation path: a Transmitter sends a session-revoked event to
Receivers, and each Receiver decides what enforcement follows.

OAuth token revocation (RFC 7009) and CAEP events can curtail an agent's future access,
subject to Receiver enforcement and propagation; for self-contained access tokens, immediate
revocation requires interaction between the authorization server and the resource server,
which RFC 7009 §3 does not standardize, and otherwise short lifetimes bound how long an
already-issued token may continue to be accepted.

## Resources

- [@official@RFC 7009 — Token Revocation](https://datatracker.ietf.org/doc/html/rfc7009)
- [@official@OpenID CAEP — Continuous Access Evaluation Profile](https://openid.net/specs/openid-caep-1_0-final.html)

---

[← 10 · Zero trust & continuous access](README.md) · [Map](../../README.md)
