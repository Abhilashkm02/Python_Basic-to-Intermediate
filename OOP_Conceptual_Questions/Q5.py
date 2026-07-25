'''Encapsulation:
        Create a class BankAccount with private attributes account_number and balance.
        Write methods to check balance, deposit and withdraw money, and a method to display the account details.
        try accessing the private attributes directly and observe the result.'''

class Bankaccount:
    def __init__(self, accNo,balance):
        self.__accNo=accNo
        self.__balance=balance

    def check_balance(self):
        print(f"Account Number: {self.__accNo}, Balance: {self.__balance}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

# Create an object of the class
account = Bankaccount("123456789", 1000)
account.check_balance()
account.deposit(500)
account.withdraw(200)
account.check_balance()