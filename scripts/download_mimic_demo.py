import argparse
import os
from pathlib import Path
import urllib.request

# Downloads the publicly-available MIMIC-III Demo CSVs from PhysioNet into --out_dir.
# Source: https://physionet.org/content/mimiciii-demo/1.4/
FILES = [
    "ADMISSIONS.csv.gz",
    "PATIENTS.csv.gz",
    "ICUSTAYS.csv.gz",
    "D_ITEMS.csv.gz",
    "D_LABITEMS.csv.gz",
    "LABEVENTS.csv.gz",
    "CHARTEVENTS.csv.gz",
    "DIAGNOSES_ICD.csv.gz",
    "PROCEDURES_ICD.csv.gz",
    "DRGCODES.csv.gz",
    "PRESCRIPTIONS.csv.gz",
    "INPUTEVENTS_MV.csv.gz",
    "OUTPUTEVENTS.csv.gz",
    "NOTE_EVENTS.csv.gz"
]

BASE = "https://physionet.org/files/mimiciii-demo/1.4/"

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out_dir", required=True, help="Directory to save the demo CSVs")
    args = ap.parse_args()

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    for fname in FILES:
        url = BASE + fname
        dst = out / fname
        print(f"Downloading {url} -> {dst}")
        urllib.request.urlretrieve(url, dst)
    print("Done. Gzipped CSVs saved in", out)
