# Partial reproduction report

## Conclusion

Machine-readable overall verdict: `PARTIAL_CLAIM_1_TOY_CLAIMS_2_TO_5_UNSTARTED`.
`publication_allowed=false`, `score_claim=false`, and
`official_author_endorsement=false`.

The current evidence supports one narrow qualitative result: a held-out uncertainty threshold selected on a synthetic binary calibration sample produces proxy labels whose realized error is at most `epsilon=0.05` in all five retained finite populations. The result is labeled `TOY_FINITE_AUDIT`.

Claims 2–5 are not reproduced. The repository does not claim the paper's multicalibration result, PAC-router result, GPT-4o/Claude savings, ResNet-152 savings, continuous-label savings, or AlphaFold result.

## What the current evidence shows

- Mean calibrated loss: `0.011924`.
- Mean under-calibrated-control loss: `0.090008`.
- Calibrated runs at or below epsilon: `5 / 5`.
- Under-calibrated controls above epsilon: `5 / 5`.
- The control routes fewer examples to the expert by increasing the selected threshold.

## Boundaries

- The fixture is synthetic and uses a Hoeffding upper bound, not the paper's full source-faithful implementation.
- The toy result cannot establish a distribution-free theorem or recover any benchmark number.
- Official author code exists in `tijana-zrnic/pac-labels`, but it was not executed in this audit.
- Collection cleanup preserves the partial status and does not substitute proprietary model outputs, task data, expert labels, or remote compute.
