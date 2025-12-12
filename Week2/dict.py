scores = {"John": 85, "Sara": 92, "Fraol": 78}
try:
      student_name=input("Enter the student's name: ")
      score= scores[student_name]
      print(f"{student_name}'s score is {score}.")
except :
       print("Student not found!")