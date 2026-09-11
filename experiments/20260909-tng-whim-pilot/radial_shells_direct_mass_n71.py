"""Re-fetches gas cutouts for the same N=71 known-good clusters
(whim_n71_results.csv) a second time (temperature_profile_vs_mass.py's own
cutouts were deleted after that run), this time computing DIRECT
mass_inner_msun / mass_outer_msun (not the algebraically-reconstructed,
numerically fragile values from the mechanism_map check -- that
reconstruction divided by (hot_inner-hot_outer), unstable when the two are
close) plus a finer 4-shell radial split (1.0-1.5, 1.5-2.0, 2.0-2.5,
2.5-3.0 x R200) to see whether the mass-vs-hot_fraction correlation
transitions sharply or smoothly across radius, and whether the
mass-concentration-with-cluster-mass candidate (r=+0.437 in the
reconstructed check) is a real, direct measurement or an artifact of that
reconstruction.

Positive control: recomputed hot_fraction_inner_pct/hot_fraction_outer_pct
(the ORIGINAL 2-bin split) must match temperature_profile_vs_mass.py's own
whim_n71_temperature_profile.csv values -- same formula, same fields, same
cutout content -- confirms this is a real re-measurement, not a different
pipeline giving a different answer by accident.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR
"""

import csv
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

SHELL_EDGES = [1.0, 1.5, 2.0, 2.5, 3.0]
SHELL_NAMES = ["s1_1.0_1.5", "s2_1.5_2.0", "s3_2.0_2.5", "s4_2.5_3.0"]

IN_CSV = Path(__file__).parent / "whim_n71_results.csv"
REF_CSV = Path(__file__).parent / "whim_n71_temperature_profile.csv"
OUT_CSV = Path(__file__).parent / "whim_n71_radial_shells_direct.csv"
SCRATCH_DIR = Path("C:/Users/serge/AppData/Local/Temp/tng_radial_shells")
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

    hot_mask_base = temp_k > WHIM_T_MAX

    # --- ORIGINAL 2-bin split, for positive control against the prior CSV ---
    inner_ann = in_annulus & (r_over_r200 < 2.0)
    outer_ann = in_annulus & (r_over_r200 >= 2.0)
    mass_inner = masses_msun[inner_ann].sum()
    mass_outer = masses_msun[outer_ann].sum()
    hot_frac_inner = (
        100.0 * masses_msun[inner_ann & hot_mask_base].sum() / mass_inner
        if mass_inner > 0
        else float("nan")
    )
    hot_frac_outer = (
        100.0 * masses_msun[outer_ann & hot_mask_base].sum() / mass_outer
        if mass_outer > 0
        else float("nan")
    )

    out = {
        "halo_id": hid,
        "mass_annulus_msun_check": mass_annulus,
        "mass_inner_msun_DIRECT": mass_inner,
        "mass_outer_msun_DIRECT": mass_outer,
        "hot_fraction_inner_pct_check": hot_frac_inner,
        "hot_fraction_outer_pct_check": hot_frac_outer,
    }

    # --- NEW: 4 equal-width radial shells, direct mass + hot fraction each ---
    for name, lo, hi in zip(SHELL_NAMES, SHELL_EDGES[:-1], SHELL_EDGES[1:], strict=True):
        shell = (r_over_r200 >= lo) & (r_over_r200 < hi if hi < 3.0 else r_over_r200 <= hi)
        mass_shell = masses_msun[shell].sum()
        out[f"mass_{name}_msun"] = mass_shell
        out[f"hot_frac_{name}_pct"] = (
            100.0 * masses_msun[shell & hot_mask_base].sum() / mass_shell
            if mass_shell > 0
            else float("nan")
        )

    return out


def main() -> None:
    api_key = get_api_key()
    session = requests.Session()
    session.headers.update({"api-key": api_key})

    source_rows = list(csv.DictReader(open(IN_CSV, encoding="utf-8")))
    ref_rows = {r["halo_id"]: r for r in csv.DictReader(open(REF_CSV, encoding="utf-8"))}
    print(f"Processing {len(source_rows)} clusters for direct-mass radial shells...")

    done_ids: set[str] = set()
    out_rows: list[dict] = []
    if OUT_CSV.exists():
        with open(OUT_CSV, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                out_rows.append(r)
                done_ids.add(r["halo_id"])
        print(f"Resuming: {len(done_ids)} clusters already done.")

    # WHY: OUT_CSV.exists() alone is wrong -- open(path, "a") creates an empty
    # file even if the writer never gets to write a row (e.g. a killed run,
    # 0 successful clusters before being stopped). An empty-but-existing file
    # then makes a later run skip writeheader(), producing a headerless CSV
    # whose first DATA row silently becomes the DictReader header on resume
    # (caused the KeyError: 'halo_id' crash on the second resume attempt).
    csv_exists = OUT_CSV.exists() and OUT_CSV.stat().st_size > 0
    fieldnames = None

    with open(OUT_CSV, "a", newline="", encoding="utf-8") as csvfile:
        writer = None
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

            if writer is None:
                fieldnames = list(result.keys())
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                if not csv_exists:
                    writer.writeheader()

            writer.writerow(result)
            csvfile.flush()
            out_rows.append(result)

            ref = ref_rows.get(hid)
            control_note = ""
            if ref is not None:
                d_in = result["hot_fraction_inner_pct_check"] - float(ref["hot_fraction_inner_pct"])
                d_out = result["hot_fraction_outer_pct_check"] - float(
                    ref["hot_fraction_outer_pct"]
                )
                control_note = f"  [control: d_in={d_in:+.4f} d_out={d_out:+.4f}]"
            print(
                f"  [{i + 1}/{len(source_rows)}] halo {hid}: "
                f"m_in={result['mass_inner_msun_DIRECT']:.3e} "
                f"m_out={result['mass_outer_msun_DIRECT']:.3e}{control_note}"
            )

    print(f"\nWrote {len(out_rows)} rows to {OUT_CSV}")

    n = len(out_rows)
    max_d_in = max_d_out = 0.0
    for r in out_rows:
        ref = ref_rows.get(r["halo_id"])
        if ref is None:
            continue
        d_in = abs(float(r["hot_fraction_inner_pct_check"]) - float(ref["hot_fraction_inner_pct"]))
        d_out = abs(float(r["hot_fraction_outer_pct_check"]) - float(ref["hot_fraction_outer_pct"]))
        max_d_in = max(max_d_in, d_in)
        max_d_out = max(max_d_out, d_out)
    print(
        f"\nPOSITIVE CONTROL over {n} clusters: max|d_in|={max_d_in:.6f} pp, max|d_out|={max_d_out:.6f} pp"
    )
    print(
        "(should be ~0 -- confirms this re-fetch reproduces the original 2-bin measurement exactly)"
    )


if __name__ == "__main__":
    main()
