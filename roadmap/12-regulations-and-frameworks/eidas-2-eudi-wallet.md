# eIDAS 2.0 & the EU Digital Identity Wallet

**TL;DR:** Regulation (EU) 2024/1183 requires each member state to provide at least one
European Digital Identity Wallet through which users control and present identity data and
attestations. The wallet must support selective disclosure, locally stored pseudonyms and free
qualified electronic signatures. A relying party must register and declare the data it will
request. Three groups must accept it: public sector bodies that require electronic
identification for an online public service; private relying parties, except micro and small
enterprises, that Union or national law requires to use strong user authentication, within 36
months of the implementing acts and only on voluntary request; and designated very large online
platforms where they require user authentication, on voluntary request and for the minimum data
necessary. The Architecture and Reference Framework specifies the common technical baseline.

Inserted Art. 5a lists the wallet's functions — request, store, select, combine and present
person identification data and attestations "while ensuring that selective disclosure of data
is possible", "generate pseudonyms and store them encrypted and locally", and sign "by means of
qualified electronic signatures by default and free of charge" — and puts its use "under the
sole control of the user"; Art. 5b makes a relying party register where it is established and
declare the data it will request, forbids requesting more, and forbids refusing a pseudonym
where identification is not required by law. Art. 5f(1) obliges public sector bodies that
require electronic identification for an online service to accept the wallet; Art. 5f(2)
obliges private relying parties that Union or national law binds to strong user authentication,
micro and small enterprises excepted, to accept it no later than 36 months after the
implementing acts named in Art. 5a(23) and 5c(6) and only on the user's voluntary request; Art.
5f(3) obliges very large online platforms designated under Regulation (EU) 2022/2065 to accept
it for user authentication on the user's voluntary request and for the minimum data necessary.
The Architecture and Reference Framework (v3.0.0) specifies the common technical baseline:
OpenID4VCI profiled by HAIP for issuance, OpenID4VP profiled by HAIP required among its
remote-presentation options, ISO/IEC 18013-5 for proximity presentation, and ISO/IEC 18013-5
mdoc, SD-JWT VC or, optionally, W3C VCDM v2.0 as attestation formats — see [Issuance &
presentation: OpenID4VCI & OpenID4VP](../05-identity-protocols/openid4vc.md) and [selective
disclosure with SD-JWT](../05-identity-protocols/selective-disclosure-sd-jwt.md). Art. 5a(4)
keeps presentation under the user's sole control and Art. 5b(3) caps the data a relying party
may request at what it registered.

_Not legal advice. Obligations and dates are quoted as published on 2026-09-17; check the
official text before relying on them._

## Resources

- [@official@Regulation (EU) 2024/1183 (eIDAS 2.0) — European Digital Identity Wallet, Art. 5a–5f](https://eur-lex.europa.eu/eli/reg/2024/1183/oj)
- [@official@EUDI Wallet Architecture and Reference Framework (ARF) v3.0.0 — attestation formats and OpenID4VC protocols](https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/)

---

[← European Union: identity regulation](eu-identity-regulation.md) · [12 · Regulations, frameworks & controls](README.md) · [Map](../../README.md)
