#Exercise 1
class Person:
    def __init__(self, name,age ):
        self.name=name 
        self.age=age
    
p=Person('Dagamwi',22)
print (p.name,p.age)
#Exercise 2
class Dog:
    def __init__(self, sound):
        self.sound=sound
    def bark(self):
        return self.sound
b=Dog('WOOF')
print(b.bark())
#Exercise 3
class Car:
    def __init__(self,make):
        self.make=make
    def get_make(self):
        return self.make
m=Car('Make')
print(m.get_make())
#Exercise 4
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
c=Rectangle(3,4)
print(c.area())
#Exercise 5
class Student:
    def __init__(self,__grade):
        self.__grade=__grade
    def set_grade():
        return {'Dagmawi',__grade}
    def get_grade():
        return set_grade()
g=Student(5)

        

        