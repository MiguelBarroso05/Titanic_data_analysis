import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

from .pie_chart_menu import pie_chart_menu
from .bar_chart_menu import bar_chart_menu
from .interactions_menu import clean

def data_visualization_menu(db_path):
    """
    Displays a menu for generating various bar charts and pie charts to visualize
    the provided dataframe. The user can select different parameters to visualize
    data related to survival, gender, passenger class, embarkation port, and more.

    Parameters:
        db_path (str): The path to the SQLite database containing the data to be visualized.

    Returns:
        None
    """
    while True:
        with sqlite3.connect(db_path) as conn:
            df = pd.read_sql("SELECT * FROM titanic_data", conn)
        clean()
        print("\n### Data Visualization Menu ###")
        print("1. Bar Chart: Passenger Count by Class")
        print("2. Pie Chart: Survival Rate by Sex")
        print("0. Exit to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            bar_chart_menu(df)
        elif choice == "2":
            pie_chart_menu(df)
        elif choice == "0":
            return
        else:
            print("Invalid choice. Please try again.")
