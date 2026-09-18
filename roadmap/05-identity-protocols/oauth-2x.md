# OAuth 2.x

**TL;DR:** OAuth 2.x lets an application call an HTTP API on a user's behalf with limited
access and without holding the user's password. Without it, an app that wants a user's calendar
asks for the password and gets every right the user has. The user, the resource owner, approves
the request at an authorization server. The client receives an access token and presents it to
the resource server in the Authorization header. A refresh token lets the client get new access
tokens later without the user. OAuth 2.1, still an Internet-Draft, folds RFC 6749, PKCE and the
OAuth Security BCP together and drops the implicit and resource owner password credentials
grants. Agents without a browser use grants built for that and should hold tokens scoped and
audience-restricted to the task.

RFC 6749 §1: a framework that lets a third-party application obtain limited access to an
HTTP service, on behalf of a resource owner or on its own behalf, so the application never
has to hold the owner's password. OAuth 2.0 is the 2012 framework (RFC 6749) plus its
extensions; OAuth 2.1 (still an Internet-Draft) consolidates RFC 6749, RFC 6750, PKCE and
the security BCP into one document and omits the implicit and resource owner password
credentials grants (§10). The sub-topics take it apart. Agents that register at runtime (RFC
7591) or run without a suitable browser (RFC 8628 §1) can use these mechanisms, and should
hold tokens scoped and audience-restricted to the task (RFC 6749 §3.3, RFC 9700 §2.3).

## Resources

- [@official@RFC 6749 — The OAuth 2.0 Authorization Framework](https://datatracker.ietf.org/doc/html/rfc6749)
- [@official@OAuth 2.1](https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/) (draft-ietf-oauth-v2-1)

---

[← 05 · Identity protocols](README.md) · [Map](../../README.md)
