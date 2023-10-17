#Access the class members (data or methods)

"""
The class members we can access object of that class
We can create an object of a class using class name


class student:
    pass

s1=student()

s1 is a object of student() class
"""


class student:
    def display():
        print("hello world")


#display()
s1=student()
s1.display()# type error :display() takes 0 positional arguments but 1 was given

