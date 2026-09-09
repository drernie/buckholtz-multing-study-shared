"""
Center-of-mass vs. potential-minimum offset as a dynamical-state proxy
-- a real, standard technique in cluster astrophysics (e.g. Mohr et al.
1993; the same real physical idea Ansarifard+2019 use in their own 2D
projected X-ray form, "centroid shift"). A large offset between
GroupCM (mass-weighted center) and GroupPos (potential minimum / most
bound particle position) indicates an ongoing merger / disturbed
system; a small offset indicates a relaxed one.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR

Re-fetches only the small info.json per cluster (fast, no gas cutout
needed -- the batch's own gas cutouts were deleted after Stage 2, but
GroupCM/GroupPos are catalog fields, cheap to re-fetch).
"""

import csv
import math
import statistics as st
from pathlib import Path

import requests

API_KEY_FILE = Path.home() / ".secrets" / "tng_api_key.env"
BASE_URL = "https://www.tng-project.org/api/TNG300-1/snapshots/99"
BOX_SIZE = 205000.0  # ckpc/h
IN_CSV = Path(__file__).parent / "whim_n71_results.csv"
OUT_CSV = Path(__file__).parent / "whim_n71_with_offset.csv"


def get_api_key() -> str:
    text = API_KEY_FILE.read_text()
    for line in text.splitlines():
        if line.startswith("TNG_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise RuntimeError("TNG_API_KEY not found")


def periodic_offset(cm: list[float], pos: list[float]) -> float:
    delta = [cm[i] - pos[i] for i in range(3)]
    delta = [d - BOX_SIZE * round(d / BOX_SIZE) for d in delta]
    return math.sqrt(sum(d**2 for d in delta))


def main() -> None:
    api_key = get_api_key()
    session = requests.Session()
    session.headers.update({"api-key": api_key})

    rows = list(csv.DictReader(open(IN_CSV)))
    print(f"Re-fetching info.json for {len(rows)} clusters (light, no gas cutout)...")

    out_rows = []
    for r in rows:
        hid = r["halo_id"]
        resp = session.get(f"{BASE_URL}/halos/{hid}/info.json", timeout=30)
        if resp.status_code != 200:
            print(f"  halo {hid}: fetch failed, skip")
            continue
        info = resp.json()
        cm = info["GroupCM"]
        pos = info["GroupPos"]
        r200 = info["Group_R_Crit200"]
        offset_ckpc_h = periodic_offset(cm, pos)
        offset_over_r200 = offset_ckpc_h / r200

        out_rows.append(
            {
                **r,
                "cm_pot_offset_over_r200": offset_over_r200,
            }
        )
        print(f"  halo {hid}: offset/R200 = {offset_over_r200:.4f}")

    with open(OUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)
    print(f"\nWrote {len(out_rows)} rows to {OUT_CSV}")

    # ---- Analysis, same structure as the nsubs check ----
    n = len(out_rows)
    log_m = [math.log10(float(r["m200_msun"])) for r in out_rows]
    offsets = [float(r["cm_pot_offset_over_r200"]) for r in out_rows]
    whim = [float(r["whim_mass_fraction_pct"]) for r in out_rows]

    def pearson(x, y):
        mx, my = st.mean(x), st.mean(y)
        cov = sum((x[i] - mx) * (y[i] - my) for i in range(n)) / n
        return cov / (st.stdev(x) * st.stdev(y))

    def t_p(r, n):
        df = n - 2
        t = r * math.sqrt(df) / math.sqrt(1 - r**2)
        at = abs(t)
        p = "<0.001" if at > 3.46 else "<0.01" if at > 2.65 else "<0.05" if at > 1.99 else "n.s."
        return t, p

    print("\n=== Offset/R200 distribution ===")
    print(
        f"  min={min(offsets):.4f}  max={max(offsets):.4f}  mean={st.mean(offsets):.4f}  "
        f"median={st.median(offsets):.4f}  stdev={st.stdev(offsets):.4f}"
    )

    print("\n=== Step 1: is offset collinear with mass? ===")
    r_m_off = pearson(log_m, offsets)
    t1, p1 = t_p(r_m_off, n)
    print(f"Pearson r(log M200, offset/R200) = {r_m_off:.3f}  (t={t1:.2f}, p{p1})")

    print("\n=== Step 2: does offset predict WHIM% directly? ===")
    r_off_whim = pearson(offsets, whim)
    t2, p2 = t_p(r_off_whim, n)
    print(f"Pearson r(offset/R200, WHIM%) = {r_off_whim:.3f}  (t={t2:.2f}, p{p2})")

    if abs(r_m_off) > 0.3:
        print(f"\nOffset shows some collinearity with mass (r={r_m_off:.2f}) -- de-trending:")
        mean_lm, mean_off = st.mean(log_m), st.mean(offsets)
        b = sum((log_m[i] - mean_lm) * (offsets[i] - mean_off) for i in range(n)) / sum(
            (log_m[i] - mean_lm) ** 2 for i in range(n)
        )
        a = mean_off - b * mean_lm
        resid = [offsets[i] - (a + b * log_m[i]) for i in range(n)]
        r_resid = pearson(resid, whim)
        t3, p3 = t_p(r_resid, n)
        print(
            f"Pearson r(mass-detrended offset residual, WHIM%) = {r_resid:.3f}  (t={t3:.2f}, p{p3})"
        )
    else:
        print(f"\nOffset is NOT substantially collinear with mass (r={r_m_off:.2f}) -- ")
        print("the raw offset-vs-WHIM% correlation above is already a clean, independent test.")


if __name__ == "__main__":
    main()
