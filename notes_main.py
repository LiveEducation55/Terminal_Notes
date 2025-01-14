import os
from datetime import datetime

class NotesApp:
    def __init__(self):
        self.notes = []
        self.filename = "my_notes.txt"
        self.load_notes()

    def load_notes(self):
        """Load existing notes from file if it exists"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.notes = file.readlines()

    def save_notes(self):
        """Save notes to file"""
        with open(self.filename, 'w') as file:
            file.writelines(self.notes)

    def add_note(self, note):
        """Add a new note with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_note = f"[{timestamp}] {note}\n"
        self.notes.append(formatted_note)
        self.save_notes()
        print("Note added successfully!")

    def view_notes(self):
        """Display all notes"""
        if not self.notes:
            print("No notes found!")
        else:
            print("\n=== Your Notes ===")
            for note in self.notes:
                print(note.strip())
            print("================")

    def delete_note(self, index):
        """Delete a note by its index"""
        if 0 <= index < len(self.notes):
            deleted_note = self.notes.pop(index)
            self.save_notes()
            print(f"Deleted note: {deleted_note.strip()}")
        else:
            print("Invalid note index!")

def main():
    app = NotesApp()
    
    while True:
        print("\n=== Notes App Menu ===")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            note = input("Enter your note: ")
            app.add_note(note)
        
        elif choice == '2':
            app.view_notes()
        
        elif choice == '3':
            app.view_notes()
            if app.notes:
                try:
                    index = int(input("Enter the index of note to delete: "))
                    app.delete_note(index)
                except ValueError:
                    print("Please enter a valid number!")
        
        elif choice == '4':
            print("Thank you for using Notes App!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()