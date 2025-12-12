class Student:
    def set_grade(self, grade):
        self.__grade = grade

    def get_grade(self):
        return self.__grade


s = Student()
s.set_grade("Dagmawi's Grade: A")
print(s.get_grade())
