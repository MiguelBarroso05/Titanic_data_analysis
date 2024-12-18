import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

def data_visualization_menu(db_path):
    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql("SELECT * FROM titanic_data", conn)

    print("\n### Data Visualization Menu ###")
    print("1. Bar Chart: Passenger Count by Class")
    print("2. Pie Chart: Survival Rate by Sex")
    print("3. Exit to Main Menu")

    choice = input("Choose an option: ")

    if choice == "1":
        df['Pclass'].value_counts().plot(kind='bar', title="Passenger Count by Class")
        plt.xlabel("Class")
        plt.ylabel("Count")
        plt.show()
    elif choice == "2":
        survival_rate = df.groupby('Sex')['Survived'].mean()
        survival_rate.plot(kind='pie', autopct='%1.1f%%', title="Survival Rate by Sex")
        plt.ylabel("")
        plt.show()
    elif choice == "3":
        return
    else:
        print("Invalid choice. Please try again.")
