"""EXPLORATORY, read-only -- test hdfstream connectivity to the
FLAMINGO data service and list what's available, before downloading
any real data. Not a claim.
"""

import hdfstream


def main() -> None:
    root = hdfstream.open("cosma", "/")
    print("Connected. Root contents:")
    print(list(root.keys()))

    flamingo_dir = root["FLAMINGO"]
    print("\nFLAMINGO/ contents:")
    print(list(flamingo_dir.keys()))

    l1m9 = flamingo_dir["L1_m9"]
    print("\nFLAMINGO/L1_m9/ contents:")
    print(list(l1m9.keys()))

    base_run = l1m9["L1_m9"]
    print("\nFLAMINGO/L1_m9/L1_m9/ contents:")
    print(list(base_run.keys()))

    soap = base_run["SOAP-HBT"]
    halo_files = sorted(k for k in soap.keys() if k.startswith("halo_properties_"))
    print(f"\nSOAP-HBT/ halo_properties files: {len(halo_files)}")
    print(f"first: {halo_files[0]}, last: {halo_files[-1]}")

    last_file = soap[halo_files[-1]]
    print(f"\n{halo_files[-1]} top-level groups:")
    print(list(last_file.keys()))
    print("\nHeader attrs:")
    for k, v in last_file["Header"].attrs.items():
        print(f"  {k}: {v}")

    print("\nCosmology attrs:")
    for k, v in last_file["Cosmology"].attrs.items():
        print(f"  {k}: {v}")

    mass_ds = last_file["SO"]["200_crit"]["TotalMass"]
    pos_ds = last_file["InputHalos"]["FOF"]["Centres"]
    print(f"\nSO/200_crit/TotalMass: shape={mass_ds.shape}, dtype={mass_ds.dtype}")
    print(f"InputHalos/FOF/Centres: shape={pos_ds.shape}, dtype={pos_ds.dtype}")
    for k, v in mass_ds.attrs.items():
        print(f"  attr {k}: {v}")


if __name__ == "__main__":
    main()
