# Keyless signing: Sigstore

**TL;DR:** Sigstore's keyless mode signs a software artifact, such as a container image,
without maintaining a long-lived signing key. Cosign generates a fresh key pair, obtains an
OIDC token for the CI job or maintainer, and sends the public key and token to Fulcio. Fulcio
verifies the token and returns a ten-minute certificate whose identity derives from the token.
The signature and certificate are recorded through Rekor's append-only transparency log, and
the private key is discarded. A verifier checks the expected certificate identity and OIDC
issuer instead of pinning a signer key. A SLSA provenance attestation records which build
platform executed a build definition to produce the artifact; higher SLSA levels require
platform-signed provenance.

Sigstore removes the long-lived signing key: a client such as Cosign generates an ephemeral key pair, sends the public key with an OIDC token to Fulcio, and Fulcio verifies the token and issues an X.509 certificate valid for ten minutes whose subject alternative name is the token's identity, a maintainer's email or, for a CI job, the workflow itself (`https://github.com/<org>/<repo>/.github/workflows/<file>@refs/heads/<branch>`, issuer `https://token.actions.githubusercontent.com`). Signature and certificate are recorded in Rekor, an append-only transparency log, the private key is discarded, and a verifier checks for the `certificate-identity` and `certificate-oidc-issuer` it expects rather than for a key it was handed. The artifact therefore carries the [workload identity](workload-identity-federation.md) that built it, and SLSA provenance (an attestation describing which build platform executed which build definition; Build L2 requires it signed by a hosted platform and Build L3 keeps signing secrets out of reach of user-defined build steps) is the standard statement of what that identity did.

## Resources

- [@official@Sigstore documentation](https://docs.sigstore.dev/)
- [@official@SLSA specification v1.2](https://slsa.dev/spec/v1.2/)

---

[← Workload identity federation](workload-identity-federation.md) · [07 · Workload & agent identity](README.md) · [Map](../../README.md)
