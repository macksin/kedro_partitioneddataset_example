"""
This is a boilerplate pipeline 'create_big_data'
generated using Kedro 0.18.1
"""
from random import random
import numpy as np
from sklearn.datasets import (make_classification)
import pandas as pd

def make_dataset(random_seed: int = 42) -> pd.DataFrame:
    X, y = make_classification(n_samples=1000, n_features=20, random_state=random_seed)
    data = np.concatenate((X, y.reshape((-1, 1))), axis=1)
    df = pd.DataFrame(data, columns=[f"col_{i}" for i in range(data.shape[1])])
    df["col_20"] = df["col_20"].astype(int)
    return df
