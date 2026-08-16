# Branch audit

The final public repository has one branch: `main`.

| Former branch | Pre-dossier tip | Purpose and outcome | Disposition |
| --- | --- | --- | --- |
| `main` | `fa479e9e7dcbfb9a88606d769fdda6f6f49cef77` | Current source snapshot, Claim 1 implementation, toy outputs, and saved state. | Keep as canonical main |
| `master` | `0370b741d2f0f90b23bbf5f42f5154ad00e78d7f` | Older default branch without the current Claim 1 implementation and evidence. | Delete stale pointer; no public master branch remains |

There were no experiment branches. `master` was a stale pointer rather than a complementary implementation. The current local and remote ref layout is intentionally only `main`; `verify_final.py` fails if another branch appears.

All seven reachable pre-dossier commits use `MachineLearning-Nerd <37579156+MachineLearning-Nerd@users.noreply.github.com>` for both author and committer. A complete recovery bundle was created before publication changes; its SHA-256 is `ce0525de120bc1bf78f0e0be963b852a42ed9e9f80d233ad3a06ee696bff034d`.
