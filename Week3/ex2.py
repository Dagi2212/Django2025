#Exercise 2
class Dog:
    def __init__(self, sound):
        self.sound=sound
    def bark(self):
        return self.sound
b=Dog('WOOF')
print(b.bark())