import pandas as pd
import sqlite3

from .interactions_menu import *
from .average_menu import average_menu
from .sum_menu import sum_menu
def data_processing_menu(db_path):
    while True:
        try:
            with sqlite3.connect(db_path) as conn:
                df = pd.read_sql("SELECT * FROM titanic_data", conn)
            
            clean()
            print("\n### Data Processing Menu ###")
            print("1. Show Summary Statistics")
            print("2. Calculate Average")
            print("3. Calculate Total Sum")
            print("4. Return to Main Menu")

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
                case "4":
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


