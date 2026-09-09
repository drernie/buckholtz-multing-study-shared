"""
Third dynamical-state confound-control proxy for the N=71 WHIM sample:
DM particle velocity dispersion within R200, relative to the group's own
bulk velocity (GroupVel). This is the "one named, untested candidate"
left open by FINDING_stage2_batch_n71.md's Second Addendum, after
GroupNsubs and CM/potential-minimum offset both came back null.

Design choice (checked live before building, not assumed from memory --
integrity.md's own Red-Flags rule): a subhalo/galaxy-based sigma_v would
match real observational practice more closely, but a live probe showed
individual clusters carry hundreds of subhalos (halo 200: GroupNsubs=859)
with no bulk field-selection available on the subhalo search endpoint for
velocity columns -- that route would need one API call PER SUBHALO,
tens of thousands total. A DM-particle-based sigma_v within R200 is the
standard theoretical/simulation proxy for the same physical quantity
(closely tracks the Evrard et al. 2008-type M-sigma relation), and is a
single cutout call per cluster -- the same pattern already validated for
the gas cutouts in whim_batch_n71.py.

Positive control built into the design itself: sigma_v is expected to be
STRONGLY, POSITIVELY correlated with M200 (the M-sigma relation is one of
the tightest scaling relations in cluster physics) -- if that collinearity
check fails to show a strong positive r, something is wrong with the
measurement, independent of the confound question.

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
BOX_SIZE_CKPC_H = 205000.0
CUTOUT_TMP = Path("C:/Users/serge/AppData/Local/Temp/vdisp_cutout.hdf5")
IN_CSV = Path(__file__).parent / "whim_n71_results.csv"
OUT_CSV = Path(__file__).parent / "whim_n71_with_vdisp.csv"


def get_api_key() -> str:
    text = API_KEY_FILE.read_text()
    for line in text.splitlines():
        if line.startswith("TNG_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise RuntimeError("TNG_API_KEY not found")


def periodic_delta(pos: np.ndarray, center: np.ndarray) -> np.ndarray:
    d = pos - center
    return d - BOX_SIZE_CKPC_H * np.round(d / BOX_SIZE_CKPC_H)


def _get_with_retries(
    session: requests.Session, url: str, retries: int = 3, **kwargs
) -> requests.Response | None:
    """A transient timeout/connection error is not a finding about the
    data (Substrate Gate, falsification-ladder.md Step 2a) -- retry a
    few times before giving up on this one request."""
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
    group_vel = np.array(info["GroupVel"])
    r200 = info["Group_R_Crit200"]

    cutout_resp = _get_with_retries(
        session,
        f"{BASE_URL}/halos/{hid}/cutout.hdf5",
        params={"dm": "Coordinates,Velocities"},
        timeout=300,
        stream=True,
    )
    if cutout_resp is None or cutout_resp.status_code != 200:
        print(f"  halo {hid}: cutout failed, skip")
        return None
    with open(CUTOUT_TMP, "wb") as f:
        for chunk in cutout_resp.iter_content(chunk_size=1 << 20):
            f.write(chunk)

    try:
        with h5py.File(CUTOUT_TMP, "r") as f:
            coords = f["PartType1/Coordinates"][:].astype(np.float64)
            vels = f["PartType1/Velocities"][:].astype(np.float64)
    finally:
        CUTOUT_TMP.unlink(missing_ok=True)

    delta = periodic_delta(coords, group_pos)
    r = np.sqrt((delta**2).sum(axis=1))
    inside = r < r200
    n_inside = int(inside.sum())
    if n_inside < 50:
        print(f"  halo {hid}: only {n_inside} DM particles within R200, skip")
        return None

    v_rel = vels[inside] - group_vel[None, :]
    # 1D-equivalent velocity dispersion: sqrt(mean(|v_rel|^2)/3), matches the
    # standard astronomical convention (line-of-sight sigma_v).
    sigma_3d_sq = (v_rel**2).sum(axis=1).mean()
    sigma_v_1d = math.sqrt(sigma_3d_sq / 3.0)

    return {
        "halo_id": hid,
        "n_dm_in_r200": n_inside,
        "sigma_v_1d_kms": sigma_v_1d,
    }


def main() -> None:
    api_key = get_api_key()
    session = requests.Session()
    session.headers.update({"api-key": api_key})

    source_rows = list(csv.DictReader(open(IN_CSV)))
    print(f"Processing {len(source_rows)} clusters for DM velocity dispersion...")

    done_ids: set[str] = set()
    out_rows: list[dict] = []
    if OUT_CSV.exists():
        with open(OUT_CSV) as f:
            for r in csv.DictReader(f):
                out_rows.append(r)
                done_ids.add(r["halo_id"])
        print(f"Resuming: {len(done_ids)} clusters already done.")

    csv_exists = OUT_CSV.exists()
    fieldnames = list(source_rows[0].keys()) + ["n_dm_in_r200", "sigma_v_1d_kms"]
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
            merged = {
                **src_row,
                "n_dm_in_r200": result["n_dm_in_r200"],
                "sigma_v_1d_kms": result["sigma_v_1d_kms"],
            }
            writer.writerow(merged)
            csvfile.flush()
            out_rows.append(merged)
            print(
                f"  [{i + 1}/{len(source_rows)}] halo {hid}: "
                f"n_dm={result['n_dm_in_r200']}, sigma_v={result['sigma_v_1d_kms']:.1f} km/s"
            )

    print(f"\nWrote {len(out_rows)} rows to {OUT_CSV}")

    # ---- Analysis, same structure as the nsubs/offset checks ----
    n = len(out_rows)
    log_m = [math.log10(float(r["m200_msun"])) for r in out_rows]
    log_sigma = [math.log10(float(r["sigma_v_1d_kms"])) for r in out_rows]
    whim = [float(r["whim_mass_fraction_pct"]) for r in out_rows]

    def pearson(x: list[float], y: list[float]) -> float:
        mx, my = st.mean(x), st.mean(y)
        cov = sum((x[i] - mx) * (y[i] - my) for i in range(n)) / n
        return cov / (st.stdev(x) * st.stdev(y))

    def t_p(r: float, n: int) -> tuple[float, str]:
        df = n - 2
        t = r * math.sqrt(df) / math.sqrt(1 - r**2)
        at = abs(t)
        p = "<0.001" if at > 3.46 else "<0.01" if at > 2.65 else "<0.05" if at > 1.99 else "n.s."
        return t, p

    print("\n=== Positive-control check: is sigma_v collinear with mass, and positively? ===")
    r_m_sigma = pearson(log_m, log_sigma)
    t1, p1 = t_p(r_m_sigma, n)
    print(f"Pearson r(log M200, log sigma_v) = {r_m_sigma:.3f}  (t={t1:.2f}, p{p1})")
    print("(expected: strongly POSITIVE -- M-sigma relation; if not, the measurement is suspect)")

    print("\n=== Does raw sigma_v predict WHIM% directly? ===")
    r_sigma_whim = pearson(log_sigma, whim)
    t2, p2 = t_p(r_sigma_whim, n)
    print(f"Pearson r(log sigma_v, WHIM%) = {r_sigma_whim:.3f}  (t={t2:.2f}, p{p2})")

    print("\n=== Mass-detrended residual vs WHIM% ===")
    mean_lm, mean_ls = st.mean(log_m), st.mean(log_sigma)
    b = sum((log_m[i] - mean_lm) * (log_sigma[i] - mean_ls) for i in range(n)) / sum(
        (log_m[i] - mean_lm) ** 2 for i in range(n)
    )
    a = mean_ls - b * mean_lm
    resid = [log_sigma[i] - (a + b * log_m[i]) for i in range(n)]
    r_resid = pearson(resid, whim)
    t3, p3 = t_p(r_resid, n)
    print(
        f"Pearson r(mass-detrended log-sigma_v residual, WHIM%) = {r_resid:.3f}  (t={t3:.2f}, p{p3})"
    )


if __name__ == "__main__":
    main()
