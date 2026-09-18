# OpenFGA

**TL;DR:** OpenFGA is a CNCF-owned, open-source relationship-based authorization engine that
implements the Zanzibar model. You define types such as user, folder, and document and the
relations each type permits, such as owner, editor, or viewer. The service stores relationship
tuples, for example that `user:anne` is an editor of `document:roadmap`, and asks whether that
user has a requested relation. OpenFGA follows stored relationships to answer Check and reverse
queries. Because those relationship facts persist in OpenFGA, the application must keep them
synchronized as sharing and membership change.

OpenFGA is a relationship-based authorization engine in the Zanzibar lineage (→ [ReBAC &
Zanzibar](rebac-zanzibar.md)): you write an authorization model of types and relations,
store tuples such as "user:anne is editor of document:roadmap", and ask Check questions the
engine answers by walking the relationships. It is a CNCF project. OpenFGA ordinarily
persists relationship tuples, while the OPA and Cedar request flows can supply input, data
or entities at evaluation time.

## Resources

- [@official@OpenFGA (CNCF)](https://openfga.dev/docs)

---

[← Policy engines](policy-engines.md) · [03 · Authorization](README.md) · [Map](../../README.md)
