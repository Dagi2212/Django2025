import json
from pathlib import Path
from abc import ABC, abstractmethod
   
data=Path("Django2025/Week4/9/9.json").read_text()
emails=json.loads(data)

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass
class EmailNotification(Notification):
    def send(self, message):
        for item in emails:        
          if item["type"] == "email":
            print("Email object created")
class SMSNotification(Notification):
    def send(self, message):
        for item in emails:        
          if item["type"] == "sms":
            print("SMS object created")
e=EmailNotification()
s=SMSNotification()
e.send("")
s.send("")