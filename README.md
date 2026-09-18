# Identity Engineering Roadmap

A [roadmap.sh](https://roadmap.sh)-style map of **identity engineering in the AI era**: the
concepts an identity engineer needs, in learning order, from first primitives to AI agents.
Every node points at the RFCs, specs, papers, and docs that define it.

Follow the spine top to bottom for the full trail, or jump to any area. Side branches
(directories, secrets) are detours you take when your job needs them.

## The map

![The Identity Engineering Roadmap: 14 areas, 85 topics and 48 sub-topics laid out as a learning path, with side detours for directories and secrets](assets/roadmap.png)

<details>
<summary>Text version of the map (Mermaid source)</summary>

```mermaid
%%{init: {"flowchart": {"rankSpacing": 28, "nodeSpacing": 30, "subGraphTitleMargin": {"top": 6, "bottom": 10}}}}%%
flowchart TD
  subgraph A01["01 · Primitives"]
    a1["What is an identity?"] --> a2["The parties: user, workload, resource, agent"] --> a3["Accounts"] --> a4["Identifiers & account linking"] --> a5["Directories & groups"] --> a6["Subject vs. actor"] --> a7["Authority, realm & trust"] --> a8["Delegation as a primitive"]
    a4 -.-> a4a["Pairwise identifiers & data minimization"]
  end
  subgraph A02["02 · Authentication"]
    b1["Assurance levels: IAL, AAL, FAL"] --> b2["Passwords"] --> b3["Sessions & cookies"] --> b4["Multi-factor"] --> b5["Account recovery"] --> b6["Phishing-resistant: FIDO2, WebAuthn, passkeys"] --> b7["Aside: Kerberos"]
    b3 -.-> b3a["Device-bound sessions: DBSC"]
    b4 -.-> b4a["Step-up authentication: RFC 9470"]
  end
  subgraph A03["03 · Authorization"]
    c1["The authn/authz split"] --> c2["ACL & RBAC"] --> c3["ABAC & XACML"] --> c4["ReBAC & Zanzibar"] --> c5["Policy engines"] --> c6["Interop: AuthZEN"] --> c7["Choosing a model"]
    c5 -.-> c5a["OPA & Rego"] --> c5b["Cedar"] --> c5c["OpenFGA"] --> c5d["Casbin"]
  end
  subgraph A04["04 · Tokens & cryptography"]
    d1["JWT: JWS, JWE, JWK"] --> d2["JWT validation pitfalls & BCP"] --> d3["How JWT was born"] --> d4["Hashing & password storage"] --> d5["Keys, certificates & PKI"] --> d6["Post-quantum watch"]
  end
  subgraph A05["05 · Identity protocols"]
    e1["Before OAuth"] --> e2["OAuth 2.x"] --> e3["OpenID Connect"] --> e4["SAML 2.0"] --> e5["Verifiable credentials"]
    e2 -.-> e2a["OAuth 2.0 roles & grants"] --> e2b["Scopes, audience & consent"] --> e2b2["Authorization requests: JAR & PAR"] --> e2c["PKCE & OAuth 2.1"] --> e2d["Client registration & discovery"] --> e2e["Token lifecycle: introspection & revocation"] --> e2f["Sender-constrained tokens"] --> e2g["OAuth Security BCP"]
    e2d -.-> e2d1["Server metadata: RFC 8414 & RFC 9728"] --> e2d2["Manual registration"] --> e2d3["Dynamic client registration: RFC 7591"] --> e2d4["Client ID Metadata Documents: CIMD"]
    e2e -.-> e2e1["Token formats: opaque, JWT, phantom tokens & macaroons"]
    e2f -.-> e2f1["DPoP: RFC 9449"] --> e2f2["mTLS-bound tokens: RFC 8705"]
    e2g -.-> e2g1["Native apps: RFC 8252"] --> e2g2["Browser-based apps & the BFF pattern"] --> e2g3["FAPI 2.0 security profile"]
    e3 -.-> e3a["ID token & claims"] --> e3b["Authentication flows: code, implicit, hybrid"] --> e3c["Decoupled authentication: CIBA"] --> e3d["UserInfo & standard claims"] --> e3e["OIDC Discovery & registration"] --> e3e2["OpenID Federation 1.0"] --> e3f["Session management & logout"]
    e4 -.-> e4a["SAML 2.0 assertions"] --> e4b["Bindings & profiles"] --> e4c["SAML in the enterprise today"]
    e5 -.-> e5a["Selective disclosure: SD-JWT"] --> e5b["Issuance & presentation: OpenID4VCI & OpenID4VP"]
  end
  subgraph A06["06 · Directories & provisioning"]
    f1["X.500 & LDAP"] --> f2["Active Directory"] --> f3["The sync problem"] --> f4["SCIM"] --> f5["Multi-tenant SaaS: organizations & enterprise SSO"] --> f5b["Identity governance: lifecycle & access reviews"] --> f6["Provisioning non-humans"]
  end
  subgraph A07["07 · Workload & agent identity"]
    g1["Machine identity & SPIFFE"] --> g2["Workload identity federation"] --> g3["Non-human identities"] --> g3b["API keys & static credentials"] --> g4["Attestation: RATS"] --> g5["Agent identity"] --> g6["Agent protocols"] --> g7["Bots on the web: Web Bot Auth & Privacy Pass"] --> g8["Least privilege & audit for agents"] --> g9["Cross-app access: XAA"] --> g10["WIMSE"]
    g2 -.-> g2a["Kubernetes service accounts & projected tokens"] --> g2b["Keyless signing: Sigstore"]
    g6 -.-> g6a["MCP authorization"] --> g6b["AAuth"] --> g6c["A2A"]
  end
  subgraph A08["08 · Delegation & impersonation"]
    h1["Impersonation vs. delegation"] --> h2["The confused deputy"] --> h3["Assume-role"] --> h4["On-behalf-of"] --> h5["Token exchange: RFC 8693"] --> h6["Call chains: transaction tokens & identity chaining"] --> h7["Capabilities & attenuation: macaroons, Biscuit, UCAN"]
  end
  subgraph A09["09 · Privileged access"]
    i1["PAM & just-in-time access"] --> i2["Break-glass access"] --> i3["Human-in-the-loop"] --> i4["Audit trails & attribution"]
  end
  subgraph A10["10 · Zero trust & continuous access"]
    j1["Zero trust architecture"] --> j2["Device identity & posture"] --> j3["Shared Signals & CAEP"] --> j4["Revocation & the kill switch"]
    j1 -.-> j1a["Identity-aware proxies: BeyondCorp"]
  end
  subgraph A11["11 · Threat modeling"]
    k1["Threat modeling identity systems"] --> k2["Identity attack catalog"] --> k3["Case studies: identity breaches"] --> k4["Agentic threats"]
  end
  subgraph A12["12 · Regulations, frameworks & controls"]
    n1["Law, standard, control & audit"] --> n2["ISO/IEC 27001:2022 & the Annex A identity controls"] --> n3["ISO/IEC 42001:2023: AI management systems"] --> n4["SOC 2 & the Trust Services Criteria"] --> n5["US federal: OMB zero trust, NIST CSF 2.0 & the AI RMF"] --> n6["European Union: identity regulation"] --> n7["Sector rules: PCI DSS, HIPAA & open banking"] --> n8["Agentic control catalogs: ATC, CSA AICM & AIUC-1"]
    n6 -.-> n6a["GDPR: identity data as personal data"] --> n6b["eIDAS 2.0 & the EU Digital Identity Wallet"] --> n6c["NIS2 & DORA: access control and MFA as legal duties"] --> n6d["PSD2 & strong customer authentication"] --> n6e["EU AI Act: logging & human oversight"]
  end
  subgraph A13["13 · The practice: living off RFCs"]
    l1["How the IETF works"] --> l2["Reading a spec"] --> l3["Working groups to watch"] --> l4["Choosing an IdP: build, buy, certify"]
  end
  subgraph A14["14 · Secrets & vaults"]
    m1["How a vault works"] --> m2["Dynamic secrets & rotation"] --> m3["Secret zero: vaults vs. workload identity"]
  end

  %% spine (last node of one area -> first node of the next)
  a8 --> b1
  b7 --> c1
  c7 --> d1
  d6 --> e1
  e5 --> g1
  g10 --> h1
  h7 --> i1
  i4 --> j1
  j4 --> k1
  k4 --> n1
  n8 --> l1
  %% side branches
  c7 --> f1
  f6 --> g1
  g10 --> m1
```

</details>

## Areas

| # | Area | Covers |
|---|---|---|
| 01 | [Primitives](roadmap/01-primitives/README.md) | identity, parties, accounts, identifiers & account linking, groups, subject vs. actor, authority & trust |
| 02 | [Authentication](roadmap/02-authentication/README.md) | assurance levels, passwords, sessions (DBSC), MFA & step-up, account recovery, FIDO2/WebAuthn/passkeys |
| 03 | [Authorization](roadmap/03-authorization/README.md) | RBAC, ABAC, ReBAC/Zanzibar, policy engines (OPA, Cedar, OpenFGA, Casbin), AuthZEN |
| 04 | [Tokens & cryptography](roadmap/04-tokens-and-cryptography/README.md) | JWT/JOSE, validation, hashing, PKI, post-quantum |
| 05 | [Identity protocols](roadmap/05-identity-protocols/README.md) | OAuth 2.x (grants, scopes & consent, PKCE, registration & metadata, JAR & PAR, token formats, DPoP & mTLS, security BCP, native/browser apps, FAPI), OpenID Connect (ID token, flows, CIBA, UserInfo, discovery & federation, logout), SAML 2.0, verifiable credentials (SD-JWT, OpenID4VC) |
| 06 | [Directories & provisioning](roadmap/06-directories-and-provisioning/README.md) | LDAP, Active Directory, SCIM, multi-tenant SaaS, identity governance & access reviews, provisioning non-humans |
| 07 | [Workload & agent identity](roadmap/07-workload-and-agent-identity/README.md) | SPIFFE, federation (Kubernetes, Sigstore), NHI, API keys, attestation, agent identity & protocols, web bots, XAA, WIMSE |
| 08 | [Delegation & impersonation](roadmap/08-delegation-and-impersonation/README.md) | confused deputy, assume-role, on-behalf-of, RFC 8693, call chains, capabilities |
| 09 | [Privileged access](roadmap/09-privileged-access/README.md) | PAM, just-in-time, break-glass, human-in-the-loop, audit trails |
| 10 | [Zero trust & continuous access](roadmap/10-zero-trust-and-continuous-access/README.md) | SP 800-207, device posture, BeyondCorp, Shared Signals, CAEP, revocation |
| 11 | [Threat modeling](roadmap/11-threat-modeling/README.md) | identity threat model, attack catalog, breach case studies, agentic threats |
| 12 | [Regulations, frameworks & controls](roadmap/12-regulations-and-frameworks/README.md) | law vs standard vs control, ISO 27001 & 42001, SOC 2, OMB/NIST CSF/AI RMF, EU (GDPR, eIDAS 2.0, NIS2, DORA, PSD2, AI Act), PCI DSS & HIPAA, agentic control catalogs |
| 13 | [The practice: living off RFCs](roadmap/13-standards-watch/README.md) | IETF, reading specs, working groups, choosing an IdP |
| 14 | [Secrets & vaults](roadmap/14-secrets-and-vaults/README.md) | vaults, dynamic secrets, secret zero |

## How to read a topic

Each topic is one short page: a **TL;DR** paragraph written for a developer new to identity,
then the dense version (what it is, why it exists, what AI agents change), then its
**Resources**. Resources are tagged. `@official@` is the spec, RFC, standard, or vendor
documentation that defines the thing. `@article@` is an explainer, `@video@` a talk,
`@paper@` a paper. Read the official one first. A topic with nothing to cite yet says so
instead of guessing.

Some topics have sub-topics: the parts of one thing (OAuth 2.x has its grants, PKCE, DPoP and
security BCP). They hang off their topic on the map and sit indented under it in the area page. A sub-topic can
have parts of its own, one level down (Client registration: manual, RFC 7591, CIMD).

## Contributing

Add a resource, fix wording, or propose a topic. See [CONTRIBUTING.md](CONTRIBUTING.md).
Nothing here is written from memory: every claim has a resource behind it, and history
claims stay flagged until they are backed by evidence.
