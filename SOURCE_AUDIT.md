# Source and paper audit

## Paper identity

- Title: *Probably Approximately Correct Labels*
- Authors: Emmanuel J. Candès, Andrew Ilyas, and Tijana Zrnic
- arXiv: [2506.10908](https://arxiv.org/abs/2506.10908); the live arXiv record is version 3, last revised 2025-10-18.
- OpenReview: [Yhv4d8wfbi](https://openreview.net/forum?id=Yhv4d8wfbi)
- Submission number: `19651`

The paper proposes using model predictions for low-uncertainty examples and expert labels for high-uncertainty examples, with a nonasymptotic average-error guarantee. It also studies multicalibration, a multi-model PAC router, and text, image, continuous-label, and protein-folding applications. The current repository audits only a reduced finite mechanism.

## Pinned source records

| Source | Record |
| --- | --- |
| Source archive | `evidence/source/arxiv_source.tar.gz` |
| Archive SHA-256 | `0d4ea33f63c846648d01c8d597cd0564f3d7331982cb04e8c3801051fa296bd5` |
| PDF | `evidence/source/paper.pdf` |
| PDF SHA-256 | `39a7b844fc0f252a054fe4c106bd3a382f0b5636f042380543893aa055608181` |
| Source/contract retrieval | `2026-08-01T22:30:37Z` |
| Contract manifest | `contract/contract_manifest.json`, SHA-256 `2d35608d5efc4d673c8cf6de67dce196fea08319b526cf175ba4426516f84839` |

## Official implementation provenance

The author publication page links the public [tijana-zrnic/pac-labels](https://github.com/tijana-zrnic/pac-labels) repository as the official code release. Its observed `main` tip on 2026-08-17 was `b415b58756b14b384529ac9cf146bd5d4c8139aa`; the repository contains calibration and router notebooks, `pac_utils.py`, router utilities, example datasets, and `requirements.txt`.

This audit does not execute or modify the official repository. The current Claim 1 result is independent clean-room code. The workspace does not yet pin an official checkout together with the paper's model outputs, expert labels, prompts, or benchmark result files, so Claims 2–5 remain unstarted.

## Local implementation provenance

The source archive is retained for paper inspection. The local producer in `src/` uses only the Python standard library and creates a synthetic binary population; it is not presented as author code.

## Version and claim boundaries

- Claim 1 is a qualitative finite proxy for the threshold-and-calibration mechanism, not a theorem proof.
- Claims 2–5 retain the live contract statements but have no current evidence.
- The official code link is recorded separately from the clean-room evidence so provenance is not conflated.
- No proprietary model output, expert-label file, task dataset, or benchmark checkpoint is silently substituted.
