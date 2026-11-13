# Workload credentials: WIT & WIC

**TL;DR:** WIMSE defines two credentials that bind a workload identifier to a key. The
Workload Identity Token (WIT) is a signed JWT for the application layer. Its `sub` claim is
the workload identifier, and its `cnf` claim holds the workload's public key. The Workload
Identity Certificate (WIC) is an X.509 certificate for the transport layer. It carries the
identifier in exactly one URI subject alternative name. A WIT is useless on its own: the
draft forbids using it as a bearer token. A workload must also prove on each request that it
holds the matching private key. That is why a stolen WIT, copied from a log line, does not
let the thief call the payments service.

The credentials draft (draft-ietf-wimse-workload-creds) defines the WIT in Section 5.1: a JWS
signed JWT with `sub`, `exp` and a mandatory `cnf` containing a `jwk`, with `iss` recommended
and `jti` optional. It travels in an HTTP header named `Workload-Identity-Token`, not in
Authorization. The WIC is in Section 6.1. Each credential carries one workload identity
(Section 4). The draft names three ways to prove possession, each its own document: mutual
TLS for the WIC, and the Workload Proof Token or HTTP Message Signatures for the WIT (→
[Workload-to-workload
authentication](wimse-workload-to-workload-authentication.md)). For agents, proof of
possession is the point: a prompt-injected agent that leaks its WIT has not leaked a usable
credential, as long as the key stays outside the model's reach (→ [AIMS](wimse-aims.md)). The
draft is a working-group document, revision -03 as of October 2026.

## Resources

- [@official@IETF draft — WIMSE Workload Credentials (draft-ietf-wimse-workload-creds-03), Section 5.1](https://datatracker.ietf.org/doc/html/draft-ietf-wimse-workload-creds-03#section-5.1)
- [@official@IETF draft — WIMSE Workload Credentials, Section 6.1: the Workload Identity Certificate](https://datatracker.ietf.org/doc/html/draft-ietf-wimse-workload-creds-03#section-6.1)

---

[← WIMSE](wimse.md) · [07 · Workload & agent identity](README.md) · [Map](../../README.md)
