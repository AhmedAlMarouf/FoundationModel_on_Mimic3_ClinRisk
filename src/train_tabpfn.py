import argparse, numpy as np, pandas as pd
from tabpfn import TabPFNClassifier
from pathlib import Path
from src.dataset import load_csv
from src.preprocessing import Preprocessor
from src.metrics import evaluate_all
from src.config import Config
from src.utils import set_seed

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--target", default="in_hosp_mortality")
    ap.add_argument("--continuous_cols", default="")
    ap.add_argument("--categorical_cols", default="")
    ap.add_argument("--context_size", type=int, default=Config.context_size)
    ap.add_argument("--val_size", type=float, default=Config.val_size)
    ap.add_argument("--seed", type=int, default=Config.seed)
    ap.add_argument("--out_dir", default="runs/tabpfn_baseline")
    args = ap.parse_args()

    set_seed(args.seed)
    out_dir = Path(args.out_dir); out_dir.mkdir(parents=True, exist_ok=True)

    Xtr_raw, Xval_raw, ytr, yval = load_csv(args.csv, args.target, args.val_size, args.seed)

    cont = [c for c in args.continuous_cols.split(',') if c]
    cat  = [c for c in args.categorical_cols.split(',') if c]

    pp = Preprocessor(cont, cat)
    pp.fit(Xtr_raw)
    Xtr = pp.transform(Xtr_raw)
    Xval = pp.transform(Xval_raw)

    clf = TabPFNClassifier(N_ensemble_configurations=16, device="cuda" if False else "cpu")
    clf.fit(Xtr, ytr, overwrite_warning=True, sample_weights=None, context_set_size=args.context_size)

    proba = clf.predict_proba(Xval)[:,1]
    preds = (proba>=0.5).astype(int)
    pd.DataFrame({"y":yval,"proba":proba,"pred":preds}).to_csv(out_dir/"preds_val.csv", index=False)

    metrics = evaluate_all(yval, proba, preds)
    print(metrics)
    pd.Series(metrics).to_json(out_dir/"metrics.json", indent=2)
