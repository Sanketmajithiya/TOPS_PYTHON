import generate_note, view_note

def display_menu():
    """Display the main menu."""

    print("Welcome to Python E - Note")
    print("Press 1 for generate Note")
    print("Press 2 for view Note")
    print("press 4 for exit")
    print("Enter your choice : ")

while True:
    display_menu()

    try:
        user_choice = int(input())
    except ValueError:
        print("Error: Invalid Input")
        continue

    if user_choice == 1:
        generate_note.generate_note()
    elif user_choice == 2:
        view_note.view_notes()
    elif user_choice == 4:
        print("Exiting...")    
        break
    else:
        print("Error: Invalid Input")
        message = " viewed"
        log_file(message)