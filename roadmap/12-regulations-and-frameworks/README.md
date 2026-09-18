# 12 · Regulations, frameworks & controls

Everything before this area is technique: protocols, tokens, policies, threat models. This
area is about obligation: the laws that bind an identity system by jurisdiction or sector, the
standards a contract or a regulator can cite, the control catalogs that turn both into
checkable statements, and the audits that produce evidence. The vocabulary comes first, because
"compliant" means four different things depending on whether a law, a standard, a control or an
auditor's report is speaking. Then the two ISO management-system standards that most control
catalogs anchor to, the SOC 2 attestation most SaaS buyers ask for, the US federal path from
NIST guidance to binding OMB memoranda, the European Union's regulations and directives that
reach identity systems directly, the sector rules for card data, health data and open banking,
and finally the control catalogs written for AI agents.

_Not legal advice. This area describes what published texts say as of 2026-09-17. Regulations,
implementing acts and standards change; application dates move; national transpositions
differ. Check the official text (EUR-Lex, eCFR, the Federal Register, the publisher's own site)
before relying on anything here. ISO standards are paywalled: only ISO's free catalogue and
preview pages are cited, and Annex A numbers quoted from a control catalog are that catalog's
wording, not ISO's text._

## Topics

1. [Law, standard, control & audit](law-standard-control-audit.md)
2. [ISO/IEC 27001:2022 & the Annex A identity controls](iso-iec-27001.md)
3. [ISO/IEC 42001:2023: AI management systems](iso-iec-42001.md)
4. [SOC 2 & the Trust Services Criteria](soc-2-trust-services-criteria.md)
5. [US federal: OMB zero trust, NIST CSF 2.0 & the AI RMF](us-federal-omb-nist-csf-ai-rmf.md)
6. [European Union: identity regulation](eu-identity-regulation.md)
   1. [GDPR: identity data as personal data](gdpr-identity-data.md)
   2. [eIDAS 2.0 & the EU Digital Identity Wallet](eidas-2-eudi-wallet.md)
   3. [NIS2 & DORA: access control and MFA as legal duties](nis2-dora.md)
   4. [PSD2 & strong customer authentication](psd2-strong-customer-authentication.md)
   5. [EU AI Act: logging & human oversight](eu-ai-act.md)
7. [Sector rules: PCI DSS, HIPAA & open banking](sector-rules-pci-dss-hipaa-open-banking.md)
8. [Agentic control catalogs: ATC, CSA AICM & AIUC-1](agentic-control-catalogs.md)

## What AI agents change

Every text in this area was written for human users and conventional software, and every one
of them still applies to an agent: an agent's identity is an identity under ISO/IEC 27001 and
SOC 2, its actions are events to be logged under the AI Act and ISO/IEC 42001, and its access to
card or health data is access under PCI DSS and HIPAA. What is new is the pressure points: an
agent holding a human's delegated authority tests the "unique user identification" and
"person or entity authentication" clauses; an agent that acts without a person in the loop
tests the human-oversight and automated-decision articles; an agent that runs for days tests
every clause about session length, credential rotation and least privilege. The agentic
control catalogs exist because those pressure points were not obvious from the older texts.

---

[← Map](../../README.md)
