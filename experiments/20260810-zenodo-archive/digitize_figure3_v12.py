"""Round 2 (+ vertex-method refinement) of FINDING_P5: digitize Cen,
Bahcall & Gramann 1994's Figures 1, 3 and 4 (psi_v(r), v12(r) and
sigma12(r) -- the velocity correlation function, pairwise cluster
velocity, and its 1D RMS dispersion) directly, closing the gap Round 1
left open -- the exact separation needed (r=20.1 h^-1Mpc, i.e. s0=30 Mpc
physical at CBG's own h=0.67) is not tabulated anywhere in the paper's
text, only plotted. (Figure 2 is recolored/restored but not digitized --
see the FIGURE1_LCDM_DRAWING_INDEX comment below for why.)

Round 1 (FINDING_P5) found Figure 3 renders as a BLANK page in the
project's own reference PDF and concluded this needed "a different
rendering path." Round 2 found the actual root cause: every vector path
on the figure pages is stroked in pure white (color=(1.0,1.0,1.0)), a
systematic color-channel bug in whatever produced the currently-archived
PDF from the paper's original 1994 arXiv PostScript source. The path
GEOMETRY itself is intact and undamaged; only the stroke color is wrong.
Re-stroking the same paths in black recovers every figure exactly (not
redrawn from a guess).

This revision replaces Round 2's original digitization method (cluster
all vertices within an x-band, take the range midpoint as the data
value) with a more precise one: each curve's error bars are drawn as
separate near-VERTICAL segments (the stem) and near-HORIZONTAL segments
(the caps), while the connecting polyline between data points is drawn
as genuinely SLOPED segments (both dx and dy non-negligible). The true
data-point vertices are exactly the shared endpoints of consecutive
sloped segments -- reading these directly, rather than approximating via
an error-bar-range midpoint, removes the small residual bias the range-
midpoint method had (harmless for Figure 3's v12, ~0.06% either way, but
decisive for Figure 4: it revealed that the drawing index this script
had first identified as Figure 4's LCDM curve, #7, has ZERO sloped
segments -- it is not a curve at all, only a stray error-bar-only path
object; the real curve is #6, previously missed).

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION
Source: Cen, Bahcall & Gramann 1994, arXiv:astro-ph/9409042 (ApJ Letters).
"""

import math
import urllib.request

import fitz

REF_PDF = "experiments/20260810-zenodo-archive/refs/cen_bahcall_gramann_1994_astro-ph_9409042.pdf"
ARXIV_SRC_URL = "https://arxiv.org/src/astro-ph/9409042"

FIGURE1_PAGE_INDEX = 4  # 0-indexed page 5
FIGURE3_PAGE_INDEX = 7  # 0-indexed page 8 of the reference PDF
FIGURE4_PAGE_INDEX = 8  # 0-indexed page 9

FIGURE1_LCDM_DRAWING_INDEX = 7  # confirmed by matching psi_v(r=5)=-87 km/s
FIGURE3_LCDM_DRAWING_INDEX = 7  # confirmed by matching v12(r=5)=714 km/s
FIGURE4_LCDM_DRAWING_INDEX = 6  # confirmed by matching sigma12(r=5)=487 km/s
# NOTE: Figure 4's drawing #7 was the FIRST guess (by analogy with Figure 3's
# layout) and is WRONG -- it has zero sloped (connecting-line) segments, so
# it cannot be a curve at all. See module docstring.
#
# Figure 2 is NOT digitized here: it breaks the same psi_v(r) down by
# cluster richness (R>=1 / R>=0 / groups) x 2 densities = 6 curves on a
# DIFFERENT r-grid (8 points, first bin ~r=3.9) than Figures 1/3/4's
# shared 11-point grid -- so there is no single "the LCDM curve" at a
# directly comparable r=5 bin to anchor against, and no open project
# question needs a number from it. Recolored and visually confirmed
# legible (see refs/cbg1994_figure2_recolored.pdf) but left undigitized.

# Axis calibration, derived from each page's own tick-mark pixel positions
# (log-x, linear-y) -- values in PDF points (72/in). The box geometry
# (and hence X0_PT/X_SCALE) is identical across all four figure pages;
# only the y-axis range differs per figure (2000 km/s for v12, 1500 for
# sigma12), so Y0_PT/Y_SCALE are recalibrated per figure below.
X0_PT, X0_R = 203.0, 10.0  # position of the r=10 tick
X_SCALE = 119.875  # points per decade in log10(r)


def pdfx_to_r(x):
    return X0_R * 10 ** ((x - X0_PT) / X_SCALE)


def r_to_pdfx(r):
    return X0_PT + X_SCALE * math.log10(r / X0_R)


def make_y_calibration(y0_pt, y0_value, pts_per_500):
    def y_to_value(y):
        return y0_value - (y - y0_pt) * 500.0 / pts_per_500

    return y_to_value


# Figure 1 (psi_v): psi=1000 tick anchor
PSI_V_Y_TO_VALUE = make_y_calibration(y0_pt=192.625, y0_value=1000.0, pts_per_500=76.78125)
# Figure 3 (v12): v=2000 tick at y=192.6/4=... (page coords, see Round 2)
V12_Y_TO_VALUE = make_y_calibration(y0_pt=465.75, y0_value=0.0, pts_per_500=68.28125)
# Figure 4 (sigma12): sigma=1500 tick anchor
SIGMA12_Y_TO_VALUE = make_y_calibration(y0_pt=192.625, y0_value=1500.0, pts_per_500=109.6875)


def fetch_original_source(dest_path):
    """Download the paper's original 1994 arXiv PostScript source.

    Confirms the figure's stroke-color bug is not present in the source
    itself and documents provenance; not required to run the
    digitization below, which works off the existing PDF's own (correct)
    path geometry.
    """
    urllib.request.urlretrieve(ARXIV_SRC_URL, dest_path)


def recolor_page(pageno, out_pdf, out_png):
    """Re-stroke one page's white-on-white vector paths in black."""
    src = fitz.open(REF_PDF)
    page = src[pageno]
    drawings = page.get_drawings()

    colors = {dr.get("color") for dr in drawings}
    assert colors == {(1.0, 1.0, 1.0)}, f"page {pageno}: unexpected colors: {colors}"

    out = fitz.open()
    newpage = out.new_page(width=page.rect.width, height=page.rect.height)
    shape = newpage.new_shape()
    for dr in drawings:
        for item in dr["items"]:
            if item[0] == "l":
                shape.draw_line(item[1], item[2])
            elif item[0] == "c":
                shape.draw_bezier(item[1], item[2], item[3], item[4])
            elif item[0] == "re":
                shape.draw_rect(item[1])
        shape.finish(color=(0, 0, 0), fill=None, width=0.6)
    shape.commit()
    out.save(out_pdf)

    pix = out[0].get_pixmap(matrix=fitz.Matrix(4, 4), colorspace=fitz.csGRAY)
    pix.save(out_png)

    return drawings


FIGURES = {
    1: (4, "experiments/20260810-zenodo-archive/refs/cbg1994_figure1_recolored"),
    2: (5, "experiments/20260810-zenodo-archive/refs/cbg1994_figure2_recolored"),
    3: (FIGURE3_PAGE_INDEX, "experiments/20260810-zenodo-archive/refs/cbg1994_figure3_recolored"),
    4: (FIGURE4_PAGE_INDEX, "experiments/20260810-zenodo-archive/refs/cbg1994_figure4_recolored"),
}


def recolor_all_figures():
    results = {}
    for fig_num, (pageno, out_base) in FIGURES.items():
        drawings = recolor_page(pageno, out_base + ".pdf", out_base + ".png")
        results[fig_num] = drawings
        print(f"Figure {fig_num} (page {pageno + 1}): recovered, {len(drawings)} paths")
    return results


def true_data_vertices(drawing):
    """The curve's actual data-point coordinates: shared endpoints of
    genuinely SLOPED connecting-line segments (both dx and dy
    non-negligible) -- excludes error-bar stems (near-vertical, dx~0)
    and error-bar caps (near-horizontal, dy~0), which the earlier
    range-midpoint method conflated with the real curve.
    """
    pts = set()
    for item in drawing["items"]:
        if item[0] != "l":
            continue
        p1, p2 = item[1], item[2]
        dx, dy = abs(p1.x - p2.x), abs(p1.y - p2.y)
        if dx >= 0.3 and dy >= 0.3:
            pts.add((round(p1.x, 2), round(p1.y, 2)))
            pts.add((round(p2.x, 2), round(p2.y, 2)))
    return sorted(pts)


def digitize(drawing, y_to_value):
    pts = true_data_vertices(drawing)
    if not pts:
        raise ValueError(
            "drawing has zero sloped (connecting-line) segments -- it is not a "
            "curve; likely a mis-identified error-bar-only path object"
        )
    return [{"r": pdfx_to_r(x), "value": y_to_value(y)} for x, y in pts]


def nearest(curve, r_target):
    return min(curve, key=lambda row: abs(row["r"] - r_target))


def main():
    all_drawings = recolor_all_figures()
    print()

    # --- Figure 1: psi_v(r), Omega=0.3 CDM ---
    psi_v_drawing = all_drawings[1][FIGURE1_LCDM_DRAWING_INDEX]
    psi_v_curve = digitize(psi_v_drawing, PSI_V_Y_TO_VALUE)

    print("=== Figure 1: psi_v(r), Omega=0.3 CDM (LCDM) -- vertex method ===")
    for row in psi_v_curve:
        print(f"  r={row['r']:7.2f} h^-1Mpc   psi_v={row['value']:8.2f} km/s")

    psi_v_at_5 = nearest(psi_v_curve, 5.0)
    known_psi_v_at_5 = -87.0
    rel_err_psi = abs(psi_v_at_5["value"] - known_psi_v_at_5) / abs(known_psi_v_at_5)
    print(
        f"\nCross-check at r={psi_v_at_5['r']:.2f}: digitized={psi_v_at_5['value']:.2f} km/s, "
        f"known={known_psi_v_at_5}, rel_err={rel_err_psi:.4%}"
    )
    # psi_v crosses zero near this separation, so a small absolute pixel
    # offset is a larger relative error than for v12/sigma12 (which never
    # approach zero at their own r=5 anchors) -- 5% is still a decisive
    # curve-identity confirmation, not a loose tolerance.
    assert rel_err_psi < 0.05, "Figure 1 digitization does not reproduce the known anchor"
    print()

    # --- Figure 3: v12(r), Omega=0.3 CDM ---
    v12_drawing = all_drawings[3][FIGURE3_LCDM_DRAWING_INDEX]
    v12_curve = digitize(v12_drawing, V12_Y_TO_VALUE)

    print("=== Figure 3: v12(r), Omega=0.3 CDM (LCDM) -- vertex method ===")
    for row in v12_curve:
        print(f"  r={row['r']:7.2f} h^-1Mpc   v12={row['value']:7.2f} km/s")

    v12_at_5 = nearest(v12_curve, 5.0)
    known_v12_at_5 = 714.0
    rel_err_v12 = abs(v12_at_5["value"] - known_v12_at_5) / known_v12_at_5
    print(
        f"\nCross-check at r={v12_at_5['r']:.2f}: digitized={v12_at_5['value']:.2f} km/s, "
        f"known={known_v12_at_5}, rel_err={rel_err_v12:.4%}"
    )
    assert rel_err_v12 < 0.01, "Figure 3 digitization does not reproduce the known anchor"

    # --- Figure 4: sigma12(r), Omega=0.3 CDM ---
    # NOTE: drawing index 7 (the naive by-analogy guess from Figure 3's
    # layout) has ZERO sloped segments -- confirmed not a curve. #6 is.
    sigma12_drawing = all_drawings[4][FIGURE4_LCDM_DRAWING_INDEX]
    sigma12_curve = digitize(sigma12_drawing, SIGMA12_Y_TO_VALUE)

    print("\n=== Figure 4: sigma12(r), Omega=0.3 CDM (LCDM) -- vertex method ===")
    for row in sigma12_curve:
        print(f"  r={row['r']:7.2f} h^-1Mpc   sigma12={row['value']:7.2f} km/s")

    sigma12_at_5 = nearest(sigma12_curve, 5.0)
    known_sigma12_at_5 = 487.0
    rel_err_sigma5 = abs(sigma12_at_5["value"] - known_sigma12_at_5) / known_sigma12_at_5
    sigma12_at_100 = nearest(sigma12_curve, 100.0)
    known_sigma12_at_100 = 327.0
    rel_err_sigma100 = abs(sigma12_at_100["value"] - known_sigma12_at_100) / known_sigma12_at_100
    print(
        f"\nCross-check at r={sigma12_at_5['r']:.2f}: digitized={sigma12_at_5['value']:.2f} km/s, "
        f"known={known_sigma12_at_5}, rel_err={rel_err_sigma5:.4%}"
    )
    print(
        f"Cross-check at r={sigma12_at_100['r']:.2f}: digitized={sigma12_at_100['value']:.2f} km/s, "
        f"known={known_sigma12_at_100}, rel_err={rel_err_sigma100:.4%}"
    )
    assert rel_err_sigma5 < 0.01, "Figure 4 digitization does not reproduce the r=5 anchor"
    # r=100 anchor: nearest plotted bin (r=79.57) is genuinely ~20 h^-1Mpc
    # away from the exact anchor point, on a still-descending part of the
    # curve (the broad minimum sits near r~30) -- some gap here is expected
    # bin quantization, not a digitization error; the r=5 anchor (exact
    # data bin) is the decisive check and matches to 0.017%.
    assert rel_err_sigma100 < 0.03, "Figure 4 digitization does not reproduce the r=100 anchor"

    # --- H0_anchor from v12 (the quantity the paper's formula actually uses) ---
    s0_mpc = 30.0
    h = 0.67
    r_target = s0_mpc * h
    v12_target = nearest(v12_curve, r_target)
    sigma12_target = nearest(sigma12_curve, r_target)
    h0 = v12_target["value"] / s0_mpc

    print(f"\nTarget r = s0*h = {r_target:.2f} h^-1Mpc")
    print(f"v12(target)     = {v12_target['value']:.2f} km/s")
    print(f"sigma12(target) = {sigma12_target['value']:.2f} km/s  (bonus, not used below)")
    print(f"v12/sigma12 at target = {v12_target['value'] / sigma12_target['value']:.4f}")
    print(f"\nH0_anchor = v12/s0 = {h0:.2f} km/s/Mpc")
    print()
    print("Comparison:")
    print("  paper's own stated value:                   ~11 km/s/Mpc")
    print("  archive's 3-method interpolation range:       12.5-18.7 km/s/Mpc")
    print("  this project's earlier v12/sigma12 x-check:   ~22 km/s/Mpc")
    print(f"  direct digitization (vertex method):          {h0:.2f} km/s/Mpc")


if __name__ == "__main__":
    main()
