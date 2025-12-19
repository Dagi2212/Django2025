from abc import ABC, abstractmethod
class Emoloyee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass        
class FullTimeEmployee(Emoloyee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary
s=FullTimeEmployee(30000)
print("Dagi's monthly salary: ",s.calculate_salary())
