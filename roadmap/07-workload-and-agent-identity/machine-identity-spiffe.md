# Machine identity & SPIFFE

**TL;DR:** SPIFFE defines open-source standards that give a running workload a URI identity of
the form `spiffe://trust-domain/path` and a short-lived signed document, an SVID, that proves
it. Without it, services often rely on copied secrets or shared accounts that weaken
attribution. An implementation such as SPIRE attests the node and workload, then supplies SVIDs
through a local Workload API that requires no bootstrap token from the workload. Current SPIFFE
standards define X.509, JWT, and WIT SVIDs, although project guidance chiefly documents X.509
and JWT use. Credentials rotate automatically, and SPIFFE advises X.509-SVIDs where possible
because bearer JWT-SVIDs can be replayed.

Google recommends single-purpose service accounts and avoiding service-account keys where
possible; SPIFFE is the standard that follows: SPIFFE IDs, trust domains, and SVIDs (X.509,
JWT, or the newer WIT format), with SPIRE as the project's production-ready implementation
that attests nodes and workloads before issuing SVIDs.

## Resources

- [@official@SPIFFE — Secure Production Identity Framework For Everyone](https://spiffe.io/docs/latest/spiffe-about/overview/)
- [@official@Google Cloud — Best practices for using service accounts](https://cloud.google.com/iam/docs/best-practices-service-accounts)

---

[← 07 · Workload & agent identity](README.md) · [Map](../../README.md)
