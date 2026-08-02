#!/usr/bin/env python3
"""Clean-room finite PAC-proxy-label experiment for Claim 1.

A synthetic binary population has a model whose error rises with its reported
uncertainty.  A held-out expert-labelled calibration split chooses the largest
uncertainty cutoff whose one-sided Hoeffding upper bound is at most epsilon.
Examples above the cutoff receive exact expert labels.  This is a finite
experiment, not an independent proof of Theorem 2.1.
"""
import argparse, csv, hashlib, json, math, random
from pathlib import Path

EPSILON = 0.05
ALPHA = 0.05
N_CAL = 5000
N_POP = 50000


def generate(n, seed):
    r = random.Random(seed)
    rows = []
    for _ in range(n):
        # uncertainty U is observable; model error increases monotonically in U
        u = r.random()
        y = 1 if r.random() < 0.5 else 0
        p_error = 0.01 + 0.24 * u * u
        pred = y if r.random() >= p_error else 1 - y
        rows.append((u, y, pred))
    return rows


def choose_threshold(cal, epsilon=EPSILON, alpha=ALPHA):
    """Largest threshold with Hoeffding UCB on model-label error <= epsilon."""
    ordered = sorted(cal, key=lambda z: z[0])
    best = -1.0
    errors = 0
    for j, (u, y, pred) in enumerate(ordered, 1):
        errors += int(y != pred)
        ucb = errors / j + math.sqrt(math.log(1 / alpha) / (2 * j))
        if ucb <= epsilon:
            best = u
    return best


def evaluate(pop, threshold):
    # Expert label is y, thus loss only occurs when model label is selected.
    labels = [pred if u <= threshold else y for u, y, pred in pop]
    loss = sum(int(label != row[1]) for label, row in zip(labels, pop)) / len(pop)
    expert_fraction = sum(int(u > threshold) for u, _, _ in pop) / len(pop)
    return loss, expert_fraction


def run(seed):
    cal = generate(N_CAL, seed)
    pop = generate(N_POP, seed + 1_000_000)
    threshold = choose_threshold(cal)
    if threshold < 0:
        raise RuntimeError("no calibrated threshold passed; fixture should be feasible")
    calibrated_loss, expert_fraction = evaluate(pop, threshold)
    # Deliberately under-calibrated control: route far fewer examples to expert.
    under_threshold = min(1.0, threshold + 0.70)
    under_loss, under_expert_fraction = evaluate(pop, under_threshold)
    return {
        "seed": seed, "n_calibration": N_CAL, "n_population": N_POP,
        "epsilon": EPSILON, "alpha": ALPHA, "threshold": threshold,
        "calibrated_loss": calibrated_loss, "calibrated_expert_fraction": expert_fraction,
        "under_calibrated_threshold": under_threshold,
        "under_calibrated_loss": under_loss,
        "under_calibrated_expert_fraction": under_expert_fraction,
        "calibrated_passes_population_epsilon": calibrated_loss <= EPSILON,
        "under_calibrated_fails_population_epsilon": under_loss > EPSILON,
    }


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--seeds", nargs="+", type=int, default=[101, 202, 303, 404, 505])
    args = ap.parse_args()
    out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
    rows = [run(s) for s in args.seeds]
    with (out / "results.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    config = {"method": "held-out Hoeffding-UCB calibrated proxy labels", "seeds": args.seeds,
              "epsilon": EPSILON, "alpha": ALPHA, "n_calibration": N_CAL, "n_population": N_POP,
              "control": "threshold increased by 0.70, routing fewer examples to expert"}
    write_json(out / "config.json", config)
    summary = {"all_calibrated_pass": all(r["calibrated_passes_population_epsilon"] for r in rows),
               "all_under_controls_fail": all(r["under_calibrated_fails_population_epsilon"] for r in rows),
               "mean_calibrated_loss": sum(r["calibrated_loss"] for r in rows)/len(rows),
               "mean_under_calibrated_loss": sum(r["under_calibrated_loss"] for r in rows)/len(rows),
               "scope": "clean-room finite synthetic binary proxy-label experiment; not a proof of Theorem 2.1"}
    write_json(out / "summary.json", summary)
    (out / "run.log").write_text("python src/claim1_proxy_label_calibration.py --out outputs/claim1_proxy_label_calibration --seeds " + " ".join(map(str,args.seeds)) + "\n")
    files = ["config.json", "results.csv", "summary.json", "run.log"]
    with (out / "SHA256SUMS").open("w") as f:
        for name in files:
            f.write(f"{hashlib.sha256((out/name).read_bytes()).hexdigest()}  {name}\n")

if __name__ == "__main__": main()
