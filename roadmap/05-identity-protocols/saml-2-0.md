# SAML 2.0

**TL;DR:** SAML 2.0 is an XML-based standard in which an Identity Provider sends authentication
and attribute statements to a Service Provider. In Web Browser SSO, the browser carries a
response containing an assertion about the subject. Depending on the binding and profile, the
response, the assertion, or both are signed. The Service Provider validates the applicable
signature, issuer, time conditions and audience before creating its own session. Bindings
define how SAML messages travel, while profiles combine assertions, protocol messages and
bindings for a use case such as browser single sign-on.

OASIS's Security Assertion Markup Language: an XML framework in which an identity provider
issues assertions, statements about a subject's authentication and attributes (Core §2),
which a service provider that trusts the issuer acts on; whether an assertion or response
must be signed depends on the binding and profile in use (Core §5). The Web Browser SSO
profile is the part the enterprise runs on and the part this map covers; the sub-topics take
it apart. Agents meet SAML second-hand: the sessions and group claims an enterprise IdP
issues to a human are what the agent's owner logged in with.

## Resources

- [@official@OASIS SAML 2.0 Core](https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf)
- [@article@OASIS SAML 2.0 Technical Overview](https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html)

---

[← 05 · Identity protocols](README.md) · [Map](../../README.md)
