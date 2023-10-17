class Employee:
    def name(self):
        print("employee name:kushi")
    def age(self):
        print("employee age:28")
class Details(Employee):
    def salary(self):
        print("employee salary: 25000")
 
a=Details()
a.salary()
a.name()
a.age()
#Multilevel inheritance
 
class Employee:  #grandfather
    def name(self):
        print("employee name:kushi")
    def age(self):
        print("employee age:28")
class Details(Employee):#father
    def salary(self):
        print("employee salary: 25000")
class Designation(Details):#child
    def design(self):
        print("Designation:Test Engineer")
call=Designation()
call.name()
call.age()
call.salary()
call.design()

#multiple inheritance
class Employee:  #father
    def name(self):
        print("employee name:kushi")
    def age(self):
        print("employee age:28")
class Details():#mother
    def salary(self):
        print("employee salary: 25000")
class Designation(Employee,Details):#child
    def design(self):
        print("Designation:Test Engineer")
call=Designation()
call.name()
call.age()
call.salary()
call.design()

class Employee:  #parent
    def name(self):
        print("employee name:kushi")
    def age(self):
        print("employee age:28")
class Details(Employee):#child
    def salary(self):
        print("employee salary: 25000")
class Designation(Employee):#child
    def design(self):
        print("Designation:Test Engineer")
call=Designation()
c=Details()
call.name()
call.age()
c.salary()
call.design()

 

