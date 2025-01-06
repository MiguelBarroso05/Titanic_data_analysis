from ..modules.data_visualization_module import *
from .interactions_menu import *

def bar_chart_menu(df):
    """
    Displays a menu for generating various bar charts and comparisons based on
    the provided dataframe. The user can select different parameters to visualize
    data related to survival, gender, passenger class, embarkation port, and more.

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
        print("5. Survived vs Sex")
        print("6. Survived vs Pclass")
        print("7. Survived vs Embarked")
        print("8. Pclass vs Sex")
        print("9. Pclass vs Embarked")
        print("10. Average Fare by Pclass")
        print("11. Average Age by Pclass")
        print("12. Average Age by Survived")
        print("13. Survived by Pclass (Stacked)")
        print("14. Sex by Embarked (Stacked)")
        print("0. Exit")

        try:
            choice = int(input("Choose an option: "))
            clean()

            match choice:
                case 1:
                    bar_chart(df['Survived'], "Survival Count", "Survival Status", "Count")
                case 2:
                    bar_chart(df['Sex'], "Gender Distribution", "Gender", "Count")
                case 3:
                    bar_chart(df['Pclass'], "Passenger Class Distribution", "Passenger Class", "Count")
                case 4:
                    bar_chart(df['Embarked'], "Embarkation Port Distribution", "Port", "Count")
                case 5:
                    survival_by_category(df, 'Sex', "Survival Rate by Gender", "Gender", "Survival Rate")
                case 6:
                    survival_by_category(df, 'Pclass', "Survival Rate by Passenger Class", "Passenger Class", "Survival Rate")
                case 7:
                    survival_by_category(df, 'Embarked', "Survival Rate by Embarkation Port", "Port", "Survival Rate")
                case 8:
                    category_comparison(df, 'Pclass', 'Sex', "Passenger Class vs Gender Survival Rate", "Passenger Class", "Survival Rate")
                case 9:
                    category_comparison(df, 'Pclass', 'Embarked', "Passenger Class vs Embarkation Port Survival Rate", "Passenger Class", "Survival Rate")
                case 10:
                    average_value_by_category(df, 'Fare', 'Pclass', "Average Fare by Passenger Class", "Passenger Class", "Average Fare")
                case 11:
                    average_value_by_category(df, 'Age', 'Pclass', "Average Age by Passenger Class", "Passenger Class", "Average Age")
                case 12:
                    average_value_by_category(df, 'Age', 'Survived', "Average Age by Survival Status", "Survival Status", "Average Age")
                case 13:
                    stacked_bar_chart(df, 'Survived', 'Pclass', "Survival Count by Passenger Class", "Passenger Class", "Count")
                case 14:
                    stacked_bar_chart(df, 'Sex', 'Embarked', "Gender Count by Embarkation Port", "Embarkation Port", "Count")
                case 0:
                    break
                case _:
                    raise ValueError
            press_any_key_with_animation()
        except ValueError:
            print("Invalid option. Please enter a valid number.")
            press_any_key_with_animation()
        except Exception as e:
            print(f"An error occurred: {e}")
            press_any_key_with_animation()

# Helper functions
