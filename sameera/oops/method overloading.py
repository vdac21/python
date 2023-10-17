"""
method overloading:
    if the class contains more than one method has same name & the methods contain different data types of parameters or different no of parameters both is called method overloading.

class A:
    def method(int,int):
        pass
    def method(str,str):
        pass
    def method(float,float):
        pass
class B:
    def method(int):
        pass
    def method(int,int):
        pass
    def method(int,int,int):
        pass
class c:
    def method(int,int):
        pass
    def method(float,float,float):
        pass
    def method(str,str,str,str):
      pass
we want to perform addition
"""
class A:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c
obj=A()
print(obj.add(1,2,3))
print(obj.add(1,2))
