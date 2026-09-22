# SourceVerifier — Intelligent Contract Submission

## Summary

SourceVerifier is a reusable GenLayer Intelligent Contract that verifies a factual claim against two independent public web sources and stores a consensus-backed verdict on-chain.

## Repository

https://github.com/maho0638/sourceverifier-genlayer

## Contract source

https://github.com/maho0638/sourceverifier-genlayer/blob/main/contracts/source_verifier.py

## Why it needs GenLayer

The contract:
- fetches live public web content,
- semantically compares evidence with a natural-language claim,
- asks an LLM for a structured judgment,
- independently re-runs the evaluation in validator execution,
- reaches consensus over a non-deterministic result.

## Tests

https://github.com/maho0638/sourceverifier-genlayer/blob/main/tests/direct/test_source_verifier.py

## Live Studionet verification

Contract:
https://explorer-studio.genlayer.com/address/0x393a60abeCaB5caCe6b084387AfBbA58c8227D1A

Contract address:
`0x393a60abeCaB5caCe6b084387AfBbA58c8227D1A`

Live transaction:
https://explorer-studio.genlayer.com/tx/0xde4bfb0a2143562e434490445fb7b55184a8b2a886fa54b4c13a90d8964b9303

Transaction hash:
`0xde4bfb0a2143562e434490445fb7b55184a8b2a886fa54b4c13a90d8964b9303`

Studionet workflow:
https://github.com/maho0638/sourceverifier-genlayer/actions/runs/35791814646

Live claim:
`example.com is intended for use in documentation examples.`

Sources:
- https://example.com
- https://www.iana.org/help/example-domains

Consensus-backed stored result:
- verdict: `supported`
- confidence: `100/100`
- sources_agree: `2/2`
- consensus: `MAJORITY_AGREE`

The standalone repository includes direct tests, GenVM lint/validation CI, and a reproducible Studionet deployment workflow.
