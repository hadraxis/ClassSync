# schedule.py

def organize_lessons(students):
    # Example logic for organizing lessons
    for student in students:
        if student["lesson_of_the_day"] % 2 == 0:
            print(f"{student['nome_do_aluno']}'s lesson is an input session.")
        else:
            print(f"{student['nome_do_aluno']}'s lesson is an output session.")

def schedule_class(students):
    # Example logic for scheduling classes
    for student in students:
        print(f"Scheduling class for {student['nome_do_aluno']} on {student['lesson_of_the_day']}.")
