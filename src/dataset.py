import pandas as pd
from sklearn.model_selection import train_test_split

def load_csv(csv_path, target, val_size=0.2, seed=42):
    df = pd.read_csv(csv_path)
    y = df[target].astype(int).values
    X = df.drop(columns=[target])
    Xtr, Xval, ytr, yval = train_test_split(X, y, test_size=val_size, random_state=seed, stratify=y)
    return Xtr, Xval, ytr, yval
