from abc import ABC, abstractmethod
class SchoolMember(ABC):
    @abstractmethod
    def work(self):
        pass
class Teacher(SchoolMember):
    def work(self):
        return "A Teacher teaches students."
class Student(SchoolMember):
    def work(self):
        return "A Student takes lessons."
t=Teacher()
s=Student()
print(t.work())
print(s.work())