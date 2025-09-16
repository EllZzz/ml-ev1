from kedro.pipeline import Pipeline, node
from .nodes import clean_cardio

def create_pipeline(**kwargs) -> Pipeline:
    """
    Crea el pipeline de limpieza de datos.
    """
    return Pipeline(
        [
            node(
                func=clean_cardio,
                inputs="cardio",
                outputs="cardio_clean",
                name="clean_cardio_node"
            )
        ]
    )
