
"""
Python OOP – Classes and Objects

Overview:
Introduction to Object-Oriented Programming using a
simple Patient Management example.

Concepts Covered:
1. Class – Creating a class named patient.
2. Constructor (__init__) – Initialising objects.
3. self – Accessing attributes of the current object.
4. Attributes – Storing patient name and age.
5. Methods – Defining display_detail().
6. Objects – Creating multiple objects from one class.

Code Implementation:
The patient class stores:
- name: Patient's name
- age: Patient's age
- display_detail(): Displays patient information

Objects:
- Patient1: Rachel, 25
- Patient2: Monica, 30

Expected Output:
patient Name: Rachel
patient Age: 25
patient Name: Monica
patient Age: 30

How to Run:
python lesson5_oop.py

Learning Outcome:
Learned to create classes and objects, initialise attributes
using constructors, use the self keyword, and call methods.

Technologies:
- Python 3
- Visual Studio Code
"""


class patient:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_detail(self):
        print("patient Name:", self.name)
        print("patient Age:", self.age)


# Creating objects

Patient1 = patient("Rachel", 25)
Patient2 = patient("Monica", 30)


# Calling methods

Patient1.display_detail()
Patient2.display_detail()

