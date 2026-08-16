# Repository status

Paper: Probably Approximately Correct Labels
Authors: Emmanuel J. Candès, Andrew Ilyas, and Tijana Zrnic
Primary source: arXiv:2506.10908
OpenReview ID: Yhv4d8wfbi
Submission number: 19651
Collection label: ICML 2026
Live claim count / maximum points: 5 / 10
Selection timestamp: 2026-08-01T22:30:37Z

Former GitHub repository: https://github.com/MachineLearning-Nerd/icml26-repro-Yhv4d8wfbi-probably-approximately-correct-labels
Target GitHub repository: https://github.com/MachineLearning-Nerd/icml26-probably-approximately-correct-labels
Canonical branch: main

Current phase: claim_1_attempt_1_local_proxy_label_toy_complete_with_standardized_dossier
Publication status: normalized GitHub repository with standardized dossier; stale master branch removed
Compute policy: local CPU and local GPU only; no Hugging Face, Jobs, paid, or remote compute

Source pins:

- Contract manifest SHA-256: 2d35608d5efc4d673c8cf6de67dce196fea08319b526cf175ba4426516f84839
- Pinned arXiv source archive SHA-256: 0d4ea33f63c846648d01c8d597cd0564f3d7331982cb04e8c3801051fa296bd5
- Pinned arXiv PDF SHA-256: 39a7b844fc0f252a054fe4c106bd3a382f0b5636f042380543893aa055608181
- Source/contract retrieval timestamp: 2026-08-01T22:30:37Z

Official code/data status:

- No code is present in the pinned arXiv source archive.
- The official author implementation is https://github.com/tijana-zrnic/pac-labels, observed at b415b58756b14b384529ac9cf146bd5d4c8139aa on 2026-08-17.
- No official checkout together with complete model, dataset, prompt, expert-label, or benchmark-output pins is available in this workspace.
- The current implementation is independent clean-room audit code.

Claim status:

- Claim 1 / Theorem 2.1: TOY_FINITE_AUDIT; five synthetic runs pass the finite epsilon criterion and five under-calibrated controls fail
- Claim 2 / uncertainty multicalibration: UNSTARTED
- Claim 3 / PAC router: UNSTARTED
- Claim 4 / single-model benchmark savings: UNSTARTED
- Claim 5 / multi-model router savings: UNSTARTED

The normalized repository preserves the source snapshot and finite toy evidence while clearly separating them from the official implementation and the missing benchmark assets and theorem-level verification. The standardized dossier records the claim producers, evidence paths, branch inventory, citation, and author acknowledgement.
