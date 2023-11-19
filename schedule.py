# schedule.py

def organize_lessons(students):
    """
    Organizes lessons for each student based on certain criteria.
    For example, even-numbered lessons might be input sessions, and odd-numbered lessons might be output sessions.
    """
    for student in students:
        try:
            # Convert lesson_of_the_day to an integer
            lesson_number = int(student["lesson_of_the_day"])
            
            if lesson_number % 2 == 0:
                print(f"{student['nome_do_aluno']}'s lesson is an input session.")
            else:
                print(f"{student['nome_do_aluno']}'s lesson is an output session.")
        except ValueError:
            # Handle cases where conversion to integer fails
            print(f"Error: Invalid lesson number for {student['nome_do_aluno']}.")

def schedule_class(students):
    """
    Schedules classes for each student. This function is a placeholder and currently
    just prints a scheduling message for each student. Replace this with your actual
    scheduling logic.
    """
    for student in students:
        print(f"Scheduling class for {student['nome_do_aluno']}.")
