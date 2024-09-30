import streamlit as st
from src.extraction import load_data

st.set_page_config(
    layout="wide"
)

def main():
    """
    Run the main script.
    """
    # Load the data
    df_raw = load_data()

    # Display the data
    st.dataframe(df_raw)

if __name__ == "__main__":
    main()

