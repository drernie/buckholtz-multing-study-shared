#!/usr/bin/env python3
"""
cluster_data_pipeline.py — MULTING H(z) data ingestion
NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION

Steps:
  1. Download MCXC-I  (M500, R500, z)        → data/catalogs/mcxc.csv
  2. Cross-match PSZ2 for Y_SZ proxy          → joined in memory
  3. Cross-match Wen & Han 2024 merger flags  → joined in memory
  4. Derive E_thermal/c²                      → data/catalogs/clusters_raw.csv
  5. Export merger-excluded table             → data/clusters_clean.csv
  6. Save Moresco+2022 CC H(z)               → data/hz_cc.csv

Usage:
  python src/cluster_data_pipeline.py
  python src/cluster_data_pipeline.py --max-rows 500 --z-max 0.6

Dependencies (add to requirements.txt):
  astropy>=5.3
  astroquery>=0.4.6
  requests>=2.28
"""

from __future__ import annotations

import argparse
import logging
from pathlib import Path

import numpy as np
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger(__name__)

# ── Physical constants ──────────────────────────────────────────────────────
_C_M_S = 2.998e8  # m/s
_C2 = _C_M_S**2  # m²/s²
_MSUN_KG = 1.989e30  # kg
_MP_KG = 1.673e-27  # kg  proton mass
_KB_J = 1.381e-23  # J/K Boltzmann
_KEV_J = 1.602e-16  # J per keV
_MU = 0.61  # mean molecular weight (fully ionized H+He, 25% He)
_SIGMA_T = 6.652e-29  # m²  Thomson cross-section
_ME_KG = 9.109e-31  # kg  electron mass

# ── Hard-exclude: confirmed major mergers ───────────────────────────────────
# Source: literature (Bullet Cluster, El Gordo, Abell 2744, Abell 520)
_HARD_EXCLUDE_IDS = frozenset(
    [
        "MCXC J0658.5-5556",  # Bullet Cluster 1E 0657-56   z=0.296
        "MCXC J0014.3-3023",  # Abell 2744 (Pandora's Box)  z=0.308
        "MCXC J0454.4-0254",  # Abell 520  (Train Wreck)    z=0.199
    ]
)
_HARD_EXCLUDE_NAMES = frozenset(
    [
        "1E 0657-56",
        "ACT-CL J0102-4915",  # El Gordo z=0.87
    ]
)

# ── Moresco+2022 CC H(z) — hardcoded from arXiv:2201.07241 ─────────────────
# [VERIFIED] from Table 1, subset of 27 points (full set at gitlab.com/mmoresco)
# NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION
_HZ_CC_DATA = [
    # (z,    Hz [km/s/Mpc],  sigma_Hz)
    (0.070, 69.0, 19.6),
    (0.090, 69.0, 12.0),
    (0.120, 68.6, 26.2),
    (0.170, 83.0, 8.0),
    (0.179, 75.0, 4.0),
    (0.199, 75.0, 5.0),
    (0.200, 72.9, 29.6),
    (0.270, 77.0, 14.0),
    (0.280, 88.8, 36.6),
    (0.352, 83.0, 14.0),
    (0.380, 83.0, 13.5),
    (0.400, 95.0, 17.0),
    (0.480, 97.0, 62.0),
    (0.593, 104.0, 13.0),
    (0.680, 92.0, 8.0),
    (0.750, 98.8, 33.6),
    (0.781, 105.0, 12.0),
    (0.875, 125.0, 17.0),
    (0.880, 90.0, 40.0),
    (0.900, 117.0, 23.0),
    (1.037, 154.0, 20.0),
    (1.300, 168.0, 17.0),
    (1.363, 160.0, 33.6),
    (1.430, 177.0, 18.0),
    (1.530, 140.0, 14.0),
    (1.750, 202.0, 40.0),
    (1.965, 186.5, 50.4),
]


# ── Thermal energy derivations ──────────────────────────────────────────────


def e_thermal_path_a(mgas_msun: float, tx_kev: float) -> float:
    """
    Path A: E_thermal/c² [M_sun] from gas mass [M_sun] + T_X [keV].
    Formula: E = (3/2) × (Mgas / μmp) × kB × T
    Assumptions: μ=0.61, single-temperature, spherical.
    """
    n_particles = (mgas_msun * _MSUN_KG) / (_MU * _MP_KG)
    t_kelvin = tx_kev * _KEV_J / _KB_J
    e_joules = 1.5 * n_particles * _KB_J * t_kelvin
    return e_joules / (_MSUN_KG * _C2)


def e_thermal_path_b(y500_arcmin2: float, z: float) -> float:
    """
    Path B: E_thermal/c² [M_sun] from Y_SZ [arcmin²] + redshift.
    Formula: E = Y_SZ_sr × D_A² × (me c² / σ_T)
    Requires: astropy + Planck18 cosmology (ΛCDM assumed).
    """
    try:
        from astropy import units as u
        from astropy.cosmology import Planck18
    except ImportError:
        return float("nan")

    y_sr = y500_arcmin2 * (np.pi / 10800.0) ** 2  # arcmin² → steradians
    d_a_m = Planck18.angular_diameter_distance(z).to(u.m).value
    e_joules = y_sr * d_a_m**2 * (_ME_KG * _C2 / _SIGMA_T)
    return e_joules / (_MSUN_KG * _C2)


# ── Angular cross-match ─────────────────────────────────────────────────────


def _crossmatch_idx(
    ra1: np.ndarray,
    dec1: np.ndarray,
    ra2: np.ndarray,
    dec2: np.ndarray,
    radius_arcsec: float,
) -> np.ndarray:
    """Return per-row index into catalog2 (or -1 if no match within radius)."""
    try:
        from astropy import units as u
        from astropy.coordinates import SkyCoord
    except ImportError:
        log.warning("astropy not available — cross-match skipped, returning -1")
        return np.full(len(ra1), -1, dtype=int)

    c1 = SkyCoord(ra=ra1 * u.deg, dec=dec1 * u.deg)
    c2 = SkyCoord(ra=ra2 * u.deg, dec=dec2 * u.deg)
    idx, sep, _ = c1.match_to_catalog_sky(c2)
    return np.where(sep.arcsec < radius_arcsec, idx, -1)


# ── VizieR download ─────────────────────────────────────────────────────────


def _vizier_download(catalog_id: str, columns: list[str], row_limit: int) -> pd.DataFrame:
    """Download a VizieR catalog table via astroquery."""
    from astroquery.vizier import Vizier  # type: ignore[import]

    v = Vizier(columns=columns, row_limit=row_limit)
    result = v.get_catalogs(catalog_id)
    if not result:
        raise RuntimeError(f"VizieR returned nothing for {catalog_id!r}")
    return result[0].to_pandas()


# ── Step 1: MCXC-I backbone ─────────────────────────────────────────────────


def _sexagesimal_to_deg(ra_col: pd.Series, dec_col: pd.Series) -> tuple[np.ndarray, np.ndarray]:
    """Convert MCXC sexagesimal RA (HH MM SS) and Dec (±DD MM SS) to decimal degrees."""
    from astropy import units as u
    from astropy.coordinates import Angle

    ra_deg = np.array(
        [
            Angle(v, unit=u.hourangle).deg if isinstance(v, str) and v.strip() else np.nan
            for v in ra_col
        ]
    )
    dec_deg = np.array(
        [Angle(v, unit=u.deg).deg if isinstance(v, str) and v.strip() else np.nan for v in dec_col]
    )
    return ra_deg, dec_deg


def step1_mcxc(out_dir: Path, row_limit: int, z_max: float) -> pd.DataFrame:
    log.info("Step 1: MCXC-I backbone (VizieR J/A+A/534/A109)...")
    raw = _vizier_download(
        "J/A+A/534/A109",
        columns=["MCXC", "RAJ2000", "DEJ2000", "z", "M500", "R500"],
        row_limit=row_limit,
    )
    # MCXC RA/Dec are sexagesimal strings — convert to decimal degrees
    ra_deg, dec_deg = _sexagesimal_to_deg(raw["RAJ2000"], raw["DEJ2000"])
    df = pd.DataFrame(
        {
            "cluster_id": raw["MCXC"].astype(str).str.strip(),
            "catalog": "MCXC-I",
            "ra_deg": ra_deg,
            "dec_deg": dec_deg,
            "z": pd.to_numeric(raw["z"], errors="coerce"),
            "M500c_Msun": pd.to_numeric(raw["M500"], errors="coerce") * 1e14,
            "M500c_method": "X-ray_Lx_scaling",
            "R500c_Mpc": pd.to_numeric(raw["R500"], errors="coerce"),
        }
    )
    df = df.dropna(subset=["ra_deg", "dec_deg", "z", "M500c_Msun"])
    df = df[(df["z"] > 0) & (df["z"] <= z_max)].reset_index(drop=True)
    out = out_dir / "mcxc.csv"
    df.to_csv(out, index=False)
    log.info(f"  → {len(df)} clusters (z ≤ {z_max}) saved to {out.name}")
    return df


# ── Step 2: PSZ2 Y_SZ cross-match ──────────────────────────────────────────


def step2_psz2(df: pd.DataFrame, row_limit: int) -> pd.DataFrame:
    log.info("Step 2: PSZ2 Y_SZ cross-match (VizieR J/A+A/594/A27)...")
    try:
        raw = _vizier_download(
            "J/A+A/594/A27",
            columns=["PSZ2", "RAJ2000", "DEJ2000", "Y5R500", "MCXC"],
            row_limit=row_limit,
        )
        # Y5R500 in units of 0.001 arcmin² (PSZ2 ReadMe, J/A+A/594/A27)
        psz_ra = pd.to_numeric(raw["RAJ2000"], errors="coerce").to_numpy()
        psz_dec = pd.to_numeric(raw["DEJ2000"], errors="coerce").to_numpy()
        psz_y = pd.to_numeric(raw["Y5R500"], errors="coerce").to_numpy() * 0.001

        # Primary join: PSZ2.MCXC column → MCXC-I name (normalize to "MCXC J..." form)
        psz_mcxc_raw = raw["MCXC"].astype(str).str.strip()
        psz_mcxc_norm = psz_mcxc_raw.apply(
            lambda x: (
                ("MCXC " + x)
                if (x and x not in {"--", "nan", ""} and not x.startswith("MCXC"))
                else x
            )
        )
        valid_name = psz_mcxc_norm.str.startswith("MCXC J")
        name_to_y = dict(zip(psz_mcxc_norm[valid_name], psz_y[valid_name.values], strict=False))

        def _norm_id(cid: str) -> str:
            cid = cid.strip()
            return cid if cid.startswith("MCXC ") else f"MCXC {cid}"

        df["Y500_arcmin2"] = df["cluster_id"].apply(_norm_id).map(name_to_y)
        n_by_name = int(df["Y500_arcmin2"].notna().sum())
        log.info(f"  → {n_by_name}/{len(df)} matched by MCXC name join")

        # Fallback: coordinate cross-match for clusters still unmatched
        unmatched = df["Y500_arcmin2"].isna()
        if unmatched.any():
            valid_coord = np.isfinite(psz_ra) & np.isfinite(psz_dec) & np.isfinite(psz_y)
            if valid_coord.any():
                idx = _crossmatch_idx(
                    df.loc[unmatched, "ra_deg"].to_numpy(),
                    df.loc[unmatched, "dec_deg"].to_numpy(),
                    psz_ra[valid_coord],
                    psz_dec[valid_coord],
                    radius_arcsec=60.0,
                )
                psz_y_c = psz_y[valid_coord]
                coord_y = np.where(idx >= 0, psz_y_c[np.maximum(idx, 0)], np.nan)
                df.loc[unmatched, "Y500_arcmin2"] = coord_y
                n_by_coord = int((idx >= 0).sum())
                log.info(f'  → {n_by_coord} additional matched by coordinates (r<60")')

        df["ICM_proxy_type"] = np.where(
            df["Y500_arcmin2"].notna() & (df["Y500_arcmin2"] > 0),
            "Y_SZ_derived_LCDM",
            "not_available",
        )

        # Derive E_thermal via Path B
        mask_b = df["Y500_arcmin2"].notna() & (df["Y500_arcmin2"] > 0) & (df["z"] > 0)
        df["Ethermal_c2_Msun"] = np.nan
        if mask_b.any():
            df.loc[mask_b, "Ethermal_c2_Msun"] = [
                e_thermal_path_b(y, z)
                for y, z in zip(df.loc[mask_b, "Y500_arcmin2"], df.loc[mask_b, "z"], strict=False)
            ]
            log.info(f"  → E_thermal (Path B, Y_SZ) for {mask_b.sum()} clusters")
    except Exception as exc:
        log.warning(f"  PSZ2 step failed ({exc}); Y_SZ left as NaN")
        df["Y500_arcmin2"] = np.nan
        df["ICM_proxy_type"] = "not_available"
        df["Ethermal_c2_Msun"] = np.nan
    return df


# ── Step 3: Wen & Han 2024 merger flags ────────────────────────────────────


def step3_merger_flags(df: pd.DataFrame) -> pd.DataFrame:
    """Wen & Han 2024 not yet indexed on VizieR — hard-exclude only.
    Replace with VizieR cross-match once J/MNRAS/532/1849 becomes available."""
    log.info("Step 3: merger flags (hard-exclude list; Wen & Han 2024 not yet on VizieR)...")
    df["dynamical_state"] = "unknown"
    df["merger_exclusion_flag"] = False
    df["merger_exclusion_reason"] = ""

    # Robust to both "J0658.5-5556" (bare) and "MCXC J0658.5-5556" (full) formats
    _bare_ids = frozenset(n.removeprefix("MCXC ") for n in _HARD_EXCLUDE_IDS)
    hard_mask = df["cluster_id"].apply(
        lambda cid: cid.strip() in _bare_ids or cid.strip() in _HARD_EXCLUDE_IDS
    )
    df.loc[hard_mask, "merger_exclusion_flag"] = True
    df.loc[hard_mask, "dynamical_state"] = "disturbed"
    df.loc[hard_mask, "merger_exclusion_reason"] = "named_known_merger"
    log.info(f"  → {hard_mask.sum()} clusters hard-excluded by name")
    return df


# ── Step 4: export clean table ──────────────────────────────────────────────


def step4_export(df: pd.DataFrame, data_dir: Path) -> pd.DataFrame:
    log.info("Step 4: exporting cluster tables...")
    df["TX_keV"] = np.nan  # placeholder; fill via CHEX-MATE crossmatch later
    df["Mgas_Msun"] = np.nan  # placeholder
    df["source_url"] = "https://cdsarc.u-strasbg.fr/viz-bin/cat/J/A+A/534/A109"

    schema_cols = [
        "cluster_id",
        "catalog",
        "ra_deg",
        "dec_deg",
        "z",
        "M500c_Msun",
        "M500c_method",
        "R500c_Mpc",
        "TX_keV",
        "Mgas_Msun",
        "Y500_arcmin2",
        "ICM_proxy_type",
        "Ethermal_c2_Msun",
        "dynamical_state",
        "merger_exclusion_flag",
        "merger_exclusion_reason",
        "source_url",
    ]
    df_all = df.reindex(columns=schema_cols)

    # Save raw (all clusters before exclusion)
    raw_out = data_dir / "catalogs" / "clusters_raw.csv"
    raw_out.parent.mkdir(parents=True, exist_ok=True)
    df_all.to_csv(raw_out, index=False)

    # Save clean (merger-excluded)
    clean = df_all[~df_all["merger_exclusion_flag"]].copy()
    clean_out = data_dir / "clusters_clean.csv"
    clean.to_csv(clean_out, index=False)

    n_with_e = clean["Ethermal_c2_Msun"].notna().sum()
    log.info(f"  → raw: {len(df_all)} clusters → {raw_out.name}")
    log.info(f"  → clean (merger-excluded): {len(clean)} clusters → {clean_out.name}")
    log.info(f"  → clusters with E_thermal/c²: {n_with_e}")
    return clean


# ── Step 5: Moresco+2022 CC H(z) ───────────────────────────────────────────


def step5_hz(data_dir: Path) -> pd.DataFrame:
    log.info("Step 5: Moresco+2022 CC H(z)...")
    df_hz: pd.DataFrame | None = None

    # Try fetching live from GitLab
    try:
        import requests  # type: ignore[import]

        url = "https://gitlab.com/mmoresco/CCcovariance/-/raw/master/data/CC_Hubble.dat"
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        rows = []
        for line in resp.text.strip().splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) >= 3:
                rows.append((float(parts[0]), float(parts[1]), float(parts[2])))
        if rows:
            df_hz = pd.DataFrame(rows, columns=["z", "Hz_km_s_Mpc", "sigma_Hz"])
            log.info(f"  → {len(df_hz)} CC points fetched from GitLab")
    except Exception as exc:
        log.warning(f"  GitLab fetch failed ({exc}); using hardcoded table")

    if df_hz is None or df_hz.empty:
        df_hz = pd.DataFrame(_HZ_CC_DATA, columns=["z", "Hz_km_s_Mpc", "sigma_Hz"])
        log.info(f"  → {len(df_hz)} CC points from hardcoded Moresco+2022 table")

    df_hz["source"] = "Moresco+2022_arXiv:2201.07241"
    df_hz["method"] = "cosmic_chronometer"
    df_hz["FLRW_independent"] = True
    out = data_dir / "hz_cc.csv"
    df_hz.to_csv(out, index=False)
    log.info(f"  → saved to {out.name}")
    return df_hz


# ── Main ────────────────────────────────────────────────────────────────────


def main() -> None:
    parser = argparse.ArgumentParser(
        description="MULTING cluster data pipeline. "
        "NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION"
    )
    parser.add_argument(
        "--max-rows",
        type=int,
        default=2000,
        help="VizieR row limit per catalog (-1 = all, slow)",
    )
    parser.add_argument(
        "--z-max",
        type=float,
        default=1.2,
        help="Maximum redshift to include (default: 1.2)",
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=Path("data"),
        help="Root data directory (default: data/)",
    )
    args = parser.parse_args()

    args.data_dir.mkdir(parents=True, exist_ok=True)
    (args.data_dir / "catalogs").mkdir(exist_ok=True)

    # Check astroquery availability
    try:
        import astroquery  # noqa: F401  # type: ignore[import]
    except ImportError:
        log.error(
            "astroquery not installed. Run:\n"
            "  pip install astropy astroquery requests\n"
            "Then re-run this script."
        )
        raise SystemExit(1) from None

    df = step1_mcxc(args.data_dir, args.max_rows, args.z_max)
    df = step2_psz2(df, args.max_rows)
    df = step3_merger_flags(df)
    clean = step4_export(df, args.data_dir)
    hz = step5_hz(args.data_dir)

    log.info("")
    log.info("=" * 60)
    log.info("NOT_VALIDATION · NOT_REFUTATION · OUR_RECONSTRUCTION")
    log.info(f"  Clusters (clean):       {len(clean)}")
    log.info(f"  With E_thermal/c²:      {clean['Ethermal_c2_Msun'].notna().sum()}")
    log.info(f"  z range:                {clean['z'].min():.3f} – {clean['z'].max():.3f}")
    log.info(f"  Merger-excluded:        {(~df['merger_exclusion_flag']).sum()} kept")
    log.info(f"  H(z) CC points:         {len(hz)}")
    log.info("")
    log.info("Next: fit β_d·r_A and β_q via src/k_a_closure_test.py")
    log.info("      using data/clusters_clean.csv + data/hz_cc.csv")
    log.info("=" * 60)


if __name__ == "__main__":
    main()
