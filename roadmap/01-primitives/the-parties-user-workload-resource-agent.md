# The parties: user, workload, resource, agent

**TL;DR:** User, workload, resource, and agent are the names this map gives to the parties in a
system. A user is a person. A workload is a running piece of software, such as a payroll
service or a CI runner, that needs an identity of its own because it calls other services. A
resource is what gets accessed, such as an HR API. These are roles, not kinds of code. The same
process can be a workload with its own identity, an OAuth client making requests on behalf of a
resource owner and with that owner's authorization, and a delegate acting for a user, all in
one request. An AI agent can occupy several of these roles, depending on the request.

User, workload, resource, agent: this map's working names for what RFC 4949 §4 calls a
"system entity", "an active part of a system -- a person, a set of persons (e.g., some kind
of organization), an automated process, or a set of processes". The same piece of software
can be a workload in SPIFFE's sense (it runs somewhere and needs an identity of its own), an
OAuth client, "an application making protected resource requests on behalf of the resource
owner and with its authorization" (RFC 6749 §1.1), and a delegate acting for a user
([Delegation as a primitive](delegation-as-a-primitive.md)) at the same time.

## Resources

- [@official@RFC 4949 — Internet Security Glossary, Version 2](https://datatracker.ietf.org/doc/html/rfc4949)
- [@official@SPIFFE](https://spiffe.io/docs/latest/spiffe-about/overview/) for the workload definition
- [@official@RFC 6749 — The OAuth 2.0 Authorization Framework §1.1 Roles](https://datatracker.ietf.org/doc/html/rfc6749#section-1.1)

---

[← 01 · Primitives](README.md) · [Map](../../README.md)
