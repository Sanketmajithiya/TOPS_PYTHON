"""Generate a new note and save it to a file."""

generator_name = input("Enter Python E-Note Generator Name: ")
while not generator_name.isalpha():
        print("Error: Invalid Input")
        generator_name = input("Enter Python E-Note Generator Name: ")
         
        message = " viewed"
        log_file(message)
        
note_title = input("Enter Python E-Note Title: ")
while not note_title.isalpha():
        print("Error: Invalid Input")
        note_title = input("Enter Python E-Note Title: ")

note_content = input("Enter E-Note Content: ")

note = f"Generator: {generator_name}\nTitle: {note_title}\nContent:\n{note_content}\n--END---\n"

try:
        with open("notes.txt", "a") as f:
            f.write(note)
        print("Note created successfully!")
except Exception as e:
        print(f"Error: {e}")

def view_notes():
    """View all notes in the file."""

    try:
        with open("notes.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Error: {e}")

while True:
    print("1. Add a new note")
    print("2. View all notes")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
        
message = " viewed"
log_file(message)