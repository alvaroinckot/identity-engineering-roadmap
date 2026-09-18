# 05 · Identity protocols

The protocols that carry identity and delegated access across a trust boundary, which is what
NIST SP 800-63 calls federation: conveying identity and authentication information across a
set of networked systems. OAuth 2.x delegates access across that boundary, OpenID Connect puts
identity on top of it, SAML 2.0 did both earlier in XML and still runs the enterprise, and
verifiable credentials take the live identity provider out of the presentation altogether.

## Topics

1. [Before OAuth](before-oauth.md)
2. [OAuth 2.x](oauth-2x.md)
   1. [OAuth 2.0 roles & grants](oauth-2-0-roles-grants.md)
   2. [Scopes, audience & consent](scopes-audience-consent.md)
   3. [Authorization requests: JAR & PAR](authorization-requests-jar-par.md)
   4. [PKCE & OAuth 2.1](pkce-oauth-2-1.md)
   5. [Client registration & discovery](client-registration-discovery.md)
      1. [Server metadata: RFC 8414 & RFC 9728](server-metadata.md)
      2. [Manual registration](manual-registration.md)
      3. [Dynamic client registration: RFC 7591](dynamic-client-registration.md)
      4. [Client ID Metadata Documents: CIMD](client-id-metadata-documents.md)
   6. [Token lifecycle: introspection & revocation](token-lifecycle-introspection-revocation.md)
      1. [Token formats: opaque, JWT, phantom tokens & macaroons](token-formats.md)
   7. [Sender-constrained tokens](sender-constrained-tokens.md)
      1. [DPoP: RFC 9449](dpop.md)
      2. [mTLS-bound tokens: RFC 8705](mtls-bound-tokens.md)
   8. [OAuth Security BCP](oauth-security-bcp.md)
      1. [Native apps: RFC 8252](native-apps.md)
      2. [Browser-based apps & the BFF pattern](browser-based-apps-bff.md)
      3. [FAPI 2.0 security profile](fapi-2-0.md)
3. [OpenID Connect](openid-connect.md)
   1. [ID token & claims](id-token-claims.md)
   2. [Authentication flows: code, implicit, hybrid](authentication-flows.md)
   3. [Decoupled authentication: CIBA](decoupled-authentication-ciba.md)
   4. [UserInfo & standard claims](userinfo-standard-claims.md)
   5. [OIDC Discovery & registration](oidc-discovery-registration.md)
   6. [OpenID Federation 1.0](openid-federation.md)
   7. [Session management & logout](session-management-logout.md)
4. [SAML 2.0](saml-2-0.md)
   1. [SAML 2.0 assertions](saml-2-0-assertions.md)
   2. [Bindings & profiles](bindings-profiles.md)
   3. [SAML in the enterprise today](saml-in-the-enterprise-today.md)
5. [Verifiable credentials](verifiable-credentials.md)
   1. [Selective disclosure: SD-JWT](selective-disclosure-sd-jwt.md)
   2. [Issuance & presentation: OpenID4VCI & OpenID4VP](openid4vc.md)

## What AI agents change

Agents are OAuth clients that register dynamically, run without a browser (device grant,
client credentials), need scopes narrower than "everything the user can do", and must be
revocable mid-task. MCP's authorization spec is OAuth 2.1 applied to agent↔tool
(→ [07](../07-workload-and-agent-identity/README.md)). SAML's Web Browser SSO profile changes
almost nothing directly, it is a human-in-a-browser flow, but agents inherit the sessions and
group claims the enterprise IdP issued through it.

---

[← Map](../../README.md)
