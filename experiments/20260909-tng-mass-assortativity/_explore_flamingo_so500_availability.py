"""EXPLORATORY, not a claim -- checks whether FLAMINGO's real SOAP halo
catalog provides SO/500_crit/TotalMass alongside the already-used
SO/200_crit/TotalMass, for the SAME halos -- the data needed for a
real M500c vs M200c overlap cross-check (Step 8a skeptic's own named
kill-criterion for P230's R500-vs-R200 finding).
"""

import hdfstream

root = hdfstream.open("cosma", "/")
halo_file = root["FLAMINGO"]["L1_m9"]["L1_m9"]["SOAP-HBT"]["halo_properties_0077.hdf5"]

print("Top-level groups under SO/:")
so_group = halo_file["SO"]
for key in so_group.keys():
    print(f"  {key}")

print("\nChecking for 500_crit specifically...")
if "500_crit" in list(so_group.keys()):
    print("SO/500_crit EXISTS. Fields:")
    for key in so_group["500_crit"].keys():
        print(f"  {key}")
else:
    print("SO/500_crit NOT found under this exact path.")
