from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass

class BankAccount(Bank):
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    def check_balance(self):
        return self.balance

account = BankAccount("John Doe")
account.deposit(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
account.withdraw(1)
print(f"Account balance for {account.owner_name}: ${account.check_balance()}")
