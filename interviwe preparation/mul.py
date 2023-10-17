"""class Vdac:
  def __init__(self):
    self.course="python programing course"
    self.tech="python"
  def CourseName(self):
    return self.course +  self.tech
ob=Vdac()
#print(ob.course)
#print(ob.tech)
print(ob.CourseName())


#2.Protected access specifiers

class Vdac:
  def __init__(self):
    self.course="python programing course"
    self._tech="python"
  def CourseName(self):
    return self.course +  self._tech
ob=Vdac()
print(ob.course)
print(ob._tech)
print(ob.CourseName())

class Vdac:
  def __init__(self):
    self.course="python programing course"
    self.__tech="python"
  def CourseName(self):
    return self.course +  self.__tech
ob=Vdac()
print(ob.course)
print(ob.__tech)
print(ob.CourseName())


#we can use name mangling in python
class Vdac:
  def __init__(self):
    self.course="python programing course"
    self.__tech="python"
  def CourseName(self):
    return self.course +  self.__tech
ob=Vdac()
print(ob.course)
print(ob._Vdac__tech)
print(ob.CourseName())


class Person:
  def __init__(self,name,age):
    self.__name=name
    self.__age=age
  def display_info(self):
    print(f"the person name is {self.__name}and the age is {self.__age}")


person=Person("vedhu",23)


person.display_info()
"""
class Bankaccount:
    def __init__(self):
        self.__balance=0
 
    def amount_deposite(self,amount):
        self.__balance+=amount
        #print(self.__balance)
 
    def amount_withdrawal(self,amount1):
        if(self.__balance>amount1):
            self.__balance-=amount1
        else:
            print("NO sufficient amount ")
 
    def get_balance(self):
        print(self.__balance)
   
obj_bank=Bankaccount()
obj_bank.amount_deposite(10000)
obj_bank.amount_withdrawal(5000)
#obj_bank.get_balance()
 



obj_bank.get_balance()




