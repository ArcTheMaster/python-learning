student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# Don't change the code above
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Covert scores into grades.
for student in student_scores:
    if student_scores[student] <= 70 :
        student_grades[student] = "Fail"
    elif student_scores[student] > 70 and student_scores[student] <= 80 :
        student_grades[student] = "Acceptable"
    elif student_scores[student] > 80 and student_scores[student] <= 90 :
        student_grades[student] = "Exceeds Expectations"
    else :
        student_grades[student] = "Outstanding"

# Dont change the code below
print(student_grades)