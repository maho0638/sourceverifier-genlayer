# SourceVerifier — Intelligent Contract Submission

## Summary

SourceVerifier is a reusable GenLayer Intelligent Contract that verifies a factual claim against two independent public web sources and stores a consensus-backed verdict on-chain.

## Repository

https://github.com/maho0638/sourceverifier-genlayer

## Contract

https://github.com/maho0638/sourceverifier-genlayer/blob/main/contracts/source_verifier.py

## Why it needs GenLayer

The contract:
- fetches live public web content,
- semantically compares evidence with a natural-language claim,
- asks an LLM for a structured judgment,
- independently re-runs the evaluation in validator execution,
- reaches consensus over a non-deterministic result.

## Live verified deployment

The previously verified Studionet deployment of this exact contract logic remains live:

- Contract: https://explorer-studio.genlayer.com/address/0x10F95C997358EfbFfc586979ED8E4c6568609B5c
- Address: `0x10F95C997358EfbFfc586979ED8E4c6568609B5c`
- Live tx: https://explorer-studio.genlayer.com/tx/0xdff346bd4b4bd87546b577879c25f0f9ee805e2dd1d629d4263776aef6d2086d
- Tx hash: `0xdff346bd4b4bd87546b577879c25f0f9ee805e2dd1d629d4263776aef6d2086d`

Live result:
- verdict: `supported`
- confidence: `98/100`
- sources_agree: `2/2`
- consensus: `MAJORITY_AGREE`

This standalone repository contains its own CI and Studionet workflow so the same contract can be independently retested and redeployed.
