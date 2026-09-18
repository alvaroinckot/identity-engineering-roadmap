# Assurance levels: IAL, AAL, FAL

**TL;DR:** NIST SP 800-63 rates confidence in a user along three separate scales. IAL says how
well the service checked that a real, specific person is behind the account. AAL says how
strongly that person proved control of their authenticators at login. FAL says how well a
signed assertion about that login survives transit between an identity provider and the relying
party that consumes it. An organization picks each level on its own, so a lightly proofed but
strongly authenticated account, IAL1 with AAL2, is a valid design and no single score exists. A
session inherits at most the AAL of the login that created it, and a requirement for AAL2 means
two distinct factors with a phishing-resistant option offered.

NIST SP 800-63-4 separates assurance into three independently selected dimensions, each with
its own levels defined in its own volume: IAL, identity assurance, how well the person was
proofed against a real-life identity (SP 800-63A); AAL, authentication assurance, how
strongly the claimant proved control of their authenticators at login (SP 800-63B); and FAL,
federation assurance, how well an assertion about that login survives the trip from IdP to
RP (SP 800-63C). The base volume requires organizations to pick a level for each function
separately, so an IAL1/AAL2 system (lightly proofed, strongly authenticated) is a legitimate
choice and the three numbers never collapse into one score. A session may be treated at a
lower AAL than the authentication event that created it, but never at a higher one (SP
800-63B-4 §5.1). On this map AAL is covered here under Authentication and FAL under Identity
protocols.

## Resources

- [@official@NIST SP 800-63-4 — Digital Identity Guidelines (base volume)](https://pages.nist.gov/800-63-4/sp800-63.html)
- [@official@NIST SP 800-63A-4 — Identity Proofing and Enrollment, §1.2 Identity Assurance Levels](https://pages.nist.gov/800-63-4/sp800-63a.html#identity-assurance-levels)
- [@official@NIST SP 800-63B-4 — Authentication and Authenticator Management, §2 Authentication Assurance Levels](https://pages.nist.gov/800-63-4/sp800-63b.html#authentication-assurance-level-1)
- [@official@NIST SP 800-63C-4 — Federation and Assertions, §2 Federation Assurance Level](https://pages.nist.gov/800-63-4/sp800-63c.html#fal)

---

[← 02 · Authentication](README.md) · [Map](../../README.md)
