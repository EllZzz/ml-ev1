from kedro.pipeline import Pipeline, node
from .nodes import clean_data

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=clean_data,            # función definida en nodes.py
                inputs="raw_dataset",       # dataset de entrada
                outputs="clean_dataset",    # dataset de salida
                name="clean_data_node",     # nombre único del node
            )
        ]
    )
