# ReBAC & Zanzibar

**TL;DR:** Relationship-based access control (ReBAC) stores access as relationships between
users and objects, and between objects, and answers a check by following them. The stored
record is a relation tuple such as document:roadmap, editor, user:anne; the user side can
itself be a set such as the members of group:eng. Rewrite rules state which relations imply
others, for example that every editor is also a viewer, so a check walks a graph. Google's
Zanzibar paper describes this model and the "new enemy" problem: a check against stale
permissions lets a just-removed user see content added after the removal. Zookies are opaque
consistency tokens a client stores with content and sends back so a later check is at least
that fresh. OpenFGA states that it implements the Zanzibar model.

Relationships as the primary data: "user X is editor of doc Y". The Zanzibar paper (USENIX
ATC 2019) describes relation tuples, userset rewrites, and consistency tokens called
zookies; OpenFGA says it implements the Zanzibar model.

## Resources

- [@official@Zanzibar: Google's Consistent, Global Authorization System](https://www.usenix.org/conference/atc19/presentation/pang) (USENIX ATC 2019)
- [@official@OpenFGA (CNCF)](https://openfga.dev/docs)

---

[← 03 · Authorization](README.md) · [Map](../../README.md)
