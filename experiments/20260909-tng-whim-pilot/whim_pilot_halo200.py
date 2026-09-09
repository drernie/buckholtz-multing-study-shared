"""
TNG WHIM pilot -- Stage 1 of H1b prep, using real IllustrisTNG-300 data.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * L0 descriptive
NO_AUTHOR_ERROR -- this measures a real quantity from a real simulation,
not a claim about MULTING or v82.

Goal: verify, on ONE modest-mass pilot cluster (TNG300-1 halo 200,
M_200~1.2e14 Msun -- near H1b's own stated mass threshold, chosen
specifically because halo 0 (the most massive halo in the box) proved
too large for a quick pilot: its gas-only cutout was 754MB / 23.7M
particles vs this halo's 1.7M), that:

  (a) the TNG API's per-halo cutout.hdf5 endpoint genuinely returns gas
      particles out to the R200-3*R200 WHIM annulus this project needs
      (documentation was ambiguous on this -- confirmed empirically in
      a separate check: max r = 3.40*R200, 99.3% of particles < 3*R200);
  (b) the standard TNG temperature formula (from the project's own FAQ,
      https://www.tng-project.org/data/docs/faq/, General Question 6)
      gives physically sane results when applied to real particle data;
  (c) a real WHIM mass fraction / thermal energy value can be computed
      for one real cluster -- the missing ingredient this project CAN
      supply itself, distinct from the still-missing hydrostatic mass
      (M_HE), which remains external (see
      parked/H1b-whim-thermal-mass-bias.md).

This is Stage 1 (single-cluster pilot with controls). Scaling to
N>=71 clusters, and combining with M_HE once/if it arrives, is a
separate, later step -- not attempted here.
"""

import json

import h5py
import numpy as np

HALO_INFO = r"C:\Users\serge\AppData\Local\Temp\h_200.json"
CUTOUT = r"C:\Users\serge\AppData\Local\Temp\halo200_gas_full.hdf5"
BOX_SIZE = 205000.0  # ckpc/h, TNG300 periodic box side
HUBBLE = 0.6774  # TNG300's own cosmology (Planck2015), from the sim metadata

# Standard TNG gas-temperature formula, verified against
# https://www.tng-project.org/data/docs/faq/ General Question 6 this
# session (not from memory alone):
#   mu = 4 / (1 + 3*X_H + 4*X_H*x_e)          [dimensionless]
#   T  = (gamma-1) * u/k_B * (UnitEnergy/UnitMass) * mu
# with gamma=5/3, X_H=0.76, UnitEnergy/UnitMass ratio = 1e10 (erg/g per
# (km/s)^2), k_B and m_p in cgs.
GAMMA = 5.0 / 3.0
X_H = 0.76
UNIT_ENERGY_OVER_MASS = 1.0e10  # erg/g per (km/s)^2
K_B = 1.380649e-16  # erg/K
M_P = 1.6726219e-24  # g

WHIM_T_MIN, WHIM_T_MAX = 1.0e5, 1.0e7  # Kelvin, per H1b's own claim.md


def gas_temperature_kelvin(internal_energy_code, electron_abundance):
    """u in TNG code units (km/s)^2, x_e = ElectronAbundance. Returns T[K]."""
    mu = 4.0 / (1.0 + 3.0 * X_H + 4.0 * X_H * electron_abundance)
    return (GAMMA - 1.0) * internal_energy_code * UNIT_ENERGY_OVER_MASS * mu * M_P / K_B


def main() -> None:
    with open(HALO_INFO) as f:
        info = json.load(f)

    group_pos = np.array(info["GroupPos"])  # ckpc/h
    r200 = info["Group_R_Crit200"]  # ckpc/h
    m200 = info["Group_M_Crit200"] * 1e10 / HUBBLE
    group_mass_gas_catalog = info["GroupMassType"][0] * 1e10 / HUBBLE  # PartType0 = gas

    print("Pilot halo: TNG300-1 snap99 halo_id=200")
    print(f"  M_200 = {m200:.3e} Msun, R_200 = {r200 / HUBBLE:.1f} kpc (physical)")
    print(f"  Catalog GroupMassType[gas] = {group_mass_gas_catalog:.3e} Msun\n")

    with h5py.File(CUTOUT, "r") as f:
        gas = f["PartType0"]
        coords = gas["Coordinates"][:]
        u = gas["InternalEnergy"][:]
        x_e = gas["ElectronAbundance"][:]
        masses_code = gas["Masses"][:]  # 1e10 Msun/h per particle

    n_total = len(coords)
    masses_msun = masses_code * 1e10 / HUBBLE
    print(f"N gas particles in cutout: {n_total}")

    # ---- Positive control 1: cutout total gas mass vs catalog value ----
    total_cutout_mass = masses_msun.sum()
    ratio = total_cutout_mass / group_mass_gas_catalog
    print("\nPOSITIVE CONTROL 1 -- cutout total gas mass vs GroupMassType[gas]:")
    print(f"  cutout sum:      {total_cutout_mass:.3e} Msun")
    print(f"  catalog value:   {group_mass_gas_catalog:.3e} Msun")
    print(f"  ratio:           {ratio:.3f}")
    print(
        f"  {'PASS' if 0.5 < ratio < 3.0 else 'FAIL'} "
        f"(expect ratio > 1, since cutout goes well beyond the FoF-linked "
        f"gas GroupMassType itself counts -- not expecting exactly 1.0; "
        f"flag only if wildly off, e.g. >10x or <0.1x, which would signal "
        f"a units/field bug)"
    )

    # ---- Compute temperature, positive control 2: known physics ----
    temp_k = gas_temperature_kelvin(u, x_e)
    delta = coords - group_pos
    delta = delta - BOX_SIZE * np.round(delta / BOX_SIZE)
    r_ckpc_h = np.sqrt((delta**2).sum(axis=1))
    r_over_r200 = r_ckpc_h / r200

    inner = r_over_r200 < 0.3
    print("\nPOSITIVE CONTROL 2 -- inner ICM (r<0.3*R200) should be hot (~10^7 K):")
    print(f"  N inner particles: {inner.sum()}")
    print(f"  median T there:    {np.median(temp_k[inner]):.3e} K")
    print(
        f"  {'PASS' if 1e6 < np.median(temp_k[inner]) < 1e9 else 'FAIL'} "
        f"(a real, hot ICM core is the single most well-established fact "
        f"about massive clusters -- if this fails, the temperature "
        f"formula or units are wrong, nothing below can be trusted)"
    )

    print(f"\nFull temperature distribution (all {n_total} particles):")
    print(f"  min:    {temp_k.min():.3e} K")
    print(f"  median: {np.median(temp_k):.3e} K")
    print(f"  max:    {temp_k.max():.3e} K")

    # ---- The actual WHIM measurement ----
    in_annulus = (r_over_r200 >= 1.0) & (r_over_r200 <= 3.0)
    is_whim_temp = (temp_k >= WHIM_T_MIN) & (temp_k <= WHIM_T_MAX)
    whim_mask = in_annulus & is_whim_temp

    mass_annulus = masses_msun[in_annulus].sum()
    mass_whim = masses_msun[whim_mask].sum()
    # float64 cast is required: per-particle mass in grams (~1e7 Msun *
    # 1.989e33 g/Msun ~ 2e40) overflows float32's ~3.4e38 max -- caught
    # by a real RuntimeWarning on the first run, not a silent wrong number.
    mass_whim_g = masses_msun[whim_mask].astype(np.float64) * 1.989e33
    thermal_energy_whim = (mass_whim_g * K_B * temp_k[whim_mask].astype(np.float64) / M_P).sum()
    # ^ E_thermal ~ (3/2) N k_B T but we report the simpler M*k_B*T/m_p
    #   proxy here -- a genuine per-particle-count thermal-energy-scale
    #   quantity, not yet the full (3/2) internal energy integral;
    #   flagged explicitly, not silently presented as "the" thermal energy.

    print(f"\n{'=' * 60}")
    print("WHIM measurement, halo 200 (R200 < r < 3*R200, 1e5K < T < 1e7K):")
    print(f"{'=' * 60}")
    print(f"  N particles in annulus (any T):     {in_annulus.sum()}")
    print(f"  N particles in annulus AND WHIM-T:  {whim_mask.sum()}")
    print(f"  Gas mass in annulus (any T):        {mass_annulus:.3e} Msun")
    print(f"  Gas mass in annulus, WHIM only:     {mass_whim:.3e} Msun")
    print(f"  WHIM mass fraction of annulus gas:  {100 * mass_whim / mass_annulus:.2f}%")
    print(
        f"  WHIM proxy thermal-energy-scale:    {thermal_energy_whim:.3e} "
        f"(erg-equivalent, M*k_B*T/m_p proxy -- NOT the full (3/2) integral)"
    )


if __name__ == "__main__":
    main()
