#__init__()method

"""

The __init__() method is special method we can call it is a constractor As a programmer we no need to call explicity, the interpreter will call this method as the time of object creation.

class student:

    def __init__(self):
        print("inside init method")

    def display(self):
        print("inside a display method")

s1= student()
s1.display()


class student:

    def __init__(self):
        print("python")
    def display(self):
        print("python is a powerful language")
s1=student()
s2=student()
s3=student()

s1.display()
s2.display()
s3.display()
"""
class student:
    def __init__(self):
        print("python")

    def marks(self):
        print("marks")

    def display(self):
        print("score")

#The student class contains or defined or having 3 methods

#for student class we have created two objects i.e s1 and s2
s1=student()
s2=student()

s1.marks()
s1.display()

s1.marks()
s1.display()
s2.display()
