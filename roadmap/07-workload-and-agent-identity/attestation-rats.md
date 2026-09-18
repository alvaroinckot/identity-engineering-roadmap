# Attestation: RATS

**TL;DR:** Attestation is how a running system proves what it is instead of only proving that
it holds a key. RFC 9334 names the roles: the Attester produces Evidence about itself, the
Verifier appraises that Evidence against a policy and returns an Attestation Result, and the
Relying Party acts on the result. Attestation is layered: a lower layer that is hard to modify
vouches for the layer above it. An EC2 instance reads a signed JSON identity document and a
verifier checks it against an AWS certificate; SPIRE attests the node, then the workload,
before issuing an SVID. An OAuth working-group draft, not yet an RFC, uses the same pattern to
authenticate a client instance with a Client Attestation JWT from its backend.

Proving *what* is running, not just presenting a key. RFC 9334 defines the RATS roles
(attester, verifier, relying party) and layered attestation, where a previous layer acts as
the Attesting Environment for the next. AWS's instance identity document and SPIRE's node
and workload attestation separately illustrate the platform-instance and node-workload
layers; the OAuth attestation-based client authentication draft maps client-instance
authentication to a RATS Passport-model flow.

## Resources

- [@official@RFC 9334 — Remote ATtestation procedureS (RATS) Architecture](https://datatracker.ietf.org/doc/html/rfc9334)
- [@official@AWS EC2 Instance Identity Documents](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-identity-documents.html)
- [@official@IETF draft — OAuth 2.0 Attestation-Based Client Authentication](https://datatracker.ietf.org/doc/draft-ietf-oauth-attestation-based-client-auth/)

---

[← 07 · Workload & agent identity](README.md) · [Map](../../README.md)
