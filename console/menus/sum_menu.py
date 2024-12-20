from .interactions_menu import *
from ..modules.data_processing_module import *

def sum_menu(df):
    while True:
        clean()

        print("\n### Select a parameter ###")
        print("1. Survived")
        print("2. Women/Men")
        print("3. Total People Embarked (by port)")
        print("4. Total Passengers")
        print("5. Exit")

        try:
            choice = int(input("Choose an option: "))
            clean()

            match choice:
                case 1:
                    calculate_sum(df['Survived'])
                case 2:
                    sex = input("\nChoose the gender (w/m): ").lower()
                    if sex == "w":
                        count_column(df['Sex'], "female")
                    elif sex == "m":
                        count_column(df['Sex'], "male")
                    else:
                        print("Invalid gender. Please choose 'w' or 'm'.")
                        continue
                case 3:
                    port = input("\nChoose the port (s/q/c): ").lower()
                    if port == "s":
                        count_column(df['Embarked'], "S")
                    elif port == "q":
                        count_column(df['Embarked'], "Q")
                    elif port == "c":
                        count_column(df['Embarked'], "C")
                    else:
                        print("Invalid port. Please choose 's', 'q', or 'c'.")
                        continue
                case 4:
                    calculate_sum(df['Fare'])
                case 5:
                    return 
                case _:
                    raise ValueError

            press_any_key_with_animation()
            break
        except ValueError:
            clean()
            print("Invalid choice. Please try again.")
            press_any_key_with_animation()
