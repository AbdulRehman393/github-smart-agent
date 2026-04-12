# class variables = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class
from tkinter.font import names

from dulwich.protocol import agent_string


# instance variables are defined inside the constructor , class variables are defined outside the
# constructor




class Student:
    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name                       # self refers to the object we are currently working with, if we are constructing student1
        self.age = age                         # just imagine we are replacing self with student1 and same as for student2
        Student.num_students += 1              # if we are modifying a class variable instead of self we will use the name of class



student1 = Student("Bilal",20)
student2 = Student("Ahmad", 21)
student3 = Student("Jawad", 24)
student4 = Student("Shameer", 20)

print(student1.name)
print(student1.age)
print(Student.class_year)
# It's good practice to access a class variable by the name of the class rather than any object created from the class
# e.g., print(Student.class_year)
print(Student.num_students)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
