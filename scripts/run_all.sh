#!/usr/bin/env bash
set -e
python scripts/prepare_mimic_demo.py --raw_dir data/raw --out_csv data/interim/mimic_demo.csv
python -m src.train_tabpfn --csv data/interim/mimic_demo.csv --target in_hosp_mortality --continuous_cols "age,first_saps,hemoglobin,platelets,creatinine" --categorical_cols "gender,first_icu_type" --val_size 0.2 --context_size 1024 --seed 42 --out_dir runs/tabpfn_baseline
python -m src.evaluate --preds runs/tabpfn_baseline/preds_val.csv
