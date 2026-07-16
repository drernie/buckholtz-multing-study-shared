"""
Parse Mahdavi et al. 2013 (arXiv:1210.3689) Tables 1 and 2 into a merged CSV.
Source: pdfplumber text extraction directly from the downloaded PDF, cross-checked
against the rendered page images (Read tool page-image view) for the first 4 rows.
NOT_VALIDATION - NOT_REFUTATION - OUR_RECONSTRUCTION
"""

import csv
import re
import statistics


def parse_pm(token):
    """'1.16±0.02' -> (1.16, 0.02). Handles '<3', '...', asymmetric not present here."""
    token = token.strip()
    if token in ("···", "..."):
        return (None, None)
    if token.startswith("<"):
        return (None, None)  # upper limit only, no point estimate
    if "±" in token:
        val, err = token.split("±")
        return (float(val), float(err))
    return (float(token), None)


# ---- Table 1: Cluster RA DEC z ChandraObsID Exposure XMM-ObsID Exposure L_X T_X ----
t1_rows = {}
with open("table1_raw.txt", encoding="utf-8") as f:
    lines = f.readlines()
for line in lines[6:56]:  # data rows only (0-indexed: lines[6] = 7th line = 3C295)
    line = line.rstrip("\n")
    parts = line.split()
    name = parts[0]
    z = float(parts[3])
    # last two whitespace-separated tokens are L_X and T_X (both "x±y" format)
    lx_tok, tx_tok = parts[-2], parts[-1]
    lx, lx_err = parse_pm(lx_tok)
    tx, tx_err = parse_pm(tx_tok)
    t1_rows[name] = {
        "z": z,
        "L_X_1e45ergs": lx,
        "L_X_err": lx_err,
        "T_X_keV": tx,
        "T_X_err": tx_err,
    }

# ---- Table 2: Cluster r500WL M_WL M_Gas M_hydro K0 D_BCG w_X P3/P0 ----
t2_rows = {}
with open("table2_raw.txt", encoding="utf-8") as f:
    lines = f.readlines()
for line in lines[15:65]:  # data rows (0-indexed: lines[15] = 16th line = 3C295)
    line = line.rstrip("\n")
    # K0 has a space before its error ("12.8± 2.4") -- normalize first
    line_norm = re.sub(r"±\s+", "±", line)
    parts = line_norm.split()
    name = parts[0]
    r500, _ = parse_pm(parts[1])
    mwl, mwl_err = parse_pm(parts[2])
    mgas, mgas_err = parse_pm(parts[3])
    mhydro, mhydro_err = parse_pm(parts[4])
    k0, k0_err = parse_pm(parts[5])
    dbcg_tok = parts[6]
    dbcg = None if dbcg_tok.startswith("<") else float(dbcg_tok)
    wx, wx_err = (None, None)
    p3p0, p3p0_err = (None, None)
    if len(parts) >= 8:
        wx, wx_err = parse_pm(parts[7])
    if len(parts) >= 9:
        p3p0, p3p0_err = parse_pm(parts[8])
    t2_rows[name] = {
        "r500_WL_Mpc": r500,
        "M_WL_1e14Msun": mwl,
        "M_WL_err": mwl_err,
        "M_Gas_1e14Msun": mgas,
        "M_Gas_err": mgas_err,
        "M_hydro_1e14Msun": mhydro,
        "M_hydro_err": mhydro_err,
        "K0_keVcm2": k0,
        "K0_err": k0_err,
        "D_BCG_kpc": dbcg,
        "wX": wx,
        "wX_err": wx_err,
        "P3P0": p3p0,
        "P3P0_err": p3p0_err,
    }

names_t1 = set(t1_rows.keys())
names_t2 = set(t2_rows.keys())
print("Table 1 rows:", len(names_t1))
print("Table 2 rows:", len(names_t2))
print("In T1 not T2:", names_t1 - names_t2)
print("In T2 not T1:", names_t2 - names_t1)

# ---- Merge + derived quantities ----
out_rows = []
for name in sorted(
    names_t1 & names_t2, key=lambda n: list(t1_rows.keys()).index(n) if n in t1_rows else 0
):
    r1, r2 = t1_rows[name], t2_rows[name]
    delta_M = None
    if r2["M_WL_1e14Msun"] is not None and r2["M_hydro_1e14Msun"] is not None:
        delta_M = r2["M_WL_1e14Msun"] - r2["M_hydro_1e14Msun"]
    e_icm = None
    if r2["M_Gas_1e14Msun"] is not None and r1["T_X_keV"] is not None:
        e_icm = r2["M_Gas_1e14Msun"] * r1["T_X_keV"]  # proxy, 1e14 Msun*keV units
    row = {
        "cluster_name": name,
        **r1,
        **r2,
        "delta_M_1e14Msun": delta_M,
        "E_ICM_proxy_MgasTx": e_icm,
    }
    out_rows.append(row)

# preserve original Table 1 order
ordered_names = list(t1_rows.keys())
out_rows.sort(key=lambda r: ordered_names.index(r["cluster_name"]))

fieldnames = list(out_rows[0].keys())
with open("cccp_mahdavi2013_merged.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(out_rows)

print(f"\nWrote {len(out_rows)} merged rows to cccp_mahdavi2013_merged.csv")

# ---- Sanity checks against paper's own stated aggregate results ----
ratios = []
for r in out_rows:
    if r["M_WL_1e14Msun"] and r["M_hydro_1e14Msun"]:
        ratios.append(r["M_hydro_1e14Msun"] / r["M_WL_1e14Msun"])
mean_ratio = statistics.mean(ratios)
print(
    f"\nSanity check: mean(M_hydro/M_WL) = {mean_ratio:.3f} (paper abstract claims "
    f"~10% underestimate on average -> expect ~0.90)"
)
