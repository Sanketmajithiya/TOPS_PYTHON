from log import log_file

print("Welcome to Python E - Note")
print("Press 1 for generate Note")
print("Press 2 for view Note")
print("press 4 for exit")

user_choice = int(input("Enter your choice : "))

notes_file = "e_notes.txt"

def generate_note():
    
    generator_name = input("Enter Python E-Note Generator Name : ")
    note_title = input("Enter Python E-Note Title : ")
    note_content = input("Enter E-Note Content : ")

    with open(notes_file, 'a') as file:
        file.write(f"{generator_name} - {note_title}\n")
        file.write(note_content)
        file.write("\n------END------\n")

    print(f"Note for '{note_title}' has been created by {generator_name}")
    message = " Generated"
    log_file(message)
    
def view_notes():
   
    with open(notes_file, 'r') as file:
        notes = file.read()

    print("Your Notes:")
    print(notes)
    message = " viewed"
    log_file(message)

def handle_choice():
    if user_choice == 1:
        generate_note()
    elif user_choice == 2:
        view_notes()
    elif user_choice == 4:
        print("Exiting...")
    else:
        print("Invalid choice. Please try again.")

handle_choice()