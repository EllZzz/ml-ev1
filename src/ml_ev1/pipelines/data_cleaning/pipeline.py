from kedro.pipeline import Pipeline, node
from .nodes import clean_cardio, clean_heart, clean_lifestyle

def create_pipeline(**kwargs):
    return Pipeline([
        node(clean_cardio, "cardio", ["cardio_clean", "cardio_summary"], name="clean_cardio_node"),
        node(clean_lifestyle, "lifestyle", ["lifestyle_clean", "lifestyle_summary"], name="clean_lifestyle_node"),
        node(clean_heart, "heart_data", ["heart_clean", "heart_summary"], name="clean_heart_node"),
    ])
