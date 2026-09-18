# Browser-based apps & the BFF pattern

**TL;DR:** RFC 10017 is the best current practice for OAuth in JavaScript applications that run
in the browser. Its attacker runs code inside the page, which becomes indistinguishable from
the application's own code. The safest pattern is a Backend for Frontend: a confidential
server-side client does not expose OAuth tokens to browser code and proxies API calls for a
cookie-authenticated session. A token-mediating backend instead gives the access token to the
page. A client running entirely in the browser is vulnerable to every attack scenario in the
RFC. Browser clients must use the authorization code grant and must not use the implicit grant.

RFC 10017 (BCP 212, the browser counterpart to RFC 8252) starts from an attacker running JavaScript inside the page and ranks three architectures "in decreasing order of security" (§6): a Backend for Frontend, where a server-side component is the confidential OAuth client, stores the tokens server-side, ties them to a cookie-based browser session and proxies every API call, so "there are no tokens available to extract from the browser" (§6.1); a token-mediating backend, which obtains tokens as a confidential client but hands the access token to the page (§6.2); and a browser-based OAuth client that does everything in JavaScript and "is vulnerable to all attack scenarios" (§6.3). Wherever the page holds a token, localStorage, sessionStorage and IndexedDB differ only in exposure and "none of these options can fully mitigate token exfiltration" (§8.5). Browser-based clients MUST use the authorization code grant and MUST NOT use the implicit grant, and authorization servers MUST issue access tokens only from the token endpoint (§7.2). A browser-hosted agent front end acting as an OAuth client chooses from the same three patterns, plus whatever trust boundaries an extension adds.

## Resources

- [@official@RFC 10017 — OAuth 2.0 for Browser-Based Applications](https://datatracker.ietf.org/doc/html/rfc10017)
- [@official@RFC 10017 §6 — Application Architecture Patterns](https://datatracker.ietf.org/doc/html/rfc10017#section-6)

---

[← OAuth Security BCP](oauth-security-bcp.md) · [OAuth 2.x](oauth-2x.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
