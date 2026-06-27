"""
Author: Abdelhamid Hamdy

Project:
Automotive Spare Parts Business Analytics

Description:
Load and clean Excel datasets for analysis.
"""

import pandas as pd


def load_sheet(file_path, sheet_name, header_row=3):
    """
    Load and clean Excel sheet.

    Parameters
    ----------
    file_path : str
    sheet_name : str
    header_row : int

    Returns
    -------
    DataFrame
    """

    df = pd.read_excel(
         "/content/sample_data/Sample_data.xlsx",
         sheet_name="دفتر اليومية",
         header=4
    )

    # Convert column names to string
    df.columns = df.columns.astype(str)

    # Remove unnamed columns
    df = df.loc[:, ~df.columns.str.contains("Unnamed")]

    # Remove empty rows
    df.dropna(how="all", inplace=True)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Reset index
    df.reset_index(drop=True, inplace=True)

    return df
