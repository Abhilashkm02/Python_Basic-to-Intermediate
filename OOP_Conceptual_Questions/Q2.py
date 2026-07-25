'''Method definition:
    *Define a class Student with attributes name and marks
    *Write a method display_info() to display the name and marks of the student
    *Create multiple objects of the class and call the display_info() method for each object'''


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_info(self):
        print(f"Student Name: {self.name}, Marks: {self.marks}")

# Create multiple objects of the class
student1 = Student("Abhi", 85)
student2 = Student("Yash", 90)
student3 = Student("Raj", 78)

# Call the display_info() method for each object
student1.display_info()
student2.display_info()
student3.display_info()
