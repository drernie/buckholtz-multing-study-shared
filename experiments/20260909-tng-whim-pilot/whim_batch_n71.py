"""
TNG WHIM batch -- Stage 2: scale the Stage 1 pilot (single halo 200) to
N=71 real clusters, matching H1b's own AMENDMENT 2 minimum sample size
for a reachable KILL verdict.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR -- real measurements from a real public simulation, not
a claim about MULTING or v82. Still does NOT compute H1b's actual
correlation test -- hydrostatic mass (M_HE) remains external and
missing; see parked/H1b-whim-thermal-mass-bias.md.

Scope decision, stated explicitly (not hidden): candidate halo_ids are
drawn from a mid-mass window (id 5-400, skipping the top 5 most massive
halos in the box) rather than sampled evenly across the full mass range
above the 1e14 Msun threshold. Reason: halo 0's own Coordinates-only
cutout was 754MB (Stage 1 finding) -- including the very largest halos
would make a 71-cluster batch impractically slow. This is a real,
documented mass-range restriction, not a silent one. Catalog order is
NOT strictly mass-monotonic by halo_id (verified directly: halo 150 gave
8.83e13 Msun, halo 160 gave 1.71e14 Msun -- non-monotonic) -- so each
candidate's mass is checked individually, not assumed from its ID.

Checkpointed: each cluster's result is appended to the output CSV
immediately after computation, so an interrupted run still yields usable
partial data.
"""

import csv
import time
from pathlib import Path

import h5py
import numpy as np
import requests

API_KEY_FILE = Path.home() / ".secrets" / "tng_api_key.env"
BASE_URL = "https://www.tng-project.org/api/TNG300-1/snapshots/99"
OUT_CSV = Path(__file__).parent / "whim_n71_results.csv"
SCRATCH_DIR = Path("C:/Users/serge/AppData/Local/Temp/tng_batch")
SCRATCH_DIR.mkdir(exist_ok=True)

BOX_SIZE = 205000.0  # ckpc/h
HUBBLE = 0.6774
GAMMA = 5.0 / 3.0
X_H = 0.76
UNIT_ENERGY_OVER_MASS = 1.0e10
K_B = 1.380649e-16
M_P = 1.6726219e-24
WHIM_T_MIN, WHIM_T_MAX = 1.0e5, 1.0e7
MASS_THRESHOLD_MSUN = 1.0e14
N_TARGET = 71
CANDIDATE_ID_START = 5  # skip the top 5 most massive halos -- see docstring
CANDIDATE_ID_END = 400

FIELDS = "Coordinates,InternalEnergy,ElectronAbundance,Masses"


def get_api_key() -> str:
    text = API_KEY_FILE.read_text()
    for line in text.splitlines():
        if line.startswith("TNG_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise RuntimeError("TNG_API_KEY not found in key file")


def gas_temperature_kelvin(u_code: np.ndarray, x_e: np.ndarray) -> np.ndarray:
    mu = 4.0 / (1.0 + 3.0 * X_H + 4.0 * X_H * x_e)
    return (GAMMA - 1.0) * u_code * UNIT_ENERGY_OVER_MASS * mu * M_P / K_B


def fetch_halo_info(session: requests.Session, halo_id: int) -> dict | None:
    url = f"{BASE_URL}/halos/{halo_id}/info.json"
    r = session.get(url, timeout=30)
    if r.status_code != 200:
        return None
    d = r.json()
    if "Group_M_Crit200" not in d:
        return None
    return d


def fetch_gas_cutout(session: requests.Session, halo_id: int) -> Path:
    url = f"{BASE_URL}/halos/{halo_id}/cutout.hdf5"
    out_path = SCRATCH_DIR / f"halo{halo_id}_gas.hdf5"
    r = session.get(url, params={"gas": FIELDS}, timeout=600, stream=True)
    r.raise_for_status()
    with open(out_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=1 << 20):
            f.write(chunk)
    return out_path


def process_cluster(info: dict, cutout_path: Path) -> dict:
    group_pos = np.array(info["GroupPos"])
    r200 = info["Group_R_Crit200"]
    m200 = info["Group_M_Crit200"] * 1e10 / HUBBLE
    group_mass_gas_catalog = info["GroupMassType"][0] * 1e10 / HUBBLE
    group_mass_total = info["GroupMass"] * 1e10 / HUBBLE
    first_sub_id = info.get("GroupFirstSub", -1)

    with h5py.File(cutout_path, "r") as f:
        if "PartType0" not in f:
            return {"error": "no_gas_particles"}
        gas = f["PartType0"]
        coords = gas["Coordinates"][:]
        u = gas["InternalEnergy"][:]
        x_e = gas["ElectronAbundance"][:]
        masses_code = gas["Masses"][:]

    n_total = len(coords)
    masses_msun = masses_code.astype(np.float64) * 1e10 / HUBBLE
    total_cutout_mass = masses_msun.sum()
    control_ratio = (
        total_cutout_mass / group_mass_gas_catalog if group_mass_gas_catalog > 0 else float("nan")
    )

    temp_k = gas_temperature_kelvin(u, x_e)
    delta = coords - group_pos
    delta = delta - BOX_SIZE * np.round(delta / BOX_SIZE)
    r_ckpc_h = np.sqrt((delta**2).sum(axis=1))
    r_over_r200 = r_ckpc_h / r200

    inner = r_over_r200 < 0.3
    inner_median_t = float(np.median(temp_k[inner])) if inner.sum() > 10 else float("nan")

    in_annulus = (r_over_r200 >= 1.0) & (r_over_r200 <= 3.0)
    whim_mask = in_annulus & (temp_k >= WHIM_T_MIN) & (temp_k <= WHIM_T_MAX)

    mass_annulus = masses_msun[in_annulus].sum()
    mass_whim = masses_msun[whim_mask].sum()
    whim_fraction = 100.0 * mass_whim / mass_annulus if mass_annulus > 0 else float("nan")

    return {
        "m200_msun": m200,
        "r200_kpc_h": r200,
        "n_gas_particles": n_total,
        "control_gas_mass_ratio": control_ratio,
        "control_inner_icm_T_K": inner_median_t,
        "control_pass": bool(0.5 < control_ratio < 3.0 and 1e6 < inner_median_t < 1e9),
        "n_annulus": int(in_annulus.sum()),
        "n_whim": int(whim_mask.sum()),
        "mass_annulus_msun": mass_annulus,
        "mass_whim_msun": mass_whim,
        "whim_mass_fraction_pct": whim_fraction,
        "group_mass_total_msun": group_mass_total,
        "group_nsubs": info.get("GroupNsubs", -1),
        "group_first_sub_id": first_sub_id,
    }


def main() -> None:
    api_key = get_api_key()
    session = requests.Session()
    session.headers.update({"api-key": api_key})

    write_header = not OUT_CSV.exists()
    n_collected = 0
    n_checked = 0
    t_start = time.time()

    fieldnames = [
        "halo_id",
        "m200_msun",
        "r200_kpc_h",
        "n_gas_particles",
        "control_gas_mass_ratio",
        "control_inner_icm_T_K",
        "control_pass",
        "n_annulus",
        "n_whim",
        "mass_annulus_msun",
        "mass_whim_msun",
        "whim_mass_fraction_pct",
        "group_mass_total_msun",
        "group_nsubs",
        "group_first_sub_id",
        "elapsed_s",
    ]

    with open(OUT_CSV, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
            csvfile.flush()

        already_done = set()
        if not write_header:
            with open(OUT_CSV) as rf:
                for row in csv.DictReader(rf):
                    already_done.add(int(row["halo_id"]))
            n_collected = len(already_done)
            print(f"Resuming: {n_collected} clusters already done, skipping those IDs.")

        for halo_id in range(CANDIDATE_ID_START, CANDIDATE_ID_END):
            if n_collected >= N_TARGET:
                break
            if halo_id in already_done:
                continue

            n_checked += 1
            t0 = time.time()
            info = fetch_halo_info(session, halo_id)
            if info is None:
                print(f"  halo {halo_id}: no info, skip")
                continue

            m200 = info["Group_M_Crit200"] * 1e10 / HUBBLE
            if m200 < MASS_THRESHOLD_MSUN:
                print(f"  halo {halo_id}: M200={m200:.2e} Msun < threshold, skip")
                continue

            try:
                cutout_path = fetch_gas_cutout(session, halo_id)
            except Exception as e:
                print(f"  halo {halo_id}: M200={m200:.2e} Msun, cutout FAILED: {e}")
                continue

            try:
                result = process_cluster(info, cutout_path)
            except Exception as e:
                print(f"  halo {halo_id}: processing FAILED: {e}")
                cutout_path.unlink(missing_ok=True)
                continue
            finally:
                cutout_path.unlink(missing_ok=True)  # don't keep 71x ~50-150MB files

            if "error" in result:
                print(f"  halo {halo_id}: {result['error']}, skip")
                continue

            elapsed = time.time() - t0
            row = {"halo_id": halo_id, "elapsed_s": round(elapsed, 1), **result}
            writer.writerow(row)
            csvfile.flush()
            n_collected += 1

            print(
                f"  [{n_collected}/{N_TARGET}] halo {halo_id}: M200={m200:.2e} Msun, "
                f"WHIM%={result['whim_mass_fraction_pct']:.1f}, "
                f"control={'PASS' if result['control_pass'] else 'FAIL'}, "
                f"{elapsed:.1f}s"
            )

    total_elapsed = time.time() - t_start
    print(
        f"\nDone. {n_collected}/{N_TARGET} clusters collected, {n_checked} IDs checked, "
        f"{total_elapsed / 60:.1f} min elapsed. Output: {OUT_CSV}"
    )


if __name__ == "__main__":
    main()
