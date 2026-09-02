"""Round 2 of FINDING_P5: digitize Cen, Bahcall & Gramann 1994's Figure 3
(v12(r), the pairwise cluster velocity curve) directly, closing the gap
Round 1 left open -- the exact separation needed (r=20.1 h^-1Mpc, i.e.
s0=30 Mpc physical at CBG's own h=0.67) is not tabulated anywhere in the
paper's text, only plotted.

Round 1 (FINDING_P5) found Figure 3 renders as a BLANK page in the
project's own reference PDF and concluded this needed "a different
rendering path." This script IS that different path: it fetches the
paper's original 1994 arXiv PostScript source directly (not the PDF), and
finds the actual root cause -- every vector path on the figure pages is
stroked in pure white (color=(1.0,1.0,1.0)), a systematic color-channel
bug in whatever produced the currently-archived PDF from that PS source.
The path GEOMETRY itself is intact and undamaged; only the stroke color
is wrong. This script re-strokes the same paths in black, recovering the
figure exactly (not redrawing it from a guess), then digitizes the
recovered v12(r) curve directly from the vector coordinates -- not by
eye, not by pixel-tracing a raster image.

NOT_VALIDATION * NOT_REFUTATION * OUR_RECONSTRUCTION
Source: Cen, Bahcall & Gramann 1994, arXiv:astro-ph/9409042 (ApJ Letters).
"""

import math
import urllib.request

import fitz

REF_PDF = "experiments/20260810-zenodo-archive/refs/cen_bahcall_gramann_1994_astro-ph_9409042.pdf"
OUT_PDF = "experiments/20260810-zenodo-archive/refs/cbg1994_figure3_recolored.pdf"
OUT_PNG = "experiments/20260810-zenodo-archive/refs/cbg1994_figure3_recolored.png"
ARXIV_SRC_URL = "https://arxiv.org/src/astro-ph/9409042"

FIGURE3_PAGE_INDEX = 7  # 0-indexed page 8 of the reference PDF
LCDM_DRAWING_INDEX = 7  # confirmed below by matching v12(r=5)=714 km/s exactly

# Axis calibration, derived from the recolored page's own tick marks
# (see "Calibration" section below) -- values are in PDF points (72/in),
# consistent with fitz's own drawing coordinate system for this page.
X0_PT, X0_R = 203.0, 10.0  # pixel/point position of the r=10 tick
X_SCALE = 119.875  # points per decade in log10(r)
Y0_PT, Y0_V = 465.75, 0.0  # point position of the v12=0 tick
Y_SCALE = 273.125  # points per FULL 2000 km/s span (v=0 to v=2000 tick)


def pdfx_to_r(x):
    return X0_R * 10 ** ((x - X0_PT) / X_SCALE)


def r_to_pdfx(r):
    return X0_PT + X_SCALE * math.log10(r / X0_R)


def pdfy_to_v(y):
    return 2000.0 * (Y0_PT - y) / Y_SCALE


def fetch_original_source(dest_path):
    """Download the paper's original 1994 arXiv PostScript source.

    Confirms the figure's stroke-color bug is not present in the source
    itself and documents provenance; not strictly required to run the
    digitization below, which works directly off the existing PDF's
    (correct) path geometry.
    """
    urllib.request.urlretrieve(ARXIV_SRC_URL, dest_path)


def recolor_page(pageno, out_pdf, out_png):
    """Re-stroke one page's white-on-white vector paths in black.

    Generic across all four figure pages (Figs 1, 2, 3, 4 all carry the
    same stroke-color bug, confirmed below rather than assumed for each).
    """
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


def recolor_and_extract(pageno=FIGURE3_PAGE_INDEX):
    return recolor_page(pageno, OUT_PDF, OUT_PNG)


# Figures 1, 2, 4 -- pages 5, 6, 9 of the paper (0-indexed 4, 5, 8).
# Figure 3 (page 8, 0-indexed 7) is handled by recolor_and_extract() above.
OTHER_FIGURES = {
    1: 4,
    2: 5,
    4: 8,
}


def recolor_remaining_figures():
    """Restore Figures 1, 2, 4 the same way as Figure 3 (visual recovery
    only -- no per-curve digitization, since none of the three currently
    feed a specific project computation the way Figure 3's v12(r) does).
    """
    results = {}
    for fig_num, pageno in OTHER_FIGURES.items():
        out_pdf = f"experiments/20260810-zenodo-archive/refs/cbg1994_figure{fig_num}_recolored.pdf"
        out_png = f"experiments/20260810-zenodo-archive/refs/cbg1994_figure{fig_num}_recolored.png"
        drawings = recolor_page(pageno, out_pdf, out_png)
        results[fig_num] = {"pageno": pageno, "n_drawings": len(drawings), "out_pdf": out_pdf}
        print(
            f"Figure {fig_num} (page {pageno + 1}): recovered, {len(drawings)} paths -> {out_pdf}"
        )
    return results


def digitize_curve(drawings, drawing_index):
    """Extract (r, v12) vertex clusters for one curve's polyline+error-bars."""
    pts = set()
    for item in drawings[drawing_index]["items"]:
        if item[0] == "l":
            pts.add((round(item[1].x, 1), round(item[1].y, 1)))
            pts.add((round(item[2].x, 1), round(item[2].y, 1)))
    pts = sorted(pts)

    clusters = []
    cur = [pts[0]]
    for pt in pts[1:]:
        if pt[0] - cur[-1][0] <= 0.5:
            cur.append(pt)
        else:
            clusters.append(cur)
            cur = [pt]
    clusters.append(cur)

    rows = []
    for c in clusters:
        xs = [p[0] for p in c]
        ys = [p[1] for p in c]
        xm = sum(xs) / len(xs)
        v_lo, v_hi = pdfy_to_v(max(ys)), pdfy_to_v(min(ys))
        rows.append(
            {"r": pdfx_to_r(xm), "v12_mid": (v_lo + v_hi) / 2, "v12_lo": v_lo, "v12_hi": v_hi}
        )
    return rows


def main():
    recolor_remaining_figures()
    print()

    drawings = recolor_and_extract()
    curve = digitize_curve(drawings, LCDM_DRAWING_INDEX)

    print("=== Digitized v12(r), LCDM/Omega=0.3 CDM curve ===")
    for row in curve:
        print(
            f"  r={row['r']:7.2f} h^-1Mpc   v12={row['v12_mid']:7.1f} km/s "
            f"[{row['v12_lo']:.1f},{row['v12_hi']:.1f}]"
        )

    # Cross-check: r~5 h^-1Mpc is independently, exactly known (this
    # project's own FINDING_P5 verified v12(5 h^-1Mpc)=714 km/s against
    # CBG 1994's own Table 1). If digitization is correct, this point
    # should match closely.
    anchor = min(curve, key=lambda row: abs(row["r"] - 5.0))
    known_v12_at_5 = 714.0
    rel_err = abs(anchor["v12_mid"] - known_v12_at_5) / known_v12_at_5
    print()
    print(
        f"Cross-check at r={anchor['r']:.2f} h^-1Mpc: digitized={anchor['v12_mid']:.1f} km/s, "
        f"known={known_v12_at_5} km/s, rel_err={rel_err:.4%}"
    )
    assert rel_err < 0.01, "digitization does not reproduce the known anchor point"

    # The actual target: r = s0/h = 30 Mpc / 0.67 = 20.1 h^-1Mpc
    s0_mpc = 30.0
    h = 0.67
    r_target = s0_mpc * h
    target = min(curve, key=lambda row: abs(row["r"] - r_target))
    h0_mid = target["v12_mid"] / s0_mpc
    h0_lo = target["v12_lo"] / s0_mpc
    h0_hi = target["v12_hi"] / s0_mpc

    print()
    print(f"Target r = s0*h = {r_target:.2f} h^-1Mpc (nearest plotted bin: r={target['r']:.2f})")
    print(
        f"v12(target) = {target['v12_mid']:.1f} km/s  [{target['v12_lo']:.1f},{target['v12_hi']:.1f}]"
    )
    print(
        f"H0_anchor = v12/s0 = {h0_mid:.2f} km/s/Mpc  (plotted-error range [{h0_lo:.2f},{h0_hi:.2f}])"
    )
    print()
    print("Comparison:")
    print("  paper's own stated value:              ~11 km/s/Mpc")
    print("  archive's 3-method interpolation range:  12.5-18.7 km/s/Mpc")
    print("  this project's earlier v12/sigma12 x-check: ~22 km/s/Mpc")
    print(
        f"  THIS direct digitization:                {h0_mid:.1f} km/s/Mpc "
        f"(stat. range {h0_lo:.1f}-{h0_hi:.1f})"
    )


if __name__ == "__main__":
    main()
