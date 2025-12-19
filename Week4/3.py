from abc import ABC, abstractmethod
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass 
    def turn_off(self):
        pass
class WashingMachine(Appliance):
    def turn_on(self):
        return "Washing Machine is now ON" 
    def turn_off(self):
        return "Washing Machine is now OFF"
wm = WashingMachine()
print(wm.turn_on()) 