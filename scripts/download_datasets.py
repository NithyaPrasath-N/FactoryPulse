"""
Download public datasets for FactoryPulse.
C-MAPSS (NASA), IMS Bearings (NASA/UC Irvine), AI4I 2020 (UCI).
"""

import os
import urllib.request
import zipfile

DATA_DIR = "data/raw"

DATASETS = {
    "cmapss": {
        "url": "https://data.nasa.gov/download/m4g5-jtyh/application%2Fzip",
        "dest": f"{DATA_DIR}/cmapss",
        "desc": "C-MAPSS Turbofan Degradation (NASA)",
    },
    "ims_bearings": {
        "url": "https://data.nasa.gov/download/2jvr-fw99/application%2Fzip",
        "dest": f"{DATA_DIR}/ims_bearings",
        "desc": "IMS Bearing Dataset (NASA/UC Irvine)",
    },
    "ai4i_2020": {
        "url": "https://archive.ics.uci.edu/static/public/601/ai4i+2020+predictive+maintenance+dataset.zip",
        "dest": f"{DATA_DIR}/ai4i_2020",
        "desc": "AI4I 2020 Predictive Maintenance (UCI)",
    },
}


def download_dataset(name: str, info: dict):
    """Download and extract a dataset."""
    os.makedirs(info["dest"], exist_ok=True)
    zip_path = f"{info['dest']}/{name}.zip"
    print(f"Downloading {info['desc']}...")

    try:
        urllib.request.urlretrieve(info["url"], zip_path)
        with zipfile.ZipFile(zip_path, "r") as z:
            z.extractall(info["dest"])
        os.remove(zip_path)
        print(f" ✅ {name} ready at {info['dest']}")
    except Exception as e:
        print(f" ❌ FAIL {name}: {e}")
        print(f" -> Download manually from {info['url']}")


if __name__ == "__main__":
    for name, info in DATASETS.items():
        download_dataset(name, info)

    print("\nDone. Run 'dvc add data/raw/*' to track with DVC.")
