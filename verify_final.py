#!/usr/bin/env python3
"""Fail-closed verification for the published partial PAC-labels audit."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_REPOSITORY = "MachineLearning-Nerd/icml26-probably-approximately-correct-labels"
CANONICAL_NAME = "MachineLearning-Nerd"
CANONICAL_EMAIL = "37579156+MachineLearning-Nerd@users.noreply.github.com"
EXPECTED_COMMIT_COUNT = 8
EXPECTED_STATUSES = {
    "C1": "TOY_FINITE_AUDIT",
    "C2": "UNSTARTED",
    "C3": "UNSTARTED",
    "C4": "UNSTARTED",
    "C5": "UNSTARTED",
}


def command(*args: str) -> str:
    result = subprocess.run(args, cwd=ROOT, check=True, capture_output=True, text=True)
    return result.stdout


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    failures: list[str] = []
    origin = command("git", "config", "--get", "remote.origin.url").strip()
    if EXPECTED_REPOSITORY not in origin:
        failures.append(f"unexpected origin: {origin}")

    local_branches = set(command("git", "for-each-ref", "--format=%(refname)", "refs/heads").splitlines())
    if local_branches != {"refs/heads/main"}:
        failures.append(f"local branches are {sorted(local_branches)}")
    remote_branches = set(command("git", "for-each-ref", "--format=%(refname)", "refs/remotes/origin").splitlines())
    if remote_branches - {"refs/remotes/origin/HEAD", "refs/remotes/origin/main"}:
        failures.append(f"unexpected remote branches: {sorted(remote_branches)}")
    backup_refs = command("git", "for-each-ref", "--format=%(refname)", "refs/original").splitlines()
    if backup_refs:
        failures.append(f"backup refs remain: {backup_refs}")

    commits = command("git", "rev-list", "main").splitlines()
    if len(commits) != EXPECTED_COMMIT_COUNT:
        failures.append(f"expected {EXPECTED_COMMIT_COUNT} commits, found {len(commits)}")
    if command("git", "rev-parse", "main") != command("git", "rev-parse", "origin/main"):
        failures.append("main and origin/main differ")
    for commit in commits:
        identity = command("git", "show", "-s", "--format=%an%n%ae%n%cn%n%ce", commit).splitlines()
        if identity != [CANONICAL_NAME, CANONICAL_EMAIL, CANONICAL_NAME, CANONICAL_EMAIL]:
            failures.append(f"non-canonical identity at {commit[:12]}")
            break
    if "co-authored-by:" in command("git", "log", "main", "--format=%B").lower():
        failures.append("co-author trailer found")

    manifest = json.loads((ROOT / "EVIDENCE_MANIFEST.json").read_text())
    for relative in manifest["required_audit_files"]:
        if not (ROOT / relative).is_file():
            failures.append(f"missing audit file: {relative}")

    claims = json.loads((ROOT / "claims.json").read_text())
    statuses = {claim["id"]: claim["status"] for claim in claims["claims"]}
    if statuses != EXPECTED_STATUSES:
        failures.append(f"unexpected claim statuses: {statuses}")
    if len(claims["claims"]) != 5:
        failures.append("claim ledger does not contain five claims")

    summary = json.loads((ROOT / "outputs/claim1_proxy_label_calibration/summary.json").read_text())
    if not summary.get("all_calibrated_pass"):
        failures.append("Claim 1 calibrated runs are not recorded as passing")
    if not summary.get("all_under_controls_fail"):
        failures.append("Claim 1 under-calibrated controls are not recorded as failing")

    for item in manifest["content_addressed_artifacts"]:
        path = ROOT / item["path"]
        if not path.is_file():
            failures.append(f"missing evidence artifact: {item['path']}")
        elif sha256(path) != item["sha256"]:
            failures.append(f"evidence hash mismatch: {item['path']}")

    source_sums = {}
    for line in (ROOT / "evidence/source/SHA256SUMS").read_text().splitlines():
        expected, relative = line.split(maxsplit=1)
        source_sums[relative] = expected
    for relative in ("arxiv_source.tar.gz", "paper.pdf"):
        path = ROOT / "evidence/source" / relative
        if source_sums.get(relative) != sha256(path):
            failures.append(f"source checksum mismatch: {relative}")

    readme = (ROOT / "README.md").read_text()
    for marker in [
        "CLAIM_EVIDENCE.md",
        "SOURCE_AUDIT.md",
        "BRANCH_AUDIT.md",
        "ENVIRONMENT.md",
        "REPORT.md",
        "CITATION.cff",
        "AUTHOR_THANK_YOU.md",
        "verify_final.py",
    ]:
        if marker not in readme:
            failures.append(f"README missing dossier marker: {marker}")
    branch_audit = (ROOT / "BRANCH_AUDIT.md").read_text()
    if "| `main` |" not in branch_audit or "| `master` |" not in branch_audit:
        failures.append("branch audit does not record main and stale master")
    source_audit = (ROOT / "SOURCE_AUDIT.md").read_text()
    if "tijana-zrnic/pac-labels" not in source_audit or "b415b58756b14b384529ac9cf146bd5d4c8139aa" not in source_audit:
        failures.append("official implementation pin is missing")

    state = json.loads((ROOT / "AUTONOMOUS_STATE.json").read_text())
    if state.get("canonical_identity", {}).get("email") != CANONICAL_EMAIL:
        failures.append("autonomous state does not record canonical email")
    if state.get("canonical_identity", {}).get("verified_reachable_commits") != 7:
        failures.append("autonomous state does not record the seven pre-dossier commits")

    result = {
        "passed": not failures,
        "failures": failures,
        "repository": EXPECTED_REPOSITORY,
        "commit_count": len(commits),
        "claim_statuses": statuses,
        "evidence_artifacts": len(manifest["content_addressed_artifacts"]),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
