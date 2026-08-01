# Claim 1 protocol

Exact live claim: proxy labels use model labels below a calibrated uncertainty threshold and expert labels above it, guaranteeing mean loss at most epsilon with probability at least 1-alpha.

Attempt 1 will construct a finite binary-label population, use held-out calibration to choose the uncertainty threshold, route high-uncertainty examples to exact expert labels, calculate population error, and compare with a deliberately under-calibrated threshold control. It will retain seeds, raw arrays, and exact confidence criterion. This is not a theorem proof unless it independently validates all Theorem 2.1 conditions.
