# Bots on the web: Web Bot Auth & Privacy Pass

**TL;DR:** Two mechanisms let an automated client, a crawler or a shopping agent, prove
something to a website without relying on its IP address or User-Agent string, which are easy
to fake. Web Bot Auth, an IETF working-group draft, has the bot sign each request with RFC 9421
HTTP Message Signatures and add a signed Signature-Agent header naming the HTTPS origin where
it publishes its public keys as a JWKS. The site fetches those keys, verifies the signature,
and can allow, rate-limit, or block that URL. Privacy Pass is the anonymous counterpart: a
client passes a check such as a CAPTCHA with an Attester, and an Issuer hands it tokens
unlinkable to that check. The site challenges with WWW-Authenticate: PrivateToken and accepts a
token in the Authorization header.

IP allowlists and `User-Agent` strings are weak identifiers for an automated client acting on a user's behalf: IP ranges change and `User-Agent` values are spoofable. Web Bot Auth (IETF `draft-ietf-webbotauth-httpsig-protocol`, a working-group draft, not an RFC) has the agent sign each request with RFC 9421 HTTP Message Signatures (`created`, `expires`, a JWK-thumbprint `keyid` and `tag="web-bot-auth"`, covering at least `@authority` or `@target-uri`, §5.2) and sign a `Signature-Agent` header that locates its candidate keys, by default a JWKS at that origin's `/.well-known/http-message-signatures-directory` (§5.2.1, §5.5), so the origin ends up with "a key that URL publishes signed this" and can allowlist, rate-limit or block by that URL (§4.1). Privacy Pass is the anonymous counterpart: RFC 9576 separates Client, Attester, Issuer and Origin so that a client which has passed attestation (a CAPTCHA, device attestation) is issued tokens that cannot be linked back to that issuance (§2, §3.1), and RFC 9577 challenges through `WWW-Authenticate` and redeems a typically single-use token through `Authorization: PrivateToken` (§2.1, §2.2). Identified bots, a search crawler or an operator's shopping agent, can publish keys and sign to be recognised, while a client whose user should stay anonymous can redeem Privacy Pass tokens; both are alternatives to relying on IP signals alone.

## Resources

- [@official@RFC 9421 — HTTP Message Signatures](https://datatracker.ietf.org/doc/html/rfc9421)
- [@official@HTTP Message Signatures for automated traffic — draft-ietf-webbotauth-httpsig-protocol (IETF draft)](https://datatracker.ietf.org/doc/draft-ietf-webbotauth-httpsig-protocol/)
- [@official@RFC 9576 — The Privacy Pass Architecture](https://datatracker.ietf.org/doc/html/rfc9576)
- [@official@RFC 9577 — The Privacy Pass HTTP Authentication Scheme](https://datatracker.ietf.org/doc/html/rfc9577)
- [@article@Cloudflare — Forget IPs: using cryptography to verify bot and agent traffic](https://blog.cloudflare.com/web-bot-auth/)

---

[← 07 · Workload & agent identity](README.md) · [Map](../../README.md)
