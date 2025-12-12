class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def annual_salary(self):
        return self.salary * 12 
    
e = Employee("Dagi", 20000)
print("Dagi's annual salary is: ",e.annual_salary())
