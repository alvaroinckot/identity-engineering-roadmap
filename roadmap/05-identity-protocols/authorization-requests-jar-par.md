# Authorization requests: JAR & PAR

**TL;DR:** JAR and PAR protect the authorization request on its way through the browser. The
plain request is a query string in a redirect: it leaks into logs and referrers, and an
attacker on the path can change the scope or swap a payment. With JAR the client packs every
parameter into a signed JWT, the Request Object, sent in `request` or by reference in
`request_uri`, and the authorization server reads only what is inside. With PAR the client
POSTs the request directly to the pushed authorization request endpoint, authenticating as at
the token endpoint, and gets a short-lived `request_uri` for the authorization endpoint. The
server can then refuse a bad client before the user sees anything. A server can require PAR in
its metadata, and FAPI 2.0 does.

The authorization request of RFC 6749 travels through the user agent as a query string, so RFC 9126 §1 lists what goes wrong: "There is no cryptographic integrity and authenticity protection", an attacker "could, for example, modify the scope of access requested or swap the context of a payment transaction by changing scope values", the parameters leak "to web server logs and to other sites via the referrer", and fine-grained requests make URLs "quite large". RFC 9101 (JAR) answers integrity: the client wraps every parameter in a Request Object, a JWT that is JWS-signed or signed-then-encrypted, passed by value in `request` or by reference in `request_uri`, and the authorization server "MUST only use the parameters included in the Request Object" (§5). RFC 9126 (PAR) answers the channel: the client POSTs the request directly to the `pushed_authorization_request_endpoint`, authenticating as it would at the token endpoint (§2), and gets back a short-lived, client-bound `request_uri` (which MAY take the form `urn:ietf:params:oauth:request_uri:<reference-value>`, §2.2) to hand to the authorization endpoint, so the server can authenticate the client and refuse an illegitimate request "before any user interaction happens" (§1); a server may declare PAR the only accepted path with `require_pushed_authorization_requests` (server metadata §5, client metadata §6), and FAPI 2.0 does exactly that (§5.3.2.2). RFC 9396 closes the loop: when the integrity of `authorization_details` matters, "clients MUST protect authorization_details against tampering and swapping" by signing (JAR) or pushing (PAR) the request (§12).

## Resources

- [@official@RFC 9101 — JWT-Secured Authorization Request (JAR)](https://datatracker.ietf.org/doc/html/rfc9101)
- [@official@RFC 9126 — Pushed Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9126)
- [@official@RFC 9396 — Rich Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9396)
- [@official@FAPI 2.0 Security Profile (OpenID Foundation, Final)](https://openid.net/specs/fapi-security-profile-2_0.html)

---

[← OAuth 2.x](oauth-2x.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
