import pandas as pd

def load_data(path):
    """Läser in CSV-fil och returnerar en DataFrame."""
    return pd.read_csv(path)
