# SourceVerifier — Reusable GenLayer Intelligent Contract

SourceVerifier is a standalone GenLayer Intelligent Contract for verifying a factual claim against **two independent public web sources** and storing a consensus-backed verdict on-chain.

## What it does

`verify_claim(verification_id, claim, source_url_1, source_url_2)`

1. Fetches both HTTPS sources with `gl.nondet.web.render`.
2. Evaluates only the supplied evidence with an LLM.
3. Produces `supported`, `contradicted`, or `insufficient`.
4. Re-runs the evaluation during validator execution.
5. Requires validator agreement on the verdict and source-agreement count.
6. Stores the result, confidence, rationale, claim, sources, and creator on-chain.

## Why GenLayer

A deterministic smart contract cannot fetch arbitrary webpages and reason about their meaning. SourceVerifier uses GenLayer for live web access, LLM-based semantic evaluation, non-deterministic execution, and validator consensus.

## Safety properties

- HTTPS-only sources
- two different source URLs required
- duplicate verification IDs rejected
- bounded claim, ID, confidence, and rationale
- source text treated as untrusted evidence
- validators independently recompute the result
- exact agreement on verdict and source-agreement count
- bounded confidence variance

## Live Studionet deployment

This standalone repository deployed and verified SourceVerifier on GenLayer Studionet:

- Contract: `0x393a60abeCaB5caCe6b084387AfBbA58c8227D1A`
- Explorer: https://explorer-studio.genlayer.com/address/0x393a60abeCaB5caCe6b084387AfBbA58c8227D1A
- Live verification tx: `0xde4bfb0a2143562e434490445fb7b55184a8b2a886fa54b4c13a90d8964b9303`
- Transaction: https://explorer-studio.genlayer.com/tx/0xde4bfb0a2143562e434490445fb7b55184a8b2a886fa54b4c13a90d8964b9303
- Workflow: https://github.com/maho0638/sourceverifier-genlayer/actions/runs/35791814646

Verified live result:

- verdict: `supported`
- confidence: `100/100`
- sources agreeing: `2/2`
- consensus: `MAJORITY_AGREE`

## Files

- Contract: `contracts/source_verifier.py`
- Direct tests: `tests/direct/test_source_verifier.py`
- Live Studionet test: `tests/integration/test_source_verifier_studionet.py`
- Submission evidence: `SUBMISSION.md`
