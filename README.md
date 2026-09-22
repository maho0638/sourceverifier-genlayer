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

The original verified deployment remains live on GenLayer Studionet:

- Contract: `0x10F95C997358EfbFfc586979ED8E4c6568609B5c`
- Explorer: https://explorer-studio.genlayer.com/address/0x10F95C997358EfbFfc586979ED8E4c6568609B5c
- Live verification tx: `0xdff346bd4b4bd87546b577879c25f0f9ee805e2dd1d629d4263776aef6d2086d`
- Transaction: https://explorer-studio.genlayer.com/tx/0xdff346bd4b4bd87546b577879c25f0f9ee805e2dd1d629d4263776aef6d2086d

Verified live result:

- verdict: `supported`
- confidence: `98/100`
- sources agreeing: `2/2`
- consensus: `MAJORITY_AGREE`

This repository also includes an independent Studionet workflow so the contract can be redeployed and verified again from this standalone repository.
