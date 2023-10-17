#method overriding
"""super class & sub class has same method if we acceess the method is subclass then only subclass method is accessed without accessing super classs method.

Already created a method in superclass then implementing same method in subclass with different  logic & accessing in subclass if it overrides superclass method then it is called method overriding


class parent:
    pass
class child(parent):
    pass



class parent:
    def method(self):
        print("this is parent method")
class child(parent):
    def method(self):
        print("this is child method")


obj=child()
obj.method()



class grandparent:
    def method(self):
        print("this is grandparent method")
class parent(grandparent):
    def method(self):
        print("this is parent method")
class child(parent):
    def method(self):
        print("this is child method")
obj1=child()
obj2=parent()
obj1.method()
obj2.method()


class grandparent:
    def method(self):
        print("this is grandparent method")
class parent:
    def method(self):
        print("this is parent method")
class child(grandparent,parent):
    def method(self):
       print("this is parent method")
obj=child()

obj.method()

        
"""
class parent:
    def __init__(self):
        print("this is constructor method")
class child(parent):
    def __init__(self):
        print("this is method")
child()




