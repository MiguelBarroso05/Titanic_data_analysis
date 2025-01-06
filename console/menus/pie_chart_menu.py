import matplotlib.pyplot as plt
from .interactions_menu import *
from ..modules.data_visualization_module import *

def pie_chart_menu(df):
    """
    Menu to generate pie charts based on the provided dataframe.

    Parameters:
        df (pd.DataFrame): The dataframe containing the data to be visualized.

    Returns:
        None
    """
    # Convert 1 to 'Survived' and 0 to 'Died' in the 'Survived' column
    df['Survived'] = df['Survived'].replace({1: 'Survived', 0: 'Died'})

    while True:
        clean()
        print("\n### Select a parameter ###")
        print("1. Survived")
        print("2. Sex")
        print("3. Pclass")
        print("4. Embarked")
        print("5. Survived by Sex")
        print("6. Survived by Pclass")
        print("7. Survived by Embarked")
        print("0. Exit")

        try:
            choice = int(input("Choose an option: "))
            clean()

            match choice:
                case 1:
                    pie_chart(df['Survived'], "Survival Distribution")
                case 2:
                    pie_chart(df['Sex'], "Gender Distribution")
                case 3:
                    pie_chart(df['Pclass'], "Passenger Class Distribution")
                case 4:
                    pie_chart(df['Embarked'], "Embarkation Port Distribution")
                case 5:
                    survival_by_category_pie(df, 'Sex', "Survived by Gender")
                case 6:
                    survival_by_category_pie(df, 'Pclass', "Survived by Passenger Class")
                case 7:
                    survival_by_category_pie(df, 'Embarked', "Survived by Embarkation Port")
                case 0:
                    return
                case _:
                    raise ValueError
            press_any_key_with_animation()
        except ValueError:
            print("Invalid option. Please enter a valid number.")
            press_any_key_with_animation()

