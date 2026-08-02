# Claim 1 — calibrated proxy labels

**Live claim.** The method uses model labels below a calibrated uncertainty threshold and expert labels above it, guaranteeing average labeling error at most epsilon with probability at least 1-alpha.

## Scope and protocol

This is a clean-room **toy** experiment, not an independent proof of Theorem 2.1. It uses a synthetic binary population whose model error increases with uncertainty. For each of five fixed seeds, 5,000 expert-labelled calibration examples choose the largest uncertainty threshold whose one-sided Hoeffding error upper bound is at most `epsilon=0.05` at `alpha=0.05`. A separate population of 50,000 examples receives model labels at or below that threshold and exact expert labels above it.

Source context is retained in `evidence/claim1_attempt1/theorem_excerpt.txt`; source hashes are in `evidence/source/SHA256SUMS`.

## Commands and evidence

```bash
python3 src/claim1_proxy_label_calibration.py \
  --out outputs/claim1_proxy_label_calibration --seeds 101 202 303 404 505
(cd outputs/claim1_proxy_label_calibration && sha256sum -c SHA256SUMS)
```

Raw rows: `outputs/claim1_proxy_label_calibration/results.csv`; configuration and aggregate: `config.json`, `summary.json`.

## Result and control

All five calibrated runs satisfy the finite population criterion. Mean proxy-label error is **0.011924**, below 0.05; the mean routed-to-expert fraction is about 0.553. The negative control raises the threshold by 0.70 (routing fewer examples to expert); it routes no examples in these fixtures and has mean error **0.090008**, exceeding 0.05 in all five runs.

**Verdict: toy.** This demonstrates the stated routing mechanism and an expected failure under deliberate under-calibration on a finite synthetic setting. It does not establish the theorem's distribution-free nonasymptotic guarantee or reproduce the paper's benchmark experiments.
