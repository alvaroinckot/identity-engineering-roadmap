# Cedar

**TL;DR:** Cedar is an open-source policy language and evaluation engine made only for
authorization. Each policy is a permit or forbid statement naming which principals, actions and
resources it covers, with optional conditions on their attributes and on request context. A
caller sends principal, action, resource and context together with the entities involved and
their attributes, and Cedar returns allow or deny: with no matching permit the answer is deny,
and one matching forbid wins over any permit. Scope-only policies express role-style rules;
policies with conditions express attribute-based rules. A schema describes entity types and
attributes, and Cedar validates policies against it when they are written, not at evaluation
time. The language is built for automated reasoning, so tools can prove properties of a whole
policy set.

Cedar is an open-source policy language and evaluation engine built for authorization:
policies are `permit` or `forbid` statements with principal, action and resource scope plus
optional conditions that may inspect context; schemas validate policies, and `forbid`
overrides `permit`. The language was designed to be analyzable, so a policy set can be
checked for properties rather than only tested. A caller expresses an authorization request
as principal, action, resource and context, and supplies the entities the decision needs.

## Resources

- [@official@Cedar Policy Language (AWS)](https://www.cedarpolicy.com/)

---

[← Policy engines](policy-engines.md) · [03 · Authorization](README.md) · [Map](../../README.md)
