"""EXPLORATORY, not a claim -- download ONLY the SO/200_crit/TotalMass
array (real, ~61MB, no positions yet) from the real FLAMINGO L1_m9
fiducial z=0 halo catalog, and check which mass-threshold N_sub range
would give a typical nearest-neighbor separation near v82's own
40-45 Mpc target -- WITHOUT yet downloading the much larger (368MB)
full position array. This determines exactly how many objects' own
positions actually need to be fetched (targeted download).
"""

import hdfstream
import numpy as np

HUBBLE = 0.681  # FLAMINGO fiducial cosmology, confirmed via Cosmology group


def main() -> None:
    root = hdfstream.open("cosma", "/")
    halo_file = root["FLAMINGO"]["L1_m9"]["L1_m9"]["SOAP-HBT"]["halo_properties_0077.hdf5"]

    mass_ds = halo_file["SO"]["200_crit"]["TotalMass"]
    print(f"Downloading TotalMass array: shape={mass_ds.shape}, dtype={mass_ds.dtype}")
    mass = np.asarray(mass_ds[:]) * 1e10  # SWIFT internal units -> Msun (standard convention)
    print(f"Downloaded {mass.nbytes / 1e6:.1f} MB")
    print(f"Mass range: {mass[mass > 0].min():.3e} - {mass.max():.3e} Msun")
    print(f"N with mass > 0: {(mass > 0).sum()} of {len(mass)}")

    order = np.argsort(-mass)
    mass_sorted = mass[order]

    # Rough density-based estimate: box volume / N -> mean spacing, then
    # actual thresholds will be checked with real positions in the next
    # script -- this just brackets plausible N_sub values cheaply.
    box_physical_mpc = 1000.0 / HUBBLE
    volume = box_physical_mpc**3
    print(f"\nBox: 1000 Mpc/h = {box_physical_mpc:.1f} Mpc physical, volume={volume:.3e} Mpc^3")

    print(f"\n{'N_sub':>8} {'mass_floor(Msun)':>18} {'mean_spacing_est(Mpc)':>22}")
    for n_sub in [500, 1000, 2000, 3000, 5000, 8000, 10000, 15000, 20000]:
        n_sub = min(n_sub, len(mass_sorted))
        floor = mass_sorted[n_sub - 1]
        mean_spacing = (volume / n_sub) ** (1 / 3)
        print(f"{n_sub:>8} {floor:>18.3e} {mean_spacing:>22.2f}")

    print("\nTargeted (fancy-indexed) position download, top 20000 (bracketing range)...")
    top_idx = order[:20000]
    pos_ds = halo_file["InputHalos"]["FOF"]["Centres"]
    sorted_idx = np.sort(top_idx)
    pos_all = np.asarray(pos_ds[sorted_idx, :])
    mass_all = mass[sorted_idx]
    print(f"Downloaded positions shape={pos_all.shape}, {pos_all.nbytes / 1e6:.2f} MB")

    reorder = np.argsort(-mass_all)
    pos_all, mass_all = pos_all[reorder], mass_all[reorder]

    print(
        f"position units check -- max coord: {pos_all.max():.2f} "
        f"(box should be ~1000 comoving Mpc/h or ~1468 physical Mpc)"
    )
    for k, v in pos_ds.attrs.items():
        if "exponent" in k.lower() or "convers" in k.lower() or "comoving" in k.lower():
            print(f"  Centres attr {k}: {v}")

    def true_nn_mpc(pos: np.ndarray, box_mpc: float) -> np.ndarray:
        diff = pos[:, None, :] - pos[None, :, :]
        diff = diff - box_mpc * np.round(diff / box_mpc)
        sep = np.sqrt((diff**2).sum(axis=-1))
        np.fill_diagonal(sep, np.inf)
        return sep.min(axis=1)

    print(f"\n{'N_sub':>8} {'mass_floor(Msun)':>18} {'med_true_NN':>12} {'mean_true_NN':>13}")
    for n_sub in [
        700,
        800,
        900,
        1000,
        1100,
        1200,
        1300,
        1500,
        2000,
        2500,
        3000,
        4000,
        5000,
        8000,
        10000,
        15000,
        20000,
    ]:
        n_sub = min(n_sub, len(mass_all))
        sub_pos = pos_all[:n_sub]
        # CORRECTED: h-scale exponent=0 on Centres means the stored box
        # size (1000.0) IS already physical Mpc at z=0 (a-scale=1) --
        # SWIFT's own convention, not h^-1 Mpc despite the "L1000" name.
        nn = true_nn_mpc(sub_pos, 1000.0)
        print(f"{n_sub:>8} {mass_all[n_sub - 1]:>18.3e} {np.median(nn):>12.2f} {nn.mean():>13.2f}")


if __name__ == "__main__":
    main()
