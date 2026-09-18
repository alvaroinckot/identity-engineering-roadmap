# EU AI Act: logging & human oversight

**TL;DR:** The Artificial Intelligence Act (Regulation (EU) 2024/1689) sets requirements for
"high-risk" AI systems. Annex III lists candidate high-risk uses, subject to the Art. 6(3)
derogation, including remote biometric identification, recruitment screening and
creditworthiness scoring; point 1(a) excludes biometric verification whose sole purpose is
confirming that a person is who they claim to be, and point 5(b) excludes fraud detection.
Providers must build high-risk systems that automatically record events over their lifetime and
can be effectively overseen by people, with the Art. 14(4) capabilities enabled as appropriate
and proportionate. Deployers must assign oversight to competent people with authority and keep
the logs under their control for at least six months unless Union or national law provides
otherwise. For high-risk systems within these provisions, logging and human oversight are legal
requirements.

Art. 12(1) requires that high-risk systems "technically allow for the automatic recording of
events (logs) over the lifetime of the system", and for remote biometric identification Art.
12(3) requires logging the start and end of each use; Art. 14(1) requires design such that
systems "can be effectively overseen by natural persons", Art. 14(4) names the capabilities to
be enabled "as appropriate and proportionate" — awareness of "automation bias", the ability to
"disregard, override or reverse the output", a "‘stop’ button or a similar procedure" — and
Art. 14(5) forbids acting on an Annex III point 1(a) identification unless it is "separately
verified and confirmed by at least two natural persons", except for law-enforcement, migration,
border-control or asylum uses where Union or national law considers that disproportionate; Art.
26(2) makes deployers "assign human oversight to natural persons who have the necessary
competence, training and authority", and Art. 26(6) makes them keep the logs, to the extent
under their control, for "at least six months" unless applicable Union or national law provides
otherwise. Annex III, the list of "High-risk AI systems referred to in Article 6(2)", covers
remote biometric identification in point 1(a) but excludes verification "the sole purpose of
which is to confirm that a specific natural person is the person he or she claims to be",
covers recruitment screening in point 4(a) and creditworthiness scoring in point 5(b) with an
exception for systems used to detect financial fraud, and under Art. 6(3) a listed system is
not high-risk where it does not pose a significant risk of harm — so, among identity-related
systems, the listed uses such as remote biometric identification are in scope, not the login
itself. These are the controls area 09 treats as engineering practice — [human in the
loop](../09-privileged-access/human-in-the-loop.md) and [audit trails &
attribution](../09-privileged-access/audit-trails-attribution.md) — and they apply as legal
requirements when a system is classified as high-risk under Art. 6 and Annex III.

_Not legal advice. Obligations and dates are quoted as published on 2026-09-17; check the
official text before relying on them._

## Resources

- [@official@Regulation (EU) 2024/1689 (AI Act) — Art. 12 logging, Art. 14 human oversight, Art. 26 deployer duties, Annex III, Art. 113](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)

---

[← European Union: identity regulation](eu-identity-regulation.md) · [12 · Regulations, frameworks & controls](README.md) · [Map](../../README.md)
