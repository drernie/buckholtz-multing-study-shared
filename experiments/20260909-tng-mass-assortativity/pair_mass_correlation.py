"""
Direct empirical measurement of halo-pair mass correlation (rho) as a
function of separation, in real TNG300-1 data -- answers one of the two
open unknowns named in FINDING_P158_jensen_mass_averaging_v82_force_terms.md
("the sign of the log-mass correlation rho between paired nodes... noted
as a real, studied effect in cosmic-web connectivity literature ('mass
assortativity'), NOT checked by that file"), by measuring it directly from
simulation data instead of a literature search.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR -- this characterizes real cosmic structure in TNG300-1,
not a claim about TJB's own theory or v82's own text.

Design:
  1. Fetch info.json for the top N_TOP halos by ID (== top N_TOP by total
     FOF mass, the catalog's own sort key -- NOT necessarily monotonic in
     Group_M_Crit200 specifically, a fact this project already discovered
     2026-09-09 in whim_batch_n71.py; using a contiguous top-N-by-ID slice
     sidesteps that by not assuming M_Crit200 monotonicity at all).
  2. Compute all pairwise 3D separations (periodic-corrected, box=205 Mpc/h).
  3. Bin by separation; in each bin, Pearson r(log M1, log M2).
  4. Positive control: very small separations (<5 Mpc) should show strong
     positive assortativity almost trivially (halos close together tend to
     share a larger host structure) -- confirms the pipeline can detect a
     real signal when one plainly exists.
  5. Negative control / floor: shuffle masses among halo IDs (breaking the
     spatial-mass link) and recompute r on the SAME pairs -- should be ~0.
  6. Headline number: r in the 40-45 Mpc physical-separation band, the
     characteristic node separation named in this project's own bottleneck-1
     planning material.
"""

import csv
import math
import statistics as st
from pathlib import Path

import numpy as np
import requests

API_KEY_FILE = Path.home() / ".secrets" / "tng_api_key.env"
BASE_URL = "https://www.tng-project.org/api/TNG300-1/snapshots/99"
BOX_SIZE_CKPC_H = 205000.0
HUBBLE = 0.6774
N_TOP = 1500
OUT_CSV = Path(__file__).parent / "top_halos_pos_mass.csv"
TARGET_BAND_MPC = (40.0, 45.0)
BIN_EDGES_MPC = list(range(0, 105, 5))  # 0-100 Mpc in 5 Mpc bins


def get_api_key() -> str:
    text = API_KEY_FILE.read_text()
    for line in text.splitlines():
        if line.startswith("TNG_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise RuntimeError("TNG_API_KEY not found")


def fetch_top_halos(session: requests.Session, n_top: int) -> list[dict]:
    rows: list[dict] = []
    existing_ids: set[int] = set()
    if OUT_CSV.exists():
        with open(OUT_CSV) as f:
            for r in csv.DictReader(f):
                rows.append(r)
                existing_ids.add(int(r["halo_id"]))
        print(f"Resuming: {len(rows)} halos already fetched.")

    csv_exists = OUT_CSV.exists()
    with open(OUT_CSV, "a", newline="") as csvfile:
        fieldnames = ["halo_id", "m200_msun", "pos_x", "pos_y", "pos_z"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not csv_exists:
            writer.writeheader()

        for hid in range(n_top):
            if hid in existing_ids:
                continue
            try:
                resp = session.get(f"{BASE_URL}/halos/{hid}/info.json", timeout=30)
                if resp.status_code != 200:
                    print(f"  halo {hid}: fetch failed ({resp.status_code}), skip")
                    continue
                info = resp.json()
                m200 = info.get("Group_M_Crit200", 0.0)
                pos = info.get("GroupPos")
                if not m200 or m200 <= 0 or pos is None:
                    print(f"  halo {hid}: no well-defined M200/pos, skip")
                    continue
                row = {
                    "halo_id": hid,
                    "m200_msun": m200 * 1e10 / HUBBLE,
                    "pos_x": pos[0],
                    "pos_y": pos[1],
                    "pos_z": pos[2],
                }
                writer.writerow(row)
                csvfile.flush()
                rows.append({k: str(v) for k, v in row.items()})
            except requests.RequestException as e:
                print(f"  halo {hid}: request error {e}, skip")
            if hid % 200 == 0:
                print(f"  ...{hid}/{n_top}")
    return rows


def periodic_delta(p1: np.ndarray, p2: np.ndarray) -> np.ndarray:
    d = p1 - p2
    return d - BOX_SIZE_CKPC_H * np.round(d / BOX_SIZE_CKPC_H)


def pearson(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.corrcoef(x, y)[0, 1])


def t_p(r: float, n: int) -> tuple[float, str]:
    if n < 3 or abs(r) >= 1.0:
        return float("nan"), "n/a"
    df = n - 2
    t = r * math.sqrt(df) / math.sqrt(1 - r**2)
    at = abs(t)
    p = "<0.001" if at > 3.29 else "<0.01" if at > 2.58 else "<0.05" if at > 1.96 else "n.s."
    return t, p


def main() -> None:
    api_key = get_api_key()
    session = requests.Session()
    session.headers.update({"api-key": api_key})

    print(f"Fetching top {N_TOP} halos by ID (== top {N_TOP} by total FOF mass)...")
    rows = fetch_top_halos(session, N_TOP)
    print(f"Total usable halos: {len(rows)}")

    masses = np.array([float(r["m200_msun"]) for r in rows])
    pos = np.array([[float(r["pos_x"]), float(r["pos_y"]), float(r["pos_z"])] for r in rows])
    log_m = np.log10(masses)
    n = len(rows)

    # All pairwise separations, vectorized, periodic-corrected
    diff = pos[:, None, :] - pos[None, :, :]
    diff = diff - BOX_SIZE_CKPC_H * np.round(diff / BOX_SIZE_CKPC_H)
    sep_ckpc_h = np.sqrt((diff**2).sum(axis=-1))
    sep_mpc = sep_ckpc_h / HUBBLE / 1000.0  # physical Mpc at z=0

    iu, ju = np.triu_indices(n, k=1)
    pair_sep = sep_mpc[iu, ju]
    pair_logm1 = log_m[iu]
    pair_logm2 = log_m[ju]
    n_pairs_total = len(pair_sep)
    print(f"\nTotal pairs: {n_pairs_total}")

    print("\n=== Assortativity vs separation (5 Mpc bins, 0-100 Mpc) ===")
    print(f"{'bin (Mpc)':>12} | {'N pairs':>8} | {'r(logM1,logM2)':>15} | {'p':>8}")
    for lo, hi in zip(BIN_EDGES_MPC[:-1], BIN_EDGES_MPC[1:], strict=True):
        mask = (pair_sep >= lo) & (pair_sep < hi)
        n_bin = int(mask.sum())
        if n_bin < 10:
            print(f"{lo:>5}-{hi:<5} | {n_bin:>8} | {'(too few)':>15} | {'':>8}")
            continue
        r_bin = pearson(pair_logm1[mask], pair_logm2[mask])
        t_bin, p_bin = t_p(r_bin, n_bin)
        print(f"{lo:>5}-{hi:<5} | {n_bin:>8} | {r_bin:>15.4f} | {p_bin:>8}")

    print(
        f"\n=== Headline: {TARGET_BAND_MPC[0]}-{TARGET_BAND_MPC[1]} Mpc band (v82's own node separation) ==="
    )
    mask_target = (pair_sep >= TARGET_BAND_MPC[0]) & (pair_sep < TARGET_BAND_MPC[1])
    n_target = int(mask_target.sum())
    r_target = pearson(pair_logm1[mask_target], pair_logm2[mask_target])
    t_target, p_target = t_p(r_target, n_target)
    print(f"N pairs = {n_target}")
    print(f"r(log M1, log M2) = {r_target:.4f}  (t={t_target:.2f}, p{p_target})")

    print(
        "\n=== Positive control: <5 Mpc separation (should show strong positive assortativity) ==="
    )
    mask_pos = pair_sep < 5.0
    n_pos = int(mask_pos.sum())
    if n_pos >= 10:
        r_pos = pearson(pair_logm1[mask_pos], pair_logm2[mask_pos])
        t_pos, p_pos = t_p(r_pos, n_pos)
        print(f"N pairs = {n_pos}, r = {r_pos:.4f} (t={t_pos:.2f}, p{p_pos})")
    else:
        print(f"N pairs = {n_pos} -- too few for a reliable positive-control number")

    print(
        "\n=== Negative control / floor: shuffle masses, recompute on the SAME target-band pairs ==="
    )
    rng = np.random.default_rng(42)
    shuffled_log_m = log_m.copy()
    rng.shuffle(shuffled_log_m)
    shuf_m1 = shuffled_log_m[iu][mask_target]
    shuf_m2 = shuffled_log_m[ju][mask_target]
    r_shuf = pearson(shuf_m1, shuf_m2)
    print(f"Shuffled-mass r (target band) = {r_shuf:.4f}  (expected ~0)")

    print("\n=== Mass range of the N_TOP sample ===")
    print(f"min={masses.min():.3e}  max={masses.max():.3e}  median={st.median(masses):.3e} Msun")


if __name__ == "__main__":
    main()
