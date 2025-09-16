import pandas as pd

def clean_cardio(cardio: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia el dataset de cardio:
    - Elimina filas duplicadas
    """
    cardio_clean = cardio.drop_duplicates()
    return cardio_clean
