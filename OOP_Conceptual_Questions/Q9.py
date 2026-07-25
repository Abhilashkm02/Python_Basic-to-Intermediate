''' Getters & Setters:
        Create a class Bankaccount with private attribute balance.
        write getter method to retrieve balance and setter method to update it,ensuring that balance cannot be set to a negative value.'''

class BankAccount:
    def __init__(self,Balance):
        self.__Balance=Balance

    def get_Balance(self):
        return self.__Balance

    def set_Balance(self,update_Balance):
        if update_Balance >= 0:
            self.__Balance = update_Balance
        else:
            print("Error: Balance cannot be negative.")

balance = BankAccount(1000)
print(balance.get_Balance())  # Output: 1000
balance.set_Balance(500)
print(balance.get_Balance())  # Output: 500
balance.set_Balance(-200)  # Output: Error: Balance cannot be negative.