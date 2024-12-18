from .interactions_menu import *
from ..modules.data_processing_module import *


def sum_menu(df):
    clean()
    print("\n### Select a parameter ###")
    print("1. Survived")
    print("2. Women/Men")
    print("3. Total People Embarked (by port)")
    print("4. Total Passengers")
    print("5. Exit")
    choice = int(input("Choose an option: "))
    clean()
    match choice:
        case 1:
            calculate_sum(df['Survived'])
        case 2:
            sex = input("\nChoose the gender(w/m): ")
            if sex == "w":
                count_column(df['Sex'], "female")
            elif sex == "m":
                count_column(df['Sex'], "male")
                
        case 3:
            port = input("\nChoose the port(s/q/c): ")
            if port == "s":
                count_column(df['Embarked'], "S")
            elif port == "q":
                count_column(df['Embarked'], "Q")
            elif port == "c":
                count_column(df['Embarked'], "C")
        case 4:
            calculate_sum(df['Fare'])
        case 5:
            return
    press_any_key_with_animation()
    