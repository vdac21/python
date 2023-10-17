# default vs non default args 


# add function with two params
def add(x, y, z=0):
    c = x+y+z
    return c

"""
Defined add function with three params
x , y, z

Here x and y are the non-default args and z is default args
"""

r1 = add(10, 20, 30)
print(f"Res1 {r1}")


r2 = add(100, 200)
print(f"Res2 {r2}")


"""
def add3(x, y, z):
    c = x+y+z
    return c
"""




