# Cross-app access: XAA

**TL;DR:** Cross-app access is a pattern published by Okta that implements an OAuth
working-group draft, ID-JAG. It lets one enterprise application, or an AI agent inside it, call
another application's API on a signed-in user's behalf with the company's identity provider in
the middle. In the direct OAuth pattern it addresses, the applications establish a per-user
connection that the enterprise identity provider does not see or control. With XAA, the
requesting app exchanges the user's ID token or SAML assertion at the identity provider for an
identity assertion authorization grant when administrator policy allows. It presents that grant
to the resource app's authorization server through the JWT bearer grant and receives a scoped
access token without another consent screen.

Enterprise-managed app-to-app and agent-to-app access: with ID-JAG, the enterprise identity
provider issues an identity assertion that a resource application's authorization server can
exchange for a token without another user interaction when policy permits, so the IdP
becomes the policy decision point over which application, or the agent inside it, may reach
which other application, and the security team sees and controls the connections.

## Resources

- [@official@Cross App Access (XAA)](https://xaa.dev/)

---

[← 07 · Workload & agent identity](README.md) · [Map](../../README.md)
