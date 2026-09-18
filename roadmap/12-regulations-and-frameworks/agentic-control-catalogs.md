# Agentic control catalogs: ATC, CSA AICM & AIUC-1

**TL;DR:** A control catalog publishes control objectives or requirements together with
mappings or crosswalks to standards and frameworks such as ISO/IEC 42001 or 27001; unlike a
protocol specification it defines no wire format. This page compares two expressly agent-
focused catalogs with the Cloud Security Alliance's matrix for cloud-based AI systems. Agentic
Trust Controls (ATC) is a control catalog written for AI agents that maps its controls to
ISO/IEC 42001:2023 and ISO/IEC 27001:2022; it is not yet publicly published. CSA's AI Controls
Matrix v1.1 has 247 control objectives in 18 domains with mappings to ISO 42001, ISO 27001,
NIST AI RMF 1.0 and BSI AIC4. AIUC-1 is a certification standard for AI agents in six domains,
maintained by the Artificial Intelligence Underwriting Company. None of them is a law.

ISO/IEC 42001 and 27001 state management-system requirements, not agent-specific safeguards, so
these catalogs supply the safeguards and the mapping. ATC, by its own description, separates
controls for the party that builds an agent from controls for the organization that deploys it,
and one of its domains covers agent identity and authority: who an agent is, what it may call,
how privilege is granted and how its actions are evidenced. The catalog had not been published
when this page was written; the description here comes from a pre-release export shared with
the author and should be read with that caveat until the published text can be cited. CSA's
AICM (v1 released 2025-07-09 with 243 objectives, v1.1 on 2026-06-22 with 247) is "freely
available to download" behind an account login and feeds CSA's STAR for AI, described as "an
upcoming certification". AIUC-1 publishes its requirement text openly, including the mandatory
B006 "Prevent unauthorized AI agent actions" and B007 "Enforce user access privileges to AI
systems"; AIUC says certification runs through scoping, evals, audit and certification, that
the audit is conducted by an accredited auditor such as Schellman or Coalfire, and that the
certificate is valid for one year. Related OWASP publications document agentic-AI threats and
non-human-identity risks — the Agentic AI threats-and-mitigations guide and the Non-Human
Identities Top 10 — and AIUC-1 states that its certification "covers all OWASP Agentic Top 10
threats", while CSA's matrix carries a Threat Category pillar. Keep the layers straight: none
of the three is a law, ISO/IEC 42001 is the management-system standard all three map to, AIUC-1
certifies against its own text and CSA's certification is upcoming — see [ISO/IEC 42001:2023:
AI management systems](iso-iec-42001.md).

_Not legal advice. Obligations and dates are quoted as published on 2026-09-17; check the
official text before relying on them._

## Resources

- [@official@Agentic Trust Controls — control catalog for AI agents (not yet publicly published)](https://trustcontrols.ai/)
- [@official@Cloud Security Alliance — AI Controls Matrix (AICM) v1](https://cloudsecurityalliance.org/artifacts/ai-controls-matrix)
- [@official@AIUC-1 — the AI agent security, safety and reliability standard (Artificial Intelligence Underwriting Company)](https://www.aiuc-1.com/)
- [@official@OWASP GenAI Security Project — Agentic AI: Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)
- [@official@OWASP Non-Human Identities Top 10](https://owasp.org/www-project-non-human-identities-top-10/)

---

[← 12 · Regulations, frameworks & controls](README.md) · [Map](../../README.md)
