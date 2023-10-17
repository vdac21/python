#WAF  to sum two values and multiply results with 100


def add(x,y):
    c=x+y
    print(f"Addtion of x={x}y y={y} is{c}")
    r=c*100
    print(r)

c=add(10,20)

print(c*100)#nameerror :name 'c' is not defined
"""
The varaibles which we have defined inside function are the local variables

we are not suppose to access outside of the functiom

to get the value outside of the function

we need to return the value from the function

"""


#how to return


#we can return values from the function by using return statement.




        
