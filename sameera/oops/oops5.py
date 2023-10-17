#__init__() method
"""the __init__method is special method  we can call it as a constructor as progremmer we no need to call explication
the interpreter will call this method at the time of object creation"""



class student:
    def __init__(self):
        print("inside init method")
    def display(self):
        print("inside display method")
s1=student()
s1.display()
        
