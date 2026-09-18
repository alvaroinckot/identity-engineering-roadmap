# Scopes, audience & consent

**TL;DR:** Scope says what access a token carries, audience says which resource server may
accept it, and consent is the resource owner's authorization decision for that client. Without
audience restriction, one resource server can replay a bearer token at another. The client
sends `scope` as space-separated strings defined by the authorization server, which can grant
less and report the result. The `resource` parameter names a target resource by URI, and the
server should audience-restrict the token accordingly; a JWT commonly represents that
restriction in `aud`. Rich Authorization Requests use typed JSON objects when scope strings
cannot express details such as a payment amount.

For an authorization that involves a resource owner, three questions matter before the server mints a token: what access, where it applies, and what decision was obtained. *What* access: the `scope` parameter, RFC 6749 §3.3, "a list of space-delimited, case-sensitive strings" defined by the server, which "MAY fully or partially ignore the scope requested by the client" and MUST then report the scope it actually granted; when a string cannot say it ("transfer 123.50 EUR to Merchant A"), RFC 9396's `authorization_details` carries an array of typed JSON objects instead. *Where* the token may be used: the optional `resource` parameter of RFC 8707, an absolute URI naming the protected resource, which the server SHOULD turn into an audience restriction (`aud`) so a token accepted at one API "cannot then be taken by that resource and presented elsewhere" (§3); and *who agreed*: consent is the resource owner approving that scope for that client at the authorization endpoint, where the server "obtains an authorization decision (by asking the resource owner or by establishing approval via other means)" (RFC 6749 §4.1.1). Agents should request only the scopes they need, and audience restriction is what stops one token, once handed to a tool server, from being replayed at another tool the user connected.

## Resources

- [@official@RFC 6749 §3.3 — Access Token Scope](https://datatracker.ietf.org/doc/html/rfc6749#section-3.3)
- [@official@RFC 8707 — Resource Indicators for OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc8707)
- [@official@RFC 9396 — Rich Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9396)

---

[← OAuth 2.x](oauth-2x.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
