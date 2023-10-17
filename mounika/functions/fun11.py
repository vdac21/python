#Default vs non-default args

#add function with two params


def add(x,y,z=0):
    c=x+y+z
    return c
"""
Defined add function with three params
x,y,z
here x,y are the non-default args and z is the default args

"""
r1=add(10,20,30)
print(r1)

r2=add(100,102)
print(r2)

r2=add(100)
print(r2)
