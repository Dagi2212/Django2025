from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class PartTimeEmployee(Employee):
    def __init__(self, hourly_wage, hours_worked):
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_wage * self.hours_worked
c=PartTimeEmployee(30, 40)
print("Salary:",c.calculate_salary())