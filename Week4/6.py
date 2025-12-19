from abc import ABC, abstractmethod
class Transport(ABC):
    @abstractmethod
    def move(self):
        pass
class Bus(Transport):
    def move(self):
        return "The bus moves on the asphalt road."
class Train(Transport):
    def move(self):
        return "The train moves on the railway tracks."
b=Bus()
t=Train()   
print(b.move())
print(t.move())