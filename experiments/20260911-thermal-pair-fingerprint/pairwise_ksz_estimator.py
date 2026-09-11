"""pairwise_ksz_estimator.py -- core classical pairwise-momentum kSZ
estimator (Fork 1b, data_acquisition_plan.md item 2), Phase 1: build and
validate the estimator MATH on synthetic data, real-map/real-catalog
application is a separate, much larger, not-yet-started phase.

NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION - NO_AUTHOR_ERROR

[CORRECTION to data_acquisition_plan.md's own ingredient table, found
before writing any code] Item 2's "Access" column says kSZ pairwise
dynamics reuses "Same y-map (#1)" (the Compton-y map). That is wrong for
the classical estimator this file implements: Hand et al. 2012
(arXiv:1203.4219, [VERIFIED] via mcp__arxiv__download_paper, full text
read directly, not assumed from memory) use the ACT 148 GHz *brightness
TEMPERATURE* map, not a component-separated Compton-y map -- the kSZ
signal IS a temperature distortion (frequency-independent), distinct
from the tSZ spectral distortion the y-map isolates. Their own text:
"we treat the effective microwave temperature at 148 GHz measured by
ACT in the direction of the cluster as a noisy estimator of the
cluster's line-of-sight momentum". The pairwise DIFFERENCE statistic
(Eq. 2 below) is insensitive to tSZ/dust/noise precisely because those
components do not correlate with pair separation direction -- no tSZ
subtraction is required for the basic estimator (their Table 1 uses a
148/218 GHz linear combination only as a separate cross-check, not as
an input to the momentum estimator itself). This file's real-data phase
will need ACT DR6's coadded temperature map product, not
`ilc_actplanck_ymap.fits` -- corrected here, not yet corrected in
`data_acquisition_plan.md` (see that file's own item 2 row for the
still-uncorrected original text).

Estimator (Hand et al. 2012, arXiv:1203.4219, Eqs. 1-3, transcribed
directly from the paper's own arXiv HTML source, not re-derived):

    p_pair(r) = < (p_i - p_j) . r_hat_ij >                         (1)

    p_tilde_pair(r) = sum_{i<j} (q_i - q_j) c_ij / sum_{i<j} c_ij^2  (2)

    c_ij = r_hat_ij . (r_hat_i + r_hat_j)/2
         = (r_i - r_j)(1 + cos theta) / (2 sqrt(r_i^2+r_j^2-2 r_i r_j cos theta))
                                                                      (3)

where q_i == p_i . r_hat_i is cluster i's line-of-sight momentum
component (the quantity actually probed by the kSZ temperature via
T_kSZ,i = -N_kSZ * q_i), r_hat_i is the unit vector from the observer
to cluster i, r_i = |r_i| is the comoving distance to cluster i, and
theta is the angular separation between clusters i and j on the sky.
Sum is over pairs in a bin around comoving separation r = |r_i - r_j|.

`core_pairwise_estimator()` below implements Eq. 2-3 exactly, working
directly in the caller's chosen units for q_i (so it can be tested
against a KNOWN synthetic q_i without any T<->q sign/normalization
question). `pairwise_momentum_from_temperature()` is a thin wrapper
implementing the T_i = -N_kSZ * q_i sign convention for real map data,
kept separate so the core formula stays auditable line-by-line against
the paper.

Validation strategy (this file's Phase-1 scope): reuse REAL (RA, Dec, z)
cluster positions from `exact_pair_census.py` (ACT-DR5 MCMF,
arXiv:2406.14754) -- same convention as `power_analysis_s_dependent.py`
and `synthetic_four_world_battery.py` in this same experiment folder --
but with a SYNTHETIC, ground-truth-known line-of-sight momentum field,
not real map data (no real ACT temperature map has been downloaded or
touched by this file). Two controls:

  - Positive control: a toy softened pairwise "infall" velocity field
    (`toy_infall_velocity()`) that is attractive by construction (every
    pair pulls every other pair together) -- the estimator MUST recover
    a negative p_tilde_pair(r) (pairs approaching each other) at small
    r, weakening at large r, or the implementation has a sign/formula
    bug.
  - Negative control: q_i = pure Gaussian noise, no velocity signal --
    p_tilde_pair(r) must be consistent with zero (within jackknife
    error bars) at every r, or the implementation has a spurious-signal
    bug.

Real-map real-catalog application (per data_acquisition_plan.md's own
honest costing, the dominant ~1-3 week item) is explicitly NOT attempted
here -- this file only builds and validates the estimator machinery
itself, which data_acquisition_plan.md flagged as having "no existing
code anywhere in this repo to build from."
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from exact_pair_census import Z_HIGH, Z_LOW, load_catalog, radec_z_to_cartesian_mpc

sys.path.insert(0, str(Path(__file__).resolve().parent))

RNG_SEED = 20260911
MIN_PAIRS_PER_BIN = 30  # below this, jackknife error bars are unstable:
# delete-one-cluster jackknife on a 1-2-pair bin either destroys the
# only pair or doesn't touch it -- gives a near-zero, meaningless
# error, not a real uncertainty. Same discipline as
# power_analysis_s_dependent.py's own MIN_STRATUM_N=5 for its per-trial
# sign check, applied here to the per-bin jackknife instead.


@dataclass
class PairwiseResult:
    r_centers: np.ndarray
    p_pair: np.ndarray
    p_pair_err: np.ndarray
    n_pairs: np.ndarray


def _pairwise_geometry(pos_mpc: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Real comoving distances r_i, unit LOS vectors r_hat_i, and the
    full pairwise separation matrix s_ij = |pos_i - pos_j|, all needed
    by both c_ij (Eq. 3) and the binning in Eq. 2."""
    r = np.linalg.norm(pos_mpc, axis=1)
    r_hat = pos_mpc / r[:, None]
    diff = pos_mpc[:, None, :] - pos_mpc[None, :, :]
    s_ij = np.linalg.norm(diff, axis=2)
    return r, r_hat, s_ij


def _c_matrix(r: np.ndarray, r_hat: np.ndarray, s_ij: np.ndarray) -> np.ndarray:
    """c_ij, Eq. 3, computed via the r_hat_ij . (r_hat_i+r_hat_j)/2
    definition directly (not the algebraic cos-theta form) -- avoids a
    separate cos(theta) computation and is exactly Eq. 3's own LHS."""
    # r_hat_ij = (pos_i - pos_j) / s_ij ; pos_i = r_i * r_hat_i
    pos = r[:, None] * r_hat
    diff_pos = pos[:, None, :] - pos[None, :, :]
    with np.errstate(invalid="ignore", divide="ignore"):
        r_hat_ij = diff_pos / s_ij[:, :, None]
    mean_r_hat = (r_hat[:, None, :] + r_hat[None, :, :]) / 2.0
    c_ij = np.einsum("ijk,ijk->ij", r_hat_ij, mean_r_hat)
    np.fill_diagonal(c_ij, 0.0)
    return c_ij


def core_pairwise_estimator(
    pos_mpc: np.ndarray,
    q: np.ndarray,
    r_bins: np.ndarray,
    *,
    jackknife: bool = True,
) -> PairwiseResult:
    """Hand et al. 2012 Eqs. 1-3, exact. `q` is the caller's chosen
    line-of-sight-momentum proxy per object (units are the caller's
    choice; the estimator is linear in q so any consistent unit works).
    `pos_mpc` are observer-centered comoving Cartesian positions (Mpc),
    e.g. from `exact_pair_census.radec_z_to_cartesian_mpc`.

    Delete-one-cluster jackknife error bars (standard for this
    statistic, since pairs sharing a cluster are not independent --
    a plain per-pair bootstrap would understate the error).
    """
    n = len(q)
    assert pos_mpc.shape == (n, 3)
    r, r_hat, s_ij = _pairwise_geometry(pos_mpc)
    c_ij = _c_matrix(r, r_hat, s_ij)

    q_diff = q[:, None] - q[None, :]
    iu, ju = np.triu_indices(n, k=1)
    s_pairs = s_ij[iu, ju]
    c_pairs = c_ij[iu, ju]
    qdiff_pairs = q_diff[iu, ju]

    n_bins = len(r_bins) - 1
    bin_idx = np.digitize(s_pairs, r_bins) - 1
    r_centers = 0.5 * (r_bins[:-1] + r_bins[1:])

    def _estimate(mask_i: np.ndarray | None) -> np.ndarray:
        """Eq. 2 per bin. `mask_i`, if given, is a boolean cluster mask
        (jackknife: cluster k excluded -> False)."""
        if mask_i is None:
            pair_ok = np.ones(len(iu), dtype=bool)
        else:
            pair_ok = mask_i[iu] & mask_i[ju]
        out = np.full(n_bins, np.nan)
        for b in range(n_bins):
            sel = pair_ok & (bin_idx == b)
            denom = np.sum(c_pairs[sel] ** 2)
            if denom > 0:
                out[b] = np.sum(qdiff_pairs[sel] * c_pairs[sel]) / denom
        return out

    p_pair = _estimate(None)
    n_pairs = np.array([np.sum(bin_idx == b) for b in range(n_bins)], dtype=int)

    if not jackknife:
        return PairwiseResult(r_centers, p_pair, np.full(n_bins, np.nan), n_pairs)

    jk = np.empty((n, n_bins))
    mask = np.ones(n, dtype=bool)
    for k in range(n):
        mask[k] = False
        jk[k] = _estimate(mask)
        mask[k] = True
    jk_mean = np.nanmean(jk, axis=0)
    p_pair_err = np.sqrt((n - 1) / n * np.nansum((jk - jk_mean) ** 2, axis=0))

    return PairwiseResult(r_centers, p_pair, p_pair_err, n_pairs)


def pairwise_momentum_from_temperature(
    pos_mpc: np.ndarray,
    temperature: np.ndarray,
    r_bins: np.ndarray,
    *,
    n_ksz: float = 1.0,
    jackknife: bool = True,
) -> PairwiseResult:
    """Real-map convenience wrapper: T_kSZ,i = -N_kSZ * q_i (Hand et al.
    2012's own sign convention, stated directly under their Eq. 3) =>
    q_i = -T_i / N_kSZ. Kept separate from `core_pairwise_estimator` so
    the T<->q sign convention is isolated and independently checkable
    (see `_check_temperature_wrapper_sign_convention` in the validation
    block below)."""
    q = -temperature / n_ksz
    return core_pairwise_estimator(pos_mpc, q, r_bins, jackknife=jackknife)


def toy_infall_velocity(
    pos_mpc: np.ndarray, *, g_toy: float = 1.0, softening_mpc: float = 5.0
) -> np.ndarray:
    """POSITIVE-CONTROL SIGNAL GENERATOR, not physics. A softened
    1/r^2-attraction toy force, summed pairwise and applied as a unit
    toy velocity kick -- guarantees every pair of objects has a net
    tendency to move toward each other (coherent infall), independent
    of any real cosmological model. Returns velocity vectors (arbitrary
    toy units, same units as `q` in `core_pairwise_estimator`)."""
    diff = pos_mpc[None, :, :] - pos_mpc[:, None, :]  # pos_j - pos_i
    dist = np.linalg.norm(diff, axis=2)
    dist_soft = np.sqrt(dist**2 + softening_mpc**2)
    with np.errstate(invalid="ignore", divide="ignore"):
        unit = diff / dist[:, :, None]
    np.nan_to_num(unit, copy=False)
    # diagonal (i==j) is already exactly zero: diff[i,i]=0 -> unit[i,i]
    # is nan_to_num'd to 0 above, so force[i,i]=0 by construction, no
    # separate self-force exclusion needed.
    force = g_toy / dist_soft[:, :, None] ** 2 * unit
    v = force.sum(axis=1)
    return v


def _los_component(vectors: np.ndarray, r_hat: np.ndarray) -> np.ndarray:
    return np.einsum("ik,ik->i", vectors, r_hat)


def _load_real_positions(n_max: int, rng: np.random.Generator) -> np.ndarray:
    """Real ACT-DR5 MCMF (RA, Dec, z) -> comoving Mpc, restricted to
    z in [Z_LOW, Z_HIGH] (this experiment's own established working
    range -- reused, not reinvented, see `exact_pair_census.py` and
    every sibling script in this folder), then subsampled to `n_max`
    clusters (jackknife is O(n) reruns of an O(n^2) computation -- the
    full restricted-shell catalog (n~4390) is Phase-2/real-data scope,
    not this Phase-1 validation run)."""
    ra, dec, z = load_catalog()  # RAdeg, DEdeg, z1C -- real column names, see exact_pair_census.py
    ra = np.asarray(ra, dtype=float)
    dec = np.asarray(dec, dtype=float)
    z = np.asarray(z, dtype=float)
    ok = np.isfinite(ra) & np.isfinite(dec) & np.isfinite(z) & (z >= Z_LOW) & (z <= Z_HIGH)
    ra, dec, z = ra[ok], dec[ok], z[ok]
    if len(ra) > n_max:
        idx = rng.choice(len(ra), size=n_max, replace=False)
        ra, dec, z = ra[idx], dec[idx], z[idx]
    return radec_z_to_cartesian_mpc(ra, dec, z)


def main() -> None:
    rng = np.random.default_rng(RNG_SEED)
    n_clusters = 300
    print(f"STEP 1: real ACT-DR5 MCMF positions, subsampled to N={n_clusters}")
    pos = _load_real_positions(n_clusters, rng)
    r, r_hat, s_ij = _pairwise_geometry(pos)
    print(f"  comoving distance range: {r.min():.1f}-{r.max():.1f} Mpc")

    # Quantile bin edges on the REAL pairwise-separation distribution --
    # guarantees every bin gets ~equal (and, for N=300, comfortably
    # >MIN_PAIRS_PER_BIN) pair support, instead of guessing fixed-width
    # edges that may leave the small-separation bins nearly empty (as
    # fixed 20 Mpc-wide edges did on the first run of this script).
    n_bins_target = 7
    iu0, ju0 = np.triu_indices(n_clusters, k=1)
    s_pairs_all = s_ij[iu0, ju0]
    r_bins = np.quantile(s_pairs_all, np.linspace(0.0, 1.0, n_bins_target + 1))
    r_bins[0] = 0.0
    print(f"  separation bins (Mpc, equal-pair-count quantiles): {np.round(r_bins, 1).tolist()}")

    print("\nSTEP 2: NEGATIVE CONTROL -- pure noise, no velocity signal")
    noise_sigma = 1.0
    q_null = rng.normal(0.0, noise_sigma, n_clusters)
    res_null = core_pairwise_estimator(pos, q_null, r_bins)
    z_null = np.full_like(res_null.p_pair, np.nan)
    trusted_null = res_null.n_pairs >= MIN_PAIRS_PER_BIN
    z_null[trusted_null] = res_null.p_pair[trusted_null] / res_null.p_pair_err[trusted_null]
    for rc, p, e, npair, trusted in zip(
        res_null.r_centers,
        res_null.p_pair,
        res_null.p_pair_err,
        res_null.n_pairs,
        trusted_null,
        strict=True,
    ):
        z_score = p / e if e > 0 else np.nan
        flag = "" if trusted else f"  [SKIP: n_pairs<{MIN_PAIRS_PER_BIN}, jackknife unstable]"
        print(
            f"  r={rc:6.1f} Mpc  p_pair={p:+.4f} +/- {e:.4f}  (z={z_score:+.2f}, n_pairs={npair}){flag}"
        )
    n_trusted_null = int(np.sum(trusted_null))
    max_abs_z_null = np.nanmax(np.abs(z_null)) if n_trusted_null > 0 else np.nan
    print(
        f"  max |z| across {n_trusted_null} trusted bins (n_pairs>={MIN_PAIRS_PER_BIN}): "
        f"{max_abs_z_null:.2f}  (expect O(1-3) for a clean null, not >>3 systematically)"
    )

    print("\nSTEP 3: POSITIVE CONTROL -- toy softened pairwise infall")
    v_toy = toy_infall_velocity(pos, g_toy=50.0, softening_mpc=5.0)
    q_infall = _los_component(v_toy, r_hat)
    signal_rms = np.std(q_infall)
    q_infall_noisy = q_infall + rng.normal(0.0, 0.3 * signal_rms, n_clusters)
    res_infall = core_pairwise_estimator(pos, q_infall_noisy, r_bins)
    for rc, p, e, npair in zip(
        res_infall.r_centers,
        res_infall.p_pair,
        res_infall.p_pair_err,
        res_infall.n_pairs,
        strict=True,
    ):
        z_score = p / e if e > 0 else np.nan
        sign = "OK (infall)" if p < 0 else "WRONG SIGN"
        print(
            f"  r={rc:6.1f} Mpc  p_pair={p:+.4f} +/- {e:.4f}  "
            f"(z={z_score:+.2f}, n_pairs={npair})  {sign if npair > 0 else ''}"
        )
    n_negative = np.sum(res_infall.p_pair[res_infall.n_pairs > 0] < 0)
    n_valid_bins = np.sum(res_infall.n_pairs > 0)
    print(f"  bins with p_pair<0 (expected infall sign): {n_negative}/{n_valid_bins}")

    print("\nSTEP 4: sign-convention check, core estimator vs. temperature wrapper")
    n_ksz_test = 2.7
    temperature = -n_ksz_test * q_infall_noisy
    res_from_T = pairwise_momentum_from_temperature(pos, temperature, r_bins, n_ksz=n_ksz_test)
    max_abs_diff = np.nanmax(np.abs(res_from_T.p_pair - res_infall.p_pair))
    print(
        f"  max |p_pair(from T) - p_pair(from q)|: {max_abs_diff:.2e} "
        f"(must be ~0 -- both should recover the identical q_infall_noisy signal "
        f"through the T = -N_ksz*q convention)"
    )
    assert max_abs_diff < 1e-9, "T<->q sign-convention wrapper does not round-trip -- real bug"

    print("\nVERDICT")
    null_ok = n_trusted_null >= 3 and max_abs_z_null < 4.0
    infall_ok = n_negative == n_valid_bins and n_valid_bins >= 3
    print(f"  Negative control clean (>=3 trusted bins, max|z|<4): {null_ok}")
    print(f"  Positive control recovers correct (infall) sign in all valid bins: {infall_ok}")
    print("  Sign-convention round-trip exact: True")
    if null_ok and infall_ok:
        print("  PHASE-1 ESTIMATOR MATH: VALIDATED on synthetic data.")
    else:
        print("  PHASE-1 ESTIMATOR MATH: NOT YET VALIDATED -- see failing check(s) above.")


if __name__ == "__main__":
    main()
