"""
100 DAYS OF CODE
DAY 9
TODO-1 With a given database of students_scores in the format of a dictionary, write a program that
     converts their scores to grades.
     By the end of the program, you should have a new dictionary called studants_grades that shoud
     contain student students names for keus and their grades for values.
     Scores criteria:
        - Scores 91-100: "Outstanding"
        - Scores 81-90: "Exceeds Expectations"
        - Scores 71-80: "Acceptable"
        - Scores 70 or lower: "Fail"
TODO-2 Create an empty dictionary called students grades
TODO-3 Write the code to add the grades
     HINT: Loop through the students_scores dictionary
"""
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}
print(student_scores)
student_grades = {}
for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
print(student_grades)
