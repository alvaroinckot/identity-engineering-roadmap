# SAML 2.0 assertions

**TL;DR:** A SAML assertion is an XML package of statements issued by a SAML authority, often
an identity provider. It always contains an issuer and can contain a subject, conditions and
zero or more statements. An authentication statement records how and when a principal
authenticated, while an attribute statement carries values such as group memberships. When
conditions are present, the relying party must evaluate them before use; `AudienceRestriction`
can limit the assertion to a service provider. An assertion relayed through the browser should
be signed by its issuer, and the relying party must reject its contents if that signature is
invalid.

The assertion (authentication, attribute, and authorization-decision statements), issuer,
subject, conditions, and the XML signature that makes it trustworthy.

## Resources

- [@official@OASIS SAML 2.0 Core](https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf)

---

[← SAML 2.0](saml-2-0.md) · [05 · Identity protocols](README.md) · [Map](../../README.md)
