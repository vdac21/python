#multiple instances creation

class student:
    def __init__(self):
        print("inside init method")
    def display(self):
        print("inside display method")
s1=student()
s2=student()
s3=student()
s1.display()

#the student class contains or defined or having 3 methods
#for student class we have created 3 objects
