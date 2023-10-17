# Defalut vs non-defalut args


# WAF add two numbers


# add  function with two parameters

def add(x, y):
    c = x+y
    return c


a = 10
b = 20
r = add(a, b)# Calling funtion

print(f"sum of a={a} and b={b}is r={r}")



def add(x, y, z):
    c = x+y+z
    return c


a=10
b=20
d=30
r = add(a, b, d) # Calling function

print(f"sum of a={a} and b={b} d={d} is r={r}")

a = 100
b = 200
add(a, b)
print(f"sum of m={a} and n={b}is {x}")

#functon overloading: Defining same function name multiple times with different args and different values
*In python we dont have support of function overloading
*The previous function name will overrideds with latest function is defined
*In above example you are seeing two functions but only one function is exist i.e add
with the three parameters
       
 
