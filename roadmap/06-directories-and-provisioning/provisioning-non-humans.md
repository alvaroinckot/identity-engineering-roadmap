# Provisioning non-humans

**TL;DR:** Provisioning non-humans means giving service accounts and AI agents the same create,
disable, review, and remove lifecycle employees get. Without it a CI runner's credential or an
agent's tool access stays valid after the pipeline or agent is gone, and nobody reviews it.
NIST SP 800-53 lists system and service accounts among the account types its account-management
control covers, so inactive-account disabling and privilege review apply to them too. The
tooling lags: SCIM defines User and Group resources, the SCIM working group has published a
device schema extension and an event profile, and an AI agent resource extension is only an
individual Internet-Draft, not adopted by the group. IPSIE's draft profiles likewise speak only
of users, so a team inventorying agents has no standard schema.

Service accounts are an account type NIST SP 800-53 AC-2 already expects to be created,
disabled, reviewed and removed like any other. SCIM has no adopted agent resource schema
yet: the rechartered SCIM WG has shipped a device schema extension (RFC 9944) and an event
profile (RFC 9967) while the AI Agent Resource Extension remains an individual
Internet-Draft (draft-wzdk-scim-agent-resource-00), and IPSIE's profiles speak only of
users.

## Resources

- [@official@IETF SCIM Working Group (rechartered)](https://datatracker.ietf.org/wg/scim/documents/)
- [@official@OpenID IPSIE WG](https://openid.net/wg/ipsie/)
- [@official@NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final)

---

[← 06 · Directories & provisioning](README.md) · [Map](../../README.md)
