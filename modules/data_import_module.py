import pandas as pd
import os
import sqlite3
from datetime import datetime, timedelta


def load_csv(file_path):
    """
    Loads a CSV file into a DataFrame.
    """
    if not file_path.endswith(".csv"):
        raise ValueError("Invalid file type. Please provide a .csv file.")
    if not os.path.exists(file_path):
        raise FileNotFoundError("File not found. Please check the file path.")

    df = pd.read_csv(file_path)
    print("CSV file loaded successfully.")
    return df


def clean_and_process_data(df):
    """
    Cleans and preprocesses the DataFrame:
    - Fills missing values.
    - Converts column types.
    - Adds 'Age_Milliseconds' column.
    """
    if 'Age' in df.columns:
        df['Age'] = df['Age'].fillna(df['Age'].mean())

    if 'Fare' in df.columns:
        df['Fare'] = df['Fare'].fillna(0)

    df = df.fillna("Unknown")

    if 'Age' in df.columns:
        df['Age'] = df['Age'].astype(float)

    if 'Pclass' in df.columns:
        df['Pclass'] = df['Pclass'].astype(int)

    # Create Age_Milliseconds column using epoch
    epoch = datetime(1970, 1, 1)
    if 'Age' in df.columns:
        df['Age_Milliseconds'] = df['Age'].apply(
            lambda age: int((epoch + timedelta(days=age * 365.25)).timestamp() * 1000)
        )

    return df


def save_to_database(df, db_path, table_name):
    """
    Saves the DataFrame to an SQLite database.
    """
    conn = sqlite3.connect(db_path)
    try:
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        print("Data successfully saved to the database.")
    finally:
        conn.close()


def check_existing_table(db_path, table_name):
    """
    Checks if a table already exists in the database.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{table_name}'")
    exists = cursor.fetchone()[0] == 1
    conn.close()
    return exists


def drop_existing_table(db_path, table_name):
    """
    Drops an existing table from the database.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    conn.commit()
    conn.close()
    print("Existing data removed.")
