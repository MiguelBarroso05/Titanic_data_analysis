from .interactions_menu import *
from ..modules.data_processing_module import calculate_average

def average_menu(df):
    while True:
        clean()
        print("\n### Select a parameter ###")
        print("1. Age")
        print("2. Siblings/Spouses")
        print("3. Parent/Children")
        print("4. Fare")
        print("5. Exit")

        try:
            choice = int(input("Choose an option: "))
            clean()

            match choice:
                case 1:
                    calculate_average(df['Age'])
                case 2:
                    calculate_average(df['SibSp'])
                case 3:
                    calculate_average(df['Parch'])
                case 4:
                    calculate_average(df['Fare'])
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
