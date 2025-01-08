import sqlite3
import pandas as pd

def fetch_data_from_db(query, db_path="db/titanic.sqlite"):
    """
    Fetches data from the specified database using the given SQL query.

    Args:
        query (str): SQL query to execute on the database.
        db_path (str, optional): The path to the SQLite database file. Defaults to "db/titanic.sqlite".

    Returns:
        pd.DataFrame: The result of the query, as a Pandas DataFrame.
    """
    with sqlite3.connect(db_path) as conn:
        return pd.read_sql(query, conn)