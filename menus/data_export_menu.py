from modules.data_export_module import export_to_csv
from menus.interactions_menu import clean, press_any_key_with_animation
import os


def data_export_menu(db_path):
    """
    Menu to export the database table to a CSV file.
    """
    while True:
        clean()
        table_name = "titanic_data"
        invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']

        try:
            file_name = input("Enter the name of the CSV file to export: ").strip()

            if file_name == "":
                print("Operation canceled.")
                return

            if any(char in file_name for char in invalid_chars):
                raise ValueError(f"File name contains invalid characters: {invalid_chars}")

            if not file_name.lower().endswith(".csv"):
                file_name += ".csv"

            export_path = os.path.join("data", file_name)

            if not os.path.exists("data"):
                os.makedirs("data")

            export_to_csv(db_path, table_name, export_path)
            print(f"File successfully exported to: {export_path}")
            return

        except ValueError as ve:
            print(f"Error: {ve}")
            press_any_key_with_animation()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            press_any_key_with_animation()
