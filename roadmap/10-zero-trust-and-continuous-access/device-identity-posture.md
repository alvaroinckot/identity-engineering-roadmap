# Device identity & posture

**TL;DR:** Device identity says which machine is making a request; device posture says what
state it is in, such as its patch level. Both feed the access decision, because a correct
password and MFA from an unmanaged laptop is still a risky request. A registered device holds a
client certificate that identifies it to the identity provider, and a device management system
reports its compliance state there, so a Conditional Access policy can require a compliant
device and MFA together. Device state cannot travel through the device-code flow, so that flow
cannot satisfy a compliant-device requirement. An agent running in cloud infrastructure may
have no compliance signal to offer; in Entra's preview, agent identities can only be blocked.

Device identity and device posture are inputs to access policy: SP 800-207 tenet 5 says "The
enterprise monitors and measures the integrity and security posture of all owned and
associated assets" and "evaluates the security posture of the asset when evaluating a
resource request", and tenet 4 lists the requesting asset's state (installed software
versions, installed credentials, previously observed behavior) among the inputs to dynamic
policy (§2.1). In Entra Conditional Access, Intune or a third-party MDM supplies the
compliance state, Entra identifies a registered device by a client certificate provisioned
at registration, and the compliant-device grant can be combined with MFA. CISA's Zero Trust
Maturity Model Devices pillar is the ladder: visibility into devices not required
(Traditional), some devices reporting their characteristics (Initial), verified device
insights at initial access (Advanced), and compliance continuously verified for the device's
lifetime with real-time device risk feeding resource-access decisions (Optimal). Agent
sessions that run directly in cloud infrastructure "might not provide device compliance
signals", and in Entra's preview agent identities support only Block access; SP 800-207
allows client identity to include a service identity or "artifacts to authenticate automated
tasks" (§2.1 tenet 4) and puts virtual assets in the asset database "to some extent" (§3.3)
but names no compliance signal for a workload without a managed endpoint, so what a workload
presents instead is a question for [Workload & agent
identity](../07-workload-and-agent-identity/README.md).

## Resources

- [@official@NIST SP 800-207 — Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final)
- [@official@CISA Zero Trust Maturity Model (Version 2.0)](https://www.cisa.gov/zero-trust-maturity-model)
- [@official@Microsoft Entra Conditional Access — Grant controls](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant#require-device-to-be-marked-as-compliant)

---

[← 10 · Zero trust & continuous access](README.md) · [Map](../../README.md)
