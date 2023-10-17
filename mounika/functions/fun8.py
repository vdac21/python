#WAF find area of circle


"""
def<function_name>(arg):
    #st1
    #st2
    return statement
"""
#if you are not return anything function.the interpreter will return none value
#formula :pi*r*r


def area(r):
    pi=3.147
    a=pi*r*r
    return a


rad=10

#calling function:we can call a function by using function name and while we are calling function we must pass the required params



a1=area(rad)
print(a1)


# function definition
def get_square(num):
    return num * num

for i in [1,2,3]:
    # function call
    result = get_square(i)
    print('Square of',i, '=',result)
