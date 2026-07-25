'''Create a class:
        *Write a class mobile with attributes brand and price
        *Create two objects of the class and display their attributes using a method'''

class Mobile:
    def __init__(self,Brand,Price):
        self.Brand=Brand
        self.Price=Price
    
    def display(self):
        print(f"{self.Brand} costs {self.Price}.")

Mobile1 = Mobile("Iphone",70000)
Mobile2 = Mobile("Samsung",50000)

Mobile1.display()
Mobile2.display()
