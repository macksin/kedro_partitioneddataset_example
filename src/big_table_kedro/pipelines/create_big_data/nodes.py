"""
This is a boilerplate pipeline 'create_big_data'
generated using Kedro 0.18.1
"""

import numpy as np
from sklearn.datasets import (make_classification)
import pandas as pd
import logging
from typing import Any, Dict, Callable

logger = logging.getLogger(__name__)


def make_dataset(random_seed: int = 42, sample_size: int = 10) -> pd.DataFrame:
    X, y = make_classification(n_samples=sample_size, n_features=20,
                               random_state=random_seed)
    data = np.concatenate((X, y.reshape((-1, 1))), axis=1)
    df = pd.DataFrame(data, columns=[f"col_{i}" for i in range(data.shape[1])])
    df["col_20"] = df["col_20"].astype(int)
    return df


def generate_big_data(
    random_seed: int = 42,
    n_partitions: int = 10,
    sample_size: int = 10
) -> Dict[str, Callable[[], Any]]:

    rng = np.random.seed(random_seed)

    return {
        f"dataset_part_{i}": lambda: make_dataset(random_seed=rng, 
                                                  sample_size=sample_size)
        for i in range(n_partitions)}
