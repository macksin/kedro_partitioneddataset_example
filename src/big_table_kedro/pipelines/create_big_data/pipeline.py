"""
This is a boilerplate pipeline 'create_big_data'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import generate_big_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=generate_big_data,
            inputs=None,
            outputs="partitioned_dataframe"
        )
    ])
