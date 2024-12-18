import pandas as pd
import sqlite3

def data_processing_menu(db_path):
    with sqlite3.connect(db_path) as conn:
        df = pd.read_sql("SELECT * FROM titanic_data", conn)

    print("\n### Data Processing Menu ###")
    print("1. Show Summary Statistics")
    print("2. Calculate Average Age")
    print("3. Calculate Total Fare")
    print("4. Return to Main Menu")

    choice = input("Choose an option: ")
    
    if choice == "1":
        print("\nSummary Statistics:")
        print(df.describe())
    elif choice == "2":
        print(f"\nAverage Age: {df['Age'].mean():.2f}")
    elif choice == "3":
        print(f"\nTotal Fare: {df['Fare'].sum():.2f}")
    elif choice == "4":
        return
    else:
        print("Invalid choice. Please try again.")
