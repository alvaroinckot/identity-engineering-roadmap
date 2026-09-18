# Threat modeling identity systems

**TL;DR:** Threat modeling an identity system means documenting its login, authorization, and
token flows, what can go wrong, what mitigations apply, and how to verify them. Doing this
before deployment can expose redirect-URI prefix matching or a JWT library configured to accept
the `none` algorithm before an attacker does. The OAuth and JWT best-current-practice documents
are ready-made threat catalogs. RFC 9700 lists OAuth attacks and defenses such as PKCE for
public clients and exact redirect URI matching. RFC 8725 covers JWT validation, including
pinning accepted algorithms and keeping signing keys associated with their issuer. Revisit the
model after new features, architecture changes, and security incidents.

The process applied to authn/authz/token flows. The OAuth and JWT best-current-practice
documents double as ready-made threat catalogs.

## Resources

- [@article@OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling)
- [@official@RFC 9700 — OAuth 2.0 Security BCP](https://datatracker.ietf.org/doc/html/rfc9700)
- [@official@RFC 8725 — JWT BCP](https://datatracker.ietf.org/doc/html/rfc8725)

---

[← 11 · Threat modeling](README.md) · [Map](../../README.md)
