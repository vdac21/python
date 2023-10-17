#encapsulation

"""
Relating things combined

code will be organized and cleared

"""
class parent:
    publicData=10
    def publicmethod(self):
        print(self.publicData)
class child(parent):
    def method(self):
        print(self.publicData)

obj1=parent()
obj1.publicmethod()
print(obj1.publicData)
obj2=child()
obj2.method()
print(obj2.publicData)
