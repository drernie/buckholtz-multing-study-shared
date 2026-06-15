"""Plot helpers for double-inversion diagnostic."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from src.cluster_schedule import ClusterRow
from src.double_inversion_grid import GridSearchSummary
from src.double_inversion_isoline import isoline_residual, physical_box_ok


def _output_dir(base: Path | None = None) -> Path:
    d = base or Path(__file__).resolve().parent.parent / "audit" / "output" / "double_inversion"
    d.mkdir(parents=True, exist_ok=True)
    return d


def plot_isoline_for_z(
    row: ClusterRow,
    H_target: float,
    phi_anchor: float,
    H_anchor: float,
    beta_d: float,
    beta_q: float,
    out_path: Path,
    n: int = 80,
) -> None:
    d_min = max(2.01 * row.r_A, 0.5)
    d_max = max(row.D * 3, row.D_hi or row.D * 2)
    k_min = (row.k_A_lo or row.k_A * 0.01) * 0.1
    k_max = (row.k_A_hi or row.k_A) * 10
    D = np.logspace(np.log10(d_min), np.log10(d_max), n)
    K = np.logspace(np.log10(k_min), np.log10(k_max), n)
    DD, KK = np.meshgrid(D, K)
    Z = np.vectorize(
        lambda d, k: isoline_residual(
            d, k, row.m_A, row.r_A, beta_d, beta_q, phi_anchor, H_anchor, H_target
        )
    )(DD, KK)

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.contour(DD, KK, Z, levels=[0], colors="C0", linewidths=2)
    ax.contourf(DD, KK, Z, levels=20, alpha=0.35, cmap="coolwarm")
    phys = np.vectorize(
        lambda d, k: physical_box_ok(
            d, k, row.r_A, row.k_A_lo, row.k_A_hi, row.D_lo, row.D_hi
        )
    )(DD, KK)
    ax.contour(DD, KK, phys.astype(float), levels=[0.5], colors="green", linestyles="--")
    ax.scatter([row.D], [row.k_A], c="red", s=60, label="CSV schedule", zorder=5)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("D [Mpc]")
    ax.set_ylabel("k_A [M_sun]")
    ax.set_title(f"Isoline H={H_target:.0f} at z={row.z:.2f}  [NOT_VALIDATION]")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    plt.close(fig)


def plot_grid_heatmap(summary: GridSearchSummary, out_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(
        summary.mae_grid,
        origin="lower",
        aspect="auto",
        extent=[
            summary.gamma_values[0],
            summary.gamma_values[-1],
            summary.alpha_values[0],
            summary.alpha_values[-1],
        ],
        cmap="viridis",
    )
    ax.contour(
        summary.gamma_values,
        summary.alpha_values,
        summary.physical_mask.astype(float),
        levels=[0.5],
        colors="white",
        linestyles="--",
    )
    if summary.best_physical:
        ax.scatter(
            [summary.best_physical.gamma],
            [summary.best_physical.alpha],
            c="lime",
            s=80,
            marker="*",
            label="best physical",
        )
    if summary.best_unconstrained:
        ax.scatter(
            [summary.best_unconstrained.gamma],
            [summary.best_unconstrained.alpha],
            c="red",
            s=60,
            marker="x",
            label="best unconstrained",
        )
    plt.colorbar(im, ax=ax, label="MAE [km/s/Mpc]")
    ax.set_xlabel("gamma  (D ~ (1+z)^-gamma)")
    ax.set_ylabel("alpha  (k_A ~ (1+z)^-alpha)")
    ax.set_title("Double inversion grid  [VERIFIED_DIAGNOSTIC]")
    ax.legend(loc="upper right")
    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    plt.close(fig)


def plot_h_comparison(
    z_vals: list[float],
    H_obs: list[float],
    H_csv: list[float],
    H_best_unc: list[float] | None,
    H_best_phys: list[float] | None,
    out_path: Path,
) -> None:
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.errorbar(z_vals, H_obs, fmt="ko", label="H_obs (target)")
    ax.plot(z_vals, H_csv, "b--", label="CSV bridge")
    if H_best_unc:
        ax.plot(z_vals, H_best_unc, "r:", label="best unconstrained")
    if H_best_phys:
        ax.plot(z_vals, H_best_phys, "g-", label="best physical")
    ax.set_xlabel("z")
    ax.set_ylabel("H [km/s/Mpc]")
    ax.set_title("H(z) comparison  [NOT_VALIDATION]")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    plt.close(fig)


def generate_all_plots(
    rows: list[ClusterRow],
    H_obs: list[float],
    summary: GridSearchSummary,
    phi_anchor: float,
    H_anchor: float,
    beta_d: float = 4.5,
    beta_q: float = 18.0,
    output_dir: Path | None = None,
) -> list[Path]:
    out = _output_dir(output_dir)
    paths: list[Path] = []
    rep_z = [0.0, 1.0, 8.5]
    for z_target in rep_z:
        row = next(r for r in rows if abs(r.z - z_target) < 0.01)
        i = rows.index(row)
        p = out / f"isoline_z{z_target:.1f}.png"
        plot_isoline_for_z(row, H_obs[i], phi_anchor, H_anchor, beta_d, beta_q, p)
        paths.append(p)
    heat = out / "grid_heatmap_mae.png"
    plot_grid_heatmap(summary, heat)
    paths.append(heat)
    return paths
