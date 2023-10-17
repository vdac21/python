#recursive function:calling same function itself

#5!=5*4*3*2*1

"""
5!=5*4!
4!=4*3!
3!=3*2!
2!=2*1!
1!=1
"""


def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        
        return (x * factorial(x-1))

num = 5
result = factorial(num)
print("The factorial of", num, "is", result)
