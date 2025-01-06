from .interactions_menu import *
from ..modules.data_processing_module import calculate_average

def average_menu(df):
    """
    Menu to calculate the average of a given column in the dataframe.

    The user can select from the following options:

    1. Age
    2. Siblings/Spouses
    3. Parent/Children
    4. Fare
    0. Exit

    Each option will show the average of the selected parameter in the dataframe.
    """
    while True:
        clean()
        print("\n### Select a parameter ###")
        print("1. Age")
        print("2. Siblings/Spouses")
        print("3. Parent/Children")
        print("4. Fare")
        print("0. Exit")

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
                case 0:                   
                    return 
                case _:
                    raise ValueError

        
            press_any_key_with_animation()
            break 
        except ValueError:
            clean()
            print("Invalid choice. Please try again.")
            press_any_key_with_animation()
