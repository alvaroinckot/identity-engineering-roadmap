# mTLS-bound tokens: RFC 8705

**TL;DR:** An mTLS-bound token is tied to the X.509 certificate presented by the client, so a
copied token is unusable without the certificate's private key. RFC 8705 separately defines
certificate-based client authentication and certificate-bound tokens. For a JWT access token,
the authorization server represents the certificate thumbprint in `cnf` as `x5t#S256`; for an
opaque token, introspection returns the same binding. The resource server obtains the
certificate from TLS, compares its thumbprint with the binding, and rejects a mismatch. If TLS
terminates at a proxy, securely forwarding the certificate metadata is an implementation
responsibility outside the specification.

RFC 8705 does two things with the client's X.509 certificate on a mutual-TLS connection. It
authenticates the client to the token endpoint, with `tls_client_auth` for PKI-issued and
`self_signed_tls_client_auth` for self-signed certificates (§2), and it binds the issued
access and refresh tokens to that certificate through the `cnf` claim's `x5t#S256`
thumbprint (§3), so a resource server accepts the token only over a TLS connection
presenting the same certificate. The binding lives in the transport layer: nothing extra per
request, at the price that the client certificate has to reach the server that checks it.

## Resources

- [@official@RFC 8705 — OAuth 2.0 Mutual-TLS Client Authentication and Certificate-Bound Access Tokens](https://datatracker.ietf.org/doc/html/rfc8705)

---

[← Sender-constrained tokens](sender-constrained-tokens.md) · [OAuth 2.x](oauth-2x.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
