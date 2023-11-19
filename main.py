import tkinter as tk
from tkinter import ttk
from students import students  # Replace this with a database import later

def main():
    root = tk.Tk()
    root.title("Classync - Classroom Management")
    root.geometry("1000x600")  # Adjusted for additional columns

    # Global style configuration
    style = ttk.Style()
    style.configure('Custom.TFrame', background='#f0f0f0')
    style.configure('Custom.TButton', font=('Helvetica', 12), background='#0078D7')
    style.configure('Custom.TLabel', background='#f0f0f0', font=('Helvetica', 10))

    # Header
    header = ttk.Label(root, text="Classync - Student Management System", style='Custom.TLabel', font=('Helvetica', 16))
    header.pack(side='top', fill='x', padx=10, pady=10)

    # Main Frame
    main_frame = ttk.Frame(root, style='Custom.TFrame')
    main_frame.pack(side='top', fill='both', expand=True)

    # Treeview for Student Data
    tree = setup_treeview(main_frame)
    tree.pack(side='left', fill='both', expand=True)

    # Scrollbar for Treeview
    setup_scrollbar(main_frame, tree)

    # Control Panel for Buttons
    control_panel = setup_control_panel(root)

    # Status Bar
    status_bar = ttk.Label(root, text="Ready", style='Custom.TLabel')
    status_bar.pack(side='bottom', fill='x')

    # Populate Treeview with Data
    populate_treeview(tree, students)

    root.mainloop()

def setup_treeview(main_frame):
    columns = ('Name', 'Warm Up', 'Lesson', 'Activity', 'Homework', 'Details')
    tree = ttk.Treeview(main_frame, columns=columns, show='headings')
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150, minwidth=100)
    return tree

def setup_scrollbar(main_frame, tree):
    scrollbar = ttk.Scrollbar(main_frame, orient='vertical', command=tree.yview)
    scrollbar.pack(side='right', fill='y')
    tree.configure(yscroll=scrollbar.set)

def setup_control_panel(root):
    control_panel = ttk.Frame(root, style='Custom.TFrame')
    control_panel.pack(side='top', fill='x')
    btn_refresh = ttk.Button(control_panel, text="Refresh Data", style='Custom.TButton', command=refresh_data)
    btn_refresh.pack(side='left', padx=10, pady=10)
    return control_panel

def refresh_data():
    # Function to refresh data
    pass

def populate_treeview(tree, student_data):
    for student in student_data:
        tree.insert('', tk.END, values=(
            student['nome_do_aluno'], 
            student['warm_up'],
            student['lesson_of_the_day'], 
            student['activity'],
            student['homework'],
            student['details']
        ))

if __name__ == "__main__":
    main()
