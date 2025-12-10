def get_grade(student_grades, student_name):
    try:
       grade= student_grades[student_name]
       return f"{student_name}'s grade is {grade}."
    except :
       print(f"No grade found for {student_name}.")
students = {'Samuel': 90, 'Dagim': 90, 'Kidan': 90, 'Dagmawi': 100}
student_name=input("Enter the student's name: ")
print(get_grade(students, student_name))