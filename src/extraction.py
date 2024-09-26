import pandas as pd

def load_data():
    """
    Load the data from the processed bikes dataset.
    Returns
    -------
    pandas.DataFrame
        The loaded data.
    """
    return pd.read_csv("data/bikes_completed.csv")