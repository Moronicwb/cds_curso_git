import pandas as pd
import numpy as np
import streamlit as st

def load_data():
    """
    Load the data from the processed bikes dataset.
    Returns
    -------
    pandas.DataFrame
        The loaded data.
    """
    return pd.read_csv("data/processed/bikes_completed.csv")

df = load_data()

st.dataframe(df)
