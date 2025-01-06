import pandas as pd
import sqlite3

from .interactions_menu import *
from .average_menu import average_menu
from .sum_menu import sum_menu
def data_processing_menu(db_path):
    """
    Displays a menu for data processing operations on the given database.

    The user can select from the following options:

    1. Show Summary Statistics: Displays summary statistics of the dataframe.
    2. Calculate Average: Calculates the average of the given column in the dataframe.
    3. Calculate Total Sum: Calculates the sum of the given column in the dataframe.
    0. Return to Main Menu: Returns to the main menu.

    Parameters:
        db_path (str): The path to the SQLite database containing the data to be processed.

    Returns:
        None
    """
    while True:
        try:
            with sqlite3.connect(db_path) as conn:
                df = pd.read_sql("SELECT * FROM titanic_data", conn)
            
            clean()
            print("\n### Data Processing Menu ###")
            print("1. Show Summary Statistics")
            print("2. Calculate Average")
            print("3. Calculate Total Sum")
            print("0. Return to Main Menu")

            choice = input("Choose an option: ")
            clean()

            match choice:
                case "1":
                    print("\nSummary Statistics:")
                    print(df.describe())
                    press_any_key_with_animation()  
                case "2":
                    average_menu(df)  
                case "3":
                    sum_menu(df)  
                case "0":
                    print("Returning to Main Menu...")
                    break  
                case _:
                    raise ValueError
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            press_any_key_with_animation()
            break  
        except ValueError:
            clean()
            print("Invalid choice. Please try again.")
            press_any_key_with_animation()


