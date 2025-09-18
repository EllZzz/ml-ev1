# src/ml_ev1/context.py
from pathlib import Path
import pandas as pd
import yaml

class KedroNotebookContext:
    """
    Contexto simplificado para Jupyter en Kedro 1.0.0
    """

    def __init__(self, project_path: Path = None):
        if project_path is None:
            project_path = Path(__file__).parents[2]  # raíz del proyecto
        self.project_path = project_path
        self.catalog = self._load_catalog()

    def _load_catalog(self):
        """Crea un diccionario de datasets desde conf/base/catalog.yml"""
        catalog_path = self.project_path / "conf" / "base" / "catalog.yml"
        with open(catalog_path) as f:
            catalog_yaml = yaml.safe_load(f)

        datasets = {}
        for name, ds in catalog_yaml.items():
            if ds.get("type") == "pandas.CSVDataSet":
                filepath = self.project_path / ds["filepath"]
                datasets[name] = pd.read_csv(filepath)
        return datasets

# Función de acceso
def get_context() -> KedroNotebookContext:
    return KedroNotebookContext()
