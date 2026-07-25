'''Student Report Card Generator
Build a system that collects student data and subject-wise marks to generate a report card.

Include grade calculation, average score, and pass/fail result.
Use encapsulation for mark storage and method abstraction for result generation.'''


class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        self.__marks={} #Encapsulation: marks is a private attribute

    def add_marks(self,subject,marks):
        if marks>=0 and marks<=100:
            self.__marks[subject]=marks
        else:
            print("Marks should be between 0 and 100.")
            return False
    def calculate_average(self):
        total=0
        for marks in self.__marks.values():
            total+=marks
        average=total/len(self.__marks)
        print(f"Average Marks: {average}")

    def is_passed(self):
        for marks in self.__marks.values():
            if marks<40:
                print("Better luck next time! You have failed.")
                return False
        print("Congratulations! You have passed.")
        return True

    def calculate_grade(self):
        total=0
        for marks in self.__marks.values():
            total+=marks
        average=total/len(self.__marks)
        if average>=90:
            print("Grade: A")
        elif average>=80:
            print("Grade: B")
        elif average>=70:
            print("Grade: C")
        elif average>=60:
            print("Grade: D")
        else:
            print("Grade: F")

class ReportCard:
    def __init__(self,student):
        self.student=student

    def generate_report(self):
        print(f"Report Card for {self.student.name}, Roll No: {self.student.roll_no}")
        self.student.calculate_average()
        self.student.is_passed()
        self.student.calculate_grade()

s1=Student("Abhilash",'001')
s1.add_marks("Math",90)
s1.add_marks("English",80)
s1.add_marks("Science",99)
rc=ReportCard(s1)
rc.generate_report()

'''Its not a menu driven program, but it is a simple implementation of a student report card generator. 
You can extend this code to make it menu driven by adding options for user input and interaction.'''