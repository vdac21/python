#add function with two params


def add(x,y,z=0):
    c=x+y+z
    return c
"""
Defined add function with three params x,y,z
Here x,y are the non-default args and z is the default arg
"""
r1=add(10,20,30)
print(f"res1:{r1}")
r2=add(100,200)
print(f"res2:{r2}")
