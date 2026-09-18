# Post-quantum watch

**TL;DR:** Post-quantum cryptography is the set of public-key algorithms designed to stay
secure against a quantum computer, and NIST has published standards for it: FIPS 203 ML-KEM for
key establishment, FIPS 204 ML-DSA and FIPS 205 SLH-DSA for digital signatures. Many deployed
signatures and key-establishment mechanisms use algorithms NIST classifies as
quantum-vulnerable. NIST's position is to begin applying the new standards now; a draft, NIST
IR 8547, proposes deprecating quantum-vulnerable algorithms and removing them from NIST
standards by 2035, with high-risk systems moving earlier. Falcon and HQC are still in
standardization. The work today is an inventory: know which algorithms your services sign and
encrypt with, and plan their replacement with algorithms NIST says can be put into use now.

Track FIPS 203, 204 and 205; NIST says organizations should begin migrating now by
inventorying quantum-vulnerable algorithms and planning their replacement ahead of the 2035
transition deadline proposed in draft NIST IR 8547.

## Resources

- [@official@NIST Post-Quantum Cryptography Project](https://csrc.nist.gov/projects/post-quantum-cryptography)

---

[← 04 · Tokens & cryptography](README.md) · [Map](../../README.md)
