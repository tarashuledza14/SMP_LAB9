import sys
from Lab_5.threeD_art_generato import ThreeDArtService
from UI.MenuBuilder import MenuBuilder
from UI.MenuItem import MenuItem

def menu():
    art_service = ThreeDArtService(3, 0, False)

    while True:
        print("\n--- 3D Art Menu ---")
        print("1. Change Cube Size")
        print("2. Change Color")
        print("3. Toggle Art Direction")
        print("4. Display Art")
        print("5. Display 2D Art")
        print("6. Save Art to File")
        print("7. Load and Display Art from File")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            art_service.change_size()
        elif choice == "2":
            new_color = int(input("Enter color code (e.g., 31 for red, 32 for green, 34 for blue): "))
            art_service.change_color(new_color)
        elif choice == "3":
            art_service.change_direction()
        elif choice == "4":
            art_service.print_art()
        elif choice == "5":
            art_service.print_2d_art()
        elif choice == "6":
            file_name = input("Enter file name to save: ")
            art_service.save_art_into_file(file_name)
            print(f"Art saved to {file_name}")
        elif choice == "7":
            file_name = input("Enter file name to load: ")
            try:
                ThreeDArtService.get_art_archive(file_name)
            except FileNotFoundError:
                print("File not found. Please check the file name.")
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

def run():
    menu()

