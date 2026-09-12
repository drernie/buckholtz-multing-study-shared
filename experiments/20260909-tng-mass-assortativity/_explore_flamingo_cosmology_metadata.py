"""Exploratory check: where does the FLAMINGO halo_properties file store
its own cosmology (h) so unit conversion for the 2PCF comparison is
[VERIFIED] rather than assumed. Not part of the CLAIM's decisive run.
"""

import hdfstream

root = hdfstream.open("cosma", "/")
halo_file = root["FLAMINGO"]["L1_m9"]["L1_m9"]["SOAP-HBT"]["halo_properties_0077.hdf5"]

print("Top-level keys:", list(halo_file.keys()))

for key in halo_file.keys():
    try:
        attrs = dict(halo_file[key].attrs)
        if attrs:
            print(f"\n[{key}] attrs:")
            for k, v in attrs.items():
                print(f"  {k} = {v}")
    except Exception as e:
        print(f"  ({key}: could not read attrs: {e})")

print("\nFile-level (root of halo_file) attrs:")
try:
    for k, v in dict(halo_file.attrs).items():
        print(f"  {k} = {v}")
except Exception as e:
    print(f"  (could not read: {e})")

for candidate in ["Cosmology", "cosmology", "Header", "Parameters", "Units"]:
    if candidate in halo_file:
        print(f"\n[{candidate}] sub-keys:", list(halo_file[candidate].keys()))
        try:
            for k, v in dict(halo_file[candidate].attrs).items():
                print(f"  attr {k} = {v}")
        except Exception:
            pass
        for sub in halo_file[candidate].keys():
            try:
                val = halo_file[candidate][sub]
                print(f"  {sub}: attrs={dict(val.attrs)}")
            except Exception as e:
                print(f"  {sub}: (error {e})")
