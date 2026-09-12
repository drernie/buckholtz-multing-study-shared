"""EXPLORATORY, read-only -- check the real TNG API for what independent
simulation volumes are actually available before claiming any number
from memory. Not a claim, a live lookup.
"""

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
    resp = session.get("https://www.tng-project.org/api/", timeout=30)
    resp.raise_for_status()
    data = resp.json()
    print("Top-level API keys:", list(data.keys()))
    sims = data.get("simulations", data)
    print(f"\n{sims}")


if __name__ == "__main__":
    main()
