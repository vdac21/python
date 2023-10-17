# WAF to sum two values and multiply results with 100

def add(x,y):
    c=x+y
    print(c)
    r=c*100
    print(r)


c=add(10,20)#name error c is not defined

print(c*100)
"""

The variables which we have defined inside a function are the local varaibles

we are not suppose to access outside of the function

To get the value outside of the function

We need to return the value from the function

"""
 #We can return values from the function by using return statement
