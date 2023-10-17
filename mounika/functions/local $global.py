"""local variables:
    1.local variables are declared inside aa the function.
    2.local variables accessed only base function in the program
    3.local variable are alive with in the function they are declared.



    ex:"""

def show():
   a=15
   print(a)
show()


"""


global variable:
    1.global variable declared outside the main function
    2.global variable are accessed by all functions in the program.
    3.global variable are alive throughout the program.


"""



a=17


def something():
    

 something()
print(a)








a=10
def something():
    
    a=15
    print(a)
something()
print(a)
    
