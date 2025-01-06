from .data_import_menu import data_import_menu
from .data_export_menu import data_export_menu
from .data_processing_menu import data_processing_menu
from .data_visualization_menu import data_visualization_menu
from .interactions_menu import clean, press_any_key_with_animation
from dotenv import load_dotenv
import os


def main_menu():
    """
    Displays the main menu for the Titanic Data Project application, allowing
    the user to navigate between different functionalities such as data processing,
    data visualization, CSV import, and CSV export. The menu retrieves the database
    path from environment variables and provides options for the user to perform
    various operations on the Titanic dataset.

    Options:
        1. Data Processing - Access data processing operations.
        2. Data Visualization - Access data visualization operations.
        3. Import CSV - Import data from a CSV file into the database.
        4. Export CSV - Export data from the database to a CSV file.
        0. Exit - Exit the application.
    """

    load_dotenv()
    db_path = os.getenv('DB')

    clean()
    press_any_key_with_animation()
    
    while True:
        clean()

        print("\n" + "#" * 10 + " Main Menu " + "#" * 10)
        print("1. Data Processing")
        print("2. Data Visualization")
        print("3. Import CSV")
        print("4. Export CSV")
        print("0. Exit")
        
        try:
            choice = input("Choose an option: ")
            if choice == "1":
                data_processing_menu(db_path)
            elif choice == "2":
                data_visualization_menu(db_path)
            elif choice == "3":
                data_import_menu(db_path)
            elif choice == "4":
                data_export_menu(db_path)
            elif choice == "0":
                print("Exiting the application. Goodbye!")
                return
            else:
                raise Exception("\nInsert a valid number.")
        except Exception as e:
            print(e)
