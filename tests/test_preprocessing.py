import pandas as pd
from src.preprocessing import Preprocessor

def test_preprocessor_shapes():
    df = pd.DataFrame({
        "age":[60,70],"first_saps":[30,35],"hemoglobin":[12,13],"platelets":[200,250],"creatinine":[1.0,1.3],
        "gender":["M","F"],"first_icu_type":["MICU","CCU"],"in_hosp_mortality":[0,1]
    })
    pp = Preprocessor().fit(df)
    X = pp.transform(df)
    assert X.shape[0] == 2
    assert X.shape[1] >= 5
