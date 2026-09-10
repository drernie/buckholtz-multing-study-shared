"""
NR-015's own named "correct next direction" (Relaxation Map row 2):
cool-core (CC) vs non-cool-core (NCC) stratification, to discriminate its
two undistinguished readings of why r(delta_M, M_Gas | M_WL, T_X)
collapses -- definitional-artifact (T_X mechanically inside M_hydro's own
HSE formula) vs common-physical-driver (cluster dynamical state driving
both T_X and delta_M through separate channels).

Reuses residualize()/partial_corr() verbatim from the already-verified
h1c_p001_mgas_only_retest.py (NR-015's own script) -- same logic, not
reinvented, so this test's numbers are directly comparable to NR-015's
own reported baseline.

Design: split N=50 CCCP sample at K0~30 keV/cm^2 (standard CC/NCC cut,
per NR-015's own specification), recompute r(delta_M, T_X | M_WL) in
each subsample. Cross-checked with two independent dynamical-state
proxies already in the same dataset (wX centroid shift, P3P0 power
ratio) rather than resting on K0 alone -- NR-014 already found K0 and wX
correlated (r=0.31) but not degenerate.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import numpy as np
from scipy import stats

sys.path.insert(
    0,
    str(Path(__file__).parent.parent / "20260701-h1c-morphology-mass-bias" / "artifacts"),
)
from h1c_p001_mgas_only_retest import partial_corr  # noqa: E402

DATA_PATH = (
    Path(__file__).parent.parent
    / "20260713-h1e-agn-feedback-confound"
    / "artifacts"
    / "cccp_mahdavi2013_merged.csv"
)
K0_CUT = 30.0  # keV*cm^2, standard cool-core/non-cool-core threshold, per NR-015


REQUIRED_COLS = (
    "delta_M_1e14Msun",
    "E_ICM_proxy_MgasTx",
    "M_WL_1e14Msun",
    "T_X_keV",
    "K0_keVcm2",
    "wX",
    "P3P0",
)


def _to_float(s: str) -> float:
    return float(s) if s else float("nan")


def _rows_to_columns(rows: list[dict]) -> dict[str, np.ndarray]:
    return {
        "cluster": np.array([r["cluster_name"] for r in rows]),
        "delta_M": np.array([_to_float(r["delta_M_1e14Msun"]) for r in rows]),
        "E_ICM": np.array([_to_float(r["E_ICM_proxy_MgasTx"]) for r in rows]),
        "M_WL": np.array([_to_float(r["M_WL_1e14Msun"]) for r in rows]),
        "T_X": np.array([_to_float(r["T_X_keV"]) for r in rows]),
        "K0": np.array([_to_float(r["K0_keVcm2"]) for r in rows]),
        "wX": np.array([_to_float(r["wX"]) for r in rows]),
        "P3P0": np.array([_to_float(r["P3P0"]) for r in rows]),
    }


def load_columns_pc() -> dict[str, np.ndarray]:
    """Same filter as NR-015's own h1c_p001_mgas_only_retest.py (only
    M_Gas + T_X required) -- used ONLY for the positive control, so it
    reproduces NR-015's own exact reported numbers on its own N."""
    rows = []
    with DATA_PATH.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if not row["M_Gas_1e14Msun"] or not row["T_X_keV"]:
                continue
            rows.append(row)
    return _rows_to_columns(rows)


def load_columns() -> dict[str, np.ndarray]:
    """Full filter for the stratification test: also requires K0/wX/P3P0
    (the dynamical-state proxies), so N is smaller than the PC's N=50 --
    5 clusters lack full morphology data."""
    rows = []
    skipped = 0
    with DATA_PATH.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if any(not row[c] for c in REQUIRED_COLS):
                skipped += 1
                continue
            rows.append(row)
    print(f"Rows with all required columns present: {len(rows)} (skipped {skipped} incomplete)")
    return _rows_to_columns(rows)


def bootstrap_ci(x, y, controls, n_boot=10_000, seed=42):
    n = len(x)
    if n < 5:
        return (np.nan, np.nan), 0
    rng = np.random.default_rng(seed)
    idx = np.arange(n)
    boots = []
    for _ in range(n_boot):
        sample = rng.choice(idx, size=n, replace=True)
        try:
            r_b, _ = partial_corr(x[sample], y[sample], controls[sample])
            if not np.isnan(r_b):
                boots.append(r_b)
        except np.linalg.LinAlgError:
            continue
    boots_arr = np.array(boots)
    if len(boots_arr) == 0:
        return (np.nan, np.nan), 0
    return tuple(np.percentile(boots_arr, [2.5, 97.5])), len(boots_arr)


def report_split(name: str, mask: np.ndarray, d: dict[str, np.ndarray]) -> dict:
    n = int(mask.sum())
    print(f"\n--- {name}: N={n} ---")
    if n < 8:
        print("  Too few clusters for a meaningful partial correlation -- skipped.")
        return {"n": n, "r": np.nan, "p": np.nan, "ci": (np.nan, np.nan)}
    controls = d["M_WL"][mask].reshape(-1, 1)
    r, p = partial_corr(d["delta_M"][mask], d["T_X"][mask], controls)
    ci, n_valid = bootstrap_ci(d["delta_M"][mask], d["T_X"][mask], controls)
    print(
        f"  r(delta_M, T_X | M_WL) = {r:.4f}  p={p:.3e}  CI=[{ci[0]:.4f}, {ci[1]:.4f}] (n_boot_valid={n_valid})"
    )
    return {"n": n, "r": r, "p": p, "ci": ci}


def main() -> None:
    # --- Positive control: reproduce NR-015's own reported baseline numbers,
    # on NR-015's own exact filter (M_Gas+T_X only), before touching the
    # smaller morphology-complete subsample used below. ---
    d_pc = load_columns_pc()
    print(f"PC sample: N={len(d_pc['delta_M'])} (NR-015's own N=50)")
    controls_mwl_pc = d_pc["M_WL"].reshape(-1, 1)
    r_base, p_base = partial_corr(d_pc["delta_M"], d_pc["E_ICM"], controls_mwl_pc)
    r_dmtx, p_dmtx = partial_corr(d_pc["delta_M"], d_pc["T_X"], controls_mwl_pc)
    print("\n=== Positive control: reproduce NR-015's own reported full-sample numbers ===")
    print(
        f"r(delta_M, E_ICM | M_WL) = {r_base:.4f} (NR-015: -0.7008)  p={p_base:.3e} (NR-015: 1.46e-08)"
    )
    print(
        f"r(delta_M, T_X | M_WL)   = {r_dmtx:.4f} (NR-015: -0.8108)  p={p_dmtx:.3e} (NR-015: 9.58e-13)"
    )
    assert abs(r_base - (-0.7008)) < 0.001, f"PC FAILED: r_base={r_base}"
    assert abs(r_dmtx - (-0.8108)) < 0.001, f"PC FAILED: r_dmtx={r_dmtx}"
    print("Positive control: PASS (matches NR-015's own reported numbers to <0.001)")

    # --- Stratification test: needs K0/wX/P3P0 too -> smaller, morphology-
    # complete subsample. Report the N drop explicitly, don't silently swap. ---
    d = load_columns()
    n_total = len(d["delta_M"])
    print(f"\nStratification sample: N={n_total} (5 of the PC's 50 lack full K0/wX/P3P0 data)")

    # --- Primary test: K0-based CC/NCC split (NR-015's own pre-registered design) ---
    print("\n" + "=" * 90)
    print(f"PRIMARY TEST: K0 split at {K0_CUT} keV*cm^2 (cool-core vs non-cool-core)")
    print("=" * 90)
    cc_mask = d["K0"] < K0_CUT
    ncc_mask = d["K0"] >= K0_CUT
    print(f"K0 range: {d['K0'].min():.1f} - {d['K0'].max():.1f} keV*cm^2")
    r_cc = report_split("Cool-core (K0 < 30)", cc_mask, d)
    r_ncc = report_split("Non-cool-core (K0 >= 30)", ncc_mask, d)

    # --- Secondary/cross-check: wX-based split (median split, since no standard cut exists) ---
    print("\n" + "=" * 90)
    print("SECONDARY CROSS-CHECK: wX (centroid shift) median split (relaxed vs disturbed)")
    print("=" * 90)
    wx_med = np.median(d["wX"])
    relaxed_mask = d["wX"] < wx_med
    disturbed_mask = d["wX"] >= wx_med
    print(f"wX median = {wx_med:.4f}")
    r_relaxed = report_split("Relaxed (wX < median)", relaxed_mask, d)
    r_disturbed = report_split("Disturbed (wX >= median)", disturbed_mask, d)

    # --- Secondary/cross-check: P3P0 median split ---
    print("\n" + "=" * 90)
    print("SECONDARY CROSS-CHECK: P3P0 (power ratio) median split (relaxed vs disturbed)")
    print("=" * 90)
    p3p0_med = np.median(d["P3P0"])
    relaxed2_mask = d["P3P0"] < p3p0_med
    disturbed2_mask = d["P3P0"] >= p3p0_med
    print(f"P3P0 median = {p3p0_med:.6f}")
    r_relaxed2 = report_split("Relaxed (P3P0 < median)", relaxed2_mask, d)
    r_disturbed2 = report_split("Disturbed (P3P0 >= median)", disturbed2_mask, d)

    # --- Verdict, with a formal Fisher r-to-z test for each split (not just
    # CI-overlap eyeballing) ---
    print("\n" + "=" * 90)
    print("VERDICT")
    print("=" * 90)
    print("Reading (1) definitional-artifact predicts: similar |r| in both halves of each split.")
    print("Reading (2) common-physical-driver predicts: concentrated in the disturbed/NCC half.")
    print()
    for label, (a, b) in [
        ("K0 split (CC vs NCC)", (r_cc, r_ncc)),
        ("wX split (relaxed vs disturbed)", (r_relaxed, r_disturbed)),
        ("P3P0 split (relaxed vs disturbed)", (r_relaxed2, r_disturbed2)),
    ]:
        line = f"{label}: relaxed/CC r={a['r']:.3f} (n={a['n']}) vs disturbed/NCC r={b['r']:.3f} (n={b['n']})"
        if a["n"] >= 8 and b["n"] >= 8 and not (np.isnan(a["r"]) or np.isnan(b["r"])):
            z_a = np.arctanh(a["r"])
            z_b = np.arctanh(b["r"])
            se = np.sqrt(1 / (a["n"] - 3) + 1 / (b["n"] - 3))
            z_stat = (z_a - z_b) / se
            p_diff = 2 * (1 - stats.norm.cdf(abs(z_stat)))
            line += f"  |  Fisher z-test for difference: z={z_stat:+.3f}, p={p_diff:.3f}"
            line += (
                "  -> NO significant difference (favors reading 1)"
                if p_diff > 0.10
                else "  -> SIGNIFICANT difference (favors reading 2)"
            )
        print(line)


if __name__ == "__main__":
    main()
