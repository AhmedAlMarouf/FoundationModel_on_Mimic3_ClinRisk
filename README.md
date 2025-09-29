# FoundationModel_on_Mimic3_ClinRisk
This project in on Clinical risk prediction on MIMIC-III using **TabPFN** (Prior-Fitted Networks). Predicting in‑hospital mortality from features available within first 24h (toy example for demo). You can switch label to 30‑day mortality or prolonged LOS by editing scripts/prepare_mimic_demo.py.

## File-wise methods
- src/preprocessing.py – imputation (median/mode), scaling, one‑hot for categorical, simple time‑window aggregations.
- src/train_tabpfn.py – loads the pretrained TabPFN model and runs context‑based prediction.
- src/metrics.py – wrappers around scikit‑learn for AUROC/AUPRC/F1/Calibration.

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
