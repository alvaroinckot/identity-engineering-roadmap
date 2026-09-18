# OPA & Rego

**TL;DR:** Open Policy Agent (OPA) is a general-purpose policy engine. A service sends it a
query with a JSON document as input. OPA evaluates policies written in Rego against that input
and any loaded data, and returns a result the service enforces. It exists so the people who own
a rule can read, write, version and change it separately from the service that enforces it.
Rego is declarative: a policy states conditions over the request, visible as the global
variable input, and over data, and the result can be a boolean or any other JSON value. OPA
treats authorization as one kind of policy among many; the engine that decides whether a
payroll service may call the HR API can also decide whether a Kubernetes object is admitted.

Open Policy Agent is a general-purpose policy engine: it evaluates policies written in Rego,
a declarative query language, against JSON input and data, and returns a decision the
calling service enforces. It decouples decision from enforcement and is domain-agnostic: the
same engine can evaluate authorization policy and Kubernetes admission policy.

## Resources

- [@official@Open Policy Agent / Rego](https://www.openpolicyagent.org/docs/latest/)

---

[← Policy engines](policy-engines.md) · [03 · Authorization](README.md) · [Map](../../README.md)
