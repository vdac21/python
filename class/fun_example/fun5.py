#  WAF to sum two values and multiply results with 100

"""
A function is a peice of code it will perfrom specific task 
"""

def add(x, y):
    c = x+y
    print(f"Addition of x={x} y={y} is {c}")
    r = c * 100
    print(r)



c=add(10, 20)

print(c*100)  # NameError: name 'c' is not defined


"""
The varaibles which we have defined inside a function are the local varaibles

we are not suppose to access outside of the functiion,

To get the value outside of the function

we need to return the value from the function

"""
# How to return
"""
We can rertur values from the function by using return statement 
"""
