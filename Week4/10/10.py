import json
from pathlib import Path
from abc import ABC, abstractmethod
class Account(ABC):
    @abstractmethod
    def get_account_type(self):
        pass
class SavingsAccount(Account):   
    def get_account_type(self):
        return "This is a Savings Account."
class CurrentAccount(Account):
    def get_account_type(self):
        return "This is a Current Account."
data=Path("Django2025/Week4/10/10.json").read_text()
accounts=json.loads(data)
for item in accounts:
    if item["type"] == "savings":
        sa = SavingsAccount()
        print(sa.get_account_type())
    elif item["type"] == "current":
        ca = CurrentAccount()
        print(ca.get_account_type())
