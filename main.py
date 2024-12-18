from console.menus.interactions_menu import clean, press_any_key_with_animation
from console.menus.main_menu import main_menu
import os

def main():
    while True:
        try:
            clean()
            print("Welcome to Titanic Data Project!")
            print("1. Run Console Application")
            print("2. Run Web Application")
            print("3. Exit")
            
            choice = input("Choose an option: ").strip()

            if choice == "1":
                main_menu()
                return
            elif choice == "2":
                clean()
                frontend_url = "http://127.0.0.1:5500/frontend/index.html"
                print(f"Web Application started! Open the following URL to view it: {frontend_url}")
                print("\nStarting web server...")
                os.system("python backend/app.py")
                
                press_any_key_with_animation()
            elif choice == "3":
                print("Exiting the application. Goodbye!")
                return
            else:
                print("Invalid option. Please enter a valid number")
                press_any_key_with_animation()
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting. Goodbye!")
            return
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            press_any_key_with_animation()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Critical Error: {e}")
