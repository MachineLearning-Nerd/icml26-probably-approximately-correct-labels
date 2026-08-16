# Source and local feasibility audit

Pinned arXiv 2506.10908 source and PDF are checksum-retained. The source contains the PAC-label setup and Theorem 2.1 (main.tex lines 304--318): proxy labels use model predictions below a calibrated uncertainty threshold and expert labels above it. The pinned archive contains TeX and figures only; the separate official implementation is recorded in tijana-zrnic/pac-labels at observed main tip b415b58756b14b384529ac9cf146bd5d4c8139aa.

**Local feasibility:** Claim 1 admits a clean-room finite Bernoulli calibration/proxy-label experiment on local CPU, with exact error and confidence calculations. This audit does not execute the official code or claim complete model/data/output pins for the GPT/ResNet/AlphaFold benchmark claims. No HF compute is authorized.
