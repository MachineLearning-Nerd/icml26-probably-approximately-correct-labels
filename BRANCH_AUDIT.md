# Branch audit

The final public repository has one branch: `main`.

| Former branch | Pre-dossier tip | Purpose and outcome | Disposition |
| --- | --- | --- | --- |
| `main` | `cb95a8104161402d3055bb37bfc297b4a1958887` | Normalized source snapshot, Claim 1 implementation, toy outputs, and saved state before this publication dossier. | Keep as canonical main |
| `master` | `0370b741d2f0f90b23bbf5f42f5154ad00e78d7f` | Older default branch without the current Claim 1 implementation and evidence. | Delete stale pointer; no public master branch remains |

There were no experiment branches. `master` was a stale pointer rather than a complementary implementation. The current local and remote ref layout is intentionally only `main`; `verify_final.py` fails if another branch appears.

All eight reachable pre-dossier commits use `MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>` for both author and committer. A complete recovery bundle was created before history normalization; its SHA-256 is `5b4261de84504b5ef7d0dc1b6d95e54d38396ec393cd286c557747d7c9fe1723`.
