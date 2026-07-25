'''Add default parameter
    Create a class employee with the attributes name,designation and salary(default value of salary is 30000).
    *Write a method display_info() to display the name, designation and salary of the employee
    *create multiple objects of the class and call the display_info() method for each object
    '''

class Employee:
    def __init__(self,name,designation,salary=30000):
        self.name=name
        self.designation=designation
        self.salary=salary

    def display_info(self):
        print(f"Employee Name: {self.name}, Designation: {self.designation}, Salary: {self.salary}")

# Create multiple objects of the class
employee1 = Employee("Raj", "Manager", 50000)
employee2 = Employee("Abhi", "Developer")

# Call the display_info() method for each object
employee1.display_info()
employee2.display_info()