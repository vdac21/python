'''Python Global variables:
   These are those which are defined outside any function and which are accessible through the program,accessible throughout the program i.e inside and outside function.
   example:'''
def f():
    print("inside function",s)

s= "chandu"
f()
print("Outside Function",s)
