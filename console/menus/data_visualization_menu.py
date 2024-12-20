import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

from .bar_chart_menu import bar_chart_menu
from .interactions_menu import clean

def data_visualization_menu(db_path):
    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql("SELECT * FROM titanic_data", conn)
    clean()
    print("\n### Data Visualization Menu ###")
    print("1. Bar Chart: Passenger Count by Class")
    print("2. Pie Chart: Survival Rate by Sex")
    print("3. Exit to Main Menu")

    choice = input("Choose an option: ")

    if choice == "1":
       bar_chart_menu(df)
    elif choice == "2":
        survival_rate = df.groupby('Sex')['Survived'].mean()
        survival_rate.plot(kind='pie', autopct='%1.1f%%', title="Survival Rate by Sex")
        plt.ylabel("")
        plt.show()
    elif choice == "3":
        return
    else:
        print("Invalid choice. Please try again.")
