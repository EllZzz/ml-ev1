import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Ejemplo: eliminar filas con valores nulos."""
    return df.dropna()
