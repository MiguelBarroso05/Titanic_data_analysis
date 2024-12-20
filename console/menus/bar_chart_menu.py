import matplotlib.pyplot as plt
from .interactions_menu import *

def bar_chart_menu(df):
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
        print("15. Exit")

        try:
            choice = int(input("Choose an option: "))
            clean()

            match choice:
                case 1:
                    bar_chart(df['Survived'])
                case 2:
                    bar_chart(df['Sex'])
                case 3:
                    bar_chart(df['Pclass'])
                case 4:
                    bar_chart(df['Embarked'])
                case 5:
                    survival_by_category(df, 'Sex')
                case 6:
                    survival_by_category(df, 'Pclass')
                case 7:
                    survival_by_category(df, 'Embarked')
                case 8:
                    category_comparison(df, 'Pclass', 'Sex')
                case 9:
                    category_comparison(df, 'Pclass', 'Embarked')
                case 10:
                    average_value_by_category(df, 'Fare', 'Pclass')
                case 11:
                    average_value_by_category(df, 'Age', 'Pclass')
                case 12:
                    average_value_by_category(df, 'Age', 'Survived')
                case 13:
                    stacked_bar_chart(df, 'Survived', 'Pclass')
                case 14:
                    stacked_bar_chart(df, 'Sex', 'Embarked')
                case 15:
                    return
                case _:
                    raise ValueError
            press_any_key_with_animation()
        except ValueError:
            print("Invalid option. Please enter a valid number.")
            press_any_key_with_animation()


# Helper functions

def bar_chart(data):
    # Logic for creating a bar chart (you can use matplotlib or seaborn)
    plt.bar(data.value_counts().index, data.value_counts().values)
    plt.show()
    

def survival_by_category(df, category):
    # Plot survival rate based on the chosen category (e.g., 'Sex', 'Pclass', 'Embarked')
    df['Survived'].groupby(df[category]).mean().plot(kind='bar')
    plt.show()
    

def category_comparison(df, category1, category2):
    # Plot comparison between two categories (e.g., 'Pclass' vs 'Sex')
    df['Survived'].groupby([df[category1], df[category2]]).mean().unstack().plot(kind='bar')
    plt.show()
    

def average_value_by_category(df, value_column, category_column):
    # Plot average value (e.g., 'Fare', 'Age') by a specific category (e.g., 'Pclass', 'Survived')
    df.groupby(category_column)[value_column].mean().plot(kind='bar')
    plt.show()
    

def stacked_bar_chart(df, value_column, category_column):
    # Create stacked bar charts based on the specified columns
    df[value_column].groupby(df[category_column]).value_counts().unstack().plot(kind='bar')
    plt.show()
    
