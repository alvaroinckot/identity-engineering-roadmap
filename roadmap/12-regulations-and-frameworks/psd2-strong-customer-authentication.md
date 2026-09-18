# PSD2 & strong customer authentication

**TL;DR:** The second Payment Services Directive (Directive (EU) 2015/2366) requires payment
service providers to apply strong customer authentication (SCA) when a payer accesses a payment
account online, initiates an electronic payment, or acts through a remote channel that may
carry fraud risk. SCA means two or more independent elements from knowledge, possession and
inherence, designed so that breaching one does not compromise the others and to protect the
confidentiality of authentication data; for remote electronic payments the authentication must
dynamically link to the amount and the payee. Commission Delegated Regulation (EU) 2018/389
supplies the technical rules: a single-use authentication code, limits on failed attempts and
session inactivity, independence of elements on multi-purpose devices, exemptions from SCA, and
access interfaces through which third-party providers identify themselves and rely on the
bank's authentication.

Art. 4(30) defines SCA as authentication "based on the use of two or more elements categorised
as knowledge (something only the user knows), possession (something only the user possesses)
and inherence (something the user is) that are independent"; Art. 97(1) lists the triggers,
Art. 97(2) requires for remote electronic payments "elements which dynamically link the
transaction to a specific amount and a specific payee", Art. 97(5) makes account servicing
providers let payment initiation and account information providers "rely on the authentication
procedures provided by the account servicing payment service provider", and Art. 98 delegates
the detail to EBA-drafted regulatory technical standards. Delegated Regulation 2018/389 Art. 4
requires the elements to "result in the generation of an authentication code" that is "only
accepted once", caps consecutive failed attempts at five within a given period and inactivity
after online account access at five minutes; Art. 5 makes the code "specific to the amount of
the payment transaction and the payee", invalidated by "any change to the amount or the payee";
Arts. 6–9 set requirements per element and for independence, including "separated secure
execution environments" on multi-purpose devices; Chapter III lists the exemptions from SCA;
Arts. 30–33 require at least one access interface where third-party providers "identify
themselves" and "communicate securely", either dedicated or the customer-facing interface, with
a contingency fallback when a dedicated interface fails (API security profiles for this
interface: [FAPI 2.0](../05-identity-protocols/fapi-2-0.md)). Where Art. 97(1) is triggered,
the payment service provider applies SCA subject to the RTS exemptions; payment initiation and
account information providers may rely on the account provider's authentication under Art.
97(5).

_Not legal advice. Obligations and dates are quoted as published on 2026-09-17; check the
official text before relying on them._

## Resources

- [@official@Directive (EU) 2015/2366 (PSD2) — Art. 4(30) strong customer authentication, Art. 97 triggers, Art. 98 RTS mandate](https://eur-lex.europa.eu/eli/dir/2015/2366/oj)
- [@official@Commission Delegated Regulation (EU) 2018/389 — RTS on strong customer authentication and common and secure open standards of communication](https://eur-lex.europa.eu/eli/reg_del/2018/389/oj)

---

[← European Union: identity regulation](eu-identity-regulation.md) · [12 · Regulations, frameworks & controls](README.md) · [Map](../../README.md)
