students = [
    {
        "nome_do_aluno": "Alice Johnson",
        "warm_up": "Vocabulary Review",
        "lesson_of_the_day": "Lesson 45",
        "activity": "Speaking Practice",
        "homework": "Essay Writing",
        "details": "Focus on verb tenses"
    },
    {
        "nome_do_aluno": "Bob Smith",
        "warm_up": "Grammar Exercise",
        "lesson_of_the_day": "Lesson 12",
        "activity": "Reading Comprehension",
        "homework": "Book Review",
        "details": "Improving reading skills"
    },
    {
        "nome_do_aluno": "Charlie Davis",
        "warm_up": "Listening Exercise",
        "lesson_of_the_day": "Lesson R8",
        "activity": "Review Session",
        "homework": "Grammar Worksheet",
        "details": "Review past lessons"
    },
    {
        "nome_do_aluno": "Diana Evans",
        "warm_up": "Pronunciation Practice",
        "lesson_of_the_day": "Lesson 22",
        "activity": "Writing Exercise",
        "homework": "Compose an Email",
        "details": "Work on sentence structure"
    },
    {
        "nome_do_aluno": "Ethan Grant",
        "warm_up": "Idioms and Phrases",
        "lesson_of_the_day": "Lesson 89",
        "activity": "Debate Session",
        "homework": "Prepare a Speech",
        "details": "Enhance persuasive speaking"
    },
    {
        "nome_do_aluno": "Fiona Harris",
        "warm_up": "Synonyms and Antonyms",
        "lesson_of_the_day": "Lesson 103",
        "activity": "Creative Writing",
        "homework": "Short Story",
        "details": "Focus on narrative skills"
    },
    {
        "nome_do_aluno": "George Irving",
        "warm_up": "Conjugation Drill",
        "lesson_of_the_day": "Lesson 37",
        "activity": "Spelling and Grammar Test",
        "homework": "Spelling Practice",
        "details": "Improve spelling accuracy"
    },
    {
        "nome_do_aluno": "Hannah Johnson",
        "warm_up": "Fill in the Blanks",
        "lesson_of_the_day": "Lesson R6",
        "activity": "Vocabulary Review",
        "homework": "Vocabulary Exercises",
        "details": "Strengthen vocabulary"
    },
    {
        "nome_do_aluno": "Ian Kelly",
        "warm_up": "Sentence Rearrangement",
        "lesson_of_the_day": "Lesson 29",
        "activity": "Grammar Workshop",
        "homework": "Error Identification",
        "details": "Focus on common errors"
    },
    {
        "nome_do_aluno": "Julia Lee",
        "warm_up": "Reading Aloud",
        "lesson_of_the_day": "Lesson 130",
        "activity": "Presentation Skills",
        "homework": "Prepare a Presentation",
        "details": "Develop public speaking"
    },
    {
        "nome_do_aluno": "Kevin Moore",
        "warm_up": "Dialogue Practice",
        "lesson_of_the_day": "Lesson 50",
        "activity": "Interactive Role-play",
        "homework": "Dialogue Writing",
        "details": "Enhance conversational skills"
    },
    {
        "nome_do_aluno": "Laura Nelson",
        "warm_up": "Listening to Dialogues",
        "lesson_of_the_day": "Lesson 2",
        "activity": "Language Games",
        "homework": "Listening Comprehension",
        "details": "Improve listening skills"
    }
]
def lesson_sort_key(student):
    lesson = student["lesson_of_the_day"]
    if lesson.startswith("Lesson R"):
        # Set review lessons to high sort value
        return (3, 999)
    else:
        lesson_number = int(lesson.split()[1])
        if lesson_number % 2 == 0:
            # Even lessons
            return (1, lesson_number)
        else:
            # Odd lessons
            return (2, lesson_number)

# Sorting the students list
students = sorted(students, key=lesson_sort_key)