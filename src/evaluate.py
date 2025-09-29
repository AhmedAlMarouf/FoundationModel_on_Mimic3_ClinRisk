import argparse, pandas as pd
from src.metrics import evaluate_all

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--preds", required=True)
    args = ap.parse_args()

    df = pd.read_csv(args.preds)
    m = evaluate_all(df["y"].values, df["proba"].values, df["pred"].values)
    print(m)
