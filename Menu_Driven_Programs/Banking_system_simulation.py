'''Design a system to simulate a bank's operations, where users can create accounts, deposit and withdraw money, and check their account balance.

Extend functionality to include multiple account types (e.g., savings, current) with unique behaviors like interest calculation or overdraft limits.
Emphasize encapsulation, inheritance and polymorphism.'''


class Account():
    def __init__(self,id, Holder_name):
        self.id = id
        self.Holder_name = Holder_name
        self._balance = 0 #Encapsulation: balance is a private attribute

    def check_balance(self):
        print(f"Account Holder: {self.Holder_name}, Account ID: {self.id}, Balance: ${self._balance}")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
class Bank:
    pass

class SavingsAccount(Account): #inheritance: SavingsAccount inherits from Account
    def calculate_interest(self):
        interest_rate = 0.03 #3%
        interest=self._balance * interest_rate
        print(f"Interest earned: ${interest}. New balance after interest: ${self._balance + interest}")

class CurrentAccount(Account):
    def withdraw(self,amount): #polymorphism: overriding the withdraw method to include overdraft limit
        overdraft_limit = 500
        if amount > 0 and (self._balance + overdraft_limit) >= amount:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid withdrawal amount or exceeds overdraft limit.")

class Bank:
    def __init__(self,name,city):
        self.name=name
        self.city=city
        self.__accounts={}

    def create_account(self,account_type,id,Holder_name):
        if account_type=="savings":
            new_account=SavingsAccount(id,Holder_name)

        elif account_type=="current":
            new_account=CurrentAccount(id,Holder_name)

        self.__accounts[id]=new_account
        print(f"Account created successfully for {Holder_name} with ID: {id}.")
        return new_account

    def get_account(self,id):
        if id in self.__accounts:
            return self.__accounts[id]
        else:
            print("Account not found.")
            return None

SBI = Bank("State Bank of India", "Karnataka")
print("----------------------------------------------")
acc1SBI = SBI.create_account("savings", 101, "Abhilash")
acc2SBI = SBI.create_account("current", 102, "Shreya")
print("----------------------------------------------")
print("Account 1 Details:")
acc1SBI.deposit(1000)
acc1SBI.withdraw(200)
acc1SBI.check_balance()
acc1SBI.calculate_interest()
