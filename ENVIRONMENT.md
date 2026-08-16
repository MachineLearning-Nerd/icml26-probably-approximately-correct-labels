# Environment and run provenance

## Claim 1 command

    .venv/bin/python src/claim1_proxy_label_calibration.py --out outputs/claim1_proxy_label_calibration --seeds 101 202 303 404 505
    (cd outputs/claim1_proxy_label_calibration && sha256sum -c SHA256SUMS)

The cleanup verifier does not rerun this command or the full test suite.

## Recorded run

| Field | Value |
| --- | --- |
| Scope | Local CPU clean-room synthetic binary proxy-label fixture |
| Seeds | `101`, `202`, `303`, `404`, `505` |
| Calibration / evaluation population | `5,000` / `50,000` examples |
| Target error / confidence | `epsilon=0.05`, `alpha=0.05` |
| Method | Held-out Hoeffding-UCB threshold selection |
| Python dependency | Standard library only |
| Current inspection environment | Python `3.14.6`, Darwin `25.5.0` arm64 |
| Remote/paid compute | none |
| Claim 1 verdict | `TOY_FINITE_AUDIT` |

The retained run log records the command and the output files but not a complete interpreter and platform fingerprint; the current environment row is therefore informational rather than a claim about the historical run.

## Evidence paths

- Source pin: `evidence/source/`
- Claim context: `evidence/claim1_attempt1/`
- Human-readable result: `logbook/claim-1.md`
- Raw outputs: `outputs/claim1_proxy_label_calibration/`
- Contract: `contract/live_claims.json` and `contract/contract_manifest.json`
- Standardized ledger: `claims.json`
- Selected hash record: `EVIDENCE_MANIFEST.json`

Claims 2–5 remain unstarted. No remote, paid, or benchmark-scale run was authorized for this documentation cleanup.
