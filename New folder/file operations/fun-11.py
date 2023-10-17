# defalut vs non defalut args



# add two function with two parameters
def add(x, y, z=0):
    c = x+y+z
    return c

"""
Defind add function with three parameters
x, y, z

Here X and Y are the non defalut args z is default args
"""


r1 = add(10,20,30)
print(f"res1 {r1}")


r2 = add(100, 200)
print(f"res2, {r2}")


"""
def add3(x, y, z)
    c = x+y+z
    return c
"""
      
