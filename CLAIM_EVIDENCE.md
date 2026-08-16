# Claim-to-evidence ledger

This repository is a deliberately partial audit. Claim 1 has a reduced synthetic result labeled `TOY_FINITE_AUDIT`; Claims 2–5 have no reproduction result and remain `UNSTARTED`.

## Claim 1 — Theorem 2.1 — TOY_FINITE_AUDIT

- Contract: proxy labels use model predictions below a calibrated uncertainty threshold and expert labels above it, with a high-probability average-error target.
- Producer: `src/claim1_proxy_label_calibration.py`.
- Evidence: `outputs/claim1_proxy_label_calibration/summary.json`, `results.csv`, `config.json`, and `SHA256SUMS`.
- Method: five independent synthetic binary populations; 5,000 held-out expert labels calibrate a one-sided Hoeffding upper bound at `epsilon=0.05` and `alpha=0.05`; 50,000 fresh examples measure routed loss.
- Positive result: mean calibrated loss `0.011924`; all five calibrated populations are at or below epsilon.
- Negative control: adding `0.70` to the selected threshold routes fewer examples to the expert; mean loss is `0.090008`, and all five controls exceed epsilon.
- Boundary: this is a finite mechanism audit, not an independent proof of Theorem 2.1 and not a reproduction of the paper's model or benchmark experiments.

## Claim 2 — Section 2.1 — UNSTARTED

- Contract: uncertainty calibration is adjusted across feature or demographic subgroups through multicalibration.
- Intended producer: the official calibration notebook or an independently reconstructed implementation with the paper's groups, bins, tolerance, calibration split, and baseline.
- Current evidence: none. No subgroup calibration or budget comparison is claimed.

## Claim 3 — Section 3 — UNSTARTED

- Contract: a PAC router selects among candidate models using a learned weighting function, a differentiable sigmoid threshold relaxation, and implicit gradients.
- Intended producer: the router notebook or a source-faithful reconstruction using pinned model outputs, uncertainties, costs, and hard-routing evaluation.
- Current evidence: none. The toy threshold fixture does not implement the router.

## Claim 4 — Benchmark tables — UNSTARTED

- Contract: single-model PAC labeling produces the reported expert-label savings across text, image, and continuous-label tasks.
- Intended producer: pinned datasets, model versions, prompts or preprocessing, expert labels, uncertainty definitions, confidence-bound routine, repeated evaluation, and cost denominator.
- Current evidence: none. No GPT-4o, ResNet-152, or AlphaFold benchmark number is reproduced here.

## Claim 5 — Router benchmark — UNSTARTED

- Contract: routing between GPT-4o and Claude 3.7 produces the reported budget and cost savings.
- Intended producer: pinned model outputs, confidence scores, source costs, router training data, expert labels, and the cost-sensitive evaluation protocol.
- Current evidence: none. No multi-model router result is claimed.

## Aggregate verdict

The only supported result is the reduced synthetic Claim 1 fixture. The repository must not be described as a complete reproduction until Claims 2–5 receive independent evidence, exact source pins, and explicit controls.
