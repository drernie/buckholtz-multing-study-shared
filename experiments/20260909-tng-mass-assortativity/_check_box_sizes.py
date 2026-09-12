"""EXPLORATORY, read-only -- check real BoxSize/cosmology metadata for
the candidate independent volumes, not from memory."""

from pathlib import Path

import requests

API_KEY_FILE = Path.home() / ".secrets" / "tng_api_key.env"


def get_api_key() -> str:
    text = API_KEY_FILE.read_text()
    for line in text.splitlines():
        if line.startswith("TNG_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise RuntimeError("TNG_API_KEY not found")


def main() -> None:
    session = requests.Session()
    session.headers.update({"api-key": get_api_key()})
    for sim in ["TNG300-1", "TNG100-1", "TNG50-1", "Illustris-1"]:
        resp = session.get(f"https://www.tng-project.org/api/{sim}/", timeout=30)
        resp.raise_for_status()
        d = resp.json()
        keys_of_interest = {
            k: d[k]
            for k in [
                "boxsize",
                "hubble",
                "omega_0",
                "omega_L",
                "num_dm",
                "mass_dm",
            ]
            if k in d
        }
        print(f"{sim}: {keys_of_interest}")


if __name__ == "__main__":
    main()
