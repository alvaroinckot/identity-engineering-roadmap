# Step-up authentication: RFC 9470

**TL;DR:** Step-up authentication lets an API demand a stronger or more recent login for one
request instead of the whole session. Without it a resource server has no standard way to tell
the client that this wire transfer needs more than the password-only login behind the token.
The resource server answers 401 with a WWW-Authenticate challenge carrying
error="insufficient_user_authentication" plus, optionally, acr_values, the authentication
context it wants, or max_age, how recent the login must be in seconds. The client should repeat
those parameters in a new authorization request; a conforming authorization server puts the
resulting acr and auth_time claims into the new access token, and the client can retry. An acr
value is a deployment-defined label, not a ranking, and OAuth is still not an authentication
protocol.

A resource server that decides the user authentication behind an access token is too weak or too old for this request can reject it with a `401` whose `WWW-Authenticate` challenge carries `error="insufficient_user_authentication"` and, optionally, `acr_values` (the authentication context it wants) and/or `max_age` (how recent the login must be, in seconds); the client SHOULD carry those values into a new authorization request, and a conforming authorization server conveys the resulting `acr` and `auth_time` in the access token so the client can retry. This lets an API evaluate a token's authentication context and recency for a particular call instead of for a whole session; an `acr` value is a label the deployment defines, not inherently a NIST AAL. RFC 9470 is explicit that "authentication level" is a metaphor with no interoperable hierarchy and that OAuth is still not an authentication protocol.

## Resources

- [@official@RFC 9470 — OAuth 2.0 Step Up Authentication Challenge Protocol, §3 Authentication Requirements Challenge](https://datatracker.ietf.org/doc/html/rfc9470#section-3)
- [@official@RFC 9470 §6 Authentication Information Conveyed via Access Token](https://datatracker.ietf.org/doc/html/rfc9470#section-6)

---

[← Multi-factor](multi-factor.md) · [02 · Authentication](README.md) · [Map](../../README.md)
