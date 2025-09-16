from ml_ev1.pipelines import eda, data_cleaning
from kedro.pipeline import Pipeline

def register_pipelines() -> dict[str, Pipeline]:
    eda_pipeline = eda.create_pipeline()
    cleaning_pipeline = data_cleaning.create_pipeline()

    return {
        "eda": eda_pipeline,
        "data_cleaning": cleaning_pipeline,
        "__default__": eda_pipeline,  # pipeline por defecto
    }
