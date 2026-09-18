# OAuth 2.0 roles & grants

**TL;DR:** OAuth 2.0 names four roles and defines grants, the ways a client obtains an access
token. The resource owner controls the resource and is often a user; the client requests
access, the authorization server issues tokens, and the resource server accepts them. In the
authorization code grant, the resource owner approves through a browser and the client
exchanges a code for tokens. Client credentials is for a confidential client acting for itself,
while the device grant supports clients without a suitable browser. Bearer access tokens
commonly travel in the Authorization header, but sender-constrained tokens also exist. Current
guidance rejects the password grant and advises against the implicit grant.

Resource owner, client, authorization server, resource server. Authorization code, client
credentials, device authorization; bearer token usage; what died (implicit, resource owner
password credentials) and why. JWT-formatted access tokens and Rich Authorization Requests
are the extensions agents lean on.

## Resources

- [@official@RFC 6749 — The OAuth 2.0 Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749)
- [@official@RFC 6750 — Bearer Token Usage](https://datatracker.ietf.org/doc/html/rfc6750)
- [@official@RFC 8628 — Device Authorization Grant](https://datatracker.ietf.org/doc/html/rfc8628)
- [@official@RFC 9068 — JWT Profile for OAuth 2.0 Access Tokens](https://datatracker.ietf.org/doc/html/rfc9068)
- [@official@RFC 9396 — Rich Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9396)

---

[← OAuth 2.x](oauth-2x.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
