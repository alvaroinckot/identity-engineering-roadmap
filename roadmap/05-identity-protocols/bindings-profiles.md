# Bindings & profiles

**TL;DR:** A binding is the rule for carrying a SAML message over a transport such as HTTP; a
profile combines assertions, protocol messages and bindings to solve one use case. The Web
Browser SSO profile uses three HTTP bindings. HTTP Redirect puts the message in the URL query
string, HTTP POST puts it in a form the browser auto-submits, and HTTP Artifact sends a
reference the receiver resolves directly with the sender. The authentication request may use
any of the three; the response carrying the assertion returns by POST or Artifact. In the
common SP-initiated flow the user arrives at the service provider and is redirected to the
identity provider; in the IdP-initiated flow the user starts at the identity provider, which
POSTs an unsolicited response to the service provider.

How assertions travel (HTTP Redirect, HTTP POST, Artifact) and the Web Browser SSO profile
everyone actually deploys. SP-initiated vs. IdP-initiated flows.

## Resources

- [@article@OASIS SAML 2.0 Technical Overview](https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html)

---

[← SAML 2.0](saml-2-0.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
