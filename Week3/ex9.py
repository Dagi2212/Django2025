class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        print(f"Brand: {self.brand}, Year: {self.year}")


class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def info(self):  
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")


v = Vehicle("BMW", 2024)
c = Car("Toyota", 2020, "Corolla")

v.info()
c.info()
