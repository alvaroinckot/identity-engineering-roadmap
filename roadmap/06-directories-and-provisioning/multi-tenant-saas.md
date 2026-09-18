# Multi-tenant SaaS: organizations & enterprise SSO

**TL;DR:** A multi-tenant B2B application needs a customer boundary for identity configuration
and data access. Auth0 calls that boundary an organization, while Microsoft Entra calls a
customer-side directory a tenant. Home-realm discovery uses an entered identifier or a hint to
route a user toward the appropriate identity provider. In Auth0, authentication through an
organization adds an `org_id` claim, and the API must validate it and partition access by it.
Auth0 can also issue an organization-scoped client-credentials token for a non-human client.
IPSIE's Draft 00 common requirements tell a relying party to combine subject and tenant
identifiers when constructing a globally unique subject.

A B2B application serves many customers from one deployment, so it needs a unit to attach each customer's identity plumbing to: Auth0 calls it an *organization* (the customer's enterprise connection is enabled per organization, roles are scoped to it, and tokens issued through an organization carry an `org_id` claim the API must partition access by), while Microsoft Entra's word for the same customer-side unit is *tenant*. Home realm discovery gets a login to the right customer IdP: Entra uses the user principal name the user enters to determine where the user signs in, and an application can steer that hop with `domain_hint` or an HRD policy; Auth0's Identifier First flow does the same job, resolving the organization first and the connection second. IPSIE, the OpenID Foundation's Interoperability Profiling for Secure Identity in the Enterprise WG, is the effort to make the whole bundle (OIDC single sign-on, SCIM lifecycle, Shared Signals, logout, token revocation) interoperable with secure defaults, arranged as two independent families of levels, Session Lifecycle (SL) and Account Lifecycle (AL); no text has reached Implementer's Draft or Final, and the three published openid.net/specs texts are Draft 00. For a non-human client inside a customer's tenant, Auth0 issues organization-scoped client-credentials tokens (the `organization` parameter puts `org_id` in a token the application obtains for itself rather than for a user); the user-lifecycle rules are separate: IPSIE's common requirements make an RP combine the subject identifier with a tenant identifier to form a globally unique subject, and the AL SCIM profile ties deactivating a user account to terminating its sessions, API tokens, refresh tokens and SSH keys.

## Resources

- [@official@Auth0 Organizations](https://auth0.com/docs/manage-users/organizations)
- [@official@Microsoft Entra ID — Home Realm Discovery for an application](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/home-realm-discovery-policy)
- [@official@OpenID IPSIE WG](https://openid.net/wg/ipsie/)
- [@official@IPSIE Common Requirements Profile Draft 00](https://openid.net/specs/ipsie-common-requirements-1_0.html)
- [@official@IPSIE SL1 OpenID Connect Profile 1.0 Draft 00](https://openid.net/specs/ipsie-openid-connect-sl1-profile-1_0.html)
- [@official@IPSIE AL SCIM 2.0 Profile Draft 00](https://openid.net/specs/ipsie-al-scim-profile-1_0.html)

---

[← 06 · Directories & provisioning](README.md) · [Map](../../README.md)
