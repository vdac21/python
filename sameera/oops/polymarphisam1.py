"""
Polymarphisim:having different forms
          person------son-------employee-----husband



ability more than one task

operater---+

'+'  for two integers addition

'+' for two strings   concatenation
'+'for two list concatenation



*




multiplication-------repetation--------packing and unpacking





print(function) is a example of polymarphisim



len()
max()
"""



def sum(*args):
    if args:
        start=type(args[0])()
        for i in args:

            start+=i
        return start
print(sum(1,2,3))
print(sum(1.2+2.3+4.5))

print(sum('hi','hello'))
print(sum((1,2),(3,4)))




class A:
    def fun(self):
        print("this is class A")

class B:

    def fun(self):
        print("this is class B")
class c:
    def fun(self):

        print("this is class c")


def poly(obj):

    obj.fun()

obj1=A()

obj2=B()
obj3=c()


poly(obj1)
poly(obj2)

poly(obj3)
