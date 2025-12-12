class Car:
    def __init__(self,make):
        self.make=make
    def get_make(self):
        return self.make
m=Car('Make')
print(m.get_make())