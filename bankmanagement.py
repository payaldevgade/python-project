import json
import random
import string
from pathlib import Path


class Bank:

    DATABASE = "data.json"

    def __init__(self):

       if Path(self.DATABASE).exists():
        try:
            with open(self.DATABASE, "r") as f:
                self.data = json.load(f)
        except json.JSONDecodeError:
            self.data = []
       else:
        self.data = []


    def save(self):
        
        with open(self.DATABASE, "w") as f:
            json.dump(self.data, f, indent=4)

    def generate_account(self):
        while True:
            acc = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
            if not any(user.get("Account Number") == acc for user in self.data):
                return acc

    def create_account(self, name, age, email, pin):

        if age < 18:
           return False, "Age must be 18+"

        if len(str(pin)) != 5:
           return False, "PIN must be 5 digits"

        if not str(pin).isdigit():
            return False, "PIN should contain only digits"

        if any(user.get("Email") == email for user in self.data):
            return False, "Email already exists"
        account = {
            "Name": name,
            "Age": age,
            "Email": email,
            "PIN": str(pin),
            "Account Number": self.generate_account(),
            "Balance": 0
        }

        self.data.append(account)
        self.save()

        return True, account

    # ...existing code...
    
    def login(self, account, pin):
        for user in self.data:
            if user is None:
                continue
            if user.get("Account Number") == account and str(user.get("PIN")) == str(pin):

                return user
        return None
# ...existing code...

    def deposit(self, account, pin, amount):

        user = self.login(account, pin)

        if not user:
            
            return False, "Invalid Details"

        if amount <= 0:
            return False, "Invalid Amount"

        user["Balance"] += amount
        self.save()

        return True, "Money Deposited Successfully"

    def withdraw(self, account, pin, amount):

        user = self.login(account, pin)

        if not user:
            return False, "Invalid Details"

        if amount <= 0:
            return False, "Invalid Amount"

        if amount > user["Balance"]:
            return False, "Insufficient Balance"

        user["Balance"] -= amount
        self.save()

        return True, "Money Withdrawn Successfully"

    def update_details(self, account, pin, name, email):

        user = self.login(account, pin)

        if not user:
            return False, "Invalid Details"

        if name:
            user["Name"] = name

        if email:
            user["Email"] = email
        self.save()

        return True, "Updated Successfully"

    def delete_account(self, account, pin):

        user = self.login(account, pin)

        if not user:
            return False, "Invalid Details"

        self.data.remove(user)
        self.save()

        return True, "Account Deleted"
