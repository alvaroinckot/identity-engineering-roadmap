# Pairwise identifiers & data minimization

**TL;DR:** A pairwise identifier is a subject identifier that an identity provider varies by
client or sector identifier to limit correlation between relying parties. With one public
identifier, a travel site and a health portal using the same provider can match one person
across their databases. In OpenID Connect the provider advertises pairwise as a supported
subject type and computes a distinct sub per sector identifier that no party but the provider
can reverse. The identifier alone does not stop correlation: if the token also carries name and
email, the two sites match on those instead. Both sides exchange only the minimum data the
function needs, the rule GDPR states as data minimization; request only the claims the
application uses.

A stable identifier is also a correlation handle: give every relying party the same `sub`
and any two of them can join their records on it. A pairwise identifier breaks the join by
issuing a different identifier per relationship: OpenID Connect Core §8.1 requires a unique
`sub` per Sector Identifier that "MUST NOT be reversible by any party other than the OpenID
Provider", and SP 800-63C-4 §3.4.1.1 requires a different federated identifier for each RP
(or per agreed set of RPs), one that "SHALL contain no identifying information about the
subscriber" (§3.4.1.2). The identifier is only half of it, since two RPs holding different
pairwise identifiers can still re-identify the subscriber from the name or email carried
beside them (63C-4 §3.4.1.1), so the same volume requires that "The IdP and RP SHALL
exchange only the minimum data necessary" (§3.10) and GDPR Art. 5(1)(c) states the legal
principle: personal data "limited to what is necessary in relation to the purposes for which
they are processed".

## Resources

- [@official@OpenID Connect Core 1.0 §8 — Subject Identifier Types](https://openid.net/specs/openid-connect-core-1_0.html#SubjectIDTypes)
- [@official@Regulation (EU) 2016/679 (GDPR) — Art. 5, Principles relating to processing of personal data](https://eur-lex.europa.eu/eli/reg/2016/679/oj#art_5)
- [@official@NIST SP 800-63 Digital Identity Guidelines](https://pages.nist.gov/800-63-4/sp800-63.html) (SP 800-63C-4 §3.4.1 Pairwise Pseudonymous Identifiers, §3.10 Privacy Requirements)

---

[← Identifiers & account linking](identifiers-account-linking.md) · [01 · Primitives](README.md) · [Map](../../README.md)
