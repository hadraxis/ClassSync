import tkinter as tk
from tkinter import ttk
from database import connect_database, get_students
from schedule import organize_lessons, schedule_class
from utils import authenticate_user, send_notification

def main():
    # Backend Logic
    connect_database()
    user = authenticate_user()
    students = get_students()
    organize_lessons(students)
    schedule_class(students)
    send_notification("Classes have been scheduled and organized.")

    # Tkinter GUI
    root = tk.Tk()
    root.title("Classync - Classroom Management")

    # Add GUI components here
    # Example: Label
    label = ttk.Label(root, text="Welcome to Classync")
    label.pack()

    # Example: Button to Refresh Data
    refresh_button = ttk.Button(root, text="Refresh Data", command=lambda: refresh_data(students))
    refresh_button.pack()

    # Start the GUI event loop
    root.mainloop()

def refresh_data(students):
    # Function to refresh student data on the UI
    # This is where you will integrate backend logic with the UI
    for student in students:
        print(student['nome_do_aluno'])  # Example action

if __name__ == "__main__":
    main()
