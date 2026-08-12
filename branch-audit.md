# Branch audit

## Pre-normalization inventory

| Remote branch | Tip | Assessment |
| --- | --- | --- |
| main | 749cbfcdf5e3ba0c838782f112f3b836c6e3ffac | Current branch with Claim 1 toy code, outputs, and updated state |
| master | 0370b741d2f0f90b23bbf5f42f5154ad00e78d7f | Older default branch without the current Claim 1 implementation and evidence |

The repository had no experiment branches. master was a stale default branch, not a complementary implementation. The normalized repository retains main as the sole public branch and removes master after rewritten main history is pushed.

## Attribution decision

The pre-normalization history used Dinesh Jinjala and DineshAI identities. All reachable commits will be rewritten to:

    MachineLearning-Nerd <37579156+MachineLearning-Nerd@users.noreply.github.com>

This changes commit metadata only; the paper source and retained evidence are not replaced.
