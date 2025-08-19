import pandas as pd
import os

def load_data(path: str = "data/GlobalSuperstore.csv") -> pd.DataFrame:
    """Charge le dataset Global Superstore"""
    df = pd.read_csv(path, encoding="latin1")
    return df
