# ICML 2026 — Probably Approximately Correct Labels

Independent audit workspace for [Probably Approximately Correct Labels](https://arxiv.org/abs/2506.10908).

> Status: partial audit. Claim 1 has a verified finite synthetic proxy-label/calibration fixture labeled TOY. Claims 2–5 are unstarted. No paper-level claim is presented as fully reproduced.

This repository studies how to combine cheap model predictions with expensive expert labels while controlling the average labeling error with high probability. The current evidence checks the routing mechanism on a finite synthetic binary population; it does not reproduce the paper's proprietary-model benchmark results.

## Paper

| Item | Record |
| --- | --- |
| Title | Probably Approximately Correct Labels |
| Authors | Emmanuel J. Candès, Andrew Ilyas, and Tijana Zrnic |
| Paper | [arXiv:2506.10908](https://arxiv.org/abs/2506.10908) |
| OpenReview record | [Yhv4d8wfbi](https://openreview.net/forum?id=Yhv4d8wfbi) |
| Submission number | 19651 |
| Pinned source archive | evidence/source/arxiv_source.tar.gz |
| Source archive SHA-256 | 0d4ea33f63c846648d01c8d597cd0564f3d7331982cb04e8c3801051fa296bd5 |
| Pinned PDF SHA-256 | 39a7b844fc0f252a054fe4c106bd3a382f0b5636f042380543893aa055608181 |
| Current repository | [MachineLearning-Nerd/icml26-probably-approximately-correct-labels](https://github.com/MachineLearning-Nerd/icml26-probably-approximately-correct-labels) |
| Former repository name | icml26-repro-Yhv4d8wfbi-probably-approximately-correct-labels |
| Official author code | [tijana-zrnic/pac-labels](https://github.com/tijana-zrnic/pac-labels) at b415b58756b14b384529ac9cf146bd5d4c8139aa (observed 2026-08-17) |
| Canonical branch | main |

The pinned arXiv source archive contains the paper source and figures but no code. The authors publish a separate official implementation in tijana-zrnic/pac-labels, which contains calibration and router notebooks, utilities, example datasets, and requirements. This audit does not execute that repository or claim that its model outputs, expert labels, prompts, or benchmark artifacts are pinned here. The current Claim 1 scripts are independent clean-room audit code.

## Standardized audit dossier

| File | Purpose |
| --- | --- |
| [CLAIM_EVIDENCE.md](CLAIM_EVIDENCE.md) | Claim-by-claim producers, evidence paths, statuses, and boundaries |
| [SOURCE_AUDIT.md](SOURCE_AUDIT.md) | Paper identity, source pins, and official implementation provenance |
| [BRANCH_AUDIT.md](BRANCH_AUDIT.md) | Final branch inventory and stale-branch disposition |
| [ENVIRONMENT.md](ENVIRONMENT.md) | Reproduction command and run provenance |
| [REPORT.md](REPORT.md) | Concise partial-audit conclusion and limitations |
| [CITATION.cff](CITATION.cff) | Machine-readable citation for this audit |
| [AUTHOR_THANK_YOU.md](AUTHOR_THANK_YOU.md) | Thank-you note to the paper authors |
| [claims.json](claims.json) | Machine-readable claim ledger |
| [EVIDENCE_MANIFEST.json](EVIDENCE_MANIFEST.json) | Selected content hashes and required audit files |
| [verify_final.py](verify_final.py) | Fail-closed local publication verifier |

## What the paper is doing

The method starts with a cheap predicted label and an uncertainty score for every example. It uses a small expert-labeled sample to estimate an upper confidence bound on the error among examples below each uncertainty threshold. It then sends high-uncertainty examples to the expert and uses model labels below the selected threshold. Under a valid upper-bound subroutine, monotonicity yields a nonasymptotic average-error guarantee.

The paper also proposes multicalibration of uncertainty scores across groups and bins, and a PAC router that chooses among multiple models. The router uses a learned weighting function, a differentiable sigmoid relaxation of thresholding, and implicit gradients. Experiments cover text, image, continuous-label, protein-folding, and multi-model routing settings.

## Claim ledger

The live contract has five claims and a maximum of 10 points. Claim numbering below follows contract/live_claims.json and contract/claims_anchored.json.

| Claim | Paper statement | How the claim would be produced | Current status |
| --- | --- | --- | --- |
| 1 / Theorem 2.1 | Proxy labels use model predictions below a calibrated uncertainty threshold and expert labels above it, guaranteeing average error at most epsilon with probability at least 1 minus alpha. | Use a held-out expert-labeled calibration sample, compute a valid one-sided upper confidence bound for each threshold, route high-uncertainty examples to exact labels, and measure population loss. Include a threshold-under-calibration control. | **TOY FINITE AUDIT**: five synthetic binary populations pass the finite epsilon check; this is not a theorem proof. |
| 2 / Section 2.1 | Multicalibration adjusts uncertainty estimates across feature or demographic subgroups. | Recreate the group/bin correction loop, pin the calibration groups and bins, and compare expert-label budgets and error before and after calibration on the same task. | **UNSTARTED** |
| 3 / Section 3 | The PAC router selects among k candidate models with a learned weighting function optimized through a sigmoid relaxation and implicit gradients. | Recreate the routing dataset, model outputs, uncertainty scores, differentiable threshold equation, optimizer, and final hard routing procedure. | **UNSTARTED** |
| 4 / benchmark tables | At epsilon = 0.05, single-model PAC labeling saves 14–28% of expert labels on GPT-4o text tasks, 39–60% on ResNet-152 image tasks, and 16–51% on continuous-label tasks. | Pin the exact datasets, model versions, prompts or preprocessing, expert labels, uncertainty definitions, confidence-bound routine, 50-trial evaluation, and cost denominator. | **UNSTARTED** |
| 5 / router benchmark | Routing GPT-4o and Claude 3.7 yields about 42% budget savings and up to 482% relative cost savings in the cost-sensitive setting. | Pin both model outputs, confidence scores, current relative costs, routing data, learned router, expert labels, and the cost-sensitive evaluation protocol. | **UNSTARTED** |

TOY FINITE AUDIT is deliberately narrower than VERIFIED: it demonstrates the finite mechanism and a negative control, but it does not support the distribution-free theorem or any benchmark number.

## Claim 1: how the current result is produced

The clean-room script in src/claim1_proxy_label_calibration.py generates a synthetic binary population in which model error increases with an observable uncertainty score. For each fixed seed it:

1. Generates 5,000 expert-labeled calibration examples.
2. Selects the largest uncertainty threshold whose one-sided Hoeffding upper bound is at most epsilon = 0.05 at alpha = 0.05.
3. Generates a separate population of 50,000 examples.
4. Uses model labels at or below the threshold and exact expert labels above it.
5. Measures the realized population error and expert-label fraction.
6. Raises the threshold by 0.70 as a deliberately under-calibrated control.

The five seeds are 101, 202, 303, 404, and 505. All five calibrated runs pass the finite epsilon criterion, while all five controls fail:

| Metric | Result |
| --- | ---: |
| Mean calibrated loss | 0.011924 |
| Mean under-calibrated loss | 0.090008 |
| Mean expert fraction for calibrated routing | about 0.5527 |
| Calibrated runs at or below epsilon | 5 / 5 |
| Under-calibrated runs above epsilon | 5 / 5 |

Raw rows, configuration, runtime record, and checksums are in outputs/claim1_proxy_label_calibration/. The source context is in evidence/claim1_attempt1/theorem_excerpt.txt, and the scope decision is recorded in logbook/claim-1.md.

This is a finite synthetic audit. It does not prove that the chosen Hoeffding procedure satisfies every assumption of Theorem 2.1, establish a distribution-free guarantee, or reproduce the GPT-4o, ResNet-152, AlphaFold, or router experiments.

## How the remaining claims should be produced

1. Recover the exact theorem statement, confidence-bound routine, sampling weights, and threshold convention from the pinned source before extending Claim 1.
2. Implement multicalibration with the paper's group definitions, bin count, tolerance, and calibration split; compare against the uncalibrated baseline.
3. Reconstruct the PAC router with the same model outputs and cost definitions. Keep the differentiable training relaxation separate from final hard routing.
4. Treat proprietary model outputs, prompts, task data, and expert labels as missing until they are independently pinned. A substitute benchmark must be labeled as a proxy.
5. Add independent checks and failing controls for error, budget, and cost claims before upgrading any status.

No remote or paid compute is authorized by this repository's current policy. The current Claim 1 run is local CPU only; benchmark-scale work should remain explicitly blocked or use a separately authorized local resource.

## Reproduce the current audit

The repository does not currently include a dependency lockfile or requirements file. A minimal local environment is:

    python3 -m venv .venv
    .venv/bin/python src/claim1_proxy_label_calibration.py --out outputs/claim1_proxy_label_calibration --seeds 101 202 303 404 505
    (cd outputs/claim1_proxy_label_calibration && sha256sum -c SHA256SUMS)
    .venv/bin/pip install pytest
    .venv/bin/python -m pytest -q

The retained run uses only the Python standard library. This collection cleanup does not rerun the experiment or the full test suite.

## Repository map

| Path | Purpose |
| --- | --- |
| contract/metadata.json | Paper, author, OpenReview, and submission metadata |
| contract/live_claims.json | Five live paper claims |
| contract/claims_anchored.json | Anchored claim snapshot |
| contract/contract_manifest.json | Contract hashes and source URLs |
| evidence/source/ | Pinned arXiv source archive, PDF, and source audit |
| evidence/claim1_attempt1/ | Theorem context and evidence checksums |
| src/claim1_protocol.md | Claim 1 scope and protocol |
| src/claim1_proxy_label_calibration.py | Current finite synthetic audit |
| outputs/claim1_proxy_label_calibration/ | Raw results, summary, configuration, log, and checksums |
| tests/ | Contract and Claim 1 tests |
| logbook/claim-1.md | Human-readable Claim 1 result |
| branch-audit.md | Branch inventory and cleanup decision |
| CLAIM_EVIDENCE.md | Standardized claim-to-evidence ledger |
| SOURCE_AUDIT.md | Standardized paper and source audit |
| BRANCH_AUDIT.md | Standardized final branch audit |
| ENVIRONMENT.md | Standardized run provenance |
| REPORT.md | Standardized partial reproduction report |
| CITATION.cff | Machine-readable paper and repository citation |
| AUTHOR_THANK_YOU.md | Author acknowledgement |
| claims.json | Machine-readable claim statuses |
| EVIDENCE_MANIFEST.json | Content-addressed evidence manifest |
| verify_final.py | Final-state verifier |
| STATUS.md | Current paper, claim, and publication status |
| AUTONOMOUS_STATE.json | Machine-readable continuation state |

## Branch policy

The normalized public repository uses one stable branch: main. Before cleanup, main contained the current Claim 1 toy evidence while master was the older default branch without that evidence. The branch inventory and deletion decision are recorded in branch-audit.md and BRANCH_AUDIT.md.

## Citation

Please cite the paper when using this audit:

    @article{candes2025paclabels,
      title = {Probably Approximately Correct Labels},
      author = {Candès, Emmanuel J. and Ilyas, Andrew and Zrnic, Tijana},
      journal = {arXiv preprint arXiv:2506.10908},
      year = {2025},
      doi = {10.48550/arXiv.2506.10908}
    }

## Thank you

Thank you to Emmanuel J. Candès, Andrew Ilyas, and Tijana Zrnic for developing a clear statistical framework for using model predictions without silently treating them as expert labels. The threshold construction, monotonicity argument, and explicit cost trade-off make the central idea auditable on a small finite example. This repository labels its result as partial so future work can extend it without overstating what has been checked.

## Scope and limitations

- Claim 1 covers only five finite synthetic binary populations with a held-out calibration split.
- Claim 1 is not an independent proof of Theorem 2.1.
- Claims 2–5 are not reproduced in the current checkpoint.
- No exact GPT-4o, Claude 3.7, ResNet-152, AlphaFold, dataset, expert-label, or benchmark artifact is pinned here.
- The source archive is retained for paper-level inspection; the separate official code release is recorded in SOURCE_AUDIT.md but is not executed by this audit.
