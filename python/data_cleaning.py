"""
Data Cleaning Functions
"""

import pandas as pd


def clean_dataframe(df):

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove empty rows
    df = df.dropna(how="all")

    # Reset index
    df = df.reset_index(drop=True)

    return df
