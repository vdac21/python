#multiple instances (objects) creation

class student:
    def __init__(self):
        print("inside init method")
    def display(self):
        print("inside a display method")
s1=student()
s2=student()
s3=student()

s1.display()
s2.display()
s3.display()
