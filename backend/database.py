import sqlite3
import pandas as pd

def fetch_data_from_db(query, db_path="../db/titanic.sqlite"):
    with sqlite3.connect(db_path) as conn:
        return pd.read_sql(query, conn)