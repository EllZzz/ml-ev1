import pandas as pd
import numpy as np

# ===============================
# Funciones generales
# ===============================
def remove_outliers(df: pd.DataFrame, col: str, low: float, high: float) -> pd.DataFrame:
    """Elimina filas que estén fuera de los rangos low-high para la columna especificada."""
    return df[(df[col] >= low) & (df[col] <= high)].copy()

def impute_outliers_by_group(df: pd.DataFrame, col: str, low: float, high: float, group_cols: list) -> pd.DataFrame:
    """Imputa outliers usando la mediana del grupo definido en group_cols."""
    outliers = (df[col] < low) | (df[col] > high)
    medians = df.groupby(group_cols)[col].transform('median')
    df.loc[outliers, col] = medians[outliers]
    return df

# ===============================
# Node de Cardio
# ===============================
def clean_cardio(cardio: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    cardio = cardio.drop(columns=["age"], errors="ignore")

    # Limites realistas
    limits = {
        "height": (100, 220),
        "weight": (30, 200),
        "bmi": (10, 60),
        "ap_hi": (80, 250),
        "ap_lo": (40, 150),
        "age_years": (10, 100)
    }

    for col, (low, high) in limits.items():
        cardio = remove_outliers(cardio, col, low, high)

    # Codificar bp_category
    bp_mapping = {
        "Normal": 1,
        "Elevated": 2,
        "Hypertension Stage 1": 3,
        "Hypertension Stage 2": 4,
        "Hypertensive Crisis": 5
    }
    cardio["bp_category_encoded"] = cardio["bp_category"].map(bp_mapping)

    # Resumen
    summary = pd.DataFrame({
        "dataset": ["cardio"],
        "filas_finales": [cardio.shape[0]],
        "columnas": [list(cardio.columns)]
    })

    return cardio, summary

# ===============================
# Node de Heart
# ===============================
def clean_heart(heart: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    heart = heart.drop_duplicates()
    heart = heart[(heart['BMI'] >= 10) & (heart['BMI'] <= 60)]

    # Codificación de GenHealth
    genhealth_mapping = {
        'Poor': 1,
        'Fair': 2,
        'Good': 3,
        'Very good': 4,
        'Excellent': 5
    }
    heart['GenHealth_encoded'] = heart['GenHealth'].map(genhealth_mapping)

    # Resumen
    summary = pd.DataFrame({
        "dataset": ["heart"],
        "filas_finales": [heart.shape[0]],
        "columnas": [list(heart.columns)]
    })
    return heart, summary

# ===============================
# Node de Lifestyle / Smoking
# ===============================
def clean_lifestyle(smoking: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    # Eliminar columnas innecesarias
    cols_drop = ['sight_left', 'sight_right', 'hear_left', 'hear_right', 'waistline']
    smoking = smoking.drop(columns=[c for c in cols_drop if c in smoking.columns])

    # Calcular BMI
    smoking["height_m"] = smoking["height"] / 100
    smoking["BMI"] = smoking["weight"] / (smoking["height_m"] ** 2)
    smoking["BMI_range"] = pd.cut(smoking["BMI"], bins=[0, 18.5, 25, 30, 100],
                                  labels=["Underweight", "Normal", "Overweight", "Obese"])
    smoking.drop(columns=["height_m"], inplace=True)

    # Imputación de outliers por grupo
    ranges_adjusted = {
        "weight": (30, 200),
        "SBP": (50, 250),
        "DBP": (30, 150),
        "hemoglobin": (5, 20),
        "serum_creatinine": (0.3, 3.0),
        "gamma_GTP": (5, 500)
    }
    group_general = ['age', 'sex', 'BMI_range']
    for col in ["weight", "SBP", "DBP", "hemoglobin", "serum_creatinine"]:
        low, high = ranges_adjusted[col]
        smoking = impute_outliers_by_group(smoking, col, low, high, group_general)

    # gamma_GTP: incluir DRK_YN
    low, high = ranges_adjusted["gamma_GTP"]
    smoking = impute_outliers_by_group(smoking, "gamma_GTP", low, high, group_general + ["DRK_YN"])

    # Resumen
    summary = pd.DataFrame({
        "dataset": ["lifestyle"],
        "filas_finales": [smoking.shape[0]],
        "columnas": [list(smoking.columns)]
    })
    return smoking, summary
