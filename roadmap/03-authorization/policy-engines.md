# Policy engines

**TL;DR:** A policy engine evaluates whether a subject may perform an action on a resource
using policy and relevant data. Moving decision logic out of request handlers can make rules
easier to manage and audit together. A service supplies a request, receives a result, and
remains responsible for enforcing it. The data flow differs by engine. OPA evaluates Rego
against request input and loaded data, Cedar evaluates a request with supplied entities and
context, and OpenFGA persists relationship tuples. Casbin is a library embedded in the
application rather than a separate decision service.

Externalized decision points: a policy engine evaluates "may this subject do this action on
this resource?" against policy and relevant data, separating at least some decision logic
from the application so it can be managed and audited on its own. The engines differ in the
language they evaluate and in whether the caller supplies the facts or the engine stores
them; the sub-topics take them one at a time.

## Resources

- [@official@Open Policy Agent / Rego](https://www.openpolicyagent.org/docs/latest/)
- [@official@Cedar Policy Language (AWS)](https://www.cedarpolicy.com/)
- [@official@OpenFGA (CNCF)](https://openfga.dev/docs)
- [@official@Casbin](https://casbin.org/docs/overview)

---

[← 03 · Authorization](README.md) · [Map](../../README.md)
