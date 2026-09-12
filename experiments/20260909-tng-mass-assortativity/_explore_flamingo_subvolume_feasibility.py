"""EXPLORATORY, not a claim -- feasibility check for a real, genuinely
independent-volume replication of TNG300's N=35 rho_NN=-0.42 anomaly.

Design: partition FLAMINGO's real 1000 Mpc physical box into a 3x3x3
grid of non-overlapping sub-cubes, each EXACTLY TNG300's own physical
box size (302.6267 Mpc) -- 27 genuinely independent "TNG300-sized
volumes" carved out of one real, much larger simulation. Within each
sub-cube, apply the SAME selection protocol already used for TNG300
(scan candidate local N for one whose median AND mean true-NN
separation, computed treating the sub-cube as its own periodic box,
land in 40-45 Mpc) -- to get an EMPIRICAL distribution of rho_NN
values from many real, independent TNG300-sized regions, directly
testing whether |rho_NN|>=0.42 is a rare outlier or a common outcome
of this small-N selection protocol.

This script ONLY checks: (a) how many of a global top-N-by-mass sample
land in each sub-cube, (b) whether each sub-cube has enough halos to
find a usable local N. NO correlation is computed here.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION * exploratory only
"""

import hdfstream
import numpy as np

TNG300_MPC = 302.6267  # matches TNG300's own physical box size, for direct comparability
N_GRID = 3  # 3x3x3 = 27 sub-cubes, using [0, 3*TNG300_MPC) of the 1000 Mpc box per axis
GLOBAL_N_TOP = 5000  # generous headroom so even underdense sub-cubes have enough candidates


def main() -> None:
    root = hdfstream.open("cosma", "/")
    halo_file = root["FLAMINGO"]["L1_m9"]["L1_m9"]["SOAP-HBT"]["halo_properties_0077.hdf5"]

    print("Downloading full SO/200_crit/TotalMass array (real, ~61MB)...")
    mass_ds = halo_file["SO"]["200_crit"]["TotalMass"]
    mass = np.asarray(mass_ds[:]) * 1e10  # -> Msun
    order = np.argsort(-mass)
    top_idx = np.sort(order[:GLOBAL_N_TOP])

    print(f"Targeted download: positions for top {GLOBAL_N_TOP} most massive halos...")
    pos_ds = halo_file["InputHalos"]["FOF"]["Centres"]
    pos = np.asarray(pos_ds[top_idx, :])
    top_mass = mass[top_idx]

    reorder = np.argsort(-top_mass)
    pos, top_mass = pos[reorder], top_mass[reorder]

    print(f"N={GLOBAL_N_TOP}, mass range {top_mass.min():.3e} - {top_mass.max():.3e} Msun")

    edge = N_GRID * TNG300_MPC
    print(
        f"\nGrid: {N_GRID}^3={N_GRID**3} sub-cubes, side={TNG300_MPC:.4f} Mpc, "
        f"covering [0,{edge:.2f}) Mpc of the 1000 Mpc box per axis"
    )

    in_grid = np.all((pos >= 0) & (pos < edge), axis=1)
    print(f"Halos inside the {edge:.2f}^3 Mpc grid region: {in_grid.sum()} / {GLOBAL_N_TOP}")

    cube_idx = np.floor(pos[in_grid] / TNG300_MPC).astype(int)
    cube_idx = np.clip(cube_idx, 0, N_GRID - 1)
    flat_id = cube_idx[:, 0] * N_GRID * N_GRID + cube_idx[:, 1] * N_GRID + cube_idx[:, 2]

    print(f"\n{'sub-cube':>9} {'n_halos':>8} {'min_mass':>12} {'max_mass':>12}")
    counts = []
    for c in range(N_GRID**3):
        mask = flat_id == c
        n = int(mask.sum())
        counts.append(n)
        if n > 0:
            m = top_mass[in_grid][mask]
            print(f"{c:>9} {n:>8} {m.min():>12.3e} {m.max():>12.3e}")
        else:
            print(f"{c:>9} {n:>8} {'--':>12} {'--':>12}")

    counts = np.array(counts)
    print(
        f"\nsub-cube halo counts: min={counts.min()}, median={np.median(counts):.1f}, "
        f"max={counts.max()}, mean={counts.mean():.1f}"
    )
    print(
        f"sub-cubes with >=35 halos (TNG300's own successful N): {(counts >= 35).sum()} / {N_GRID**3}"
    )
    print(
        f"sub-cubes with >=15 halos (minimum for a meaningful local scan): "
        f"{(counts >= 15).sum()} / {N_GRID**3}"
    )


if __name__ == "__main__":
    main()
