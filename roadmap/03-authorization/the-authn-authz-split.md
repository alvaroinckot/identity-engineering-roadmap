# The authn/authz split

**TL;DR:** Authentication and authorization answer different questions. Authentication verifies
a claim about an entity, such as proof that a caller controls a registered password or signing
key. Authorization decides whether an entity may perform a particular action on a particular
resource; it can also permit access to a public resource without authentication. A recurring
failure is treating a valid ID token as permission to read any customer record. The token is
evidence about an authentication event, but its validity alone does not authorize that
operation. After login middleware finishes, each request handler still needs the applicable
authorization check.

Authentication answers "who is this?", authorization "what may they do?". Conflating them
(treating a valid ID token as permission, for example) is a recurring design failure.

## Resources

- [@official@RFC 4949 — Internet Security Glossary v2](https://datatracker.ietf.org/doc/html/rfc4949) (definitions)

---

[← 03 · Authorization](README.md) · [Map](../../README.md)
