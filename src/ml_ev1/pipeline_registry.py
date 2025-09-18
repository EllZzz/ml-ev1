from __future__ import annotations

from kedro.pipeline import Pipeline
from ml_ev1.pipelines import data_cleaning

def register_pipelines() -> dict[str, Pipeline]:
    """
    Register the project's pipelines.
    """
    pipelines = {
        "data_cleaning": data_cleaning.create_pipeline(),
    }

    # Pipeline por defecto
    pipelines["__default__"] = pipelines["data_cleaning"]

    return pipelines
