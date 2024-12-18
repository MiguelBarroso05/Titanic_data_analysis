from menus.data_import_menu import data_import_menu
from menus.data_export_menu import data_export_menu
from menus.data_processing_menu import data_processing_menu
from menus.data_visualization_menu import data_visualization_menu
from menus.interactions_menu import clean, press_any_key_with_animation
from dotenv import load_dotenv
import os


def main_menu():
    load_dotenv()
    db_path = os.getenv('DB')

    while True:
        press_any_key_with_animation()
        clean()

        print("\n" + "#" * 10 + " Main Menu " + "#" * 10)
        print("1. Data Processing")
        print("2. Data Visualization")
        print("3. Import CSV")
        print("4. Export CSV")
        print("5. Exit")
        
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
            elif choice == "5":
                print("Exiting the application. Goodbye!")
                break
            else:
                raise Exception("\nInsert a valid number.")
        except Exception as e:
            print(e)
