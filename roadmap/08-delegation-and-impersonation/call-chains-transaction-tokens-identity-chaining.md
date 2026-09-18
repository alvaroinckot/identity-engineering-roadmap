# Call chains: transaction tokens & identity chaining

**TL;DR:** Two Internet-Drafts address context loss in long service call chains. Inside one
trust domain, a workload requests a short-lived signed transaction-token JWT through token
exchange. It identifies the transaction principal and requesting workload and can carry
narrowly defined purpose and authorization context for later workloads to verify. Across trust
domains, identity chaining has a client obtain a JWT authorization grant addressed to the other
domain's authorization server and present it there as a JWT bearer grant. That server validates
the grant under an established trust relationship and its own policy. A transaction token is
not an access token and must stay within its trust domain.

Carrying the original subject and purpose through many hops inside a trust domain
(transaction tokens) and across trust domains (identity chaining). For agent designs, we
infer these mechanisms are relevant to deep or cross-domain call chains; neither draft
mentions agents.

## Resources

- [@official@IETF draft — Transaction Tokens](https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens/)
- [@official@IETF draft — OAuth Identity and Authorization Chaining Across Domains](https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-chaining/)

---

[← 08 · Delegation & impersonation](README.md) · [Map](../../README.md)
