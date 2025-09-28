# FoundationModel_on_Mimic3_ClinRisk
This project in on Clinical risk prediction on MIMIC-III using **TabPFN** (Prior-Fitted Networks).

## ✨ Highlights
- Uses **MIMIC‑III Demo** from PhysioNet (https://physionet.org/content/mimiciii-demo/1.4/)
- End‑to‑end pipeline: preprocessing → TabPFN inference → evaluation (AUROC/AUPRC/F1/Calibration)
- Reproducible with `environment.yml` (Conda) or `requirements.txt` (pip)


## ⚠️ Data Access
- **MIMIC‑III** requires PhysioNet credential and data use agreement.
- However, this project uses the **MIMIC‑III Demo** subset (public) to run this project end‑to‑end.


## 📦 Setup
```bash
conda env create -f environment.yml
conda activate tabpfn_mimic3
# or: python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
