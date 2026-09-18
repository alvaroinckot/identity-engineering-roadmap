# Interop: AuthZEN

**TL;DR:** AuthZEN Authorization API 1.0 is an OpenID Final Specification for requests and
responses between a policy enforcement point (PEP) and a policy decision point (PDP). A common
API reduces how tightly enforcement code is bound to one decision-engine implementation. For
one access evaluation, the PEP sends an HTTPS POST with JSON naming a subject, action, and
resource, plus optional context. The PDP returns a JSON object containing a required boolean
decision. The specification takes the PEP and PDP terms from XACML and NIST's ABAC guide and
defines interoperability for products built with several authorization architectures.

AuthZEN Authorization API 1.0 defines a common request/response API between a policy
enforcement point and a policy decision point, reducing a caller's binding to one PDP
implementation.

## Resources

- [@official@OpenID AuthZEN Working Group](https://openid.net/wg/authzen/)

---

[← 03 · Authorization](README.md) · [Map](../../README.md)
