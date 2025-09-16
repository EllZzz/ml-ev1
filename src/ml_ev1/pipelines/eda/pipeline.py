from kedro.pipeline import Pipeline, node
from .nodes import describe_data

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=describe_data,
                inputs="cardio_data",
                outputs="cardio_summary",
                name="describe_cardio_node"
            )
        ]
    )