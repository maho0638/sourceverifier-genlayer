# Evidence Integrity Suite

This branch expands the original SourceVerifier into a reusable GenLayer evidence-safety catalog. The accepted SourceVerifier remains unchanged; the new contracts are separate primitives with distinct APIs and failure modes.

## Why this suite exists

A single claim verifier is useful, but production systems need more than a yes/no answer. They need corroboration thresholds, conflict detection, source-independence checks, citation provenance, policy checks, material-change monitoring, explicit abstention, auditable decision receipts, and a fresh challenge path.

The suite therefore focuses on **evidence integrity and safe refusal**, not on repackaging the original contract.

## Contracts

1. **SourceVerifier** — existing two-source factual claim verifier.
2. **EvidenceQuorum** — three-source verifier with a deterministic 2-of-3 threshold.
3. **ContradictionResolver** — measures material factual conflict between sources.
4. **CitationAttestor** — binds a claim verdict to a bounded evidence excerpt.
5. **SourceIndependenceGuard** — detects mirrors, syndication and common-origin evidence.
6. **PolicyComplianceVerifier** — evaluates a public artifact against a plain-language policy.
7. **ChallengeableAttestation** — initial attestation plus one fresh challenge round before finalization.
8. **WebChangeMonitor** — detects material semantic drift from a stored baseline.
9. **EvidenceActionRouter** — routes evidence to EXECUTE, REVIEW or ABSTAIN using support/confidence thresholds.
10. **DecisionReceipt** — creates an auditable decision record with the exact evidence URLs used.

## Safety design shared by the suite

- public HTTPS evidence only;
- source text is explicitly treated as untrusted data;
- structured JSON output with bounded fields;
- validator re-execution of semantic decisions;
- deterministic thresholds after consensus;
- duplicate IDs rejected;
- explicit insufficient/abstain paths instead of forced guesses;
- no production deployment is claimed until live Studionet proof exists.

## Verification plan

Before submission:

1. all direct tests must pass;
2. every contract must pass GenVM lint;
3. selected flagship contracts must be deployed to Studionet;
4. live writes/reads must be recorded;
5. deployment addresses and transactions must be pinned in a proof manifest;
6. only then prepare the Portal contribution.

This branch is development-only until those gates pass.
