def Add(a,b):
    return a+b
def Subtract(a,b):
    return a-b
def Multiply(a,b):
    return a*b
def Divide(a,b):
    if b==0:
        return "Error! Division by zero."
    else:
        return a/b

def display_menu():
    print("Hi, Select the operation you want to perform:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

while True:
    display_menu()
    choice = int(input("Enter the choice (1-5): "))

    if choice ==1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", Add(num1,num2))
    elif choice ==2:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", Subtract(num1,num2))
    elif choice ==3:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", Multiply(num1,num2))
    elif choice ==4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", Divide(num1,num2))
    elif choice ==5:
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option.")
    