import pandas as pd
import sqlite3

from .interactions_menu import *
from .average_menu import average_menu
from .sum_menu import sum_menu
def data_processing_menu(db_path):
    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql("SELECT * FROM titanic_data", conn)
    clean()
    print("\n### Data Processing Menu ###")
    print("1. Show Summary Statistics")
    print("2. Calculate Average")
    print("3. Calculate Total Sum")
    print("4. Return to Main Menu")

    choice = input("Choose an option: ")
    
    if choice == "1":
        clean()
        print("\nSummary Statistics:")
        print(df.describe())
        press_any_key_with_animation()
    elif choice == "2":
        average_menu(df)
    elif choice == "3":
        sum_menu(df)
    elif choice == "4":
        return
    else:
        print("Invalid choice. Please try again.")
    data_processing_menu(db_path)
