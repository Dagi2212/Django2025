class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Your balance is insufficient!")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


acc = BankAccount()
acc.deposit(1000)
acc.withdraw(2000) 
print("Your balance is:", acc.get_balance(),"birr")
