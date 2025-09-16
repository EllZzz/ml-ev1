from ml_ev1.pipelines import eda
from kedro.pipeline import Pipeline

def register_pipelines() -> dict[str, Pipeline]:
    pipelines = {
        "eda": eda.create_pipeline(),
    }
    pipelines["__default__"] = sum(pipelines.values())
    return pipelines