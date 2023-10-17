'''
str="global"
def show():
    str="local"
    print(str)
show()
print(str)


a=10
def something():
    a=15
    print(a)
something()
print(a)


a=10
def something():
    global a
    a=15
    print(a)
something()
print(a)


def person(name,age):
    print(name)
    print(age)
person('naveen')

'''
def sum(a,b):
    c=a+b
    print(c)
sum(3,4)
