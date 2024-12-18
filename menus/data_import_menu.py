from menus.interactions_menu import clean, press_any_key_with_animation
from modules.data_import_module import (
    load_csv,
    clean_and_process_data,
    save_to_database,
    check_existing_table,
    drop_existing_table
)
import os


def data_import_menu(db_path):
    """
    Menu to import a CSV file, process data, and save it to the database.
    """
    while True:
        clean()
        table_name = "titanic_data"

        try:
            file_name = input("Enter the name of the CSV file (example.csv): ")
            file_path = os.path.join("data", file_name)

            if file_name == "":
                print("Operation canceled.")
                return
            
            df = load_csv(file_path)

            if check_existing_table(db_path, table_name):
                overwrite = input("Database already contains data. Do you want to overwrite? (y/n): ").lower()
                if overwrite != 'y':
                    print("Operation canceled.")
                    return
                drop_existing_table(db_path, table_name)

            df = clean_and_process_data(df)

            save_to_database(df, db_path, table_name)

            print("Data imported and processed successfully!")
            return

        except FileNotFoundError:
            print("Error: File not found.")
            press_any_key_with_animation()
        except ValueError as ve:
            print(f"Error: {ve}")
            press_any_key_with_animation()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            press_any_key_with_animation()