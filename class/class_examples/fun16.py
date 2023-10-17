#Default vs Non-Default args

#WAf add two numbers
#add fuction with two params

def add(x,y):
    c=x+y
    return c
x=10
y=20

r=add(x,y)#calling function
print(r)

def add(x,y,z):
    c=x+y+z
    return c
x=10
y=20
z=30
r=add(x,y,z)#calling function
print(r)

