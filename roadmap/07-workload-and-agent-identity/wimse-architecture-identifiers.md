# WIMSE architecture & workload identifiers

**TL;DR:** The WIMSE architecture draft supplies the vocabulary the other WIMSE documents
build on. A trust domain is a group of systems under one set of security controls and
policies, such as one company's production cloud. A workload identifier names one workload
inside a trust domain, and an identity credential carries that identifier. The identifier
draft makes the identifier a URI whose authority part is the trust domain. It defines a
`wimse://` scheme for this, as in wimse://prod.corp.example/service/payment, and also allows
other schemes such as `spiffe://`. An identifier counts as authenticated only when it arrives
in a credential whose signature has been checked. A name in a header or a request body proves
nothing.

The architecture (draft-ietf-wimse-arch) defines a workload as "an independently addressable
and executable software entity" (Section 2), a slightly different wording from the charter.
Its three building blocks are trust domain, workload identifier and identity credentials
(Section 3.1). It also covers how security context travels along a call chain (Section
3.2.2): a bearer access token from the outside caller is not usually forwarded between
internal workloads, because it was meant for external access (→ [Call chains: transaction
tokens & identity
chaining](../08-delegation-and-impersonation/call-chains-transaction-tokens-identity-chaining.md)).
The identifier draft (draft-ietf-wimse-identifier) requires an absolute URI with a non-empty
authority naming the trust domain and a non-empty path (Section 4.1). Consumers compare and
authorize identifiers as whole URIs after normalization, not by prefix (Section 4.3). SPIFFE
IDs conform to the format but are one scheme among several, not a requirement. Both
documents are working-group drafts.

## Resources

- [@official@IETF draft — WIMSE Architecture (draft-ietf-wimse-arch-08), Section 3.1](https://datatracker.ietf.org/doc/html/draft-ietf-wimse-arch-08#section-3.1)
- [@official@IETF draft — Workload Identifier (draft-ietf-wimse-identifier-04), Section 4](https://datatracker.ietf.org/doc/html/draft-ietf-wimse-identifier-04#section-4)
- [@official@SPIFFE — SPIFFE ID specification](https://github.com/spiffe/spiffe/blob/main/standards/SPIFFE-ID.md)

---

[← WIMSE](wimse.md) · [07 · Workload & agent identity](README.md) · [Map](../../README.md)
