# WIMSE

**TL;DR:** WIMSE is the IETF working group standardizing workload identity mechanisms across
systems and trust domains over HTTP. A browser request may pass through an orders service that
calls a payments service in another cloud, and each hop needs the calling workload and
original-caller context. The charter defines a workload as a running software instance
executing for a specific purpose. Its program includes an architecture, a JOSE-based token for
chains of REST calls, local token issuance, and token exchange at trust boundaries. WIMSE
coordinates with CNCF, particularly the SPIFFE/SPIRE project, but the charter does not make
SPIFFE a dependency. Its current outputs are working-group drafts, not RFCs.

The IETF Workload Identity in Multi System Environments working group is chartered to
develop HTTP/REST workload-identity work: how a workload proves who it is across systems and
trust domains, identity credential formats, service-to-service protection, and how the
original caller's context is carried or exchanged along a chain of workload-to-workload
calls (token exchange, possibly RFC 8693). Its documents are working-group drafts, not yet
RFCs.

## Resources

- [@official@IETF WIMSE WG — Workload Identity in Multi System Environments](https://datatracker.ietf.org/wg/wimse/about/)

---

[← 07 · Workload & agent identity](README.md) · [Map](../../README.md)
