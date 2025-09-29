import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

NUMERICS_DEFAULT = ["age","first_saps","hemoglobin","platelets","creatinine"]
CATEGORICALS_DEFAULT = ["gender","first_icu_type"]

class Preprocessor:
    def __init__(self, continuous_cols=None, categorical_cols=None):
        self.cont_cols = [c for c in (continuous_cols or NUMERICS_DEFAULT) if c]
        self.cat_cols = [c for c in (categorical_cols or CATEGORICALS_DEFAULT) if c]
        self.scaler = StandardScaler()
        self.cat_maps = {}

    def fit(self, df: pd.DataFrame):
        if self.cont_cols:
            self.scaler.fit(df[self.cont_cols])
        for c in self.cat_cols:
            cats = sorted(df[c].fillna("UNK").astype(str).unique())
            self.cat_maps[c] = {v:i for i,v in enumerate(cats)}
        return self

    def transform(self, df: pd.DataFrame):
        parts = []
        if self.cont_cols:
            parts.append(self.scaler.transform(df[self.cont_cols]))
        for c in self.cat_cols:
            idx = df[c].fillna("UNK").astype(str).map(self.cat_maps[c]).fillna(0).astype(int).values.reshape(-1,1)
            parts.append(idx)
        X = np.hstack(parts) if parts else np.empty((len(df),0))
        return X
