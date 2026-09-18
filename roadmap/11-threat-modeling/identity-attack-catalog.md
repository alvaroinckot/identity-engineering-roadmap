# Identity attack catalog

**TL;DR:** The identity attack catalog maps ways attackers steal or forge working credentials
to MITRE ATT&CK techniques. Token theft covers OAuth access tokens, service-account tokens,
CI/CD tokens, and managed-identity tokens. It includes consent phishing, where a user
authorizes a malicious application to access data. Golden SAML instead uses the private key
behind an identity provider's token-signing certificate, or another trusted signing capability,
to create new assertions with chosen claims and lifetimes. MFA request generation sends
repeated prompts until a user approves one. Credential stuffing replays passwords from
unrelated breach dumps against single sign-on. Each technique has an ATT&CK identifier for
threat models and detection rules.

Stealing application access tokens, including service-account, CI/CD and managed-identity
tokens (T1528), forging SAML tokens (T1606.002), consent phishing (T1528), MFA request
generation (T1621) and credential stuffing (T1110.004), mapped to ATT&CK techniques; worked
incidents are under [Case studies: identity breaches](identity-breach-case-studies.md).

## Resources

- [@official@MITRE ATT&CK — Credential Access](https://attack.mitre.org/tactics/TA0006/)

---

[← 11 · Threat modeling](README.md) · [Map](../../README.md)
