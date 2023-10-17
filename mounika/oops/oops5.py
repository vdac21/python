#__init__ () method

"""
the __init__() method is special method  we can call it as a constructor as a programer we no need to call explicition
the interpreter will call this method at the time of object creation
"""


class student:
    def __init__(self):
        print("inside init method")
    def display(self):
        print("inside a dispaly method")
s1=student()
s1.display()
    
