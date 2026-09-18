# Case studies: identity breaches

**TL;DR:** Each of these four breaches shows a recurring identity failure. A signing key
outside its secure environment lets its holder mint tokens; here mail services that skipped
issuer and scope validation accepted a consumer key for enterprise mail. With the identity
provider's token-signing private key, a Golden SAML attacker can forge assertions for users
regardless of MFA, and trusting service providers accept them without checking back. A
service-account credential saved in an employee's personal Google profile, combined with
uploaded HAR files containing live session tokens, exposed customer sessions. A compromised
contractor password followed by repeated two-factor prompts until one was accepted is MFA
fatigue. The lessons are key custody and rotation, complete token validation, credential
isolation, and redacting reusable session tokens from support artifacts.

Storm-0558 (2023): a Microsoft consumer (MSA) signing key created in 2016 left the secure token-signing environment (Microsoft's leading hypothesis is operational error that put key material in a debugging environment reached through a compromised engineering account; it found no crash dump containing the key), and mail systems that skipped issuer/scope validation accepted tokens signed with that consumer key for enterprise Exchange Online; the CSRB traced the key's survival to manual rotation halted in 2021 with no automated replacement, so the lessons are signing-key custody, issuer and scope validation, rotation, and the blast radius of one long-lived signing key. The SolarWinds-era actor (CISA AA21-008A, January 2021) used administrator rights on the on-premises network to forge authentication tokens from the AD FS signing capability, tokens that service providers accepted without checking them against the identity provider, then added credentials to existing service principals to persist in Azure AD; the technique CyberArk Labs had named "Golden SAML" in 2017 assumes the attacker obtains the IdP's token-signing private key, after which it can mint assertions for any user with any privileges, 2FA at the IdP notwithstanding, and CISA's advisory documents the forgery and the persistence, not the theft of the key itself. Okta's support system (September–October 2023): an employee signed into a personal Google profile in Chrome on an Okta-managed laptop, saving the credentials of a service account permitted to view and update support cases into that personal account; with it the actor read HAR files customers had uploaded, which held reusable Okta session tokens, and hijacked the sessions of 5 customers: a credential in the wrong realm plus session tokens at rest in support artifacts. Uber (September 2022): an attacker likely bought an external contractor's corporate password on the dark web, then repeatedly retried the login until the contractor accepted one of the resulting two-factor approval requests, and from that account reached other employee accounts with elevated permissions to G-Suite and Slack; Uber's statement never uses the phrase, but this is the sequence the industry files as "MFA fatigue" under Multi-factor.

## Resources

- [@official@MSRC — Results of Major Technical Investigations for Storm-0558 Key Acquisition](https://www.microsoft.com/en-us/msrc/blog/2023/09/results-of-major-technical-investigations-for-storm-0558-key-acquisition)
- [@official@CSRB — Review of the Summer 2023 Microsoft Exchange Online Intrusion](https://www.cisa.gov/resources-tools/resources/CSRB-Review-Summer-2023-MEO-Intrusion)
- [@official@CISA AA21-008A — Detecting Post-Compromise Threat Activity in Microsoft Cloud Environments](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-008a)
- [@article@CyberArk Labs — Golden SAML: Newly Discovered Attack Technique Forges Authentication to Cloud Apps (2017, archived)](https://web.archive.org/web/20231215134731/https://www.cyberark.com/resources/threat-research-blog/golden-saml-newly-discovered-attack-technique-forges-authentication-to-cloud-apps)
- [@official@Okta Security — Unauthorized Access to Okta's Support Case Management System: Root Cause and Remediation](https://sec.okta.com/articles/2023/11/unauthorized-access-oktas-support-case-management-system-root-cause/)
- [@official@Uber Newsroom — Security update (September 2022)](https://www.uber.com/newsroom/security-update/)

---

[← 11 · Threat modeling](README.md) · [Map](../../README.md)
