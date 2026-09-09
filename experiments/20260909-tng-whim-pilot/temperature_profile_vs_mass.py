"""
Tests the candidate mechanism FINDING_stage2_batch_n71.md named but did
not check: "more massive clusters have deeper potential wells producing
more extended already-shock-heated (>10^7K) gas past R200, shrinking the
WHIM-temperature-window's captured fraction -- testable by checking the
full temperature profile shape vs mass, not just the binary WHIM/non-WHIM
split this batch computed."

Reuses the same N=71 halo_ids already known-good (whim_n71_results.csv,
controls already passed) -- re-fetches gas cutouts (deleted after the
original batch) with the SAME fields, so this is a real re-measurement,
not a reuse of stale numbers. Splits annulus gas into THREE temperature
bins instead of the original binary WHIM/non-WHIM split:
  cold  T < 1e5 K
  WHIM  1e5 <= T <= 1e7 K   (same definition as whim_batch_n71.py)
  hot   T > 1e7 K            (the candidate "shock-heated, pushed past
                               R200 by deeper potential wells" component)

Positive/consistency control: recomputed whim_mass_fraction_pct must
match the original CSV's own value for the same halo (same formula, same
cutout fields) -- if it doesn't, something in this script is wrong, not
a new physical finding.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR
"""

import csv
import math
import statistics as st
from pathlib import Path

import h5py
import numpy as np
import requests

API_KEY_FILE = Path.home() / ".secrets" / "tng_api_key.env"
BASE_URL = "https://www.tng-project.org/api/TNG300-1/snapshots/99"
BOX_SIZE = 205000.0  # ckpc/h
HUBBLE = 0.6774
GAMMA = 5.0 / 3.0
X_H = 0.76
UNIT_ENERGY_OVER_MASS = 1.0e10
K_B = 1.380649e-16
M_P = 1.6726219e-24
WHIM_T_MIN, WHIM_T_MAX = 1.0e5, 1.0e7
FIELDS = "Coordinates,InternalEnergy,ElectronAbundance,Masses"

IN_CSV = Path(__file__).parent / "whim_n71_results.csv"
OUT_CSV = Path(__file__).parent / "whim_n71_temperature_profile.csv"
SCRATCH_DIR = Path("C:/Users/serge/AppData/Local/Temp/tng_temp_profile")
SCRATCH_DIR.mkdir(exist_ok=True)


def get_api_key() -> str:
    text = API_KEY_FILE.read_text()
    for line in text.splitlines():
        if line.startswith("TNG_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise RuntimeError("TNG_API_KEY not found")


def gas_temperature_kelvin(u_code: np.ndarray, x_e: np.ndarray) -> np.ndarray:
    mu = 4.0 / (1.0 + 3.0 * X_H + 4.0 * X_H * x_e)
    return (GAMMA - 1.0) * u_code * UNIT_ENERGY_OVER_MASS * mu * M_P / K_B


def _get_with_retries(
    session: requests.Session, url: str, retries: int = 3, **kwargs
) -> requests.Response | None:
    for attempt in range(retries):
        try:
            return session.get(url, **kwargs)
        except requests.RequestException as e:
            print(f"    request error (attempt {attempt + 1}/{retries}): {e}")
    return None


def process_cluster(session: requests.Session, hid: str) -> dict | None:
    info_resp = _get_with_retries(session, f"{BASE_URL}/halos/{hid}/info.json", timeout=30)
    if info_resp is None or info_resp.status_code != 200:
        print(f"  halo {hid}: info.json failed, skip")
        return None
    info = info_resp.json()
    group_pos = np.array(info["GroupPos"])
    r200 = info["Group_R_Crit200"]

    cutout_resp = _get_with_retries(
        session,
        f"{BASE_URL}/halos/{hid}/cutout.hdf5",
        params={"gas": FIELDS},
        timeout=600,
        stream=True,
    )
    if cutout_resp is None or cutout_resp.status_code != 200:
        print(f"  halo {hid}: cutout failed, skip")
        return None
    out_path = SCRATCH_DIR / f"halo{hid}_gas.hdf5"
    with open(out_path, "wb") as f:
        for chunk in cutout_resp.iter_content(chunk_size=1 << 20):
            f.write(chunk)

    try:
        with h5py.File(out_path, "r") as f:
            if "PartType0" not in f:
                return None
            gas = f["PartType0"]
            coords = gas["Coordinates"][:]
            u = gas["InternalEnergy"][:]
            x_e = gas["ElectronAbundance"][:]
            masses_code = gas["Masses"][:]
    finally:
        out_path.unlink(missing_ok=True)

    masses_msun = masses_code.astype(np.float64) * 1e10 / HUBBLE
    temp_k = gas_temperature_kelvin(u, x_e)
    delta = coords - group_pos
    delta = delta - BOX_SIZE * np.round(delta / BOX_SIZE)
    r_over_r200 = np.sqrt((delta**2).sum(axis=1)) / r200

    in_annulus = (r_over_r200 >= 1.0) & (r_over_r200 <= 3.0)
    mass_annulus = masses_msun[in_annulus].sum()
    if mass_annulus <= 0:
        return None

    cold_mask = in_annulus & (temp_k < WHIM_T_MIN)
    whim_mask = in_annulus & (temp_k >= WHIM_T_MIN) & (temp_k <= WHIM_T_MAX)
    hot_mask = in_annulus & (temp_k > WHIM_T_MAX)

    cold_frac = 100.0 * masses_msun[cold_mask].sum() / mass_annulus
    whim_frac = 100.0 * masses_msun[whim_mask].sum() / mass_annulus
    hot_frac = 100.0 * masses_msun[hot_mask].sum() / mass_annulus

    # Radial sub-profile: hot fraction in inner half (1.0-2.0 R200) vs
    # outer half (2.0-3.0 R200) of the annulus -- does the hot component
    # specifically push OUTWARD with mass, or just scale up uniformly?
    inner_ann = in_annulus & (r_over_r200 < 2.0)
    outer_ann = in_annulus & (r_over_r200 >= 2.0)
    mass_inner = masses_msun[inner_ann].sum()
    mass_outer = masses_msun[outer_ann].sum()
    hot_frac_inner = (
        100.0 * masses_msun[inner_ann & (temp_k > WHIM_T_MAX)].sum() / mass_inner
        if mass_inner > 0
        else float("nan")
    )
    hot_frac_outer = (
        100.0 * masses_msun[outer_ann & (temp_k > WHIM_T_MAX)].sum() / mass_outer
        if mass_outer > 0
        else float("nan")
    )

    return {
        "halo_id": hid,
        "cold_fraction_pct": cold_frac,
        "whim_fraction_pct_recomputed": whim_frac,
        "hot_fraction_pct": hot_frac,
        "hot_fraction_inner_pct": hot_frac_inner,
        "hot_fraction_outer_pct": hot_frac_outer,
    }


def main() -> None:
    api_key = get_api_key()
    session = requests.Session()
    session.headers.update({"api-key": api_key})

    source_rows = list(csv.DictReader(open(IN_CSV)))
    print(f"Processing {len(source_rows)} clusters for temperature-profile split...")

    done_ids: set[str] = set()
    out_rows: list[dict] = []
    if OUT_CSV.exists():
        with open(OUT_CSV) as f:
            for r in csv.DictReader(f):
                out_rows.append(r)
                done_ids.add(r["halo_id"])
        print(f"Resuming: {len(done_ids)} clusters already done.")

    csv_exists = OUT_CSV.exists()
    fieldnames = list(source_rows[0].keys()) + [
        "cold_fraction_pct",
        "whim_fraction_pct_recomputed",
        "hot_fraction_pct",
        "hot_fraction_inner_pct",
        "hot_fraction_outer_pct",
    ]
    with open(OUT_CSV, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not csv_exists:
            writer.writeheader()

        for i, src_row in enumerate(source_rows):
            hid = src_row["halo_id"]
            if hid in done_ids:
                continue
            try:
                result = process_cluster(session, hid)
            except (KeyError, OSError) as e:
                print(f"  halo {hid}: unexpected error {e!r}, skip")
                continue
            if result is None:
                continue
            merged = {**src_row, **{k: v for k, v in result.items() if k != "halo_id"}}
            writer.writerow(merged)
            csvfile.flush()
            out_rows.append(merged)
            print(
                f"  [{i + 1}/{len(source_rows)}] halo {hid}: "
                f"cold={result['cold_fraction_pct']:.1f}% whim={result['whim_fraction_pct_recomputed']:.1f}% "
                f"hot={result['hot_fraction_pct']:.1f}%"
            )

    print(f"\nWrote {len(out_rows)} rows to {OUT_CSV}")

    n = len(out_rows)
    log_m = [math.log10(float(r["m200_msun"])) for r in out_rows]
    whim_orig = [float(r["whim_mass_fraction_pct"]) for r in out_rows]
    whim_recomp = [float(r["whim_fraction_pct_recomputed"]) for r in out_rows]
    hot = [float(r["hot_fraction_pct"]) for r in out_rows]
    hot_inner = [float(r["hot_fraction_inner_pct"]) for r in out_rows]
    hot_outer = [float(r["hot_fraction_outer_pct"]) for r in out_rows]

    def pearson(x: list[float], y: list[float]) -> tuple[float, int]:
        # Drop any (x,y) pair where either side is NaN (e.g. a cluster with
        # zero gas mass in one radial sub-shell) instead of crashing --
        # this is a data-availability fact about that cluster, not a bug.
        pairs = [
            (xi, yi) for xi, yi in zip(x, y, strict=True) if not (math.isnan(xi) or math.isnan(yi))
        ]
        n_valid = len(pairs)
        xs = [p[0] for p in pairs]
        ys = [p[1] for p in pairs]
        mx, my = st.mean(xs), st.mean(ys)
        cov = sum((xs[i] - mx) * (ys[i] - my) for i in range(n_valid)) / n_valid
        return cov / (st.stdev(xs) * st.stdev(ys)), n_valid

    def t_p(r: float, n: int) -> tuple[float, str]:
        df = n - 2
        t = r * math.sqrt(df) / math.sqrt(1 - r**2)
        at = abs(t)
        p = "<0.001" if at > 3.46 else "<0.01" if at > 2.65 else "<0.05" if at > 1.99 else "n.s."
        return t, p

    print("\n=== Consistency control: recomputed WHIM% vs original CSV's own value ===")
    diffs = [abs(whim_orig[i] - whim_recomp[i]) for i in range(n)]
    print(f"max abs diff = {max(diffs):.4f} pct points (should be ~0 -- same formula, same fields)")

    print("\n=== Candidate mechanism test: does hot fraction (T>1e7K) increase with mass? ===")
    r_hot, n_hot = pearson(log_m, hot)
    t_hot, p_hot = t_p(r_hot, n_hot)
    print(
        f"Pearson r(log M200, hot_fraction_pct) = {r_hot:.3f} (N={n_hot}, t={t_hot:.2f}, p{p_hot})"
    )

    print("\n=== Does the hot fraction push OUTWARD with mass specifically? ===")
    r_inner, n_inner = pearson(log_m, hot_inner)
    t_inner, p_inner_ = t_p(r_inner, n_inner)
    r_outer, n_outer = pearson(log_m, hot_outer)
    t_outer, p_outer_ = t_p(r_outer, n_outer)
    print(
        f"r(log M200, hot_fraction_inner [1.0-2.0 R200]) = {r_inner:.3f} "
        f"(N={n_inner}, t={t_inner:.2f}, p{p_inner_})"
    )
    print(
        f"r(log M200, hot_fraction_outer [2.0-3.0 R200]) = {r_outer:.3f} "
        f"(N={n_outer}, t={t_outer:.2f}, p{p_outer_})"
    )


if __name__ == "__main__":
    main()
