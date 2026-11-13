# Workload-to-workload authentication: WPT, HTTP Signatures & mTLS

**TL;DR:** WIMSE offers three ways for one workload to prove to another that it holds the key
behind its credential. With mutual TLS, both sides present Workload Identity Certificates
during the TLS handshake. With the Workload Proof Token (WPT), the caller signs a short JWT
for each request, much as DPoP does for OAuth. The WPT is bound to the request's audience
and to a hash of the WIT. With HTTP Message Signatures, the caller signs the request itself:
method, path, query and the WIT header. The choice depends on the network. TLS that ends at
a load balancer or service-mesh proxy leaves the backend unable to see who connected. The
two application-layer options survive those intermediaries.

All three replaced the original s2s-protocol draft. The HTTP Signatures profile
(draft-ietf-wimse-http-signature) profiles RFC 9421: `@method`, `@path`, `@query` and
`Workload-Identity-Token` must be signed. A `wimse-aud` signature parameter names the
intended recipient, and an optional signed response is defined. Publication as a Proposed
Standard was requested in late October 2026 and it is now in AD evaluation, the furthest any
WIMSE document has got. The WPT
(draft-ietf-wimse-wpt) is a JWT sent in the Authorization header under a new `WPT`
authentication scheme. Its `wth` claim is the SHA-256 hash of the WIT, and `tth` and `oth`
bind other tokens such as a transaction token (Section 2). A request carrying a WPT cannot
also carry a Bearer or Basic credential (Section 2.2). Mutual TLS
(draft-ietf-wimse-mutual-tls) requires exactly one URI subject alternative name carrying the
workload identifier (Section 3.3). It recommends an application-layer mechanism when TLS
terminates at an intermediary (Section 5.3). Agent tool calls often cross gateways and
proxies, which is where the application-layer options earn their place.

## Resources

- [@official@IETF draft — WIMSE Workload-to-Workload Authentication with HTTP Signatures (draft-ietf-wimse-http-signature-08), Section 3](https://datatracker.ietf.org/doc/html/draft-ietf-wimse-http-signature-08#section-3)
- [@official@IETF draft — WIMSE Workload Proof Token (draft-ietf-wimse-wpt-02), Section 2](https://datatracker.ietf.org/doc/html/draft-ietf-wimse-wpt-02#section-2)
- [@official@IETF draft — Workload Authentication Using Mutual TLS (draft-ietf-wimse-mutual-tls-03), Section 3](https://datatracker.ietf.org/doc/html/draft-ietf-wimse-mutual-tls-03#section-3)
- [@official@RFC 9421 — HTTP Message Signatures](https://datatracker.ietf.org/doc/html/rfc9421)

---

[← WIMSE](wimse.md) · [07 · Workload & agent identity](README.md) · [Map](../../README.md)
