import pandas as pd
import sqlite3


def export_to_csv(db_path, table_name, export_path):
    """
    Exports data from the specified table in the database to a CSV file.
    """
    try:
        conn = sqlite3.connect(db_path)
        print("Connected to the database.")

        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql_query(query, conn)

        df.to_csv(export_path, index=False)
        print(f"Data successfully exported to '{export_path}'.")
        
        conn.close()
    except Exception as e:
        print(f"An error occurred while exporting data: {e}")
