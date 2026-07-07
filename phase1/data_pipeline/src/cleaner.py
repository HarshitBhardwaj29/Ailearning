import pandas as pd

def clean_data(df):
    # Remove rows with missing values
    df = df.dropna()
    # Remove duplicate rows
    df = df.drop_duplicates()
    # Remove extra spaces from text columns
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].str.strip()

    return df