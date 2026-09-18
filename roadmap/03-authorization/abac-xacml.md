# ABAC & XACML

**TL;DR:** Attribute-based access control (ABAC) decides a request by evaluating name-value
attributes about the subject, resource, requested action, and environment against policy.
Encoding conditions such as shift time and customer region through roles can require many
narrow roles, while ABAC evaluates those facts directly. A policy enforcement point (PEP)
requests and enforces a decision, and a policy decision point (PDP) evaluates policy. A policy
information point (PIP) supplies attributes, while a policy administration point (PAP) creates
policy. XACML standardizes this architecture, an XML policy language, and the decisions Permit,
Deny, NotApplicable, and Indeterminate.

Attributes of subject, resource, action, and environment evaluated by policy. XACML 3.0, an
OASIS Standard published in January 2013, defines an XML policy language and a
PAP/PDP/PEP/PIP architecture that later work such as NIST SP 800-162 and AuthZEN uses or
cites; XACML itself credits the PDP and PEP terms to RFC 3198.

## Resources

- [@official@NIST SP 800-162 — Guide to ABAC](https://csrc.nist.gov/pubs/sp/800/162/upd2/final)
- [@official@OASIS XACML 3.0](https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html)

---

[← 03 · Authorization](README.md) · [Map](../../README.md)
