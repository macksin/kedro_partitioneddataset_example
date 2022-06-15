"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline

import big_table_kedro.pipelines.create_big_data as cbd


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """

    create_big_data = cbd.create_pipeline()

    return {"__default__": pipeline([create_big_data])}
